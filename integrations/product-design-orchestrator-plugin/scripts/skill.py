#!/usr/bin/env python3
"""Offline skill router and safe Markdown-only fetcher.

No external dependency. This script never executes downloaded content.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
import urllib.request
import urllib.error
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "all-skills.json"
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9+.#-]{1,}")
MAX_BYTES = 2 * 1024 * 1024
ALLOWED_HOSTS = {"raw.githubusercontent.com"}


def load_registry() -> list[dict]:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Cannot read registry: {exc}")
    if not isinstance(data, list):
        raise SystemExit("Registry must be a JSON list")
    return data


def tokens(value) -> list[str]:
    if isinstance(value, list):
        value = " ".join(str(x) for x in value)
    return TOKEN_RE.findall(str(value).lower())


def document(item: dict) -> tuple[list[str], dict[str, float]]:
    weighted: dict[str, float] = defaultdict(float)
    fields = [
        (item.get("id", ""), 7.0), (item.get("name", ""), 8.0),
        (item.get("description", ""), 4.0), (item.get("category", ""), 3.0),
        (item.get("phases", []), 2.5), (item.get("triggers", []), 3.5),
        (item.get("tags", []), 2.0), (item.get("stacks", []), 4.0),
        (item.get("source", ""), 1.0),
    ]
    flat = []
    for value, weight in fields:
        for term in tokens(value):
            flat.append(term)
            weighted[term] += weight
    return flat, weighted


def rank(items: list[dict], query: str, phase: str | None = None,
         stack: str | None = None, category: str | None = None,
         source: str | None = None) -> list[tuple[float, dict]]:
    filtered = []
    for item in items:
        if category and item.get("category") != category:
            continue
        if source and item.get("source") != source:
            continue
        filtered.append(item)
    if not filtered:
        return []

    docs = [document(x) for x in filtered]
    df = Counter()
    for flat, _ in docs:
        df.update(set(flat))
    q = tokens(query)
    if phase:
        q += tokens(phase)
    if stack:
        q += tokens(stack)
    qcounts = Counter(q)
    n = len(filtered)
    results = []
    phrase = query.strip().lower()
    for item, (flat, weighted) in zip(filtered, docs):
        score = 0.0
        for term, qtf in qcounts.items():
            idf = math.log(1 + (n - df.get(term, 0) + 0.5) / (df.get(term, 0) + 0.5))
            score += weighted.get(term, 0.0) * idf * (1 + math.log(qtf))
        haystack = " ".join(str(item.get(k, "")) for k in ("id","name","description","triggers","tags")).lower()
        if phrase and phrase in haystack:
            score += 16
        if phase and phase in item.get("phases", []):
            score += 8
        if stack and stack.lower() in [str(x).lower() for x in item.get("stacks", [])]:
            score += 12
        # Prefer locally maintained, then preserved; external stack specialists can still win on relevance.
        score += {"local-original": 3, "preserved-upstream": 1, "official-or-primary-upstream": 7}.get(item.get("trust"), 0)
        if score > 0:
            results.append((score, item))
    return sorted(results, key=lambda x: (-x[0], x[1].get("id", "")))


def print_item(item: dict, score: float | None = None) -> None:
    lead = f"{score:7.2f}  " if score is not None else ""
    print(f"{lead}{item.get('id')} — {item.get('description')}")
    print(f"         category={item.get('category')} phases={','.join(item.get('phases', [])) or '-'} "
          f"stacks={','.join(item.get('stacks', [])) or '-'} source={item.get('source')}")
    if item.get("path"):
        print(f"         local: {item['path']}")
    if item.get("install"):
        print(f"         install: {item['install']}")


def find_one(items: list[dict], ident: str) -> dict:
    exact = [x for x in items if ident in {x.get("id"), x.get("name")}]
    if len(exact) == 1:
        return exact[0]
    suffix = [x for x in items if x.get("id", "").endswith("/" + ident)]
    if len(suffix) == 1:
        return suffix[0]
    if not exact and not suffix:
        raise SystemExit(f"Skill not found: {ident}")
    matches = exact or suffix
    raise SystemExit("Ambiguous skill. Use an exact id:\n" + "\n".join(f"  {x['id']}" for x in matches))


def cmd_search(args, items):
    for score, item in rank(items, args.query, args.phase, args.stack, args.category, args.source)[:args.limit]:
        print_item(item, score)


def cmd_recommend(args, items):
    limit = max(1, min(args.limit, 3))
    results = rank(items, args.task, args.phase, args.stack, args.category, args.source)
    if not results:
        raise SystemExit("No relevant skill found. Broaden the task terms or inspect SKILLS.md.")
    selected = []
    if results:
        selected.append(results[0])
    if args.stack and len(selected) < limit:
        stack_value = args.stack.lower()
        specialist = next((pair for pair in results if stack_value in [str(x).lower() for x in pair[1].get("stacks", [])]
                           and pair[1].get("id") not in {x[1].get("id") for x in selected}), None)
        if specialist:
            selected.append(specialist)
    for pair in results:
        if len(selected) >= limit:
            break
        if pair[1].get("id") not in {x[1].get("id") for x in selected}:
            selected.append(pair)
    print("Recommended smallest useful set (maximum 3):")
    for score, item in selected:
        print_item(item, score)
    print("\nRead each selected SKILL.md fully, define its output, and unload it after the phase.")


def cmd_list(args, items):
    selected = [x for x in items if (not args.category or x.get("category") == args.category)
                and (not args.source or x.get("source") == args.source)]
    for item in sorted(selected, key=lambda x: x.get("id", "")):
        print(f"{item.get('id')}\t{item.get('category')}\t{item.get('description')}")
    print(f"\n{len(selected)} skill(s)")


def cmd_show(args, items):
    item = find_one(items, args.id)
    print(json.dumps(item, indent=2, ensure_ascii=False))
    if item.get("path"):
        path = ROOT / item["path"]
        if path.exists():
            print("\n--- local skill ---\n")
            print(path.read_text(encoding="utf-8"))


def fetch_text(url: str) -> bytes:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
        raise SystemExit(f"Refusing host or scheme: {url}. Only HTTPS raw.githubusercontent.com is allowed.")
    if not (parsed.path.lower().endswith(".md") or "skill" in parsed.path.lower()):
        raise SystemExit("Refusing non-Markdown/non-skill path")
    req = urllib.request.Request(url, headers={"User-Agent": "ProductDesignOrchestrator/4.0 text-only"})
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            content_type = response.headers.get("Content-Type", "")
            if "text" not in content_type and "octet-stream" not in content_type:
                raise SystemExit(f"Unexpected content type: {content_type}")
            data = response.read(MAX_BYTES + 1)
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"Download failed with HTTP {exc.code}: {url}") from None
    except urllib.error.URLError as exc:
        raise SystemExit(f"Download failed: {exc.reason}. Check network access and the source URL.") from None
    if len(data) > MAX_BYTES:
        raise SystemExit("Skill exceeds 2 MiB safety limit")
    return data


def cmd_fetch(args, items):
    item = find_one(items, args.id)
    url = item.get("url")
    if not url or "raw.githubusercontent.com" not in url:
        raise SystemExit("This entry has no direct raw Markdown URL. Use its printed install/source command after manual review.")
    if not args.yes:
        print(f"Review before download:\n  id: {item['id']}\n  source: {url}\n  license: {item.get('license')}\n")
        raise SystemExit("No file written. Re-run with --yes after reviewing the source and license.")
    data = fetch_text(url)
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"Skill is not UTF-8: {exc}")
    if "description:" not in text[:3000].lower() and "# " not in text[:1000]:
        raise SystemExit("Downloaded text does not resemble a skill file")
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", item.get("name", "skill")).strip("-") or "skill"
    dest = Path(args.dest).expanduser().resolve() / slug
    dest.mkdir(parents=True, exist_ok=True)
    target = dest / "SKILL.md"
    if target.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite {target}; use --force")
    target.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(data).hexdigest()
    source_note = f"""# Source record\n\n- id: {item['id']}\n- source: {url}\n- downloaded: {datetime.now(timezone.utc).isoformat()}\n- sha256: `{digest}`\n- declared/catalog license: {item.get('license', 'inspect upstream')}\n\nDownloaded as text only. No scripts or instructions were executed. Inspect this file before loading it.\n"""
    (dest / "SOURCE.md").write_text(source_note, encoding="utf-8")
    print(f"Downloaded text only to {target}\nSHA-256: {digest}")


