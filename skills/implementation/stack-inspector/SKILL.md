---
name: stack-inspector
description: Detect a project’s platform, framework, versions, rendering, styling, state, data, component, test, and deployment conventions before UI implementation.
version: "1.0.0"
category: implementation
phases: ["orient", "implement"]
triggers: ["detect stack", "inspect frontend project", "before implementation", "framework audit"]
---

# Stack Inspector

## Mission

Prevent invented dependencies and generic code by grounding design engineering in the actual repository.

## Use this skill when

- detect stack
- inspect frontend project
- before implementation
- framework audit

## Inputs

- repository
- manifests/lockfiles
- build configs
- source tree
- running app/logs

## Protocol

1. Identify platform/runtime, framework and exact version, package manager, targets, and build/deploy commands.
2. Map server/client/native boundaries, routing/navigation, data/cache, state, forms/validation, and localization.
3. Inventory styling system, tokens/themes, primitive/component/icon libraries, fonts/assets, and CSS/native conventions.
4. Locate lint/type/test/e2e/Storybook/visual/a11y/performance tooling and CI gates.
5. Trace affected feature files and ownership; identify generated code and forbidden edit zones.
6. Check available dependencies before imports and current official docs for version-sensitive APIs.
7. Document constraints, preferred patterns, gaps, and safe commands.
8. Recommend an adapter skill or official documentation source for the detected stack.

## Required outputs

- stack profile
- affected architecture map
- available UI/tooling inventory
- constraints/gaps
- safe implementation route

## Quality bar

- Versions come from files/commands, not memory.
- Existing conventions are cited.
- No package is assumed.
- Generated/critical code is protected.

## Failure modes to avoid

- Defaulting to React/Tailwind.
- Adding dependencies before package inspection.
- Ignoring server/client boundaries.
- Reading only package.json.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
