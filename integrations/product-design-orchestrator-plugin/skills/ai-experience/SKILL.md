---
name: ai-experience
description: Design AI-assisted and generative product experiences with clear capability, provenance, uncertainty, control, review, recovery, and evaluation.
version: "1.0.0"
category: experience-design
phases: ["define", "structure", "validate", "verify"]
triggers: ["AI UX", "copilot", "chat interface", "generative AI product", "agent UI"]
---

# Ai Experience

## Mission

Help users benefit from probabilistic automation without hiding uncertainty, responsibility, cost, or data use.

## Use this skill when

- AI UX
- copilot
- chat interface
- generative AI product
- agent UI

## Inputs

- user job and stakes
- model capabilities/limits
- data/provenance
- latency/cost
- human escalation and policy

## Protocol

1. Decide whether AI is necessary and identify the exact user judgment it augments or automates.
2. Set capability boundaries, unsupported requests, risk tiers, and human responsibility.
3. Design input guidance, context selection, privacy/data disclosure, progress, latency, cancellation, and retry.
4. Present outputs with provenance, editable structure, uncertainty/limitations, alternatives, and verification paths appropriate to stakes.
5. Support correction, regenerate/branch/compare, undo, history, export, escalation, and feedback without making users train the model unknowingly.
6. Separate conversational convenience from durable product objects and workflows.
7. Protect against prompt injection/content misuse, sensitive data leakage, automation bias, over-reliance, and harmful output.
8. Evaluate task quality, calibration, failure modes, user verification behavior, latency/cost, accessibility, and model/version drift.
9. Design graceful non-AI fallback for critical tasks.

## Required outputs

- AI value/risk contract
- interaction and output model
- provenance/control/recovery states
- evaluation plan
- fallback/escalation

## Quality bar

- Automation is visible and controllable.
- High-stakes output requires appropriate review.
- Data use is clear.
- Evaluation includes failures and model drift.

## Failure modes to avoid

- Chat as the default UI for every task.
- Fake confidence indicators.
- Hiding latency/cost.
- Treating thumbs-up as complete evaluation.
- No deterministic fallback.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
