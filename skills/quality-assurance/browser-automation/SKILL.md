---
name: browser-automation
description: Use browser automation to exercise journeys, capture deterministic screenshots, inspect accessibility and console/network behavior, and preserve reproducible QA evidence.
version: "1.0.0"
category: quality-assurance
phases: ["validate", "verify"]
triggers: ["Playwright", "browser test", "automate screenshots", "E2E UI test"]
---

# Browser Automation

## Mission

Turn critical UI behavior and visual contracts into repeatable checks without confusing automation with complete human evaluation.

## Use this skill when

- Playwright
- browser test
- automate screenshots
- E2E UI test

## Inputs

- running app/test environment
- journey/state matrix
- stable data/auth
- browser support

## Protocol

1. Choose high-value journeys and states; seed deterministic data and isolate external volatility.
2. Use role/label/test-id locators that reflect accessible behavior; avoid brittle CSS/XPath selectors.
3. Exercise keyboard and pointer paths, navigation/history, focus, dialogs, forms, errors, loading, permissions, and responsive viewports.
4. Capture screenshots or visual snapshots under consistent environment; mask only documented volatile content.
5. Collect console errors, failed requests, traces, videos, and network timing for failures.
6. Use retries as diagnostic, not a way to hide flakiness; eliminate race conditions with observable state.
7. Run appropriate browser/platform projects and CI; quarantine only with owner and deadline.
8. Keep manual exploratory and assistive-technology checks for behavior automation cannot judge.

## Required outputs

- E2E/visual tests
- fixtures/seeding
- trace/screenshot evidence
- CI configuration
- flakiness/coverage notes

## Quality bar

- Tests reflect user goals.
- Locators encourage accessibility.
- Screenshots are deterministic.
- Failures provide diagnosable evidence.

## Failure modes to avoid

- Sleep-based waits.
- Testing implementation internals.
- Masking large UI regions.
- Retrying flakes indefinitely.
- Calling automated axe complete accessibility testing.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
