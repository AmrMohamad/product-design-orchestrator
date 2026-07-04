#!/usr/bin/env python3
"""Install Product Design Orchestrator for Codex and/or Claude Code.

The installer is intentionally local-only. It does not access the network, invoke
package managers, or execute code from bundled skills. It copies reviewed files
into the official project/user skill locations documented by OpenAI and
Anthropic, records every managed path, and can verify or remove only what it
installed.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

PRODUCT_ID = "professional-product-design-orchestrator"
PLUGIN_NAME = "product-design-orchestrator"
MANAGED_START = "<!-- PRODUCT-DESIGN-ORCHESTRATOR:START -->"
MANAGED_END = "<!-- PRODUCT-DESIGN-ORCHESTRATOR:END -->"
MARKER_FILE = ".pdo-managed.json"
CODEX_RECEIPT = "install-receipt.codex.json"
CLAUDE_RECEIPT = "install-receipt.claude.json"
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
NAME_LINE = re.compile(r"^name:\s*(.*?)\s*$", re.M)


class InstallError(RuntimeError):
    """Raised for an expected, actionable installation failure."""


@dataclass(frozen=True)
class Context:
    package_root: Path
    plugin_source: Path
    version: str
    project_root: Path
    home: Path
    dry_run: bool
    force: bool
    no_guidance: bool
    activate_global: bool
    profile: str


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json_atomic(path: Path, value: object, dry_run: bool = False) -> None:
    if dry_run:
        print(f"DRY-RUN write JSON: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    write_text_atomic(path, text)


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def is_owned(path: Path) -> bool:
    marker = path / MARKER_FILE
    if not marker.is_file():
        return False
    try:
        return read_json(marker).get("product_id") == PRODUCT_ID
    except Exception:
        return False


def ownership_marker(version: str, component: str, source: str | None = None) -> dict:
    value = {
        "product_id": PRODUCT_ID,
        "version": version,
        "component": component,
        "managed": True,
    }
    if source:
        value["source"] = source
    return value


def atomic_copytree(
    source: Path,
    destination: Path,
    *,
    ctx: Context,
    component: str,
    transform=None,
) -> None:
    if destination.exists() and not is_owned(destination) and not ctx.force:
        raise InstallError(
            f"Refusing to replace unmanaged path: {destination}\n"
            "Move it, choose another scope, or rerun with --force only after reviewing it."
        )
    if ctx.dry_run:
        action = "update" if destination.exists() else "create"
        print(f"DRY-RUN {action}: {destination} <- {source}")
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    tmp = destination.parent / f".{destination.name}.tmp-{uuid.uuid4().hex}"
    backup = destination.parent / f".{destination.name}.backup-{uuid.uuid4().hex}"
    try:
        shutil.copytree(source, tmp, symlinks=False)
        write_json_atomic(tmp / MARKER_FILE, ownership_marker(ctx.version, component))
        if transform:
            transform(tmp)
        had_existing = destination.exists()
        if had_existing:
            os.replace(destination, backup)
        os.replace(tmp, destination)
        if backup.exists():
            shutil.rmtree(backup)
    except Exception:
        if destination.exists() and backup.exists():
            shutil.rmtree(destination, ignore_errors=True)
            os.replace(backup, destination)
        raise
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        shutil.rmtree(backup, ignore_errors=True)


def parse_skill_name(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        raise InstallError(f"Missing YAML frontmatter: {skill_md}")
    name = NAME_LINE.search(match.group(1))
    if not name:
        raise InstallError(f"Missing skill name: {skill_md}")
    return name.group(1).strip().strip("\"'")


def rewrite_skill_name(skill_md: Path, new_name: str) -> None:
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match or not NAME_LINE.search(match.group(1)):
        raise InstallError(f"Cannot rewrite skill name in {skill_md}")
    front = NAME_LINE.sub(f"name: {new_name}", match.group(1), count=1)
    updated = "---\n" + front + "\n---\n" + text[match.end():]
    skill_md.write_text(updated, encoding="utf-8", newline="\n")


def plugin_skills(plugin_source: Path) -> list[tuple[str, Path]]:
    items: list[tuple[str, Path]] = []
    for directory in sorted((plugin_source / "skills").iterdir()):
        skill_md = directory / "SKILL.md"
        if directory.is_dir() and skill_md.is_file():
            items.append((parse_skill_name(skill_md), directory))
    if not items:
        raise InstallError(f"No installable skills found in {plugin_source / 'skills'}")
    return items


def select_skills(items: Sequence[tuple[str, Path]], profile: str) -> list[tuple[str, Path]]:
    if profile == "full":
        return list(items)
    gateway = {
        "pdo-start",
        "product-design-orchestrator",
        "skill-router",
        "project-inspector",
        "stack-inspector",
    }
    selected = [item for item in items if item[0] in gateway]
    missing = gateway - {name for name, _ in selected}
    if missing:
        raise InstallError(f"Orchestrated profile is missing gateway skills: {sorted(missing)}")
    return selected


def managed_block(body: str) -> str:
    return f"{MANAGED_START}\n{body.rstrip()}\n{MANAGED_END}"


def remove_managed_block_text(text: str) -> tuple[str, bool]:
    pattern = re.compile(
        rf"\n?{re.escape(MANAGED_START)}.*?{re.escape(MANAGED_END)}\n?",
        re.S,
    )
    updated, count = pattern.subn("\n", text)
    updated = re.sub(r"\n{3,}", "\n\n", updated).strip()
    return ((updated + "\n") if updated else "", count > 0)


def upsert_managed_block(path: Path, body: str, dry_run: bool) -> bool:
    existed = path.exists()
    original = path.read_text(encoding="utf-8") if existed else ""
    clean, _ = remove_managed_block_text(original)
    new_text = clean.rstrip()
    if new_text:
        new_text += "\n\n"
    new_text += managed_block(body) + "\n"
    if dry_run:
        print(f"DRY-RUN update guidance: {path}")
    else:
        write_text_atomic(path, new_text)
    return not existed


def remove_managed_block(path: Path, *, created_by_installer: bool, dry_run: bool) -> None:
    if not path.exists():
        return
    original = path.read_text(encoding="utf-8")
    updated, found = remove_managed_block_text(original)
    if not found:
        print(f"Warning: managed guidance markers not found in {path}; leaving it unchanged.")
        return
    if dry_run:
        print(f"DRY-RUN remove guidance block: {path}")
        return
    if not updated and created_by_installer:
        path.unlink()
    else:
        write_text_atomic(path, updated)


def codex_paths(ctx: Context, scope: str) -> tuple[Path, Path, Path | None]:
    if scope == "project":
        agents_root = ctx.project_root / ".agents"
        guidance_dir = ctx.project_root
        override = guidance_dir / "AGENTS.override.md"
        guidance = override if override.exists() else guidance_dir / "AGENTS.md"
    else:
        agents_root = ctx.home / ".agents"
        codex_home = Path(os.environ.get("CODEX_HOME", str(ctx.home / ".codex"))).expanduser().resolve()
        override = codex_home / "AGENTS.override.md"
        guidance = (override if override.exists() else codex_home / "AGENTS.md") if ctx.activate_global else None
    return agents_root / "skills", agents_root / PLUGIN_NAME, guidance


def claude_paths(ctx: Context, scope: str) -> tuple[Path, Path | None]:
    if scope == "project":
        plugin = ctx.project_root / ".claude" / "skills" / PLUGIN_NAME
        guidance = ctx.project_root / "CLAUDE.md"
    else:
        plugin = ctx.home / ".claude" / "skills" / PLUGIN_NAME
        guidance = (ctx.home / ".claude" / "CLAUDE.md") if ctx.activate_global else None
    return plugin, guidance


def codex_guidance(scope: str) -> str:
    location = (
        ".agents/product-design-orchestrator/"
        if scope == "project"
        else "~/.agents/product-design-orchestrator/"
    )
    return f"""## Product Design Orchestrator for Codex

