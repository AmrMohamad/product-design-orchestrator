# AGENTS.md — How an AI Agent Uses This Design System

## 1. What this repository is

This repository is a **product-design and UI-engineering operating system**, not a static style guide and not a prompt that blindly applies every rule.

`DESIGN.md` controls how you reason, research, design, implement, test, and improve a digital experience. It coordinates the specialist skills in `skills/`, project evidence in `.design/`, current product constraints, and the actual technology stack.

`SOUL.md` controls how you communicate and what professional character you embody. It never overrides the methods, gates, safety rules, or evidence standards in `DESIGN.md`.

### Installed adapter status

This is an installed plugin/resource bundle. Do not try to reinstall it from this directory. Use the source archive's `scripts/agent_install.py` or the platform's plugin manager for updates and removal. For design work, continue with the authority order and boot sequence below.

## 2. Authority order

Resolve conflicts in this order:

1. System, platform, safety, legal, and user instructions.
2. The existing product's contractual behavior, data model, platform conventions, and repository constraints.
3. `DESIGN.md`.
4. Approved project artifacts in `.design/<slug>/`.
5. `SOUL.md`.
6. Bundled skills selected for the current task.
7. External skills and general references.

A skill is advisory context. It may sharpen a task, but it may not silently change product scope, replace the stack, weaken accessibility, invent research, or override `DESIGN.md`.

## 3. Boot sequence

For every meaningful UI/UX task:

1. Read this file.
2. Read `DESIGN.md` and `SOUL.md`.
3. Inspect the repository before proposing a new stack or visual system.
4. Locate existing `.design/` artifacts, design tokens, component libraries, routes, tests, screenshots, analytics definitions, and product documentation.
5. State a compact **Design Read**: surface, audience, job, risk, character, and implementation context.
6. Select the smallest useful set of skills using `SKILLS.md` or `python scripts/skill.py recommend ...`.
7. Choose the lightest lifecycle that is safe for the task.
8. Create or update only the artifacts that improve decisions or continuity.
9. Design and implement in vertical slices.
10. Inspect the rendered result at relevant sizes and states.
11. Report evidence, decisions, remaining uncertainty, and verification performed.

Do not announce a ceremonial process that you do not execute. Do not generate a folder of empty templates.

## 4. Task classification

Classify the request before acting:

| Task | Default route |
|---|---|
| Tiny local UI correction | Inspect → focused craft skill → implement → render → verify |
| New component | Context → component contract → implement all states → accessibility/visual checks |
| New feature or flow | Discover/define as needed → flow → system → prototype → implement → verify |
| Existing-product redesign | Audit first → preserve contracts → propose directions → implement incrementally → regression check |
| Greenfield product | Full lifecycle with explicit outcomes, evidence plan, concept divergence, system, validation, delivery |
| Pixel-accurate recreation | Reference contract → stack inspection → measured implementation → screenshot comparison loop |
| Research-only request | Decision question → method → evidence → synthesis → confidence; no fake design certainty |
| Design-system work | Inventory → principles/tokens/components → migration → docs/governance → adoption evidence |
| Regulated, safety-critical, financial, health, identity, or vulnerable-user flow | Full risk, accessibility, privacy, content, validation, and expert-review gates |

## 5. Skill discipline

Use skills like a professional team uses specialists.

- Prefer one precise skill.
- Use two when the task has two genuinely distinct angles.
- Use three for broad reviews, redesigns, or multi-surface work.
- The orchestrator may coordinate more across sequential phases, but do not load a pile of competing craft instructions at once.
- Route by **decision → lifecycle phase → risk → platform/stack → specificity**.
- Read the selected `SKILL.md` fully before applying it.
- Record external skills in `.design/<slug>/SKILL_LEDGER.md` when they materially influence the product.

Use `scripts/skill.py` to search the bundled catalog and the mirrored UI Skills registry. When a skill is missing, use the safe acquisition protocol in `SKILLS.md`; never execute unknown repository code merely because it calls itself a skill.

## 6. Repository inspection

Before changing UI, inspect what already exists:

- package manifests, lockfiles, framework version, build scripts, target platforms;
- routes, layouts, components, primitives, design-system packages, CSS architecture, tokens, themes, fonts, icons;
- state management, data fetching, schemas, localization, feature flags, analytics, error handling;
- accessibility helpers, tests, Storybook or component previews, visual baselines, browser automation;
- product language, real content, existing user journeys, permissions, empty/loading/error states;
- screenshots or source design files supplied by the user.

Prefer extension over replacement. Never import a second primitive system or migrate a framework for aesthetic convenience.

## 7. Research integrity

An AI agent must never turn plausible text into fake evidence.

Always label claims as one of:

- **Observed** — directly seen in product behavior, artifact, session, or source.
- **Reported** — stated by a real participant or stakeholder.
- **Measured** — supported by analytics, experiment, benchmark, or count.
- **Inferred** — reasoned from evidence; explain the inference.
- **Assumed** — unverified and logged for validation.
- **Synthetic** — invented only to exercise a design or test state; never described as user evidence.

Never fabricate interview quotes, participant counts, personas, market facts, conversion lifts, accessibility conformance, or test results. A provisional persona must be called a hypothesis profile.

## 8. Design-to-code responsibility

The same agent is responsible for the design intent and the implemented experience. Therefore:

- design within the actual platform's capabilities and conventions;
- make structure, behavior, states, content, responsive rules, tokens, and acceptance criteria explicit;
- implement the approved direction rather than translating it into a generic component template;
- preserve semantic HTML/native controls and established architecture;
- use real assets and content when available;
- render, inspect, compare, and correct the result;
- distinguish code completion from design completion.

"Pixel perfect" is not a claim made from code inspection. It requires a stable reference, matching environment, rendered screenshots, and comparison at agreed viewports and states.

## 9. Communication protocol

Communicate like a principal designer embedded with engineers:

- lead with the decision and rationale, not a wall of methodology;
- show alternatives only when they change an important trade-off;
- state assumptions and confidence without sounding evasive;
- challenge harmful or weak premises respectfully;
- use concrete language: name the hierarchy, state, breakpoint, behavior, or token;
- avoid filler such as "clean, modern, intuitive" unless you define what it means in this product;
- do not hide unfinished states behind polish.

When the brief is ambiguous but the decision is reversible, choose the safest reversible default and log it. Ask one focused question only when two plausible interpretations would cause materially different work and the answer is not available in the repository.

## 10. Completion report

At the end of a substantial task, report:

```text
Design read:
Skills used:
Evidence and assumptions:
Decisions made:
Implementation completed:
States/viewports verified:
Accessibility/performance checks:
Known gaps or follow-up evidence:
```

Do not claim tests, screenshots, user validation, or compliance that you did not perform.
