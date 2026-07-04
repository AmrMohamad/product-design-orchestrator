---
name: theming
description: Design semantic theme architecture for light/dark, high contrast, brand, density, and platform modes with predictable inheritance and asset behavior.
version: "1.0.0"
category: design-systems
phases: ["systemize", "implement", "verify"]
triggers: ["dark mode", "theme system", "multi brand", "design system modes"]
---

# Theming

## Mission

Let the same product meaning adapt across modes without component-level color patching or accessibility regressions.

## Use this skill when

- dark mode
- theme system
- multi brand
- design system modes

## Inputs

- semantic tokens
- mode requirements
- platform capabilities
- brand/assets
- user/system preference

## Protocol

1. List supported modes and whether they are user, system, tenant, brand, context, or accessibility controlled.
2. Map semantic roles per mode; avoid raw color overrides inside components.
3. Define inheritance, fallback, scope, persistence, server/client rendering, and no-flash behavior.
4. Tune surfaces, elevation, borders, images, charts, code, focus, disabled, selection, and status per mode.
5. Check contrast and perceptual hierarchy independently in every mode.
6. Design theme-aware assets and graceful fallback for third-party/embedded content.
7. Test mode changes, nested contexts, SSR/hydration, OS preference, high contrast/forced colors, and print/export.
8. Document ownership and prevent combinatorial mode explosion.

## Required outputs

- mode architecture
- semantic mapping
- persistence/rendering rules
- asset/chart behavior
- theme test matrix

## Quality bar

- Meaning stays constant across modes.
- No flash or hydration mismatch.
- Every mode is independently usable.
- Components do not own global theme values.

## Failure modes to avoid

- Dark mode by inversion.
- Per-component hex overrides.
- Brand themes that break status semantics.
- Ignoring forced colors.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
