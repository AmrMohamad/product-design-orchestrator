---
name: typography
description: Design and implement a readable, expressive, responsive type system with intentional hierarchy, rhythm, content fit, and language support.
version: "1.0.0"
category: visual-design
phases: ["explore", "systemize", "implement", "verify"]
triggers: ["typography", "font pairing", "type scale", "text hierarchy"]
---

# Typography

## Mission

Make language carry hierarchy and character while remaining legible across content, devices, themes, and locales.

## Use this skill when

- typography
- font pairing
- type scale
- text hierarchy

## Inputs

- brand/aesthetic thesis
- content hierarchy and samples
- platform/font constraints
- language/accessibility needs

## Protocol

1. Start from content roles and reading conditions: display, heading, body, label, data, code, annotation.
2. Choose typefaces/weights with licensing, loading, script coverage, numerals, UI legibility, and brand fit in mind.
3. Create a limited scale with size, line height, weight, tracking, max line length, and responsive behavior.
4. Use contrast in scale/weight/space deliberately; do not rely on many near-identical sizes.
5. Tune headings and body with real content, long words, numbers, tables, errors, and localization.
6. Define fallback stack and font-loading strategy to minimize layout shift.
7. Check zoom/reflow, user font settings where relevant, dark mode, anti-aliasing differences, and platform rendering.
8. Perform optical adjustments for alignment, caps, icons, punctuation, and vertical rhythm.

## Required outputs

- type role map
- font/fallback decision
- type tokens
- content stress tests
- implementation notes

## Quality bar

- Body text is comfortable and reflows.
- Hierarchy works without color.
- Weights/styles actually exist.
- Font loading does not destabilize layout.

## Failure modes to avoid

- Font choice by trend alone.
- Too many weights/sizes.
- Tiny low-contrast labels.
- Fixed-height text containers.
- Hero typography tested only with short copy.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
