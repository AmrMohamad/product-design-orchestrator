---
name: motion
description: Design purposeful, interruptible, performant motion that explains continuity, causality, hierarchy, feedback, or spatial relationships and respects user preferences.
version: "1.0.0"
category: visual-design
phases: ["explore", "systemize", "implement", "verify"]
triggers: ["animation", "motion design", "transitions", "microinteractions"]
---

# Motion

## Mission

Make change feel coherent and alive without delaying work, causing discomfort, or masking weak interaction design.

## Use this skill when

- animation
- motion design
- transitions
- microinteractions

## Inputs

- interaction/state model
- aesthetic thesis/motion dial
- platform APIs
- performance/accessibility constraints

## Protocol

1. Name the purpose of each motion: orient, connect, acknowledge, reveal, prioritize, or delight.
2. Define start/end state, trigger, duration, easing/spring, delay/stagger, interruption, reversal, and rapid-input behavior.
3. Use transform/opacity and compositor-friendly properties by default; profile exceptions.
4. Keep frequent task motion shorter and quieter than rare expressive moments.
5. Coordinate motion hierarchy; do not animate every child independently.
6. Provide reduced-motion behavior that preserves meaning and completion.
7. Avoid scroll hijacking, inaccessible parallax, autoplay distraction, and animation that blocks input.
8. Test low-end devices, dropped frames, resize, background tabs, and async state changes.

## Required outputs

- motion grammar/tokens
- interaction motion specs
- reduced-motion alternatives
- performance test notes

## Quality bar

- Every motion has purpose.
- Animations are interruptible and state-correct.
- Reduced motion is meaningful.
- Performance is measured in context.

## Failure modes to avoid

- Animation as loading delay.
- Spring on everything.
- Infinite decorative loops near content.
- Animating layout continuously.
- Hover motion with no touch equivalent.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
