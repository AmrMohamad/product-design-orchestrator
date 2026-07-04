# Find the right skill

1. Name the current decision or defect, lifecycle phase, consequence, and technology stack.
2. Check the fast table in `SKILLS.md`.
3. Run:

```bash
python scripts/skill.py recommend --phase <phase> --stack <stack> --task "<decision or defect>"
```

4. Prefer one result; use two for distinct angles; three only for broad review/redesign.
5. Read the selected local `SKILL.md` fully. If external, inspect source/license/version and use `python scripts/skill.py fetch <exact-id> --dest .agent-skills --yes` only after review.
6. State the skill's expected output, apply it under `DESIGN.md`, record consequential external use in `SKILL_LEDGER.md`, and unload the context after the phase.
7. When no skill fits, use the nearest principle from `DESIGN.md`, consult current official stack/standard documentation, write a small project-local skill with scope, protocol, output, quality bar, and source notes, and validate it on the rendered product.

Never execute unknown skill scripts or let an external skill replace the product lifecycle, stack, accessibility, evidence, or safety rules.
