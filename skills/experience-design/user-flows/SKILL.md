---
name: user-flows
description: Model complete user and system flows with decisions, states, alternate paths, permissions, recovery, and cross-channel handoffs.
version: "1.0.0"
category: experience-design
phases: ["structure"]
triggers: ["user flow", "task flow", "screen flow", "state diagram"]
---

# User Flows

## Mission

Make the temporal logic of an experience clear enough to design, implement, and test.

## Use this skill when

- user flow
- task flow
- screen flow
- state diagram

## Inputs

- user job and entry points
- rules/data/permissions
- current journey
- success/failure conditions

## Protocol

1. Define actor, goal, trigger, entry, success, and meaningful abandonment.
2. Map user actions and system responses as separate steps.
3. Include decisions, validation, asynchronous waits, permissions, role changes, timeouts, and external handoffs.
4. Add alternate, error, partial-success, retry, undo, cancellation, and support paths.
5. Name persistent state and where users can resume or inspect history.
6. Identify moments needing explanation, confirmation, reassurance, or accessibility accommodation.
7. Simplify by removing unnecessary choices/steps, not by hiding required information.
8. Translate the approved flow into screen/component contracts and journey tests.

## Required outputs

- flow diagram/text model
- state/decision table
- failure/recovery paths
- screen map
- test scenarios

## Quality bar

- System feedback follows every consequential action.
- Alternate paths are first-class.
- Flow rules match product/data behavior.
- The diagram is testable.

## Failure modes to avoid

- Happy path only.
- One box per screen with no system state.
- Adding confirmation to compensate for unclear consequences.
- Ignoring resume/history.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
