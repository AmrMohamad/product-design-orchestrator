---
name: outcomes-metrics
description: Define user-centered success measures, product outcomes, quality and harm guardrails, instrumentation, and decision thresholds.
version: "1.0.0"
category: product-strategy
phases: ["define", "live"]
triggers: ["success metrics", "UX metrics", "KPI", "measure design"]
---

# Outcomes Metrics

## Mission

Make success observable without optimizing a proxy at the expense of the user experience.

## Use this skill when

- success metrics
- UX metrics
- KPI
- measure design

## Inputs

- problem/outcome
- journey
- business/service goals
- available analytics and privacy constraints

## Protocol

1. State the behavior or condition that represents user success, not just feature use.
2. Build a metric tree: outcome → leading behaviors → task/quality measures → guardrails.
3. Include completion, efficiency, comprehension/confidence where relevant, error/recovery, accessibility, support, trust, and retention/return only when meaningful.
4. Define metric formula, denominator, segment, event/source, time window, baseline, target/range, and owner.
5. Identify gaming risks, survivorship bias, dark-pattern incentives, and missing-user signals.
6. Pair quantitative metrics with qualitative research for unexplained behavior.
7. Set decision thresholds and review cadence before launch/experiment.
8. Minimize data collection and document privacy/retention.

## Required outputs

- outcome/metric tree
- metric specifications
- instrumentation map
- guardrails
- decision/review rules

## Quality bar

- Metrics represent value, not activity alone.
- Denominators and segments are explicit.
- Guardrails prevent local optimization harm.
- Collection is proportionate and privacy-aware.

## Failure modes to avoid

- Clicks/time-on-page as universal success.
- Vanity dashboards.
- Targets without baselines.
- Measuring only successful users.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
