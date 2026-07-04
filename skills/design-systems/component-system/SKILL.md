---
name: component-system
description: Specify reusable components with purpose, anatomy, variants, states, accessibility, content, tokens, API boundaries, tests, and misuse guidance.
version: "1.0.0"
category: design-systems
phases: ["systemize", "implement", "verify"]
triggers: ["component spec", "design system component", "UI library", "component states"]
---

# Component System

## Mission

Create reusable behavior and visual consistency without turning every composition into a generic component.

## Use this skill when

- component spec
- design system component
- UI library
- component states

## Inputs

- usage/jobs
- existing primitives/components
- interaction/content requirements
- token/platform constraints

## Protocol

1. Start with repeated user/system behavior and define when the component should not be used.
2. Specify anatomy, required/optional slots, content limits, data/state ownership, and composition rules.
3. Minimize variants to meaningful semantic differences; separate size/density from intent.
4. Build a complete state matrix including focus, keyboard, loading, error, long content, theme, and responsive behavior.
5. Use native semantics or established accessible primitives; document ARIA and focus only where needed.
6. Map all styling to tokens and define extension points without arbitrary override APIs.
7. Create examples/stories for default, extremes, errors, themes, and misuse.
8. Add interaction, accessibility, unit, and visual tests; define versioning and migration.

## Required outputs

- component contract
- variant/state matrix
- token/anatomy map
- examples/stories
- test/migration plan

## Quality bar

- API follows user intent.
- All consequential states exist.
- Component composes without leaking layout assumptions.
- Accessibility is built into the primitive.

## Failure modes to avoid

- Boolean-prop explosion.
- One component for unrelated patterns.
- Visual-only specification.
- Overrides as the main API.
- No content extremes.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
