---
name: project-inspector
description: Inspect an existing product and repository before UI changes so design decisions extend the real system instead of inventing a parallel one.
version: "1.0.0"
category: orchestration
phases: ["orient", "redesign", "implement"]
triggers: ["repository audit", "existing product", "redesign", "before coding UI"]
---

# Project Inspector

## Mission

Build an accurate map of product behavior, design language, technical architecture, and constraints before proposing change.

## Use this skill when

- repository audit
- existing product
- redesign
- before coding UI

## Inputs

- repository tree
- package manifests and lockfiles
- running app or screenshots
- product docs and .design artifacts

## Protocol

1. Identify platform, framework, versions, build/deploy targets, package manager, and monorepo boundaries.
2. Trace the requested journey through routes, data, state, permissions, errors, analytics, and tests.
3. Inventory primitives, component libraries, tokens, themes, fonts, icons, assets, layout conventions, and copy tone.
4. Locate existing responsive rules, accessibility helpers, Storybook/previews, visual baselines, and browser automation.
5. Render representative current screens when possible; inspect desktop/mobile, light/dark, and real states.
6. Separate intentional system decisions from local drift, legacy debt, and broken behavior.
7. List reuse candidates, genuine gaps, migration risks, and protected contracts.
8. Recommend preserve, evolve, or replace for each affected layer, with evidence.

## Required outputs

- project context map
- existing-pattern inventory
- journey trace
- constraints and risks
- reuse/gap recommendations

## Quality bar

- No dependency or component is assumed from memory.
- Recommendations cite concrete files/behaviors.
- The audit distinguishes product defects from aesthetic preference.
- Existing correct behavior is protected.

## Failure modes to avoid

- Proposing a new framework before inspection.
- Calling every inconsistency technical debt.
- Reviewing code without rendering the interface.
- Ignoring data, permissions, or operational actors.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
