---
name: i18n-content-resilience
description: Harden UI for localization, RTL, text expansion, locale formats, input methods, pluralization, and extreme/missing content.
version: "1.0.0"
category: implementation
phases: ["structure", "implement", "verify"]
triggers: ["internationalization", "localization UI", "RTL", "long text", "content resilience"]
---

# I18N Content Resilience

## Mission

Ensure the design remains understandable and functional beyond the source language and ideal sample content.

## Use this skill when

- internationalization
- localization UI
- RTL
- long text
- content resilience

## Inputs

- supported locales/scripts
- content/components
- formatting rules
- translation workflow
- real extreme data

## Protocol

1. Inventory hard-coded strings, concatenation, fixed dimensions, directional CSS/icons, and locale-sensitive formats.
2. Use message keys with context, ICU/plural/select where supported, and avoid constructing grammar from fragments.
3. Use logical layout properties and mirror only directional meaning, not universal icons or data.
4. Support text expansion, long words, multiple lines, different scripts, font fallback, numerals, and input methods.
5. Format dates, time zones, numbers, currency, units, names, addresses, and sorting by locale and domain.
6. Design truncation with access to full content and avoid hiding critical distinctions.
7. Test pseudolocalization, RTL, representative scripts, missing translations, and mixed-direction content.
8. Coordinate translator notes, screenshots/context, review, and fallback behavior.

## Required outputs

- i18n risk audit
- resilient layout/content changes
- locale/RTL test matrix
- translation context/fallback rules

## Quality bar

- No user-visible string is assembled unsafely.
- Critical content survives expansion.
- RTL behavior is semantic.
- Formats use locale/domain rules.

## Failure modes to avoid

- Fixed-height text.
- String concatenation.
- Mirroring all icons.
- Assuming names/addresses.
- Truncating errors/actions.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
