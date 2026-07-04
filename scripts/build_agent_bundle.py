#!/usr/bin/env python3
"""Regenerate the self-contained Codex/Claude Code plugin adapter."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "integrations" / "product-design-orchestrator-plugin"
FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
NAME = re.compile(r"^name:\s*(.*?)\s*$", re.M)


def skill_name(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = FRONT.match(text)
    if not match:
        raise RuntimeError(f"Missing frontmatter: {path}")
    name = NAME.search(match.group(1))
    if not name:
        raise RuntimeError(f"Missing name: {path}")
    return name.group(1).strip().strip("\"'")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def copy_file(rel: str) -> None:
    src = ROOT / rel
    dst = DEST / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if DEST.exists():
        shutil.rmtree(DEST)
    (DEST / "skills").mkdir(parents=True)

    # Canonical governance and self-contained resources. Marketplace caches may
    # not resolve files outside the plugin directory, so everything needed at
    # runtime is copied here.
    for rel in [
        "AGENTS.md",
        "CLAUDE.md",
        "DESIGN.md",
        "SOUL.md",
        "SKILLS.md",
        "FIND_A_SKILL.md",
        "QUICKSTART.md",
        "LICENSE",
        "NOTICE",
        "VERSION",
        "CHANGELOG.md",
    ]:
        copy_file(rel)
    # The portable plugin is already installed when these copies are read, so
    # replace package-root self-install instructions with adapter-specific
    # management guidance and avoid references to a missing installer script.
    agent_text = (DEST / "AGENTS.md").read_text(encoding="utf-8")
    agent_text = re.sub(
        r"### Agent self-install entrypoint\n.*?(?=\n## 2\. Authority order)",
        "### Installed adapter status\n\nThis is an installed plugin/resource bundle. Do not try to reinstall it from this directory. Use the source archive's `scripts/agent_install.py` or the platform's plugin manager for updates and removal. For design work, continue with the authority order and boot sequence below.\n",
        agent_text,
        flags=re.S,
    )
    (DEST / "AGENTS.md").write_text(agent_text, encoding="utf-8", newline="\n")
    (DEST / "CLAUDE.md").write_text(
        "@AGENTS.md\n\n# Claude Code plugin adapter\n\nBegin meaningful UI/UX and design-to-code work with `/product-design-orchestrator:pdo-start`. `DESIGN.md` controls method; `SOUL.md` is subordinate to it.\n",
        encoding="utf-8",
        newline="\n",
    )

    for directory in ["playbooks", "templates", "registry", "resources"]:
        shutil.copytree(ROOT / directory, DEST / directory)
    (DEST / "scripts").mkdir()
    for name in ["skill.py", "new_design_project.py"]:
        shutil.copy2(ROOT / "scripts" / name, DEST / "scripts" / name)

    names: list[str] = []
    for source_md in sorted((ROOT / "skills").glob("**/SKILL.md")):
        name = skill_name(source_md)
        if name in names:
            raise RuntimeError(f"Duplicate skill name: {name}")
        names.append(name)
        source_dir = source_md.parent
        destination = DEST / "skills" / name
        shutil.copytree(source_dir, destination)

    gateway = DEST / "skills" / "pdo-start"
    gateway.mkdir()
    (gateway / "SKILL.md").write_text(
        """---
name: pdo-start
description: Mandatory gateway for UI/UX, product design, redesign, research, design systems, accessibility, prototyping, or design-to-code work. Load the Product Design Orchestrator governance, inspect the actual project, choose the lightest safe lifecycle, and route to the right specialist skills.
---

# Product Design Orchestrator — Start

Use this skill before meaningful product-design or UI implementation work.

## 1. Locate the governance bundle

The bundle is self-contained. Resolve the first location that exists:

1. The plugin root two directories above this `SKILL.md`.
2. `../../product-design-orchestrator/` relative to a Codex-installed `pdo-start` skill.
3. The project's `.agents/product-design-orchestrator/` directory.
4. The project's `.claude/skills/product-design-orchestrator/` directory.
5. The personal equivalents under `~/.agents/` or `~/.claude/skills/`.

Do not guess policy from this gateway alone. Read the located `AGENTS.md`. For a meaningful design task, then read the relevant parts of `DESIGN.md` and `SOUL.md`; use `SKILLS.md` to route expertise. `DESIGN.md` controls method and evidence. `SOUL.md` controls professional presence and never overrides it.

## 2. Orient before acting

- Inspect the repository, active stack, routes, components, tokens, assets, copy, tests, screenshots, analytics, and existing `.design/` evidence.
- State a compact Design Read: surface, audience, job, risk, desired character, and implementation context.
- Choose the lightest lifecycle that is safe and useful.
- Route to one precise specialist skill, two for genuinely distinct angles, or at most three simultaneous craft skills for a broad review.

## 3. Keep design and implementation continuous

The same agent owns intent and code. Preserve product contracts and platform conventions, define complete states and responsive behavior, implement in vertical slices, render the result, compare it with the approved direction or reference, and correct visible deviations.

