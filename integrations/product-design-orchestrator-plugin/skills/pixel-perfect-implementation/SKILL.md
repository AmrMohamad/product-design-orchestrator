---
name: pixel-perfect-implementation
description: Recreate an approved visual reference with measured, maintainable, responsive implementation and a deterministic screenshot comparison loop.
version: "1.0.0"
category: implementation
phases: ["implement", "verify", "reference rebuild"]
triggers: ["pixel perfect", "image to code", "match Figma", "screenshot recreation"]
---

# Pixel Perfect Implementation

## Mission

Achieve perceptual and measured fidelity without sacrificing semantics, behavior, accessibility, responsiveness, or architecture.

## Use this skill when

- pixel perfect
- image to code
- match Figma
- screenshot recreation

## Inputs

- reference frame/design
- viewport/DPR/platform
- fonts/assets/content
- stack profile
- allowed deviations

## Protocol

1. Create the reference contract: approval, viewport, DPR, browser/platform, theme/state, fonts/assets/content, dynamic regions, tolerance.
2. Lock deterministic comparison conditions and acquire exact assets/fonts where lawful and available.
3. Measure macro regions, container/grid, type metrics, line wraps, spacing, radii, borders, shadows, colors, and image crops.
4. Implement semantic structure and correct layout model before fine styling; avoid offset patchwork.
5. Capture actual screenshots at contract viewports/states and overlay/diff against reference.
6. Classify differences: structure, geometry, typography, spacing, color/material, assets, detail/motion.
7. Fix highest-leverage category, recapture, and regression-check adjacent widths/states.
8. Store baseline/evidence and document unavoidable renderer/platform differences.
9. Never claim pixel accuracy without actual comparison.

## Required outputs

- reference contract/measurements
- faithful implementation
- comparison screenshots/diffs
- accepted-difference log
- visual baseline

## Quality bar

- Environment is controlled.
- Typography and content match.
- Fidelity survives responsive behavior.
- Visual fixes do not break semantics or system.

## Failure modes to avoid

- Eyeballing from code.
- Absolute coordinates for entire page.
- Replacing text with images.
- Ignoring font metrics.
- Claiming exactness across uncontrolled OS/browser.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
