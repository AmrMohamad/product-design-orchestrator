---
name: search-filtering
description: Design search, query, autocomplete, filters, facets, sorting, result interpretation, and no-result recovery for realistic information spaces.
version: "1.0.0"
category: experience-design
phases: ["structure", "systemize", "verify"]
triggers: ["search UX", "filters", "faceted navigation", "results page"]
---

# Search Filtering

## Mission

Help people express intent, understand results, refine efficiently, and recover when vocabulary or data is imperfect.

## Use this skill when

- search UX
- filters
- faceted navigation
- results page

## Inputs

- content/index model
- user query behavior/logs
- result attributes
- scale/performance/accessibility constraints

## Protocol

1. Define browse versus search jobs, query types, and success signals.
2. Model searchable fields, synonyms, spelling, language, permissions, freshness, ranking, and unavailable content.
3. Design query input, suggestions/history, scope, submission, loading, and keyboard behavior.
4. Choose filters/facets from meaningful decision dimensions; show selected state, counts when reliable, clear/apply behavior, and URL persistence.
5. Explain ranking/sorting and result metadata needed for comparison/trust.
6. Design no results, partial results, corrected query, unavailable/permission, and error recovery.
7. Support responsive filter patterns without hiding active criteria.
8. Instrument query reformulation, zero results, abandonment, result selection, and task success; protect sensitive searches.

## Required outputs

- search model
- query/filter/result contracts
- recovery states
- responsive/a11y behavior
- measurement plan

## Quality bar

- Active constraints are visible.
- Keyboard/focus are complete.
- No-result state helps without fabricating results.
- Ranking supports the user decision.

## Failure modes to avoid

- Filters based only on database fields.
- Autosuggest with inaccessible focus.
- Hiding applied filters on mobile.
- Counts that leak restricted data.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