def cmd_doctor(args, items):
    errors = []
    required = [ROOT/"AGENTS.md", ROOT/"DESIGN.md", ROOT/"SOUL.md", ROOT/"SKILLS.md", REGISTRY]
    errors += [f"missing {p}" for p in required if not p.exists()]
    ids = [x.get("id") for x in items]
    if len(ids) != len(set(ids)):
        errors.append("duplicate registry ids")
    for item in items:
        if item.get("path") and not (ROOT/item["path"]).exists():
            errors.append(f"missing path for {item.get('id')}: {item['path']}")
        url = item.get("url")
        if url and not url.startswith("https://"):
            errors.append(f"non-HTTPS URL: {item.get('id')}")
    sources = Counter(x.get("source") for x in items)
    print(f"Registry: {len(items)} entries")
    for source, count in sorted(sources.items()):
        print(f"  {source}: {count}")
    if errors:
        print("Doctor failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        raise SystemExit(1)
    print("Doctor passed")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Search, recommend, inspect, or safely fetch design/UI skills")
    sub = p.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--category")
    common.add_argument("--source")
    common.add_argument("--phase")
    common.add_argument("--stack")

    s = sub.add_parser("search", parents=[common]); s.add_argument("query"); s.add_argument("--limit", type=int, default=10)
    r = sub.add_parser("recommend", parents=[common]); r.add_argument("--task", required=True); r.add_argument("--limit", type=int, default=3)
    l = sub.add_parser("list"); l.add_argument("--category"); l.add_argument("--source")
    sh = sub.add_parser("show"); sh.add_argument("id")
    f = sub.add_parser("fetch"); f.add_argument("id"); f.add_argument("--dest", required=True); f.add_argument("--yes", action="store_true"); f.add_argument("--force", action="store_true")
    sub.add_parser("doctor")
    return p


def main():
    args = parser().parse_args()
    items = load_registry()
    {"search": cmd_search, "recommend": cmd_recommend, "list": cmd_list,
     "show": cmd_show, "fetch": cmd_fetch, "doctor": cmd_doctor}[args.command](args, items)

if __name__ == "__main__":
    main()
