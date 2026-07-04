---
name: color
description: Build a perceptually coherent, accessible color system for brand, hierarchy, interaction, status, data, themes, and real display conditions.
version: "1.0.0"
category: visual-design
phases: ["explore", "systemize", "verify"]
triggers: ["color palette", "OKLCH", "dark mode colors", "accessible color system"]
---

# Color

## Mission

Use color as semantic structure and character rather than decorative variety.

## Use this skill when

- color palette
- OKLCH
- dark mode colors
- accessible color system

## Inputs

- brand inputs
- aesthetic thesis
- semantic roles
- theme/platform/accessibility requirements

## Protocol

1. Define color jobs before values: surfaces, text, border, action, focus, selection, status, data, brand/accent.
2. Build primitives in a perceptual space such as OKLCH where supported by tooling, then map semantic aliases.
3. Control lightness and chroma across steps; test gamut/fallback and real displays.
4. Verify contrast for text, controls, focus, non-text boundaries, charts, and states; never rely on color alone.
5. Design dark/high-contrast themes as semantic remaps, not inversion; adjust elevation, saturation, and images.
6. Limit accents and distribute contrast according to hierarchy.
7. Test adjacent states, disabled/unavailable, destructive, links, visited, selection, and overlays.
8. Document intended use and prohibited combinations; validate with content/screenshots.

## Required outputs

- color role model
- primitive/semantic tokens
- theme mappings
- contrast/state matrix
- usage guidance

## Quality bar

- Color roles are stable across components.
- Hierarchy works in grayscale.
- Status has non-color cues.
- Dark mode is intentionally tuned.

## Failure modes to avoid

- Palette first, semantics later.
- Too many accents.
- Pastel text for premium feel.
- Opacity-only disabled states.
- Color contrast checked only on ideal surfaces.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
