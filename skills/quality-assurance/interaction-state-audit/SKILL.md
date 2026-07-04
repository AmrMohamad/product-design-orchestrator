---
name: interaction-state-audit
description: Audit components and flows for complete, correct, accessible state transitions, feedback, concurrency, interruption, persistence, and recovery.
version: "1.0.0"
category: quality-assurance
phases: ["verify"]
triggers: ["state audit", "loading errors empty states", "interaction QA", "microinteraction audit"]
---

# Interaction State Audit

## Mission

Find experience failures that only appear outside the static happy state.

## Use this skill when

- state audit
- loading errors empty states
- interaction QA
- microinteraction audit

## Inputs

- flow/state contracts
- running app
- API/data behavior
- permissions/offline/concurrency constraints

## Protocol

1. Enumerate states and events from the contract and implementation; identify unreachable, missing, or conflicting states.
2. Exercise initial/deferred/background loading, empty variants, partial/stale/offline, validation/server errors, success, undo, and destructive failure.
3. Test rapid repeat input, double submit, navigation during request, cancellation, timeout, retry, race, and optimistic rollback.
4. Test permissions/roles, account lifecycle, external changes, multi-tab/device, and resumability where relevant.
5. Verify visible feedback, announcements, focus, disabled/unavailable explanation, persistence, and next action.
6. Check motion interruption and reduced-motion equivalent.
7. Fix the state model/root component rather than patch each screen.
8. Add deterministic tests for critical transitions and failure injection.

## Required outputs

- state coverage matrix
- missing/incorrect transition findings
- root fixes
- failure-injection/tests
- retest evidence

## Quality bar

- Every consequential event has feedback/recovery.
- Concurrency does not lose or duplicate data.
- State is accessible and persistent as expected.
- Tests cover failures, not only success.

## Failure modes to avoid

- Static screenshot review only.
- Disabled button with no reason.
- Optimistic state without rollback.
- Toast as the only durable feedback.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
