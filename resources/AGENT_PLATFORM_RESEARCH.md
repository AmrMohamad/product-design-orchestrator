# Codex and Claude Code integration research

Research date: 2026-06-25. Only official OpenAI and Anthropic documentation was used for platform behavior.

## OpenAI Codex decisions

Official sources:

- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/guides/agents-md
- https://developers.openai.com/codex/plugins
- https://developers.openai.com/codex/plugins/build
- https://developers.openai.com/codex/config-basic
- https://developers.openai.com/codex/permissions

Relevant documented behavior:

- A skill is a directory containing `SKILL.md` with `name` and `description`; optional scripts, references, assets, and agent metadata may accompany it.
- Repository skills are discovered from `.agents/skills` between the current working directory and repository root. Personal skills live in `~/.agents/skills`.
- Codex reads `AGENTS.md` before work. It builds a chain from global Codex home guidance and project-root-to-current-directory guidance, preferring `AGENTS.override.md` over `AGENTS.md` in a directory.
- The default combined project-instruction budget is 32 KiB, so this package adds only a compact activation block rather than injecting `DESIGN.md` wholesale.
- Codex initially exposes skill metadata within a bounded context budget. This package therefore provides a mandatory gateway (`pdo-start`) and an optional context-light `orchestrated` profile in addition to the full native skill installation.
- Installable Codex plugins require `.codex-plugin/plugin.json`, place `skills/` at plugin root, and are distributed through marketplace catalogs. The included local catalog is an optional native alternative; the direct installer does not depend on interactive plugin installation.

## Anthropic Claude Code decisions

Official sources:

- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/plugin-marketplaces

Relevant documented behavior:

- Personal skills live at `~/.claude/skills/<skill>/SKILL.md`; project skills live at `.claude/skills/<skill>/SKILL.md`.
- A folder inside a skills directory that contains `.claude-plugin/plugin.json` is discovered as a skills-directory plugin without a marketplace installation step.
- Skills-directory plugins may bundle multiple namespaced skills and supporting resources. Personal plugins work across projects; project plugins require workspace trust and are discovered from the exact directory where Claude Code starts.
- Claude Code uses `CLAUDE.md` for project instructions and supports `@path` imports. The package root uses `@AGENTS.md` as an interoperability bridge, while installed project guidance stays concise.
- Marketplace-installed plugins are copied to a cache and cannot safely reference files outside the plugin directory. Therefore the generated plugin is self-contained.
- Plugin manifests live at `.claude-plugin/plugin.json`; component directories such as `skills/` remain at plugin root.

## Shared implementation choices

- The canonical nested skill library remains unchanged for human maintenance.
- A generated, flat, self-contained plugin view adapts the same skills to both platforms.
- Codex direct copies receive `pdo-` names so they cannot silently replace unrelated personal or project skills.
- Claude Code uses plugin namespacing, so original skill names remain intact inside the plugin.
- The installer is local-only, standard-library Python, receipt-driven, idempotent, and reversible.
- Existing `AGENTS.md` and `CLAUDE.md` files are never replaced; only a marked block is added or updated.
- No hooks, MCP servers, or executable plugin components are installed. The plugin contributes instructions and local reference files only.
