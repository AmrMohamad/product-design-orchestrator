---
name: accessibility-audit
description: Audit a complete user journey against applicable accessibility standards using automated checks, manual inspection, keyboard, zoom/reflow, and assistive technology as warranted.
version: "1.0.0"
category: quality-assurance
phases: ["validate", "verify", "live"]
triggers: ["accessibility audit", "WCAG 2.2", "screen reader test", "fix accessibility"]
---

# Accessibility Audit

## Mission

Find, prioritize, remediate, and verify barriers based on user impact rather than produce a compliance score.

## Use this skill when

- accessibility audit
- WCAG 2.2
- screen reader test
- fix accessibility

## Inputs

- app/build
- journey/states
- standard/level
- browser/device/AT support
- existing test tooling

## Protocol

1. Define audit scope as complete processes, representative pages/components, states, and environments.
2. Run automated checks and treat results as leads; inspect semantics, names, relationships, landmarks, headings, language, and status messages.
3. Test keyboard-only navigation, focus order/visibility/obscuring, traps, dialogs, menus, drag alternatives, shortcuts, and skip paths.
4. Test zoom, reflow, text spacing, target size, contrast/non-color cues, reduced motion, orientation, and media alternatives.
5. Use screen reader/assistive technology for critical custom widgets and journeys with platform-appropriate expectations.
6. Map issues to user consequence and applicable criterion/pattern; classify severity and affected scope.
7. Fix root component/pattern where possible, add regression tests, and manually retest.
8. Document limitations; do not claim conformance from partial/automated testing.

## Required outputs

- scope/methods
- findings with evidence/severity
- remediation plan/fixes
- retest results
- limitations/conformance wording

## Quality bar

- Critical journeys and states are covered.
- Manual testing complements automation.
- Root causes are fixed systemically.
- Claims match actual scope.

## Failure modes to avoid

- Score chasing.
- ARIA patching without behavior.
- No keyboard test.
- Claiming WCAG compliance from one page/tool.
- Ignoring cognitive/content barriers.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
