---
name: layout-composition
description: Design responsive spatial systems, grids, hierarchy, rhythm, and optical balance from content and task rather than template geometry.
version: "1.0.0"
category: visual-design
phases: ["explore", "systemize", "implement", "verify"]
triggers: ["layout", "grid", "spacing", "composition", "visual hierarchy"]
---

# Layout Composition

## Mission

Create a spatial reading experience that feels deliberate at every relevant size and content condition.

## Use this skill when

- layout
- grid
- spacing
- composition
- visual hierarchy

## Inputs

- content/task hierarchy
- aesthetic thesis/density
- platform/viewport range
- existing layout/tokens

## Protocol

1. Map focal order and zones before choosing columns or cards.
2. Define containers, grid/columns, gutters, alignment lines, spacing rhythm, density modes, and overflow behavior.
3. Use asymmetry, overlap, or broken-grid moments only when they strengthen hierarchy and survive responsive transformation.
4. Prefer layout systems (grid/flex/intrinsic sizing/container queries where suitable) over brittle offsets.
5. Treat whitespace as grouping and pacing, not empty decoration.
6. Plan content extremes, sticky/fixed regions, safe areas, scroll boundaries, and nested containers.
7. Design explicit transformations for mobile/tablet/desktop rather than shrinking desktop.
8. Render awkward in-between widths and apply optical corrections for perceived alignment.

## Required outputs

- hierarchy sketch
- grid/container/spacing rules
- responsive transformation map
- layout tokens
- stress-test findings

## Quality bar

- Reading order matches DOM/accessibility order.
- Layout survives real content and intermediate widths.
- Spacing expresses relationships.
- No offset patchwork hides a wrong model.

## Failure modes to avoid

- Equal cards by default.
- Desktop-first squeeze.
- Arbitrary absolute positioning.
- Whitespace without grouping.
- Mathematical centering that looks wrong.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
