# Validation report

Build date: 2026-06-25  
Package version: 0.4.1 (beta)

## Preservation check

The product-design protocol itself was preserved from internal method version 4.0.0. Byte-for-byte comparisons passed for:

- `DESIGN.md`
- `SOUL.md`
- `SKILLS.md`
- every canonical file under `skills/`
- every file under `playbooks/`
- every file under `templates/`
- every file under `registry/`

Package version 0.4.1 adds agent-platform adapters, installation tooling, supporting documentation, manifests, tests, and generated portable views; it remains a beta release and does not alter the design method or canonical skill content.

## Platform documentation review

The adapter design was checked against current official documentation dated 2026-06-25.

OpenAI Codex coverage:

- skill format and discovery
- project and personal skill locations
- `AGENTS.md` discovery and override behavior
- plugin layout and `.codex-plugin/plugin.json`
- repository and local marketplace catalogs
- plugin component path rules and install-surface metadata

Anthropic Claude Code coverage:

- project and personal skill locations
- skills-directory plugins
- plugin namespacing and invocation
- `.claude-plugin/plugin.json` and plugin-root layout
- `CLAUDE.md` imports
- local marketplace layout, caching, and relative-path behavior
- plugin reload and development loading

The exact official source list and the decisions derived from it are recorded in `resources/AGENT_PLATFORM_RESEARCH.md`.

## Structural verification

- Required original and adapter root files exist.
- All canonical `SKILL.md` files have `name` and `description` frontmatter.
- Canonical skill names are unique.
- The portable plugin contains exactly the canonical skill set plus the `pdo-start` gateway.
- Every portable plugin skill directory matches its frontmatter name.
- Codex and Claude Code manifests parse and identify version 0.4.1.
- Both manifests point to `./skills/` at plugin root.
- The Codex repository marketplace uses the documented local-source object and policy fields.
- The Claude Code local marketplace uses the documented marketplace root and relative plugin source.
- `CLAUDE.md` imports `AGENTS.md`.
- The plugin is self-contained and contains no symlinks, hooks, MCP servers, LSP servers, or executable plugin components.
- Registry IDs are unique, all bundled registry paths exist, and remote registry URLs use HTTPS.
- Python scripts compile with the system interpreter.
- Template/playbook minimums and relative Markdown links are checked.
- Final manifest hashes are verified by `scripts/validate_package.py`.

## Installer verification

The installer was exercised in isolated temporary home and project directories.

Passed scenarios:

- project-scoped dry run for both agents makes no changes
- project-scoped Codex + Claude Code installation
- full Codex native installation: 70 `pdo-*` skills
- Claude Code skills-directory plugin installation: 70 namespaced skills
- verification after install
- idempotent update
- preservation of pre-existing `AGENTS.md` and `CLAUDE.md` content
- clean removal of only the managed guidance blocks
- clean removal of installer-created empty guidance files
- user-scoped installation for both agents
- optional global activation through `CODEX_HOME/AGENTS.md` and `~/.claude/CLAUDE.md`
- retirement of previously activated global guidance on update
- context-light Codex profile: 5 gateway skills while retaining the complete resource bundle
- full-to-context-light profile switch removes stale installer-owned skill copies
- unmanaged destination conflict refusal
- preflight prevents a conflict in one agent from leaving the other partially installed
- receipt, ownership-marker, and skill-name verification
- uninstall removes only recorded installer-owned paths

The live `codex` and `claude` executables were not installed in this build container, so the package was not launched inside those applications. Their adapters were instead validated structurally against the official schemas and behavior, and the complete local install/update/verify/uninstall lifecycle was executed against isolated filesystem fixtures.

## Counts before archive

- 67 original specialist skills.
- 2 preserved upstream reference skills with licenses and source hashes.
- 69 canonical skills total.
- 70 portable agent-plugin skills including `pdo-start`.
- 192 normalized registry entries, including all 110 UI Skills catalog records and 13 Taste Skill family records.
- 17 working Markdown artifact templates plus template documentation and a design-token JSON example.
- 9 project playbooks plus playbook documentation.
- 2 agent manifests and 2 local marketplace catalogs.
- 3 cross-platform installation wrappers plus the standard-library Python installer.

Run again from the package root:

```bash
python scripts/skill.py doctor
python scripts/validate_package.py
python scripts/test_agent_install.py
```
