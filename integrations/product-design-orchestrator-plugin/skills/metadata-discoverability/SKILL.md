---
name: metadata-discoverability
description: Implement accurate page/app metadata, structured sharing, indexing controls, deep links, titles, and install/discovery surfaces without misleading users or crawlers.
version: "1.0.0"
category: implementation
phases: ["implement", "verify"]
triggers: ["metadata", "SEO", "Open Graph", "social preview", "deep links"]
---

# Metadata Discoverability

## Mission

Make each public or shareable surface identifiable, trustworthy, and correctly represented outside the immediate UI.

## Use this skill when

- metadata
- SEO
- Open Graph
- social preview
- deep links

## Inputs

- route/content model
- brand assets
- indexing/privacy policy
- framework/platform

## Protocol

1. Define unique human-readable title and description from the actual page purpose/content.
2. Set canonical URL and indexing/robots behavior appropriate to duplicates, private, staged, filtered, or generated pages.
3. Implement Open Graph/social metadata and image with accurate content and dimensions.
4. Add structured data only when it matches visible content and current schema requirements.
5. Set language, theme color, icons/manifest, viewport, and platform deep-link/app-link metadata as relevant.
6. Handle dynamic routes, missing data, pagination, localization, and SSR/build behavior.
7. Prevent sensitive/private content from leaking through previews, logs, or metadata.
8. Validate rendered head/output and share/deep-link behavior with current tools.

## Required outputs

- metadata contract
- implemented route metadata
- privacy/indexing rules
- validation evidence

## Quality bar

- Metadata matches visible content.
- Every important route is unique.
- Private data cannot leak.
- Structured data is valid and justified.

## Failure modes to avoid

- Keyword stuffing.
- Same title everywhere.
- Fake structured data.
- Indexing internal filters/private pages.
- Unverified social images.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
