# Research synthesis — Why this architecture works differently

## The problem diagnosed

The previous large `DESIGN.md` had broad coverage but acted like an encyclopedia. A weak agent could quote rules without making a product decision, generate ceremonial artifacts, mix incompatible style advice, or stop at plausible code. That is a common path to work that is technically “good” but still feels unowned and machine-made.

The rebuilt system changes the unit of work from **rule application** to **decision orchestration**. `DESIGN.md` controls the lifecycle, evidence, gates, and design-to-code responsibility. Narrow skills provide temporary specialist context. Durable `.design/` artifacts preserve decisions. Rendered verification closes the gap between intent and implementation.

## What was learned from Taste Skill

The most transferable ideas were not specific fonts or animation libraries. They were:

- read the room before styling;
- state a compact Design Read;
- infer a design language from audience, product, reference, brand, and quiet constraints;
- tune contextual variance, motion, and density rather than applying one visual default;
- actively counter common model defaults;
- use an established design system when the brief and platform call for one;
- inspect dependencies and the existing project;
- audit redesigns before changing them;
- run a rendered preflight instead of trusting source code.

This package extends those ideas beyond marketing pages by adding research integrity, product/service strategy, whole-journey UX, design systems, any-stack implementation, accessibility, release, and live learning. It preserves the upstream Taste Skill unchanged as an optional specialist reference rather than pretending its page-focused scope is universal.

## What was learned from all 110 UI Skills catalog entries

The catalog demonstrates that quality comes from specificity: a focused accessibility fix, motion-performance audit, framework practice, typography pass, browser automation workflow, or chart skill is more useful than several overlapping “make it beautiful” prompts. Its root router explicitly favors the smallest useful set and no more than three skills for broad work.

The catalog also exposes a critical orchestration need: skills vary by topic, stack, source, maintenance, assumptions, and license. Loading them all would create conflicts and context dilution. The local registry therefore indexes every catalog entry, while the router ranks by decision, phase, stack, specificity, and source. Only two MIT-licensed upstream reference files are bundled; other skills are acquired as reviewed text when needed.

## What professional product/service lifecycles add

Strong design is nonlinear but not directionless. The combined lifecycle uses:

- discovery to understand people, systems, constraints, and the whole problem;
- definition to choose an outcome and expose assumptions;
- divergent exploration to avoid polishing the first idea;
- structure and service/interaction design before decoration;
- prototypes selected for risky assumptions, not presentation theater;
- alpha-like learning before beta-like production hardening;
- multidisciplinary implementation, accessibility, privacy, security, operations, and measurement;
- live learning and responsible retirement.

The system allows loops and proportional compression. A tiny local fix should not perform a discovery program. A high-consequence service should not skip representative research, expert review, error/recovery design, and release safeguards.

## What robust UX research requires from AI

An AI agent is useful for planning, source retrieval, note organization, hypothesis generation, and traceability. It is not a participant population. The package therefore:

- starts with the decision and uncertainty, not a favorite method;
- labels observed, reported, measured, inferred, assumed, and synthetic claims;
- forbids invented quotes, participants, personas, market facts, lifts, conformance, or test results;
- separates attitudinal from behavioral and qualitative from quantitative evidence;
- recruits by relevant behavior/context and includes often-excluded users;
- records method limits, contradiction, negative cases, and confidence;
- triangulates sources that answer different questions;
- converts evidence into act/test/hold decisions rather than decorative insights.

## What makes a design feel human-made

Human-made does not mean maximally unusual. It means the work shows selection and attention:

- a product-specific thesis and creative tension;
- one signature move rather than novelty everywhere;
- real content, states, awkward widths, and failure conditions;
- optical corrections and deliberate omission;
- familiar conventions retained when they support speed and trust;
- references decomposed into principles instead of copied costumes;
- a coherent system spanning typography, composition, material, imagery, interaction, and motion;
- rendered critique tied to the intended outcome.

## What closes the design-to-code gap

The same agent must inspect the stack, write behavior/state contracts, implement vertical slices, and compare the rendered result. “Pixel perfect” is defined as a controlled process: stable reference, matched environment, deterministic screenshots, geometry/type/material/state/responsive comparison, correction, and documented deviations. Accessibility and performance remain independent gates; a visually close result can still be unusable.

## Architectural conclusion

The final package is deliberately layered:

1. `AGENTS.md` boots the agent.
2. `DESIGN.md` controls decisions and delivery.
3. `SOUL.md` creates professional presence without overriding method.
4. `skills/` supplies narrow expertise.
5. `registry/` finds local and external expertise.
6. `.design/` templates preserve evidence and intent.
7. playbooks sequence common modes.
8. scripts initialize, route, safely fetch text, and validate.

This makes a capable agent faster and a weak agent harder to derail: it must make explicit decisions, cite evidence, stay inside the real stack, complete states, and prove the rendered result.
