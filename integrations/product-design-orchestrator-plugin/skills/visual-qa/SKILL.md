---
name: visual-qa
description: Review rendered UI across approved references, viewports, states, themes, content extremes, and platforms; classify and correct visual/system defects.
version: "1.0.0"
category: quality-assurance
phases: ["verify"]
triggers: ["visual QA", "screenshot review", "UI polish", "visual regression"]
---

# Visual Qa

## Mission

Judge the surface users actually see, not the apparent quality of source code.

## Use this skill when

- visual QA
- screenshot review
- UI polish
- visual regression

## Inputs

- brief/direction
- running build
- reference/baselines
- state/viewport matrix
- component/system context

## Protocol

1. Set deterministic data, fonts, viewport, theme, animation, and environment where comparison matters.
2. Capture key journey screens at narrow, intermediate, and wide sizes plus critical states/themes.
3. Compare hierarchy, reading order, type metrics/wrapping, geometry, spacing/rhythm, alignment, color/material, assets, and motion.
4. Check component consistency and intentional exceptions against tokens/contracts.
5. Stress real/long/missing/translatable content, zoom, and high-density cases.
6. Classify S0–S4 and distinguish defect, approved change, renderer variance, and optional craft.
7. Fix in leverage order and recapture; review changed pixels rather than auto-accept baselines.
8. Store evidence, accepted differences, and regression coverage.

## Required outputs

- screenshot set
- comparison/diff findings
- prioritized corrections
- accepted-difference log
- updated baselines

## Quality bar

- All relevant states/sizes are rendered.
- Typography/content are not ignored.
- Baselines are reviewed by intent.
- Visual QA follows functional correctness.

## Failure modes to avoid

- Code-only review.
- Desktop hero only.
- Auto-updating snapshots.
- Pixel nitpicks before flow defects.
- Ignoring intermediate widths.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
