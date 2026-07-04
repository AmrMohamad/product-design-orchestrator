---
name: native-ui-engineering
description: Implement faithful, accessible, performant native or cross-platform mobile/desktop UI using platform navigation, layout, input, lifecycle, and accessibility conventions.
version: "1.0.0"
category: implementation
phases: ["implement", "verify"]
triggers: ["mobile UI implementation", "native app design", "React Native", "Flutter", "SwiftUI", "Compose"]
---

# Native Ui Engineering

## Mission

Carry product and visual intent into platform-native behavior rather than recreating a web page inside an app.

## Use this skill when

- mobile UI implementation
- native app design
- React Native
- Flutter
- SwiftUI
- Compose

## Inputs

- platform/stack profile
- screen/flow contracts
- design system
- device/OS support

## Protocol

1. Map navigation, back behavior, deep links, lifecycle, permissions, safe areas, keyboard, window/split-view, and platform controls.
2. Use native semantic/accessibility APIs, dynamic type/text scaling, focus/rotor/order, touch targets, and reduced motion.
3. Translate tokens into platform resources/theme objects and support light/dark/high contrast.
4. Design adaptive layout for device class, orientation, fold/window, and input modality.
5. Handle asynchronous state, offline/reconnect, app background/restore, deep link, notification, and interrupted flows.
6. Use performant list/image/animation primitives; profile startup, scrolling, memory, and frame stability.
7. Test on representative real devices/OS versions, not emulator screenshots alone for release-critical work.
8. Document platform-specific deviations from shared design and keep shared semantics consistent.

## Required outputs

- native implementation map
- adaptive/navigation behavior
- accessibility/platform tests
- performance/device evidence
- deviation record

## Quality bar

- Platform conventions are respected.
- Dynamic type and assistive behavior work.
- Lifecycle/interruption is handled.
- Visual language is shared without forcing identical mechanics.

## Failure modes to avoid

- Web-style navigation/control behavior.
- Fixed text/layout sizes.
- Ignoring safe areas/keyboards.
- Testing one simulator only.
- Heavy custom rendering for standard controls.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
