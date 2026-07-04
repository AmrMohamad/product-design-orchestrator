---
name: design-system-migration
description: Plan and execute migration from fragmented or legacy UI to a coherent system without breaking product behavior or freezing delivery.
version: "1.0.0"
category: design-systems
phases: ["orient", "systemize", "implement", "live"]
triggers: ["migrate design system", "legacy UI refactor", "component consolidation", "token migration"]
---

# Design System Migration

## Mission

Reduce inconsistency and maintenance cost through evidence-based incremental migration rather than a risky big-bang rewrite.

## Use this skill when

- migrate design system
- legacy UI refactor
- component consolidation
- token migration

## Inputs

- component/style inventory
- usage data
- target system
- product roadmap
- test/baseline coverage

## Protocol

1. Inventory components, raw styles, variants, consumers, accessibility defects, ownership, and business criticality.
2. Cluster true equivalents and distinguish visual drift from semantic/behavior differences.
3. Define target tokens/components/patterns and compatibility/adaptor strategy.
4. Prioritize by user harm, change frequency, duplication, product roadmap, and migration leverage.
5. Create codemods/adapters only where safe; preserve behavior and visual baselines.
6. Migrate vertical product slices or high-leverage primitives with dual-run/feature flags when warranted.
7. Track usage and exceptions; deprecate with owners, timelines, and rollback.
8. Verify accessibility, behavior, visual diffs, bundle/performance, and team adoption after each wave.

## Required outputs

- inventory/equivalence map
- target architecture
- migration waves
- compatibility/deprecation plan
- verification/adoption dashboard

## Quality bar

- Behavioral differences are understood.
- Migration is incremental and reversible.
- Product teams can continue delivery.
- Success includes defect/duplication reduction.

## Failure modes to avoid

- Big-bang rewrite for cleanliness.
- Replacing names without semantics.
- Ignoring visual regressions.
- Forcing every legacy exception into one component.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
