---
name: experiment-design
description: Design ethical product experiments that test a causal hypothesis with valid metrics, guardrails, assignment, analysis, and stopping rules.
version: "1.0.0"
category: product-strategy
phases: ["validate", "live"]
triggers: ["A/B test", "product experiment", "hypothesis test", "evaluate change"]
---

# Experiment Design

## Mission

Reduce uncertainty without exposing users to avoidable harm or turning randomization into a substitute for product judgment.

## Use this skill when

- A/B test
- product experiment
- hypothesis test
- evaluate change

## Inputs

- hypothesis
- candidate variants
- target population
- metrics/baseline
- traffic and risk

## Protocol

1. Write causal hypothesis, mechanism, primary outcome, guardrails, and falsification condition.
2. Decide whether experimentation is ethical and feasible; exclude safety/legal/accessibility regressions from tests.
3. Define unit of assignment, eligibility, exposure, contamination risks, sample/power approach, duration, and novelty/seasonality considerations.
4. Predefine primary/secondary metrics, segments, data-quality checks, and analysis plan.
5. Keep variants meaningfully different on the hypothesis, not multiple simultaneous unknowns.
6. Instrument exposure and outcome reliably; run an A/A or validation check when warranted.
7. Set stopping rules and avoid repeated peeking or post-hoc success metrics.
8. Interpret practical significance, guardrails, segments, and qualitative evidence before shipping.
9. Document rollout, rollback, and learning even when results are null.

## Required outputs

- experiment brief
- variant contract
- instrumentation/analysis plan
- ethics/guardrails
- decision rule
- result report

## Quality bar

- The hypothesis names a mechanism.
- Assignment and exposure are valid.
- Guardrails protect users.
- Null/negative results remain useful.

## Failure modes to avoid

- Testing deceptive patterns.
- Changing five things per variant.
- Stopping at significance.
- Generalizing beyond eligible users.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
