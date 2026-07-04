# Self-install for Codex and Claude Code

This package can install its bundled governance, playbooks, registries, and skills into the official local locations used by **OpenAI Codex** and **Anthropic Claude Code**. The installer is standard-library Python, performs no network requests, invokes neither agent binary, and records every managed path for verification and uninstall.

## Agent behavior

When a user asks Codex or Claude Code to install this archive:

1. Determine scope from the request. Use `project` for “install here / in this repo”; use `user` only for “install globally / for all projects.” If unspecified, use `project`.
2. Run a dry run first.
3. Review the displayed destinations and conflicts.
4. Run the real installation without `--force`.
5. Run `verify`.
6. Tell the user which scope and paths were installed. Restart Codex; in Claude Code, restart or run `/reload-plugins`.

## One-command project installation for both agents

From the extracted package directory:

```bash
python scripts/agent_install.py install --agent both --scope project --project . --dry-run
python scripts/agent_install.py install --agent both --scope project --project .
python scripts/agent_install.py verify  --agent both --scope project --project .
```

Shell wrappers do the same install step:

```bash
./self-install.sh --agent both --scope project --project .
```

```powershell
./self-install.ps1 -Agent both -Scope project -Project .
```

```cmd
self-install.cmd --agent both --scope project --project .
```

## Install for one agent

Codex project scope:

```bash
python scripts/agent_install.py install --agent codex --scope project --project .
```

Claude Code project scope:

```bash
python scripts/agent_install.py install --agent claude --scope project --project .
```

## User-wide installation

User scope installs skills for all projects but does **not** modify global instruction files unless `--activate-global` is supplied.

```bash
python scripts/agent_install.py install --agent both --scope user
python scripts/agent_install.py verify  --agent both --scope user
```

To opt into global activation guidance:

```bash
python scripts/agent_install.py install --agent both --scope user --activate-global
```

## Codex installation model

The direct installer follows Codex's documented skill locations:

- project skills: `<project>/.agents/skills/`
- personal skills: `~/.agents/skills/`

Codex copies are named `pdo-*` to avoid colliding with existing skills. A full resource/plugin bundle is installed at `.agents/product-design-orchestrator/` or `~/.agents/product-design-orchestrator/`. Project scope adds a short managed block to the nearest root `AGENTS.override.md` when present, otherwise `AGENTS.md`.

The default `full` profile installs every bundled skill natively. For a smaller Codex startup inventory while retaining the entire library as readable resources, use:

```bash
python scripts/agent_install.py install --agent codex --scope project --profile orchestrated
```

## Claude Code installation model

The installer uses Claude Code's documented **skills-directory plugin** mechanism:

- project plugin: `<project>/.claude/skills/product-design-orchestrator/`
- personal plugin: `~/.claude/skills/product-design-orchestrator/`

The folder contains `.claude-plugin/plugin.json`, a flat `skills/` directory, and all package-local resources, so it is discovered in place with no marketplace or cache dependency. Project scope adds a short managed block to `CLAUDE.md`. Launch Claude Code from the project root for a project skills-directory plugin, or run `/reload-plugins` after changing directories.

## Native marketplace alternatives

The archive also contains valid Claude Code and Codex plugin manifests plus local marketplace catalogs.

Claude Code:

```bash
claude plugin marketplace add /absolute/path/to/product-design-orchestrator
claude plugin install product-design-orchestrator@product-design-orchestrator-local --scope user
```

Codex:

```bash
codex plugin marketplace add /absolute/path/to/product-design-orchestrator
codex
# then open /plugins and install Product Design Orchestrator from the local marketplace
```

For transient Claude Code testing without installation:

```bash
claude --plugin-dir ./integrations/product-design-orchestrator-plugin
```

The deterministic Python installer remains the recommended self-install path because it works without depending on an installed CLI version and can verify and uninstall its own files.

## Verify, status, update, uninstall

```bash
python scripts/agent_install.py status    --agent both --scope project --project .
python scripts/agent_install.py verify    --agent both --scope project --project .
python scripts/agent_install.py install   --agent both --scope project --project .
python scripts/agent_install.py uninstall --agent both --scope project --project . --dry-run
python scripts/agent_install.py uninstall --agent both --scope project --project .
```

Re-running `install` updates paths already marked as owned by this package. It refuses to replace unrelated directories unless the user explicitly chooses `--force` after review. Uninstall removes only recorded owned directories and the text between managed markers.

## Security guarantees

- No network access.
- No package-manager command.
- No execution of bundled or downloaded skill code.
- No silent overwrite of unmanaged skill directories.
- Atomic directory replacement where supported by the operating system.
- Receipts and ownership markers for every installed component.
- Existing instruction files are preserved outside a clearly marked block.