Never describe code completion as design completion without rendered verification. Never invent research, validation, accessibility conformance, or test results.

## 4. Finish with evidence

Report the Design Read, skills used, evidence and assumptions, decisions, implementation, states/viewports verified, checks performed, deviations, and remaining uncertainty.
""",
        encoding="utf-8",
        newline="\n",
    )
    names.append("pdo-start")

    codex_manifest = {
        "name": "product-design-orchestrator",
        "version": version,
        "description": "Research, design, implement, and verify professional UI/UX with a routed product-design skill system.",
        "author": {"name": "Product Design Orchestrator contributors"},
        "keywords": ["product-design", "ux", "ui", "design-systems", "design-to-code", "accessibility"],
        "skills": "./skills/",
        "interface": {
            "displayName": "Product Design Orchestrator",
            "shortDescription": "Professional product design and design-to-code workflows",
            "longDescription": "A self-contained product-design operating system with routed research, strategy, experience, visual, implementation, and QA skills.",
            "developerName": "Product Design Orchestrator contributors",
            "category": "Productivity",
            "capabilities": ["Read", "Write"],
            "defaultPrompt": [
                "Use the Product Design Orchestrator to inspect, design, implement, and verify this UI.",
                "Run pdo-start and route the right product-design skills for this task."
            ],
            "brandColor": "#1457C5"
        }
    }
    claude_manifest = {
        "name": "product-design-orchestrator",
        "displayName": "Product Design Orchestrator",
        "version": version,
        "description": "Professional product-design, UX research, visual design, design-to-code, and verification skills.",
        "author": {"name": "Product Design Orchestrator contributors"},
        "keywords": ["product-design", "ux", "ui", "design-systems", "accessibility", "frontend"],
        "skills": "./skills/"
    }
    write_json(DEST / ".codex-plugin" / "plugin.json", codex_manifest)
    write_json(DEST / ".claude-plugin" / "plugin.json", claude_manifest)
    write_json(
        DEST / ".pdo-managed.json",
        {
            "product_id": "professional-product-design-orchestrator",
            "version": version,
            "component": "portable-agent-plugin-source",
            "managed": True,
        },
    )
    write_json(
        DEST / "SKILL_INDEX.json",
        {"version": version, "skill_count": len(names), "skills": sorted(names)},
    )

    (DEST / "CLAUDE_CONTEXT.md").write_text(
        """# Product Design Orchestrator context

For meaningful UI/UX, product-design, redesign, design-system, accessibility, or design-to-code work, begin with `/product-design-orchestrator:pdo-start`.

`DESIGN.md` is the controlling method. `SOUL.md` shapes professional presence but cannot override evidence, safety, accessibility, platform, or implementation rules. Inspect the existing repository before choosing a stack or visual language. Route only the smallest relevant specialist set, implement the chosen direction faithfully, and verify the rendered experience across required states and viewports.
""",
        encoding="utf-8",
        newline="\n",
    )
    (DEST / "README.md").write_text(
        f"""# Product Design Orchestrator agent plugin {version}

This generated directory is a self-contained plugin for Claude Code and Codex. It contains both official manifest formats, a flat `skills/` directory with {len(names)} skills, and all governance/resources required after marketplace caching or direct installation.

Start with:

- Claude Code: `/product-design-orchestrator:pdo-start`
- Codex plugin: mention `pdo-start` or select it from skills
- Codex direct installation: `$pdo-start`

Regenerate from the package root with `python scripts/build_agent_bundle.py`.
""",
        encoding="utf-8",
        newline="\n",
    )

    # Local marketplace catalogs. Each platform has its own documented schema.
    write_json(
        ROOT / ".claude-plugin" / "marketplace.json",
        {
            "name": "product-design-orchestrator-local",
            "owner": {"name": "Product Design Orchestrator contributors"},
            "description": "Local offline marketplace for the Product Design Orchestrator plugin.",
            "version": version,
            "plugins": [
                {
                    "name": "product-design-orchestrator",
                    "displayName": "Product Design Orchestrator",
                    "source": "./integrations/product-design-orchestrator-plugin",
                    "description": "Professional product-design and design-to-code orchestration.",
                    "version": version,
                    "category": "design",
                    "tags": ["ui", "ux", "research", "frontend", "accessibility"]
                }
            ]
        },
    )
    write_json(
        ROOT / ".agents" / "plugins" / "marketplace.json",
        {
            "name": "product-design-orchestrator-local",
            "interface": {"displayName": "Product Design Orchestrator Local"},
            "plugins": [
                {
                    "name": "product-design-orchestrator",
                    "source": {
                        "source": "local",
                        "path": "./integrations/product-design-orchestrator-plugin"
                    },
                    "policy": {
                        "installation": "AVAILABLE",
                        "authentication": "ON_INSTALL"
                    },
                    "category": "Productivity"
                }
            ]
        },
    )
    print(f"Built {DEST} with {len(names)} skills")


if __name__ == "__main__":
    main()
