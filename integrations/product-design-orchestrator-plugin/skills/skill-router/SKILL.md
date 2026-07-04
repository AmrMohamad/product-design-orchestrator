---
name: skill-router
description: Select the smallest useful bundled or external skill set by decision, lifecycle phase, risk, platform, and specificity.
version: "1.0.0"
category: orchestration
phases: ["orient", "all"]
triggers: ["find skill", "which skill", "route UI task", "skill recommendation"]
---

# Skill Router

## Mission

Give the active agent just enough specialist context to make the current decision well.

## Use this skill when

- find skill
- which skill
- route UI task
- skill recommendation

## Inputs

- task statement
- current lifecycle phase
- risk/domain
- platform/stack
- local and external registry

## Protocol

1. Name the decision or defect in one sentence.
2. Classify it by phase and domain: research, strategy, structure, interaction, visual craft, system, implementation, or verification.
3. Detect stack and existing design system before selecting framework-specific advice.
4. Search bundled skills first, then the mirrored UI Skills registry and approved upstream resources.
5. Rank candidates by specificity, fit, maintenance/source trust, and conflict risk.
6. Choose one skill by default, two for separate angles, or three only for broad reviews and multi-surface redesigns.
7. State why each selected skill is needed and what it must output.
8. Record external source/version/hash when it materially affects the product; unload context after the phase.

## Required outputs

- ranked recommendation
- reason and expected output
- local path or safe install command
- conflict/recency warning

## Quality bar

- Specific beats broad.
- Official stack guidance beats generic implementation advice.
- The recommendation stays within the skill budget.
- No external code is executed during discovery.

## Failure modes to avoid

- Using several broad taste skills together.
- Selecting by popularity alone.
- Ignoring version or license.
- Letting a skill override DESIGN.md.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
