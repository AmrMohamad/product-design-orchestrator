---
name: data-visualization
description: Select, design, annotate, and implement charts and visual explanations that support accurate comparison, trend, distribution, relationship, and decision making.
version: "1.0.0"
category: visual-design
phases: ["structure", "systemize", "verify"]
triggers: ["charts", "data visualization", "dashboard graphs", "visualize data"]
---

# Data Visualization

## Mission

Make data easier to reason about without distorting scale, uncertainty, missingness, or context.

## Use this skill when

- charts
- data visualization
- dashboard graphs
- visualize data

## Inputs

- decision/question
- data types/quality/volume
- audience literacy
- update/freshness
- accessibility/platform

## Protocol

1. Write the question the visualization must answer and the action it may support.
2. Choose encoding by task: position/length before area/color; chart only when it improves over text/table.
3. Set honest scales, units, baselines, aggregation, time windows, comparison groups, and sorting.
4. Expose uncertainty, missing data, outliers, thresholds, provenance, and freshness.
5. Use direct labels/annotations and meaningful color; avoid legends when labels fit.
6. Provide table/text alternative and keyboard/screen-reader strategy for interactive charts.
7. Design hover/focus/touch, filtering, zoom, selection, reset, loading/error, and export behavior.
8. Test color vision, small screens, high density, low sample sizes, and misleading correlations.

## Required outputs

- question/chart rationale
- encoding/scale spec
- annotation/color rules
- interaction/accessibility contract
- data-quality notes

## Quality bar

- Visual encoding supports the task.
- Scale and denominator are honest.
- Uncertainty/missingness are visible.
- Accessible alternatives retain meaning.

## Failure modes to avoid

- 3D charts.
- Dual axes without strong reason.
- Truncated bars.
- Rainbow palettes.
- Decorative charts for single metrics.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
