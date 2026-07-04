@AGENTS.md

# Claude Code adapter

This repository is also a Claude Code extension package.

- For product-design or UI implementation work, follow the boot sequence in `AGENTS.md`; `DESIGN.md` remains the controlling method and `SOUL.md` remains subordinate to it.
- When asked to install this package for Claude Code or Codex, read `SELF_INSTALL.md` and use the local-only installer in `scripts/agent_install.py`.
- Default an unspecified installation request to **project scope**, preview with `--dry-run`, do not use `--force` without explicit permission, and verify after installation.
- The installer never downloads or executes third-party skill code. It preserves unrelated `CLAUDE.md`, `AGENTS.md`, and skill content through marked blocks and ownership receipts.