For UI/UX, product design, product research, redesign, design-system, accessibility, or design-to-code work:

1. Start with `$pdo-start`.
2. Treat `{location}` as the local governance and reference bundle.
3. Follow its `AGENTS.md`; load `DESIGN.md`, `SOUL.md`, and `SKILLS.md` only as the task requires.
4. Inspect the existing product and stack before proposing changes.
5. Implement the approved design faithfully and verify the rendered result, states, responsiveness, and accessibility.

The installer owns only this marked block and the `pdo-*` skill directories it records."""


def claude_guidance(scope: str) -> str:
    command = "/product-design-orchestrator:pdo-start"
    location = (
        ".claude/skills/product-design-orchestrator/"
        if scope == "project"
        else "~/.claude/skills/product-design-orchestrator/"
    )
    extra = (
        "Launch Claude Code from the repository root so the project skills-directory plugin is discovered."
        if scope == "project"
        else "The personal skills-directory plugin is available across projects."
    )
    return f"""## Product Design Orchestrator for Claude Code

For UI/UX, product design, product research, redesign, design-system, accessibility, or design-to-code work:

1. Start with `{command}`.
2. Treat `{location}` as the local plugin and governance bundle.
3. Follow its `AGENTS.md`; load `DESIGN.md`, `SOUL.md`, and `SKILLS.md` only as the task requires.
4. Inspect the existing product and stack, then implement and visually verify the approved direction.
5. {extra}

