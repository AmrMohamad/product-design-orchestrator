# Quickstart for an AI coding agent

## Install this package into the current project

```bash
python scripts/agent_install.py install --agent both --scope project --project . --dry-run
python scripts/agent_install.py install --agent both --scope project --project .
python scripts/agent_install.py verify  --agent both --scope project --project .
```

For one platform, use `--agent codex` or `--agent claude`. For a global installation, use `--scope user`; add `--activate-global` only when the user explicitly wants global instruction activation. Full details are in `SELF_INSTALL.md`.

## Product-design operating loop

```text
1. Read AGENTS.md → DESIGN.md → SOUL.md.
2. Inspect repository, running product, and .design/.
3. State Design Read and task mode.
4. Use SKILLS.md or scripts/skill.py; load ≤3 simultaneous craft skills.
5. Produce only decision-useful artifacts.
6. Design complete behavior and states in the actual system.
7. Implement vertical slices in the detected stack.
8. Render at relevant viewports/states; compare and correct.
9. Run accessibility, interaction, resilience, performance, and release checks proportional to risk.
10. Report evidence, decisions, files, verification, deviations, and remaining uncertainty.
```
