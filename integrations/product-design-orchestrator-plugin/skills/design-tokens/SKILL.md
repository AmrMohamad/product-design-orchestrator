---
name: design-tokens
description: Define platform-agnostic primitive, semantic, and component design tokens with themes, aliases, descriptions, governance, and code translation.
version: "1.0.0"
category: design-systems
phases: ["systemize", "implement"]
triggers: ["design tokens", "token architecture", "CSS variables", "DTCG tokens"]
---

# Design Tokens

## Mission

Encode repeated design decisions as a shared vocabulary that can flow into multiple tools and technology stacks.

## Use this skill when

- design tokens
- token architecture
- CSS variables
- DTCG tokens

## Inputs

- existing tokens/styles
- visual direction
- platform outputs
- theme/brand/density needs
- migration constraints

## Protocol

1. Inventory raw values, duplicates, semantic roles, and platform-specific constraints.
2. Define layers: primitive/reference → semantic intent → component specialization only when justified.
3. Choose naming based on purpose and state, not page location or accidental color.
4. Specify type, value, description, mode/theme, alias, owner, status, and deprecation for each token family.
5. Cover color, typography, spacing, size, layout, radius, border, elevation/shadow, opacity, motion, z/layer, and breakpoints where relevant.
6. Model light/dark/high-contrast/brand/density modes through semantic remapping.
7. Create translation targets for CSS/native/theme objects and validate alias/circular/gamut/unit issues.
8. Migrate incrementally and detect raw-value drift; document exceptions rather than hiding them.

## Required outputs

- token architecture
- token file(s)
- mode/theme mapping
- translation/migration plan
- usage/deprecation guidance

## Quality bar

- Tokens express decisions shared by multiple uses.
- Semantic names remain stable when values change.
- Modes preserve meaning.
- Output is consumable by the real stack.

## Failure modes to avoid

- Tokenizing every one-off value.
- Names like blue500Button.
- Component tokens for all properties.
- Dark mode as inversion.
- Circular aliases.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
