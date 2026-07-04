---
name: release-readiness
description: Run a final cross-functional release gate covering user outcome, behavior, content, accessibility, visual fidelity, performance, resilience, privacy, observability, rollback, and ownership.
version: "1.0.0"
category: quality-assurance
phases: ["verify", "live"]
triggers: ["release checklist", "launch UI", "design QA before release", "definition of done"]
---

# Release Readiness

## Mission

Decide whether the experience is safe and credible to ship, not merely whether the ticket is coded.

## Use this skill when

- release checklist
- launch UI
- design QA before release
- definition of done

## Inputs

- approved scope/criteria
- build and tests
- research/QA evidence
- deployment/operations plan
- known risks

## Protocol

1. Trace delivered behavior to approved outcome, scope, decisions, and acceptance criteria.
2. Confirm critical journeys, roles, data, errors, recovery, responsive states, themes, and content extremes.
3. Review accessibility methods/results and unresolved barriers.
4. Review screenshots/visual diffs and accepted changes against approved direction.
5. Check performance budgets/field plan, privacy/security/trust, localization, metadata, and support readiness.
6. Verify analytics/observability, alerting, feature flag/rollout, rollback, migration, and data compatibility.
7. Classify open issues S0–S4 with owner and explicit acceptance; block S0/S1.
8. Define post-release monitoring, research, and decision date.

## Required outputs

- release review
- go/no-go decision
- accepted-risk register
- rollout/rollback plan
- post-release watch plan

## Quality bar

- Evidence supports every gate.
- Known risks have owners.
- Rollback and observability are real.
- Design quality is judged in the deployed-like build.

## Failure modes to avoid

- Checklist theater.
- Shipping with hidden S1 issue.
- No rollback.
- Treating launch as end of ownership.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
