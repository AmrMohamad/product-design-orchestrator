---
name: responsive-design
description: Design adaptive experiences across viewport, device, orientation, input, content, and platform constraints rather than treating mobile as a scaled desktop.
version: "1.0.0"
category: visual-design
phases: ["structure", "systemize", "implement", "verify"]
triggers: ["responsive UI", "mobile adaptation", "breakpoints", "container queries"]
---

# Responsive Design

## Mission

Preserve task priority and coherence while changing composition and interaction for different environments.

## Use this skill when

- responsive UI
- mobile adaptation
- breakpoints
- container queries

## Inputs

- task/content hierarchy
- device/context evidence
- platform constraints
- existing breakpoints/layout system

## Protocol

1. Define supported environment range and prioritize based on real users/constraints.
2. Identify invariant user outcome and elements that may reorder, collapse, change control, become progressive, or move to another surface.
3. Choose breakpoints from content/layout failure, not device labels alone; use container queries when component context drives change.
4. Design navigation, tables, filters, dialogs/sheets, forms, media, and multi-pane behavior explicitly.
5. Handle safe areas, dynamic viewport units, orientation, virtual keyboards, touch targets, hover absence, pointer precision, and split-screen/window resizing.
6. Preserve reading/DOM order and accessibility through visual rearrangement.
7. Test real content at narrow, wide, and awkward intermediate sizes plus zoom/text scaling.
8. Document adaptive behavior in screen/component contracts and visual baselines.

## Required outputs

- environment priorities
- adaptive transformation map
- breakpoint/container rules
- component responsive specs
- test matrix

## Quality bar

- Behavior changes intentionally, not just size.
- No critical action disappears.
- DOM order remains logical.
- Intermediate widths are tested.

## Failure modes to avoid

- Desktop squeeze.
- Device-name breakpoints only.
- Horizontal scrolling as default mobile strategy.
- h-screen mobile traps.
- Hover-dependent controls.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
