---
name: accessibility-by-design
description: Translate accessibility and inclusive user needs into flow, component, content, token, and acceptance requirements before implementation.
version: "1.0.0"
category: design-systems
phases: ["define", "structure", "systemize"]
triggers: ["accessible design", "WCAG design requirements", "inclusive UI", "keyboard spec"]
---

# Accessibility By Design

## Mission

Prevent barriers structurally instead of discovering them only in a final automated audit.

## Use this skill when

- accessible design
- WCAG design requirements
- inclusive UI
- keyboard spec

## Inputs

- user journey
- known access needs
- platform/standard target
- components/content/motion

## Protocol

1. Identify critical tasks and barriers across perceivable, operable, understandable, and robust dimensions.
2. Map keyboard/focus order, visible focus, shortcuts, escape/cancel, and no-trap behavior.
3. Define semantic structure, landmarks/headings, names/descriptions, status announcements, and error relationships.
4. Specify contrast, non-color cues, zoom/reflow/text spacing, target size, drag alternatives, time limits, and reduced motion.
5. Use native patterns first; reference ARIA Authoring Practices for custom widgets and test actual behavior.
6. Design captions/transcripts/alternatives for media and meaningful image/diagram alternatives.
7. Include disabled people in research and assistive-technology testing proportionate to risk.
8. Write journey-level acceptance criteria and manual checks; do not equate automated score with conformance.

## Required outputs

- accessibility requirements
- focus/keyboard/announcement specs
- component criteria
- inclusive research/test plan

## Quality bar

- Requirements cover complete tasks.
- Native semantics are preferred.
- Manual checks complement automation.
- Design includes alternatives, not exceptions.

## Failure modes to avoid

- Adding ARIA to divs by default.
- Color contrast as the entire audit.
- Accessibility overlay claims.
- One screen-reader test as certification.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
