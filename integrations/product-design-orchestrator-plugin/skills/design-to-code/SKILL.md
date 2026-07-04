---
name: design-to-code
description: Translate approved flows, screen contracts, tokens, components, content, and states into maintainable production code in vertical slices.
version: "1.0.0"
category: implementation
phases: ["implement"]
triggers: ["implement design", "frontend build", "design handoff", "code UI"]
---

# Design To Code

## Mission

Carry design intent into real behavior and architecture rather than producing a static approximation.

## Use this skill when

- implement design
- frontend build
- design handoff
- code UI

## Inputs

- approved design artifacts
- stack profile
- existing system/code
- data/API contracts
- acceptance criteria

## Protocol

1. Map every screen/pattern to existing routes, components, tokens, data, and tests; identify only genuine gaps.
2. Plan vertical slices containing structure, data, content, interactions, states, responsiveness, accessibility, tests, and rendered review.
3. Implement semantic/native structure first, then system styling, states, and motion.
4. Use realistic data and content; preserve loading/error/empty/permission behavior.
5. Centralize reusable decisions; keep one-off composition local and avoid premature abstraction.
6. Respect architecture, state/data ownership, localization, feature flags, and observability.
7. Render each slice and compare with approved intent before moving on.
8. Add tests/baselines proportional to risk and document necessary divergence.

## Required outputs

- implementation plan
- working vertical slices
- tests/stories/baselines
- decision/deviation notes
- verification evidence

## Quality bar

- The UI works with real state/data.
- Code extends the existing system.
- Design intent is visible in the browser/device.
- Components are neither duplicated nor over-generalized.

## Failure modes to avoid

- Static mock markup.
- Placeholder TODO states.
- Rewriting architecture silently.
- Abstracting before two uses.
- Stopping at compile success.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
