---
name: design-system-integration
description: Integrate new UI into an existing design system by reusing primitives, adding justified tokens/components, and preventing local drift.
version: "1.0.0"
category: implementation
phases: ["implement", "systemize"]
triggers: ["use design system", "integrate components", "extend UI library", "avoid one off CSS"]
---

# Design System Integration

## Mission

Make the feature feel native to the product while evolving the system only where repeated product needs justify it.

## Use this skill when

- use design system
- integrate components
- extend UI library
- avoid one off CSS

## Inputs

- system inventory/docs
- approved design
- usage/context
- component/token source
- contribution process

## Protocol

1. Map each need to an existing primitive, component, pattern, token, or composition.
2. Check whether mismatch is an implementation defect, missing variant, missing semantic token, pattern gap, or intentional exception.
3. Prefer composition and content changes before adding broad variants.
4. For genuine gaps, define contract, states, accessibility, tokens, tests, docs, and owner.
5. Contribute to the system through its governance path; avoid local forks or deep overrides.
6. Use adapters/migration layers when replacing legacy usage incrementally.
7. Measure visual/behavior consistency and bundle/performance effects.
8. Feed repeated exceptions and product learning back into system roadmap.

## Required outputs

- reuse/gap map
- system contribution or documented exception
- integrated components/tokens
- tests/docs
- adoption feedback

## Quality bar

- Existing system is understood before extension.
- New variants represent stable semantics.
- No local fork is hidden.
- Feature and system remain testable.

## Failure modes to avoid

- Copying library code into feature folder.
- Adding a variant for every screen.
- Overriding tokens with raw values.
- Mixing primitive systems.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
