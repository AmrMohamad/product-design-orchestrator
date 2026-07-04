---
name: test-strategy
description: Define a risk-based UI test strategy across unit, component, interaction, accessibility, visual, integration, end-to-end, performance, and exploratory testing.
version: "1.0.0"
category: quality-assurance
phases: ["systemize", "implement", "verify"]
triggers: ["UI testing strategy", "component tests", "E2E plan", "visual tests"]
---

# Test Strategy

## Mission

Create fast, trustworthy coverage around user-critical behavior and design contracts without brittle duplication.

## Use this skill when

- UI testing strategy
- component tests
- E2E plan
- visual tests

## Inputs

- journey/risks
- architecture
- component/system contracts
- current tools/CI
- release model

## Protocol

1. Map risks and contracts to the cheapest test layer that can detect them reliably.
2. Use unit tests for logic, component tests for states/interactions, E2E for critical integration journeys, visual tests for rendered appearance, and manual/exploratory for human perception/AT.
3. Prioritize accessibility semantics/keyboard, data integrity, permissions, errors/recovery, responsive behavior, and visual system regressions.
4. Define deterministic fixtures, clocks, network, fonts, viewports, and data seeds.
5. Avoid duplicating the same assertion across layers; keep tests close to ownership.
6. Set CI gates, sharding/time budget, failure artifacts, flake policy, and baseline review process.
7. Measure meaningful coverage by critical behaviors/states, not line percentage alone.
8. Review strategy as product risk and architecture evolve.

## Required outputs

- risk-to-test matrix
- layered suite plan
- fixtures/environment rules
- CI/flake/baseline policy
- coverage gaps

## Quality bar

- Tests target contracts and consequences.
- The suite is deterministic and diagnosable.
- Visual/a11y behavior has appropriate coverage.
- Critical states are not left manual by accident.

## Failure modes to avoid

- E2E for everything.
- Snapshotting huge markup.
- Line coverage as quality.
- Brittle selectors.
- Never reviewing visual baselines.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