The installer owns only this marked block and the plugin directory it records."""


def preflight_path(path: Path, *, ctx: Context, kind: str) -> None:
    if path.exists() and not is_owned(path) and not ctx.force:
        raise InstallError(
            f"Refusing to replace unmanaged {kind}: {path}\n"
            "Move it, choose another scope, or rerun with --force only after reviewing it."
        )


def preflight_codex(ctx: Context, scope: str) -> None:
    skills_root, bundle_dest, guidance_path = codex_paths(ctx, scope)
    if skills_root.exists() and not skills_root.is_dir():
        raise InstallError(f"Codex skills root is not a directory: {skills_root}")
    preflight_path(bundle_dest, ctx=ctx, kind="Codex resource bundle")
    for source_name, _ in select_skills(plugin_skills(ctx.plugin_source), ctx.profile):
        codex_name = source_name if source_name.startswith("pdo-") else f"pdo-{source_name}"
        preflight_path(skills_root / codex_name, ctx=ctx, kind="Codex skill directory")
    if guidance_path is not None and guidance_path.exists() and not guidance_path.is_file():
        raise InstallError(f"Codex guidance path is not a file: {guidance_path}")


def preflight_claude(ctx: Context, scope: str) -> None:
    plugin_dest, guidance_path = claude_paths(ctx, scope)
    preflight_path(plugin_dest, ctx=ctx, kind="Claude Code plugin directory")
    if guidance_path is not None and guidance_path.exists() and not guidance_path.is_file():
        raise InstallError(f"Claude Code guidance path is not a file: {guidance_path}")


def previous_receipt(path: Path) -> dict:
    if not path.is_file():
        return {}
    try:
        data = read_json(path)
        return data if data.get("product_id") == PRODUCT_ID else {}
    except Exception:
        return {}


def retire_previous_guidance(previous: dict, new_path: Path | None, *, ctx: Context) -> None:
    old_value = previous.get("guidance_path")
    if not old_value:
        return
    old_path = Path(old_value)
    if new_path is not None and old_path.resolve() == new_path.resolve() and not ctx.no_guidance:
        return
    remove_managed_block(
        old_path,
        created_by_installer=bool(previous.get("guidance_created")),
        dry_run=ctx.dry_run,
    )


def inherited_guidance_created(previous: dict, path: Path, newly_created: bool) -> bool:
    if newly_created:
        return True
    old_value = previous.get("guidance_path")
    if not old_value:
        return False
    try:
        same = Path(old_value).resolve() == path.resolve()
    except OSError:
        same = str(Path(old_value)) == str(path)
    return same and bool(previous.get("guidance_created"))


def install_codex(ctx: Context, scope: str) -> None:
    skills_root, bundle_dest, guidance_path = codex_paths(ctx, scope)
    items = select_skills(plugin_skills(ctx.plugin_source), ctx.profile)
    old_receipt = previous_receipt(bundle_dest / CODEX_RECEIPT)

    atomic_copytree(
        ctx.plugin_source,
        bundle_dest,
        ctx=ctx,
        component="codex-resource-bundle",
    )

    installed_skills: list[dict] = []
    for source_name, source_dir in items:
        codex_name = source_name if source_name.startswith("pdo-") else f"pdo-{source_name}"
        destination = skills_root / codex_name

        def transform(temp: Path, *, new_name: str = codex_name, original: str = source_name) -> None:
            rewrite_skill_name(temp / "SKILL.md", new_name)
            write_json_atomic(
                temp / MARKER_FILE,
                ownership_marker(ctx.version, "codex-skill", original),
            )

        atomic_copytree(
            source_dir,
            destination,
            ctx=ctx,
            component="codex-skill",
            transform=transform,
        )
        installed_skills.append(
            {
                "source_name": source_name,
                "installed_name": codex_name,
                "path": str(destination),
            }
        )

    active_paths = {item["path"] for item in installed_skills}
    for old_item in old_receipt.get("skills", []):
        old_path_value = old_item.get("path")
        if not old_path_value or old_path_value in active_paths:
            continue
        old_path = Path(old_path_value)
        if old_path.exists():
            if not is_owned(old_path) and not ctx.force:
                raise InstallError(f"Refusing to prune unmanaged former skill path: {old_path}")
            if ctx.dry_run:
                print(f"DRY-RUN remove stale Codex skill: {old_path}")
            else:
                shutil.rmtree(old_path)

    effective_guidance = guidance_path if guidance_path is not None and not ctx.no_guidance else None
    retire_previous_guidance(old_receipt, effective_guidance, ctx=ctx)
    guidance_created = False
    if effective_guidance is not None:
        newly_created = upsert_managed_block(
            effective_guidance, codex_guidance(scope), ctx.dry_run
        )
        guidance_created = inherited_guidance_created(old_receipt, effective_guidance, newly_created)

    receipt = {
        "product_id": PRODUCT_ID,
        "version": ctx.version,
        "agent": "codex",
        "scope": scope,
        "profile": ctx.profile,
        "installed_at": utc_now(),
        "package_source": str(ctx.package_root),
        "bundle_path": str(bundle_dest),
        "skills_root": str(skills_root),
        "skills": installed_skills,
        "guidance_path": str(effective_guidance) if effective_guidance else None,
        "guidance_created": guidance_created,
        "managed_marker": [MANAGED_START, MANAGED_END],
    }
    write_json_atomic(bundle_dest / CODEX_RECEIPT, receipt, ctx.dry_run)
    write_json_atomic(
        bundle_dest / "skill-name-map.json",
        {item["source_name"]: item["installed_name"] for item in installed_skills},
        ctx.dry_run,
    )
    print(
        f"Codex {scope} install {'planned' if ctx.dry_run else 'complete'}: "
        f"{len(installed_skills)} skills; bundle {bundle_dest}"
    )


def install_claude(ctx: Context, scope: str) -> None:
    plugin_dest, guidance_path = claude_paths(ctx, scope)
    old_receipt = previous_receipt(plugin_dest / CLAUDE_RECEIPT)
    atomic_copytree(
        ctx.plugin_source,
        plugin_dest,
        ctx=ctx,
        component="claude-skills-directory-plugin",
    )

    effective_guidance = guidance_path if guidance_path is not None and not ctx.no_guidance else None
    retire_previous_guidance(old_receipt, effective_guidance, ctx=ctx)
    guidance_created = False
    if effective_guidance is not None:
        newly_created = upsert_managed_block(
            effective_guidance, claude_guidance(scope), ctx.dry_run
        )
        guidance_created = inherited_guidance_created(old_receipt, effective_guidance, newly_created)

    receipt = {
        "product_id": PRODUCT_ID,
        "version": ctx.version,
        "agent": "claude",
        "scope": scope,
        "profile": "plugin-full",
        "installed_at": utc_now(),
        "package_source": str(ctx.package_root),
        "plugin_path": str(plugin_dest),
        "skill_count": len(plugin_skills(ctx.plugin_source)),
        "guidance_path": str(effective_guidance) if effective_guidance else None,
        "guidance_created": guidance_created,
        "managed_marker": [MANAGED_START, MANAGED_END],
    }
    write_json_atomic(plugin_dest / CLAUDE_RECEIPT, receipt, ctx.dry_run)
    print(
        f"Claude Code {scope} install {'planned' if ctx.dry_run else 'complete'}: "
        f"skills-directory plugin {plugin_dest}"
    )


def receipt_for(ctx: Context, agent: str, scope: str) -> Path:
    if agent == "codex":
        _, bundle, _ = codex_paths(ctx, scope)
        return bundle / CODEX_RECEIPT
    plugin, _ = claude_paths(ctx, scope)
    return plugin / CLAUDE_RECEIPT


def verify_codex(ctx: Context, scope: str) -> list[str]:
    errors: list[str] = []
    receipt_path = receipt_for(ctx, "codex", scope)
    if not receipt_path.is_file():
        return [f"Codex receipt not found: {receipt_path}"]
    try:
        receipt = read_json(receipt_path)
    except Exception as exc:
        return [f"Cannot parse Codex receipt: {exc}"]
    bundle = Path(receipt["bundle_path"])
    if not is_owned(bundle):
        errors.append(f"Codex bundle is missing ownership marker: {bundle}")
    for rel in [".codex-plugin/plugin.json", ".claude-plugin/plugin.json", "DESIGN.md", "SOUL.md", "SKILLS.md"]:
        if not (bundle / rel).is_file():
            errors.append(f"Codex bundle missing {rel}")
    for item in receipt.get("skills", []):
        path = Path(item["path"])
        skill_md = path / "SKILL.md"
        if not is_owned(path):
            errors.append(f"Codex skill missing ownership marker: {path}")
            continue
        if not skill_md.is_file():
            errors.append(f"Codex skill missing SKILL.md: {path}")
            continue
        try:
            actual = parse_skill_name(skill_md)
        except Exception as exc:
            errors.append(str(exc))
            continue
        if actual != item["installed_name"]:
            errors.append(f"Codex skill name mismatch: {path}: {actual} != {item['installed_name']}")
    guidance = receipt.get("guidance_path")
    if guidance:
        path = Path(guidance)
        if not path.is_file() or MANAGED_START not in path.read_text(encoding="utf-8"):
            errors.append(f"Codex managed guidance missing: {path}")
    return errors


def verify_claude(ctx: Context, scope: str) -> list[str]:
    errors: list[str] = []
    receipt_path = receipt_for(ctx, "claude", scope)
    if not receipt_path.is_file():
        return [f"Claude Code receipt not found: {receipt_path}"]
    try:
        receipt = read_json(receipt_path)
    except Exception as exc:
        return [f"Cannot parse Claude Code receipt: {exc}"]
    plugin = Path(receipt["plugin_path"])
    if not is_owned(plugin):
        errors.append(f"Claude Code plugin is missing ownership marker: {plugin}")
    for rel in [".claude-plugin/plugin.json", ".codex-plugin/plugin.json", "skills/pdo-start/SKILL.md", "DESIGN.md", "SOUL.md"]:
        if not (plugin / rel).is_file():
            errors.append(f"Claude Code plugin missing {rel}")
    actual_count = len(plugin_skills(plugin)) if (plugin / "skills").is_dir() else 0
    if actual_count != receipt.get("skill_count"):
        errors.append(
            f"Claude Code skill count mismatch: {actual_count} != {receipt.get('skill_count')}"
        )
    guidance = receipt.get("guidance_path")
    if guidance:
        path = Path(guidance)
        if not path.is_file() or MANAGED_START not in path.read_text(encoding="utf-8"):
            errors.append(f"Claude Code managed guidance missing: {path}")
    return errors


def remove_empty_parents(path: Path, stop: Path) -> None:
    current = path
    while current != stop and current.exists():
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent


def uninstall_codex(ctx: Context, scope: str) -> None:
    receipt_path = receipt_for(ctx, "codex", scope)
    if not receipt_path.is_file():
        print(f"Codex is not recorded as installed at {receipt_path}")
        return
    receipt = read_json(receipt_path)
    for item in receipt.get("skills", []):
        path = Path(item["path"])
        if path.exists():
            if not is_owned(path) and not ctx.force:
                raise InstallError(f"Refusing to remove unmanaged skill path: {path}")
            if ctx.dry_run:
                print(f"DRY-RUN remove: {path}")
            else:
                shutil.rmtree(path)
    guidance = receipt.get("guidance_path")
    if guidance:
        remove_managed_block(
            Path(guidance),
            created_by_installer=bool(receipt.get("guidance_created")),
            dry_run=ctx.dry_run,
        )
    bundle = Path(receipt["bundle_path"])
    if bundle.exists():
        if not is_owned(bundle) and not ctx.force:
            raise InstallError(f"Refusing to remove unmanaged bundle: {bundle}")
        if ctx.dry_run:
            print(f"DRY-RUN remove: {bundle}")
        else:
            shutil.rmtree(bundle)
    if not ctx.dry_run:
        skills_root = Path(receipt["skills_root"])
        remove_empty_parents(skills_root, skills_root.parent.parent)
    print(f"Codex {scope} uninstall {'planned' if ctx.dry_run else 'complete'}")


def uninstall_claude(ctx: Context, scope: str) -> None:
    receipt_path = receipt_for(ctx, "claude", scope)
    if not receipt_path.is_file():
        print(f"Claude Code is not recorded as installed at {receipt_path}")
        return
    receipt = read_json(receipt_path)
    guidance = receipt.get("guidance_path")
    if guidance:
        remove_managed_block(
            Path(guidance),
            created_by_installer=bool(receipt.get("guidance_created")),
            dry_run=ctx.dry_run,
        )
    plugin = Path(receipt["plugin_path"])
    if plugin.exists():
        if not is_owned(plugin) and not ctx.force:
            raise InstallError(f"Refusing to remove unmanaged plugin: {plugin}")
        if ctx.dry_run:
            print(f"DRY-RUN remove: {plugin}")
        else:
            shutil.rmtree(plugin)
            remove_empty_parents(plugin.parent, plugin.parent.parent.parent)
    print(f"Claude Code {scope} uninstall {'planned' if ctx.dry_run else 'complete'}")


def show_status(ctx: Context, agents: Iterable[str], scope: str) -> int:
    found = 0
    for agent in agents:
        receipt = receipt_for(ctx, agent, scope)
        if receipt.is_file():
            data = read_json(receipt)
            found += 1
            primary = data.get("bundle_path") or data.get("plugin_path")
            print(f"{agent}: installed {data.get('version')} ({data.get('scope')}) at {primary}")
        else:
            print(f"{agent}: not installed for {scope} scope ({receipt})")
    return 0 if found else 1


def choose_agents(value: str) -> list[str]:
    return ["codex", "claude"] if value == "both" else [value]


def package_context(args: argparse.Namespace) -> Context:
    package_root = Path(__file__).resolve().parents[1]
    plugin_source = package_root / "integrations" / "product-design-orchestrator-plugin"
    if not plugin_source.is_dir():
        raise InstallError(
            f"Agent plugin bundle is missing: {plugin_source}. "
            "The archive may be incomplete."
        )
    version_path = package_root / "VERSION"
    if not version_path.is_file():
        raise InstallError(f"Missing VERSION file: {version_path}")
    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        raise InstallError(f"Project path is not a directory: {project}")
    return Context(
        package_root=package_root,
        plugin_source=plugin_source,
        version=version_path.read_text(encoding="utf-8").strip(),
        project_root=project,
        home=Path.home().resolve(),
        dry_run=bool(getattr(args, "dry_run", False)),
        force=bool(getattr(args, "force", False)),
        no_guidance=bool(getattr(args, "no_guidance", False)),
        activate_global=bool(getattr(args, "activate_global", False)),
        profile=getattr(args, "profile", "full"),
    )


def add_common(parser: argparse.ArgumentParser, *, mutating: bool = False) -> None:
    parser.add_argument("--agent", choices=["codex", "claude", "both"], default="both")
    parser.add_argument("--scope", choices=["project", "user"], default="project")
    parser.add_argument("--project", default=".", help="Project root for project-scope installs (default: current directory)")
    if mutating:
        parser.add_argument("--dry-run", action="store_true", help="Print planned changes without writing files")
        parser.add_argument("--force", action="store_true", help="Replace/remove conflicting unmanaged PDO paths")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Safely install the Product Design Orchestrator for Codex and Claude Code."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    install = sub.add_parser("install", help="Install or update agent skills and guidance")
    add_common(install, mutating=True)
    install.add_argument(
        "--profile",
        choices=["full", "orchestrated"],
        default="full",
        help="Codex native skills: all skills, or a context-light gateway set; Claude always receives the full plugin",
    )
    install.add_argument(
        "--no-guidance",
        action="store_true",
        help="Do not add a managed AGENTS.md/CLAUDE.md activation block",
    )
    install.add_argument(
        "--activate-global",
        action="store_true",
        help="For user scope, also add a managed global AGENTS.md/CLAUDE.md block",
    )

    verify = sub.add_parser("verify", help="Verify a recorded installation")
    add_common(verify)

    status = sub.add_parser("status", help="Show installation status")
    add_common(status)

    uninstall = sub.add_parser("uninstall", help="Remove only files recorded by this installer")
    add_common(uninstall, mutating=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        ctx = package_context(args)
        agents = choose_agents(args.agent)
        if args.command == "install":
            # Validate every requested destination before changing any of them so
            # a conflict in one agent cannot leave a partially installed pair.
            for agent in agents:
                if agent == "codex":
                    preflight_codex(ctx, args.scope)
                else:
                    preflight_claude(ctx, args.scope)
            for agent in agents:
                if agent == "codex":
                    install_codex(ctx, args.scope)
                else:
                    install_claude(ctx, args.scope)
            if not ctx.dry_run:
                print("Run the verify command next, then restart Codex or run /reload-plugins in Claude Code.")
            return 0
        if args.command == "verify":
            errors: list[str] = []
            for agent in agents:
                current = verify_codex(ctx, args.scope) if agent == "codex" else verify_claude(ctx, args.scope)
                if current:
                    errors.extend(f"{agent}: {message}" for message in current)
                else:
                    print(f"{agent}: verification passed")
            if errors:
                for error in errors:
                    print(f"ERROR: {error}", file=sys.stderr)
                return 1
            return 0
        if args.command == "status":
            return show_status(ctx, agents, args.scope)
        if args.command == "uninstall":
            for agent in agents:
                if agent == "codex":
                    uninstall_codex(ctx, args.scope)
                else:
                    uninstall_claude(ctx, args.scope)
            return 0
        raise AssertionError(args.command)
    except InstallError as exc:
        print(f"Installation error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
