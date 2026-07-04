# Agent platform integrations

`product-design-orchestrator-plugin/` is a generated, flat, self-contained adapter for both Claude Code and Codex.

It contains:

- `.claude-plugin/plugin.json`
- `.codex-plugin/plugin.json`
- `skills/<name>/SKILL.md` for every canonical bundled skill plus `pdo-start`
- the controlling governance, playbooks, templates, registries, sources, and helper scripts needed at runtime

Do not hand-edit generated copies. Update the canonical package and run:

```bash
python scripts/build_agent_bundle.py
```

The source archive's deterministic installer is `scripts/agent_install.py`; platform-specific marketplace catalogs are at `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`.
