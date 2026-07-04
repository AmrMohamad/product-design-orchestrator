---
name: performance
description: Design, implement, and verify UI performance for loading, responsiveness, visual stability, animation, memory, and realistic low-end conditions.
version: "1.0.0"
category: implementation
phases: ["implement", "verify", "live"]
triggers: ["UI performance", "Core Web Vitals", "jank", "slow interface", "optimize frontend"]
---

# Performance

## Mission

Protect the speed and stability of the primary user task while preserving intended visual quality.

## Use this skill when

- UI performance
- Core Web Vitals
- jank
- slow interface
- optimize frontend

## Inputs

- task/journey
- stack and bundle/runtime data
- representative devices/networks
- current measurements

## Protocol

1. Define performance budget and user-centric signals for the critical journey before optimizing.
2. Measure field data when available and lab/profile data under reproducible conditions; distinguish them.
3. Analyze loading critical path, server/data latency, fonts/assets, JavaScript/bundle, rendering, layout shift, input latency, long tasks, lists, and memory.
4. Prioritize causes by user impact and frequency; do not optimize a score alone.
5. Use progressive loading, caching, streaming/defer, code split, image/font strategy, virtualization, and compositor motion where appropriate.
6. Preserve accessibility and content while reducing visual cost; provide low-motion/low-data fallbacks when valuable.
7. Add performance tests/budgets/monitoring to prevent regression.
8. Verify on representative low-end hardware/network and after visual changes.

## Required outputs

- performance baseline/budget
- bottleneck analysis
- implemented fixes
- before/after evidence
- regression monitoring

## Quality bar

- Measurements represent the user journey.
- Field and lab data are not conflated.
- Visual stability and responsiveness are protected.
- Optimization does not hide content or access.

## Failure modes to avoid

- Lighthouse score as the only goal.
- Premature micro-optimization.
- Lazy-loading critical content.
- Heavy blur/animation without profiling.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
