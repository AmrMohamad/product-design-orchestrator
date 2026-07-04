---
name: data-dense-interfaces
description: Design dashboards, tables, admin, monitoring, and operational tools for scanning, comparison, action, exception handling, and scale.
version: "1.0.0"
category: experience-design
phases: ["structure", "systemize", "verify"]
triggers: ["dashboard", "data table", "admin UI", "analytics interface", "dense product UI"]
---

# Data Dense Interfaces

## Mission

Optimize expert and mixed-skill work for decision speed, accuracy, context, and safe bulk action rather than decorative card layouts.

## Use this skill when

- dashboard
- data table
- admin UI
- analytics interface
- dense product UI

## Inputs

- decisions/tasks
- data model/volume/freshness
- roles/permissions
- update frequency
- device/environment

## Protocol

1. Start with the decisions and actions the data must support; remove metrics without an owner or use.
2. Prioritize overview, exceptions, trends, detail, and action; do not give every metric equal visual weight.
3. Choose table, chart, list, or summary according to comparison and pattern task.
4. Design columns, alignment, units, precision, sorting, filtering, grouping, density, resizing, sticky context, and responsive alternatives.
5. Handle loading/skeleton versus stale data, freshness, partial failure, missing values, outliers, thresholds, and provenance.
6. Define row/bulk selection, destructive/action feedback, permission boundaries, export, and audit history.
7. Support keyboard navigation, screen-reader semantics/alternatives, zoom, color-independent status, and high-density readability.
8. Test realistic/high volume and slow data; use pagination/virtualization without breaking task continuity.

## Required outputs

- decision hierarchy
- data display/table contracts
- actions/permissions
- state/freshness model
- scale/accessibility test plan

## Quality bar

- Data displays map to decisions.
- Units, dates, freshness, and missing values are clear.
- Density is adjustable or appropriate.
- Actions preserve context and recovery.

## Failure modes to avoid

- Dashboard as a grid of equal cards.
- Charts for single values.
- Color-only status.
- Horizontal-scroll surprises.
- Skeletons that lie about structure.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
