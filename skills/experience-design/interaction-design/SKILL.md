---
name: interaction-design
description: Define how controls, feedback, state transitions, direct manipulation, keyboard/touch input, and recovery behave over time.
version: "1.0.0"
category: experience-design
phases: ["structure", "systemize"]
triggers: ["interaction design", "microinteraction", "state behavior", "feedback pattern"]
---

# Interaction Design

## Mission

Make system behavior predictable, responsive, learnable, and satisfying without unnecessary motion or novelty.

## Use this skill when

- interaction design
- microinteraction
- state behavior
- feedback pattern

## Inputs

- task flow
- component/screen model
- platform conventions
- state/data constraints
- accessibility needs

## Protocol

1. Describe trigger, rules, feedback, loops/modes, completion, interruption, and recovery for each interaction.
2. Choose native/familiar patterns unless a novel model creates clear value and can be taught safely.
3. Define hover/focus/press/selection, disabled/unavailable, loading, optimistic, error, success, undo, and persistence.
4. Ensure keyboard, touch, pointer, screen reader, voice/switch alternatives, and target size as relevant.
5. Use immediate local feedback; distinguish requested, processing, saved, and failed states.
6. Make destructive or irreversible actions proportionately deliberate.
7. Use motion to explain continuity, hierarchy, causality, or state—not to decorate every action.
8. Specify interruption, rapid repeat input, concurrency, latency, and reduced-motion behavior.

## Required outputs

- interaction/state specification
- input/accessibility behavior
- feedback/recovery rules
- motion intent
- acceptance tests

## Quality bar

- Behavior is deterministic and interruptible.
- Feedback communicates actual system state.
- Input modes are equivalent.
- Motion has a named purpose.

## Failure modes to avoid

- Hover-only meaning.
- Fake optimistic success.
- Disabled controls with no explanation.
- Animation as delay.
- Novel controls for ordinary tasks.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
