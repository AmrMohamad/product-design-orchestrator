---
name: web-ui-engineering
description: Implement semantic, responsive, accessible, performant web UI with robust browser behavior, intrinsic layout, and maintainable component boundaries.
version: "1.0.0"
category: implementation
phases: ["implement", "verify"]
triggers: ["web frontend", "HTML CSS UI", "responsive web implementation", "design engineering"]
---

# Web Ui Engineering

## Mission

Express the design faithfully using the web platform and project framework without brittle CSS or unnecessary JavaScript.

## Use this skill when

- web frontend
- HTML CSS UI
- responsive web implementation
- design engineering

## Inputs

- stack profile
- screen/component contracts
- browser support
- performance/accessibility targets

## Protocol

1. Start with semantic HTML and native controls; use ARIA only to supply missing semantics for custom widgets.
2. Build intrinsic layout with grid/flex, min/max/clamp, logical properties, container/media queries, and dynamic viewport/safe-area handling as appropriate.
3. Use tokens/CSS variables and existing styling conventions; avoid duplicated magic values and specificity escalation.
4. Preserve SSR/hydration, focus, form, navigation, URL, history, and progressive-enhancement behavior.
5. Isolate client interactivity; avoid state updates for continuous animation/scroll values and unnecessary re-renders.
6. Reserve media dimensions, optimize fonts/assets, and protect LCP/INP/CLS and low-end devices.
7. Implement reduced motion, forced colors/high contrast, zoom/reflow, keyboard, touch, and pointer behavior.
8. Test browsers/viewports/content extremes and capture screenshots/visual baselines.

## Required outputs

- semantic component implementation
- responsive CSS/system mapping
- browser/a11y/performance tests
- visual evidence

## Quality bar

- DOM order matches reading order.
- JavaScript is used for behavior, not avoidable layout.
- The UI survives zoom/content extremes.
- Browser evidence supports completion.

## Failure modes to avoid

- Div-button widgets.
- Absolute-position layout patchwork.
- h-screen mobile traps.
- Animation-driven React re-renders.
- Unverified browser assumptions.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
