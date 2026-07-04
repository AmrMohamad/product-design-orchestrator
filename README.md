# Product Design Orchestrator v4.1

A repository-level operating system for an AI agent that must **research, design, implement, verify, and improve** digital products with the judgment of a multidisciplinary product-design team.

It is built to prevent two common failures: a huge rulebook that produces ceremonial output, and attractive code that was never proved as a usable, faithful product experience.

## Package layers

- `AGENTS.md` — boot and operating instructions for a coding/design agent.
- `CLAUDE.md` — Claude Code bridge that imports `AGENTS.md` and exposes safe self-install behavior.
- `DESIGN.md` — controlling product-design, research, design-to-code, and quality protocol.
- `SOUL.md` — professional Product Designer / Design Engineer character, controlled by `DESIGN.md`.
- `SKILLS.md` — skill-routing and safe acquisition policy.
- `skills/` — 67 original specialist skills plus 2 preserved upstream reference skills.
- `integrations/product-design-orchestrator-plugin/` — generated flat, self-contained plugin accepted by Claude Code and Codex.
- `registry/` — searchable index of 192 local and external entries, including all 110 researched UI Skills catalog records.
- `playbooks/` — end-to-end routes for greenfield, feature, redesign, reference-to-code, design systems, research, live optimization, high-risk services, and fast polish.
- `templates/` — durable `.design/<slug>/` evidence, decision, design, implementation, and QA artifacts.
- `scripts/skill.py` — finds/recommends skills and can safely download reviewed Markdown without executing it.
- `scripts/new_design_project.py` — creates a proportional project workspace.
- `scripts/agent_install.py` — local-only, reversible installer for Codex and Claude Code.
- `scripts/validate_package.py` — validates structure, metadata, registry, plugins, and scripts.
- `resources/` — research synthesis, official platform-integration research, sources, complete upstream catalog, prior-skill crosswalk, stack adaptation, licensing, and reading map.

## Self-install for Codex and Claude Code

From the extracted package root, preview and install into the current project:

```bash
python scripts/agent_install.py install --agent both --scope project --project . --dry-run
python scripts/agent_install.py install --agent both --scope project --project .
python scripts/agent_install.py verify  --agent both --scope project --project .
```

The same install step is available through `self-install.sh`, `self-install.ps1`, and `self-install.cmd`. Read [`SELF_INSTALL.md`](SELF_INSTALL.md) for user-wide installation, context-light Codex installation, native marketplace alternatives, updates, verification, and uninstall.

The installer follows the platforms' documented conventions:

- Codex project/user skills under `.agents/skills/` or `~/.agents/skills/`, with concise `AGENTS.md` activation.
- Claude Code project/user skills-directory plugin under `.claude/skills/product-design-orchestrator/` or `~/.claude/skills/product-design-orchestrator/`, with concise `CLAUDE.md` activation.

It never downloads content, calls a package manager, or silently overwrites unrelated skill directories.

## Manual start without installation

Place this package at a project root, then instruct the agent:

```text
Read AGENTS.md, DESIGN.md, and SOUL.md. Inspect the repository and existing .design artifacts. State the Design Read, choose the lightest safe lifecycle, load the smallest relevant skill set, then research/design/implement and verify the rendered experience.
```

Find skills:

```bash
python scripts/skill.py search "accessible onboarding form in Next.js"
python scripts/skill.py recommend --phase implement --stack nextjs --task "rebuild this approved screen pixel accurately"
python scripts/skill.py list --category visual-design
python scripts/skill.py show bundled/anti-slop-taste
python scripts/skill.py doctor
```

Create project memory:

```bash
python scripts/new_design_project.py --slug account-onboarding --mode feature
```

Validate package and installer:

```bash
python scripts/test_agent_install.py
python scripts/validate_package.py
```

## Governing idea

Make the product feel as though a real team paid attention: to the underlying decision, the person and context, the complete journey, the visual thesis, the actual codebase, every meaningful state, and the evidence visible in the rendered result.
