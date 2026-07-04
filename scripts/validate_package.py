#!/usr/bin/env python3
"""Validate structure, skill metadata, registries, agent adapters, scripts, and links."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import py_compile
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
KEY = re.compile(r"^([a-zA-Z0-9_-]+):\s*(.*)$")
IGNORED_MANIFEST_PARTS = {".git", ".serena", "__pycache__"}
IGNORED_MANIFEST_NAMES = {".DS_Store", "MANIFEST.json", "CHECKSUMS.sha256"}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONT.match(text)
    if not match:
        return {}
    result = {}
    for line in match.group(1).splitlines():
        key_match = KEY.match(line)
        if key_match:
            result[key_match.group(1)] = key_match.group(2).strip().strip('"\'')
    return result


def load_json(path: Path, errors: list[str], label: str) -> dict | list:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{label} parse: {exc}")
        return {}


def is_manifest_file(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return (
        path.is_file()
        and not (set(rel.parts) & IGNORED_MANIFEST_PARTS)
        and path.name not in IGNORED_MANIFEST_NAMES
        and path.suffix != ".pyc"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--smoke-install", action="store_true", help="also run isolated installer smoke tests")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    required = [
        "AGENTS.md",
        "CLAUDE.md",
        "DESIGN.md",
        "SOUL.md",
        "SKILLS.md",
        "SELF_INSTALL.md",
        "README.md",
        "LICENSE",
        "VERSION",
        "self-install.sh",
        "self-install.ps1",
        "self-install.cmd",
        "registry/all-skills.json",
        "scripts/skill.py",
        "scripts/new_design_project.py",
        "scripts/agent_install.py",
        "scripts/build_agent_bundle.py",
        "scripts/test_agent_install.py",
        "integrations/product-design-orchestrator-plugin/.codex-plugin/plugin.json",
        "integrations/product-design-orchestrator-plugin/.claude-plugin/plugin.json",
        ".agents/plugins/marketplace.json",
        ".claude-plugin/marketplace.json",
        "resources/AGENT_PLATFORM_RESEARCH.md",
    ]
    for rel in required:
        if not (root / rel).exists():
            errors.append(f"missing {rel}")

    version = (root / "VERSION").read_text(encoding="utf-8").strip() if (root / "VERSION").is_file() else ""
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append(f"invalid VERSION: {version!r}")

    registry_path = root / "registry" / "all-skills.json"
    registry = load_json(registry_path, errors, "registry") if registry_path.exists() else []
    if not isinstance(registry, list):
        errors.append("registry root must be a list")
        registry = []
    ids = [item.get("id") for item in registry if isinstance(item, dict)]
    if len(ids) != len(set(ids)):
        errors.append("duplicate registry ids")
    for item in registry:
        if not isinstance(item, dict):
            errors.append("non-object registry entry")
            continue
        if item.get("path") and not (root / item["path"]).exists():
            errors.append(f"registry path missing: {item.get('id')} -> {item['path']}")
        if item.get("url") and not item["url"].startswith("https://"):
            errors.append(f"non-HTTPS source: {item.get('id')}")

    skill_files = sorted((root / "skills").glob("**/SKILL.md"))
    names: list[str] = []
    for path in skill_files:
        metadata = frontmatter(path)
        if not metadata.get("name"):
            errors.append(f"missing frontmatter name: {path.relative_to(root)}")
        if not metadata.get("description"):
            errors.append(f"missing frontmatter description: {path.relative_to(root)}")
        if metadata.get("name"):
            names.append(metadata["name"])
    if len(names) != len(set(names)):
        errors.append("duplicate canonical skill names")

    local_skill_files = [path for path in skill_files if "vendor" not in path.parts]
    local_names = [frontmatter(path).get("name") for path in local_skill_files]
    duplicate_local = [name for name, count in Counter(local_names).items() if name and count > 1]
    if duplicate_local:
        errors.append(f"duplicate original skill names: {duplicate_local}")
    if len(skill_files) != 69:
        errors.append(f"canonical skill count mismatch: {len(skill_files)} != 69")
    if len(local_skill_files) != 67:
        errors.append(f"original skill count mismatch: {len(local_skill_files)} != 67")

    plugin = root / "integrations" / "product-design-orchestrator-plugin"
    plugin_skill_files = sorted((plugin / "skills").glob("*/SKILL.md")) if plugin.exists() else []
    plugin_names: list[str] = []
    for path in plugin_skill_files:
        metadata = frontmatter(path)
        if not metadata.get("name") or not metadata.get("description"):
            errors.append(f"invalid plugin skill frontmatter: {path.relative_to(root)}")
        elif metadata["name"] != path.parent.name:
            errors.append(f"plugin skill directory/name mismatch: {path.relative_to(root)} -> {metadata['name']}")
        plugin_names.append(metadata.get("name"))
    expected_plugin_names = set(names) | {"pdo-start"}
    if set(plugin_names) != expected_plugin_names:
        missing = sorted(expected_plugin_names - set(plugin_names))
        extra = sorted(set(plugin_names) - expected_plugin_names)
        errors.append(f"plugin skill set mismatch; missing={missing}, extra={extra}")
    if len(plugin_skill_files) != len(expected_plugin_names):
        errors.append(f"plugin skill count mismatch: {len(plugin_skill_files)} != {len(expected_plugin_names)}")

    for manifest_rel in [
        "integrations/product-design-orchestrator-plugin/.codex-plugin/plugin.json",
        "integrations/product-design-orchestrator-plugin/.claude-plugin/plugin.json",
    ]:
        path = root / manifest_rel
        manifest = load_json(path, errors, manifest_rel) if path.exists() else {}
        if isinstance(manifest, dict):
            if manifest.get("name") != "product-design-orchestrator":
                errors.append(f"wrong plugin name in {manifest_rel}")
            if manifest.get("version") != version:
                errors.append(f"plugin version mismatch in {manifest_rel}")
            if manifest.get("skills") != "./skills/":
                errors.append(f"plugin skills path mismatch in {manifest_rel}")

    claude_market = root / ".claude-plugin" / "marketplace.json"
    codex_market = root / ".agents" / "plugins" / "marketplace.json"

    claude_data = load_json(claude_market, errors, "Claude marketplace") if claude_market.exists() else {}
    if isinstance(claude_data, dict):
        if not isinstance(claude_data.get("owner"), dict) or not claude_data["owner"].get("name"):
            errors.append("Claude marketplace owner.name is required")
        plugins = claude_data.get("plugins")
        if not isinstance(plugins, list) or len(plugins) != 1:
            errors.append("Claude marketplace must contain exactly one plugin")
        else:
            entry = plugins[0]
            rel = entry.get("source")
            if not isinstance(rel, str) or not rel.startswith("./") or not (root / rel[2:]).is_dir():
                errors.append(f"Claude marketplace has invalid local source path: {rel}")
            if entry.get("version") != version:
                errors.append("Claude marketplace plugin version mismatch")

    codex_data = load_json(codex_market, errors, "Codex marketplace") if codex_market.exists() else {}
    if isinstance(codex_data, dict):
        if not isinstance(codex_data.get("interface"), dict) or not codex_data["interface"].get("displayName"):
            errors.append("Codex marketplace interface.displayName is required")
        plugins = codex_data.get("plugins")
        if not isinstance(plugins, list) or len(plugins) != 1:
            errors.append("Codex marketplace must contain exactly one plugin")
        else:
            entry = plugins[0]
            source = entry.get("source")
            rel = source.get("path") if isinstance(source, dict) else None
            if not isinstance(source, dict) or source.get("source") != "local":
                errors.append("Codex marketplace source must be a local source object")
            if not isinstance(rel, str) or not rel.startswith("./") or not (root / rel[2:]).is_dir():
                errors.append(f"Codex marketplace has invalid local source path: {rel}")
            policy = entry.get("policy")
            if not isinstance(policy, dict) or policy.get("installation") not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
                errors.append("Codex marketplace has invalid policy.installation")
            if not isinstance(policy, dict) or policy.get("authentication") not in {"ON_INSTALL", "ON_FIRST_USE"}:
                errors.append("Codex marketplace has invalid policy.authentication")
            if not entry.get("category"):
                errors.append("Codex marketplace category is required")

    if (root / "CLAUDE.md").is_file() and "@AGENTS.md" not in (root / "CLAUDE.md").read_text(encoding="utf-8"):
        errors.append("CLAUDE.md does not import AGENTS.md")

    for script in (root / "scripts").glob("*.py"):
        try:
            py_compile.compile(str(script), doraise=True)
        except Exception as exc:
            errors.append(f"compile {script.name}: {exc}")

    if len(list((root / "templates").glob("*.md"))) < 12:
        errors.append("fewer than 12 templates")
    if len(list((root / "playbooks").glob("*.md"))) < 6:
        errors.append("fewer than 6 playbooks")

    if any(path.is_symlink() for path in root.rglob("*")):
        errors.append("package contains symlinks; portable archive must contain real files")

    for forbidden in ["hooks", "agents", "bin", "monitors", ".mcp.json", ".lsp.json", "settings.json"]:
        if (plugin / forbidden).exists():
            errors.append(f"portable plugin unexpectedly contains executable/config component: {forbidden}")
    if os.name != "nt" and (root / "self-install.sh").exists() and not os.access(root / "self-install.sh", os.X_OK):
        errors.append("self-install.sh is not executable")

    manifest_path = root / "MANIFEST.json"
    checksums_path = root / "CHECKSUMS.sha256"
    if manifest_path.exists():
        manifest = load_json(manifest_path, errors, "manifest")
        if isinstance(manifest, dict):
            if manifest.get("version") != version:
                errors.append("manifest version mismatch")
            entries = manifest.get("files", [])
            if not isinstance(entries, list):
                errors.append("manifest files must be an array")
                entries = []
            expected_paths = {
                path.relative_to(root).as_posix()
                for path in root.rglob("*")
                if is_manifest_file(path, root)
            }
            manifest_paths = {entry.get("path") for entry in entries if isinstance(entry, dict)}
            if manifest_paths != expected_paths:
                errors.append(
                    f"manifest coverage mismatch; missing={sorted(expected_paths - manifest_paths)[:10]}, "
                    f"extra={sorted(manifest_paths - expected_paths)[:10]}"
                )
            if manifest.get("file_count") != len(entries):
                errors.append("manifest file_count mismatch")
            checksum_lines: list[str] = []
            for entry in entries:
                if not isinstance(entry, dict):
                    errors.append("manifest contains non-object entry")
                    continue
                rel = entry.get("path", "")
                target = root / rel
                if not target.exists():
                    errors.append(f"manifest file missing: {rel}")
                    continue
                digest = hashlib.sha256(target.read_bytes()).hexdigest()
                checksum_lines.append(f"{digest}  {rel}")
                if digest != entry.get("sha256"):
                    errors.append(f"manifest hash mismatch: {rel}")
                if target.stat().st_size != entry.get("bytes"):
                    errors.append(f"manifest size mismatch: {rel}")
            if checksums_path.is_file():
                actual_lines = [line.rstrip() for line in checksums_path.read_text(encoding="utf-8").splitlines() if line.strip()]
                if actual_lines != checksum_lines:
                    errors.append("CHECKSUMS.sha256 does not match MANIFEST.json order/content")
            else:
                errors.append("missing CHECKSUMS.sha256")

    link_re = re.compile(r"\[[^\]]+\]\((?!https?://|#|mailto:)([^)]+)\)")
    for markdown in root.glob("**/*.md"):
        for target in link_re.findall(markdown.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if not target:
                continue
            candidate = (markdown.parent / target).resolve()
            if not candidate.exists():
                warnings.append(f"unresolved link {markdown.relative_to(root)} -> {target}")

    if args.smoke_install and not errors:
        result = subprocess.run(
            [sys.executable, str(root / "scripts" / "test_agent_install.py")],
            text=True,
            capture_output=True,
        )
        if result.returncode:
            errors.append(f"installer smoke test failed:\n{result.stdout}\n{result.stderr}")

    print(f"Root: {root}")
    print(f"Files: {sum(1 for path in root.rglob('*') if path.is_file())}")
    print(f"Canonical SKILL.md files: {len(skill_files)} ({len(local_skill_files)} original, {len(skill_files) - len(local_skill_files)} vendor)")
    print(f"Portable plugin skills: {len(plugin_skill_files)}")
    print(f"Registry entries: {len(registry)}")
    print(f"Templates: {len(list((root / 'templates').glob('*.md')))}")
    print(f"Playbooks: {len(list((root / 'playbooks').glob('*.md')))}")
    if args.smoke_install:
        print("Installer smoke test: requested")
    if warnings:
        print(f"Warnings: {len(warnings)}")
        for warning in warnings[:20]:
            print(f"  ! {warning}")
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        raise SystemExit(1)
    print("Validation passed")


if __name__ == "__main__":
    main()
