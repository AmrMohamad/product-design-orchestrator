---
name: technology-adapter
description: Translate approved design behavior into the conventions and capabilities of any detected technology stack using current official documentation.
version: "1.0.0"
category: implementation
phases: ["implement"]
triggers: ["unknown stack", "adapt design to framework", "any technology", "platform adapter"]
---

# Technology Adapter

## Mission

Preserve design intent while remaining native, maintainable, and version-correct in the target platform.

## Use this skill when

- unknown stack
- adapt design to framework
- any technology
- platform adapter

## Inputs

- stack profile
- screen/component contracts
- official docs
- existing project patterns

## Protocol

1. Identify platform-native equivalents for navigation, layout, typography, controls, state, animation, accessibility, and testing.
2. Check version-current official documentation before choosing APIs or libraries.
3. Map design tokens to the platform theme/resource mechanism.
4. Map components to native/established primitives and explain unavoidable behavioral differences.
5. Preserve platform input/back/window/safe-area/accessibility conventions.
6. Choose responsive/adaptive approach appropriate to web, mobile, desktop, embedded, or cross-platform runtime.
7. Implement a small vertical proof for uncertain rendering/interaction behavior.
8. Record adaptations in the design decision log rather than silently diverging.

## Required outputs

- platform mapping
- token/component adaptation
- implementation constraints
- proof/spike result
- documented deviations

## Quality bar

- Official current guidance is used.
- The result feels native to the platform.
- Design meaning survives adaptation.
- Differences are intentional and tested.

## Failure modes to avoid

- Web metaphors pasted into native apps.
- Invented APIs.
- Framework migration for design convenience.
- Pixel copying that breaks platform behavior.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
