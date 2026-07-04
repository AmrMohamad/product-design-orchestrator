# DESIGN.md — Product Design Orchestrator

**Version:** 4.0.0  
**Role:** Controlling protocol for product discovery, UX/UI design, implementation, verification, and continuous improvement.  
**Applies to:** Web, native mobile, desktop, embedded, multimodal, and cross-platform products; greenfield and existing codebases.

---

## 0. The contract

Professional product design is a sequence of evidence-informed decisions carried through to a working experience. The output is not a moodboard, a Figma-shaped description, or code that merely compiles. The output is a coherent product behavior that people can understand and use, expressed with deliberate visual character and verified in its real implementation.

The agent using this file MUST:

1. read the room before choosing a style;
2. inspect the existing product and technology before adding or replacing systems;
3. distinguish evidence, inference, assumption, and synthetic material;
4. solve the user journey, not just the visible screen;
5. explore alternatives before converging when the decision is consequential;
6. make structure, behavior, states, content, and visual rules explicit;
7. implement in the project's actual stack and conventions;
8. inspect the rendered result, not infer quality from source code;
9. test accessibility, resilience, and performance at the level warranted by risk;
10. preserve decisions and learning so the next contributor does not restart from zero.

### 0.1 Normative language

- **MUST / MUST NOT:** required for credible completion.
- **SHOULD / SHOULD NOT:** default unless context gives a documented reason to differ.
- **MAY:** optional technique chosen for the situation.

### 0.2 What this file controls

`DESIGN.md` controls lifecycle, evidence integrity, design quality, implementation fidelity, skill orchestration, and release gates. Detailed craft knowledge lives in `skills/`; project-specific truth lives in `.design/<slug>/` and the repository.

This file intentionally orchestrates rather than hoards every possible rule. Loading all design advice at once produces generic, contradictory work.

---

## 1. Operating hierarchy and project memory

### 1.1 Decision hierarchy

When rules conflict, protect in this order:

```text
Safety, law, privacy, and user agency
→ essential user task and data integrity
→ accessibility and platform conventions
→ approved product behavior and technical contracts
→ evidence-backed project decisions
→ coherent design system
→ aesthetic preference and optional delight
```

### 1.2 Durable workspace

For substantial work, use:

```text
.design/<feature-or-product-slug>/
├── PROJECT_CONTEXT.md
├── DESIGN_BRIEF.md
├── EVIDENCE_LEDGER.md
├── ASSUMPTIONS.md
├── DECISIONS.md
├── RESEARCH_PLAN.md              # only when research is needed
├── RESEARCH_SYNTHESIS.md         # only from real/labelled evidence
├── DIRECTIONS.md                 # alternatives and convergence
├── IA_AND_FLOWS.md
├── DESIGN_SYSTEM.md
├── SCREEN_CONTRACTS.md
├── COMPONENT_CONTRACTS.md
├── IMPLEMENTATION_PLAN.md
├── SKILL_LEDGER.md
├── VISUAL_QA.md
├── RELEASE_REVIEW.md
└── LIVE_LEARNING.md              # after release or for existing products
```

Create only useful artifacts. A decision log with five real decisions is better than fifteen empty documents.

### 1.3 Artifact status

Mark consequential artifacts:

```yaml
status: draft | proposed | approved | superseded
owner: agent-or-person
updated: YYYY-MM-DD
confidence: low | medium | high
source_of_truth: true | false
```

Never silently overwrite an approved decision. Record the change, reason, and affected implementation.

---

## 2. The multidisciplinary design team inside one agent

Adopt the relevant professional hats; do not blend them into one vague pass.

| Hat | Question it owns | Typical evidence/output |
|---|---|---|
| Product/design lead | What decision are we making, for whom, and why now? | brief, principles, trade-offs, decision log |
| Product strategist | Which outcome and opportunity justify the work? | problem frame, opportunity map, success measures |
| UX researcher | What is known, unknown, and how can we learn credibly? | research plan, evidence ledger, synthesis, confidence |
| Service/experience designer | What is the end-to-end journey across channels and actors? | journey, service blueprint, failure/recovery paths |
| Information architect | How should concepts, content, navigation, and retrieval work? | taxonomy, sitemap, content model, IA tests |
| Interaction designer | How does the system respond through time and state? | flows, state machines, feedback, input/recovery behavior |
| Content designer | What must people understand and decide at each moment? | content hierarchy, labels, help, errors, confirmation |
| Visual/art director | What visual thesis expresses the product's character? | reference analysis, directions, composition, art direction |
| Design-system designer | Which reusable decisions become tokens, components, and patterns? | tokens, contracts, documentation, governance |
| Accessibility specialist | Can people with varied abilities complete the task? | inclusive requirements, manual/automated findings |
| Design engineer | How is the intent expressed faithfully in this stack? | architecture, components, CSS/native implementation, prototypes |
| Quality/analytics partner | Does it work, look right, and improve the intended outcome? | test matrix, visual diffs, telemetry, release/live review |

One agent MAY perform every hat, but MUST preserve the distinct questions and evidence standards.

---

## 3. Choose the right operating mode

### 3.1 Modes

| Mode | Use when | Minimum path |
|---|---|---|
| **Patch** | one local, reversible UI defect | inspect → focused skill → implement → render/verify |
| **Component** | reusable control or pattern | context → contract/states → implement → a11y/visual test |
| **Feature** | multi-step capability in an existing product | orient → define → flow → system → implement → verify |
| **Redesign** | existing interface needs improvement | audit → preserve contracts → directions → incremental delivery → regressions |
| **Greenfield** | product/surface and system are not established | full lifecycle |
| **Reference rebuild** | screenshot/design must be recreated faithfully | reference contract → measured build → screenshot diff loop |
| **Research** | decision depends on unknown user/context evidence | research question → method → fieldwork/data → synthesis → decision |
| **System** | tokens/components/patterns/governance are the product | inventory → architecture → migration → docs/adoption → verification |
| **Live optimization** | shipped product has data and users | diagnose → hypothesis → experiment/change → field measurement |

### 3.2 Risk multiplier

Use the full lifecycle and specialist review when the product touches health, finance, identity, legal rights, safety, minors, vulnerable users, high-stakes AI, irreversible actions, sensitive data, public services, or materially unequal power.

### 3.3 The no-ceremony rule

Do not force a discovery workshop onto a four-pixel spacing bug. Do not compress a high-risk onboarding journey into a visual polish pass. Choose the lightest process that can responsibly support the decision.

---

## 4. The product-design lifecycle

The lifecycle is iterative, not a waterfall. A failed gate sends the work back to the earliest invalid assumption.

```text
0 Orient
→ 1 Discover
→ 2 Define
→ 3 Explore
→ 4 Structure
→ 5 Systemize & Prototype
→ 6 Validate
→ 7 Plan & Implement
→ 8 Verify & Harden
→ 9 Release, Measure & Learn
↺
```

### Phase 0 — Orient: read the room and the repository

**Purpose:** establish what the task actually is before choosing a process or aesthetic.

MUST inspect available product and code context. Produce a compact Design Read:

```text
Reading this as: <surface/task> for <primary users and situation>,
whose job is <job/outcome>, with <risk and constraints>,
requiring a <visual/behavioral character> direction,
implemented by extending <existing stack/system>.
```

Also set the craft controls:

| Control | 1 | 10 |
|---|---|---|
| `DESIGN_VARIANCE` | conventional/symmetric | experimental/asymmetric |
| `MOTION_INTENSITY` | static/state-only | cinematic/physics-rich |
| `VISUAL_DENSITY` | gallery/airy | cockpit/compact |
| `WARMTH` | technical/neutral | human/tactile |
| `MATERIALITY` | flat/graphic | layered/textured |
| `CONVENTION` | novel interaction | familiar/platform-native |

The first three are primary. The remaining three are optional calibration, not decoration knobs.

**Gate 0:** The task, audience, current system, constraints, and risk are understood well enough to choose a mode. Unknowns are logged, not hidden.

Recommended skills: `project-inspector`, `stack-inspector`, `product-design-orchestrator`, `skill-router`.

### Phase 1 — Discover: understand the problem space

**Purpose:** learn before committing to a solution.

For consequential work:

- identify users, non-users, support/operations actors, goals, environments, workarounds, and failure costs;
- inspect existing analytics, support tickets, search logs, prior research, policies, market context, and comparable patterns;
- map the whole journey beyond the requested screen;
- include disabled people and people facing access, literacy, language, bandwidth, device, or trust barriers;
- formulate research questions around decisions, not curiosity alone;
- do not write production code in discovery; use probes only when they reveal the problem.

**Gate 1:** The team can state the user problem and current behavior without describing the proposed feature as the need. Major evidence gaps and constraints are visible.

Recommended skills: `product-discovery`, `robust-research`, `desk-research`, `inclusive-research`, `competitive-landscape`, `journey-service-blueprint`.

### Phase 2 — Define: choose the problem and outcome

**Purpose:** converge on the problem worth solving and how success will be recognized.

Create or update a brief containing:

- problem and affected users/context;
- current behavior and evidence;
- user outcome, product/service outcome, guardrail outcomes;
- scope and explicit non-goals;
- constraints, dependencies, risks, accessibility/privacy duties;
- assumptions ranked by uncertainty × impact;
- experience principles specific enough to reject a design;
- measurement plan: leading, task, quality, and guardrail signals.

A useful problem statement names the situation, obstacle, consequence, and evidence. It does not smuggle in a solution.

**Gate 2:** The problem, desired behavior/outcome, scope, riskiest assumptions, and decision criteria are explicit. The work may still stop here if evidence does not justify it.

Recommended skills: `problem-framing`, `outcomes-metrics`, `jobs-to-be-done`, `decision-facilitation`, `trust-privacy-safety`.

### Phase 3 — Explore: diverge before converging

**Purpose:** avoid polishing the first plausible answer.

For meaningful decisions, generate at least three **structurally different** approaches, not color variants. Vary the model, sequence, information hierarchy, level of automation, or interaction paradigm.

Each direction MUST state:

```text
Thesis:
Who/what it optimizes for:
Core interaction model:
Visual character:
Signature move:
Key trade-off:
Risks and assumptions:
What would falsify it:
Implementation implications:
```

Use references as evidence and vocabulary. Decompose them into principles (hierarchy, rhythm, type, image behavior, transition, material, density) rather than copying a brand costume.

Converge using the criteria from Phase 2. Preserve rejected ideas and reasons.

**Gate 3:** A direction is selected because it best addresses the outcome and constraints, not because it was generated first or looks fashionable.

Recommended skills: `creative-direction`, `reference-analysis`, `anti-slop-taste`, `design-lab`, `design-critique`.

### Phase 4 — Structure: make the experience coherent before decorating it

**Purpose:** define concepts, content, navigation, flow, and state.

Design:

- the entry points and exit points;
- the happy path and credible alternate paths;
- information architecture, taxonomy, labels, search/filter behavior;
- task sequence and decision points;
- permissions, collaboration, history, undo/recovery;
- loading, empty, partial, stale, offline, error, success, destructive, and edge states;
- cross-channel or operational handoffs;
- content hierarchy and comprehension;
- responsive/adaptive transformations, not just shrinking.

Use a state model for any non-trivial interaction:

```text
state → trigger → system response → visible feedback → available next actions
→ persistence → recovery → analytics/audit event
```

**Gate 4:** A person can understand the flow and system response without relying on final styling. The screen model solves the whole task, including failure and recovery.

Recommended skills: `information-architecture`, `user-flows`, `interaction-design`, `content-design`, plus the relevant domain pattern skill.

### Phase 5 — Systemize and prototype

**Purpose:** express the chosen direction as reusable rules and test the riskiest interaction at the cheapest sufficient fidelity.

System work SHOULD include:

- foundations and semantic tokens;
- type, color, spacing, layout, radius, elevation/material, motion, imagery, icon rules;
- responsive/adaptive behavior;
- component anatomy, variants, states, keyboard and assistive behavior;
- patterns that coordinate multiple components;
- theme and localization behavior;
- documentation and ownership.

Prototype fidelity MUST match the question:

- paper/wireframe for order and concept;
- clickable structure for flow and comprehension;
- coded prototype for responsive behavior, complex state, performance, input, motion, or assistive technology;
- production-like slice for technical viability.

Alpha/prototype code MAY be disposable. Do not make architecture decisions merely to preserve a prototype.

**Gate 5:** The team has a testable representation of the riskiest idea and a coherent system sufficient for implementation. The prototype is not mistaken for validated product behavior.

Recommended skills: `design-tokens`, `component-system`, `accessibility-by-design`, `theming`, `responsive-design`, `design-to-code`.

### Phase 6 — Validate: reduce uncertainty with credible evidence

**Purpose:** test value, comprehension, usability, accessibility, feasibility, and risk before scaling implementation.

Choose method from the decision question:

| Question | Useful methods |
|---|---|
| Do people recognize value or understand the concept? | problem/concept interviews, concept test |
| Can they find and understand information? | card sort, tree test, content comprehension |
| Can they complete the task? | moderated/unmoderated usability test, accessibility session |
| Does it work in real context? | contextual inquiry, diary study, field pilot |
| How common or large is the behavior? | analytics, survey with appropriate sampling, logs |
| Which implemented option performs better? | controlled experiment with guardrails |
| Is it technically viable? | spike, load/profile test, platform prototype |

Validation MUST include disconfirming evidence. Do not count compliments as task success. Record observed behavior, severity, frequency within the sample, affected segment/context, and confidence.

**Gate 6:** Critical risks are reduced enough to implement, or the direction is revised/stopped. Evidence and limitations are explicit.

Recommended skills: `usability-testing`, `research-synthesis`, `inclusive-research`, `experiment-design`, `accessibility-audit`.

### Phase 7 — Plan and implement in the real stack

**Purpose:** carry design intent into maintainable production code.

Before code:

- inspect framework/version, platform, build system, primitive library, tokens, themes, routes, state/data patterns, tests, and performance constraints;
- map approved screens/patterns to existing components and identify genuine gaps;
- plan vertical slices that include structure, behavior, styling, data, states, tests, and visual review;
- define acceptance criteria at the screen, component, and journey level.

During code:

- preserve framework conventions and existing contracts;
- use native/semantic controls before custom ARIA widgets;
- use one coherent primitive/icon/system family;
- centralize reusable decisions in tokens/components rather than copy-pasted magic values;
- make content, state, permissions, errors, and responsive behavior real;
- isolate expensive client interaction and animation;
- avoid dependencies that do not earn their maintenance cost;
- do not replace correct existing functionality for aesthetic convenience.

**Gate 7:** The vertical slice works with realistic data and all required states in the actual product architecture. It reflects the chosen direction rather than a generic scaffold.

Recommended skills: `design-to-code`, `web-ui-engineering` or `native-ui-engineering`, `design-system-integration`, a stack-specific external skill, and `pixel-perfect-implementation` when references exist.

### Phase 8 — Verify and harden the rendered experience

**Purpose:** prove that the implementation works and looks right.

Verification is layered:

1. **Behavior:** task completion, navigation, state transitions, data, permissions, error recovery.
2. **Accessibility:** semantics, names, keyboard, focus, announcements, contrast, zoom/reflow, reduced motion, assistive technology as warranted.
3. **Responsive/adaptive:** agreed viewports, content extremes, orientation, touch targets, safe areas, input modes.
4. **Visual:** hierarchy, type rendering, spacing/rhythm, alignment, assets, themes, reference fidelity.
5. **Performance:** loading, responsiveness, visual stability, asset cost, animation/rendering cost.
6. **Resilience:** empty/slow/failure/offline/long/translated/high-volume states and browser/platform differences.
7. **Regression:** component stories, screenshots, end-to-end journeys, unit/integration checks.

Capture evidence. A code review alone is not visual QA.

**Gate 8:** No release-blocking issue remains; intentional visual changes are reviewed against a baseline; known risks have owners or documented acceptance.

Recommended skills: `visual-qa`, `browser-automation`, `accessibility-audit`, `interaction-state-audit`, `edge-case-hardening`, `performance`, `release-readiness`.

### Phase 9 — Release, measure, and learn

**Purpose:** treat launch as the beginning of evidence, not the end of design.

- release safely with observability, rollback/feature-flag strategy when appropriate;
- monitor task success, quality, support burden, accessibility feedback, performance, and guardrail outcomes;
- compare results with the original outcome, not vanity metrics;
- review unexpected segments and failure paths;
- conduct follow-up research where analytics cannot explain why;
- update the evidence ledger, system, and backlog;
- retire obsolete patterns and document learning.

**Gate 9:** The service is operable, measurable, and owned. The team knows what it will watch, when it will act, and how the next iteration will be decided.

Recommended skills: `outcomes-metrics`, `live-optimization`, `experiment-design`, `performance`, `documentation-governance`.

---

## 5. Evidence and research integrity engine

### 5.1 Evidence labels

Every non-trivial claim in research/design artifacts MUST be identifiable as:

| Label | Meaning |
|---|---|
| `OBSERVED` | directly witnessed in product behavior, fieldwork, session, artifact, or source |
| `REPORTED` | said by an identifiable real participant/stakeholder, with context |
| `MEASURED` | supported by quantitative data, count, benchmark, or experiment |
| `INFERRED` | reasoned from evidence; reasoning and alternatives visible |
| `ASSUMED` | unverified belief awaiting evidence |
| `SYNTHETIC` | invented to exercise a design/test state; never user evidence |

### 5.2 Internal confidence scale

Use this project scale to manage uncertainty; it is not a universal scientific standard:

- **C0 — unknown:** no evidence.
- **C1 — plausible:** one weak/indirect signal.
- **C2 — patterned:** repeated qualitative or converging secondary evidence.
- **C3 — grounded:** direct behavioral/operational evidence in relevant context.
- **C4 — measured:** credible quantitative or experimental support.
- **C5 — convergent:** multiple appropriate methods agree, including edge segments.

Confidence depends on relevance and method quality, not volume of links.

### 5.3 Robust research protocol

For each study or desk-research effort:

```text
Decision to support
→ research question
→ current assumptions and disconfirming condition
→ method fit
→ participant/data source fit
→ consent, privacy, and harm controls
→ capture plan
→ analysis method
→ contradictions and negative cases
→ confidence and limitations
→ design/product decision
→ next evidence trigger
```

MUST:

- recruit for relevant behavior/context, not demographic convenience alone;
- include people likely to face barriers;
- separate participant words from researcher interpretation;
- analyze each session promptly and synthesize across sessions;
- preserve contradictory evidence and segment differences;
- triangulate high-impact decisions when feasible;
- avoid leading questions and solution pitching in problem research;
- use the least burdensome credible method;
- protect personal data and informed consent;
- involve the delivery team in observing evidence when practical.

### 5.4 AI-assisted desk research

The agent MUST:

1. search current primary or official sources first;
2. record source, author/organization, publication/update date, access date, scope, and relevant claim;
3. distinguish a source's statement from the agent's inference;
4. check whether the information is current for the target market, law, product, or technology;
5. seek independent/contradictory evidence for consequential claims;
6. avoid search-result snippets as final evidence;
7. quote minimally and synthesize in original language;
8. never manufacture a source, statistic, user quote, or consensus;
9. mark inaccessible or unverified claims as such;
10. keep a source ledger for decisions that depend on external facts.

### 5.5 Synthetic research boundary

AI may generate:

- hypotheses;
- interview questions;
- recruitment criteria;
- synthetic edge-case content/data;
- heuristic critique;
- candidate patterns;
- analysis scaffolds.

AI may not present generated personas, simulated interviews, model opinions, or predicted usability outcomes as evidence about real users.

---

## 6. Human-made design: the taste and direction protocol

### 6.1 Read the room before using rules

Every visual rule is contextual. Public-service trust, dense financial operations, a children's learning product, a luxury editorial surface, and a creative portfolio require different expressions. The audience and task choose the aesthetic family; the agent does not impose a favorite.

### 6.2 Write an aesthetic thesis

Before high-fidelity work, state:

```text
This experience should feel <three precise qualities>,
because <audience/context reason>.
It will express that through <type + composition + material/image + motion principles>.
It will avoid <specific opposing qualities>.
```

Add one **creative tension**, such as "clinical precision with one warm human layer" or "editorial confidence without sacrificing operational speed." Tension produces character more reliably than a bag of styles.

### 6.3 One signature move

Choose at most one dominant memorable device per surface: a compositional gesture, typographic behavior, illustration system, spatial transition, or interaction reveal. Let the rest of the interface support it. Do not make every section audition for attention.

### 6.4 Anti-default discipline

Do not default without contextual justification to:

- purple/blue AI gradients, dark mesh heroes, decorative glow, or glass on every surface;
- a centered headline followed by three equal cards and a logo strip;
- arbitrary bento grids that do not reflect information priority;
- excessive pills, rounded rectangles, floating containers, and shadow stacks;
- generic Inter/slate palettes, stock icon soup, or random emoji;
- huge headings used to compensate for weak content;
- fake company names, testimonials, metrics, avatars, or dashboards;
- animation on every element, scroll hijacking, or motion with no state meaning;
- identical spacing everywhere, mathematically centered objects that look optically wrong;
- placeholder copy that prevents judging real hierarchy and wrapping.

These are not permanent bans. They require a reason tied to brand, task, or concept.

### 6.5 Reference analysis, not costume copying

For each reference, extract:

```text
What problem/surface it solves
Hierarchy and reading order
Grid, alignment, negative space, density
Typography roles and cadence
Color roles and contrast behavior
Material, border, shadow, and image treatment
Interaction and motion grammar
Content tone and realism
What transfers to this product
What would be imitation or contextually wrong
```

Combine principles from multiple references. Preserve brand and intellectual-property boundaries. Do not falsely claim an unofficial approximation is an official design system.

### 6.6 Craft pass

After correctness, perform a deliberate craft pass:

- optical alignment and balance;
- type scale, line length, line height, wrapping, widows/orphans where relevant;
- spacing rhythm and purposeful exceptions;
- contrast distribution and focal hierarchy;
- shape language and icon consistency;
- realistic content and data density;
- material behavior across themes;
- motion timing, easing, interruption, and reduced-motion equivalent;
- empty/error/loading states that still feel authored;
- awkward widths, long translations, zoom, and content extremes.

---

## 7. UX completeness rules

### 7.1 Every screen has a job

A screen contract MUST state:

```text
User/context:
Job and desired outcome:
Entry points:
Primary decision/action:
Information hierarchy:
Data/content dependencies:
States and permissions:
Responsive/adaptive behavior:
Accessibility behavior:
Analytics/observability:
Exit and recovery:
Acceptance evidence:
```

If the screen cannot name a primary job, reconsider whether it should exist.

### 7.2 State completeness

For every meaningful component/flow, consider:

- default, hover, focus-visible, active/pressed, selected;
- disabled versus unavailable and why;
- loading: initial, deferred, optimistic, background, retry;
- empty: first-use, filtered, no-permission, no-result, completed;
- error: field, submission, partial, stale, network, authorization, destructive failure;
- success, undo, confirmation, persistence;
- long/short/missing/malformed content;
- high volume and pagination/virtualization;
- offline/reconnect/conflict where relevant;
- localization, RTL, text expansion, date/number/currency;
- reduced motion, increased contrast, zoom, keyboard, touch, pointer, screen reader;
- role/permission/account/lifecycle variations.

### 7.3 Feedback and recovery

The system SHOULD always answer:

1. Did it receive the action?
2. What is happening now?
3. What changed?
4. Is the change saved and where?
5. What can the person do next?
6. How can they recover or undo?

Errors MUST explain what happened, why when useful, how to fix it, and whether data was preserved. Never blame the user.

### 7.4 Content is part of the interaction

Use specific labels and action verbs. Match the user's mental model. Put critical explanation at the decision point. Keep help available without forcing everyone through it. Confirm irreversible consequences in plain language. Do not hide material terms, cost, data use, or cancellation behind decorative hierarchy.

### 7.5 Whole-journey design

Account for entry, authentication, setup, core task, collaboration, notifications, support, billing/rights where relevant, export/portability, error resolution, and leaving/retiring. A beautiful middle screen does not compensate for a broken start or end.

---

## 8. System design and cross-platform expression

### 8.1 Extend before inventing

Inventory existing foundations, primitives, patterns, and debt. Reuse what serves the direction. Add a token/component only when it represents a repeated decision or behavior. A one-off composition need not become a universal component.

### 8.2 Token architecture

Prefer semantic layers:

```text
primitive/reference values
→ semantic intent (surface, text, border, action, status)
→ component tokens only when a component needs stable specialization
→ platform output (CSS variables, native resources, theme objects, etc.)
```

Tokens require names, types, descriptions, ownership, themes/modes, and deprecation strategy. Do not encode page position or accidental color in semantic names.

### 8.3 Component contract

A reusable component MUST document:

- purpose and when not to use;
- anatomy and content slots;
- variants and size/density decisions;
- full interaction/state matrix;
- keyboard/focus/assistive behavior;
- responsive and content-resilience behavior;
- theming and tokens;
- data/state ownership boundaries;
- examples and misuse;
- tests and visual baselines;
- migration/deprecation when replacing an old pattern.

### 8.4 Pattern over component

Document multi-component behavior—search, filtering, onboarding, destructive action, editing, autosave, upload, bulk operations, notifications—as a pattern with sequence, rules, states, and exceptions. Component consistency does not guarantee journey consistency.

### 8.5 Platform fidelity

Use platform-native conventions for navigation, input, safe areas, gestures, back behavior, windowing, permissions, typography, and accessibility unless deviation creates proven value and includes a learnable fallback.

The visual language may be shared across platforms; interaction mechanics may need to differ.

---

## 9. Designing through implementation

### 9.1 Inspect the stack

Before importing or generating code, identify:

```text
platform/framework/version
rendering model and component boundaries
styling/token/theme system
primitive/component/icon libraries
routing/navigation
state/data/cache/forms/validation
localization
analytics/feature flags
accessibility/test/Storybook/browser tooling
performance budgets and deployment constraints
```

Check manifests before using dependencies. Prefer official/current documentation for version-specific behavior.

### 9.2 One coherent foundation

Use one primary component/primitive system. Do not mix Material, Carbon, Fluent, shadcn/Radix, and bespoke primitives casually. If the brief clearly maps to an official design system or regulated public pattern library, use its official implementation rather than recreating a look by hand.

### 9.3 Vertical slices

Plan work as reviewable slices that produce real user value and visible behavior:

```text
route/surface + data + structure + content + interaction + states
+ responsive rules + accessibility + tests + visual review
```

Avoid "set up files" tasks that postpone all integration risk.

### 9.4 Design-system bridge

Keep design decisions close to code:

- tokens as platform-consumable data or variables;
- component contracts beside components/stories;
- approved screenshots as visual baselines;
- interaction and accessibility tests for critical patterns;
- decisions linked from code or pull request when non-obvious;
- no handoff packet that immediately diverges from implementation.

### 9.5 Dependency and trend honesty

Do not invent package names, APIs, or official support. Verify current versions and licenses. Distinguish an aesthetic approximation from an official platform feature. Avoid adding a fashionable library when native CSS/platform APIs or the current system are sufficient.

---

## 10. Pixel-accurate implementation protocol

Use this when a screenshot, design file, or approved render is the visual contract.

### 10.1 Establish the reference contract

Record:

- source and approval status;
- exact viewport, DPR/scale, browser/platform, theme, and state;
- font files/weights/fallbacks and asset sources;
- content/data and localization;
- expected responsive behavior beyond the captured frame;
- elements that are intentionally dynamic;
- fidelity priorities and permitted deviations.

Without these conditions, say **reference-faithful**, not provably pixel-identical.

### 10.2 Lock the comparison environment

Use the same browser/platform/container, deterministic data, fonts, viewport, animation state, and time-dependent content for baseline and actual screenshots. Mask only genuinely volatile regions and document the mask.

### 10.3 Build in this order

1. semantic structure and layout model;
2. macro geometry: containers, columns, regions, scroll behavior;
3. typography metrics and content wrapping;
4. spacing, alignment, and responsive transformations;
5. color, borders, material, imagery, icons;
6. component states and interaction behavior;
7. motion and fine optical corrections.

Do not patch a wrong layout model with dozens of absolute offsets.

### 10.4 Compare, classify, correct

Capture at each contract viewport/state. Use overlay or visual diff. Fix in leverage order:

```text
wrong structure/flow
→ macro geometry
→ typography/font metrics
→ spacing/alignment
→ color/material/assets
→ fine detail and motion
```

After each correction, verify that neighboring sizes and states did not regress.

### 10.5 Definition of pixel-accurate completion

The agent may claim pixel-accurate completion only when:

- reference and environment are recorded;
- screenshots were captured from the implementation;
- comparisons were reviewed at required viewports/states;
- remaining differences are below the agreed tolerance or explicitly accepted;
- behavior, accessibility, and responsiveness remain correct;
- the visual baseline is stored or the evidence is linked.

Visual similarity may never justify inaccessible semantics, broken behavior, or brittle code.

---

## 11. Accessibility, inclusion, trust, and performance

### 11.1 Accessibility is designed and tested

Target the applicable current standard; for web work the default baseline is WCAG 2.2 AA unless product/legal context requires more. Use native elements first and WAI-ARIA Authoring Practices for custom widgets. Automated tools are support, not proof: keyboard, focus, reading order, zoom/reflow, content, and assistive behavior require human/manual checks.

Accessibility acceptance MUST cover the complete process, not isolated pages.

### 11.2 Inclusive defaults

Design for varied ability, language, literacy, age, device, bandwidth, attention, environment, and confidence. Include people facing these barriers in research. Provide alternatives to drag, gesture, motion, audio, color-only, precision, memory, and time pressure where relevant.

### 11.3 Trust and agency

Never use deceptive hierarchy, forced continuity, disguised ads, confirmshaming, hidden cost, obstruction, urgency theater, default data sharing, or difficult cancellation. Make automation/AI visible where material. Allow review, correction, undo, provenance, escalation, and human control in proportion to risk.

### 11.4 Performance as experience

For web surfaces, measure real loading, responsiveness, and visual stability. Treat current Core Web Vitals as signals, not the whole experience. Test on representative devices/networks. Avoid layout shifts, blocking fonts/assets, excessive JavaScript, main-thread animation, unbounded DOM, and decorative effects that degrade the primary task.

Respect `prefers-reduced-motion`; provide a meaningful non-motion result, not merely slower animation.

---

## 12. Skill orchestration

### 12.1 Selection algorithm

```text
1. Name the decision or defect.
2. Identify lifecycle phase and risk.
3. Detect platform/stack and existing system.
4. Choose the narrowest skill that owns the decision.
5. Add a second skill only for a distinct missing angle.
6. Add a third only for broad audit/redesign/multi-surface work.
7. Read each selected skill fully.
8. Record material external skills and versions.
9. Apply them under DESIGN.md and project constraints.
10. Remove their context when the phase ends.
```

Use `SKILLS.md` and `python scripts/skill.py`.

### 12.2 When no skill fits

1. search bundled registry semantically;
2. search the mirrored UI Skills catalog;
3. consult official framework/platform/design-system documentation;
4. search reputable skill repositories/resources;
5. inspect source, scope, recency, license, and conflicts;
6. download only the skill document unless more is explicitly required;
7. pin source/version/hash in the skill ledger;
8. never execute arbitrary install scripts without review;
9. treat the new skill as advisory and test its output.

### 12.3 Conflict resolution

When skills disagree:

- context-specific beats generic;
- official platform/system guidance beats aesthetic preference;
- user evidence and tested behavior beat a pattern recommendation;
- safety/accessibility beats visual fidelity;
- existing approved project rules beat a new external opinion;
- record consequential deviations.

---

## 13. Quality gates and severity

### 13.1 Severity

| Level | Meaning | Action |
|---|---|---|
| `S0` | safety, legal, privacy, severe accessibility, data loss/corruption | stop/revert; do not release |
| `S1` | primary task impossible, major trust failure, inaccessible critical path | release blocker |
| `S2` | serious friction, misleading hierarchy/content, broken state/responsive behavior | fix before release unless explicitly accepted |
| `S3` | inconsistency, craft issue, local performance or comprehension cost | schedule/fix in quality pass |
| `S4` | optional refinement or delight | only after higher levels |

### 13.2 Release review

A substantial experience is not done until the relevant items pass:

- problem/outcome and scope are traceable;
- research claims are honest and limitations visible;
- flow covers realistic entry, success, failure, and recovery;
- content and hierarchy support decisions;
- system/tokens/components are coherent and not duplicated;
- all required states, permissions, themes, and content extremes exist;
- accessibility checks cover the journey;
- rendered screenshots were reviewed at agreed sizes;
- visual differences from approved references were resolved/accepted;
- tests and performance checks match risk;
- analytics/observability and privacy are appropriate;
- release/rollback/ownership and live learning are defined.

### 13.3 Design review format

```text
Intent and outcome
Evidence reviewed
What works and must be preserved
S0/S1 blockers
S2 important corrections
S3 craft/system corrections
S4 optional opportunities
Recommended sequence
Screenshots/states inspected
Open assumptions and proposed tests
```

Critique must include a correction and rationale, not taste adjectives alone.

---

## 14. Deliverable contracts

### 14.1 Direction contract

A direction is ready when it includes thesis, audience/outcome fit, structure, content approach, visual grammar, signature move, interaction model, system implications, risks, and falsification criteria.

### 14.2 Screen contract

A screen is ready for implementation when its job, hierarchy, data, components, states, responsive behavior, accessibility, content, telemetry, and acceptance evidence are specified enough to prevent guesswork.

### 14.3 Component contract

A component is ready when purpose, anatomy, API/content slots, variants, states, input/focus/assistive behavior, tokens, responsive behavior, examples, tests, and misuse are documented.

### 14.4 Implementation contract

A slice is ready when dependencies and architecture are understood, behavior and data are real, required states are built, accessibility is integrated, screenshots are reviewable, and acceptance tests map to the design decision.

### 14.5 Evidence contract

A research finding is ready to influence a consequential decision when source/context, observation, analysis, contradictory evidence, affected segment, confidence, limitation, and design implication are visible.

---

## 15. Final definition of done

The work is professionally complete when it is:

```text
Useful: solves a real, evidenced or explicitly hypothesized problem.
Usable: the whole task is understandable, efficient, recoverable, and tested appropriately.
Inclusive: barriers are designed out and critical accessibility behavior is verified.
Trustworthy: consequences, data use, automation, cost, and control are honest.
Distinctive: it has a coherent visual thesis rather than generic model defaults.
Systemic: repeated decisions are reusable and governed without over-componentizing.
Native: it respects the project's stack and platform conventions.
Faithful: the implementation carries the design intent into the rendered product.
Resilient: states, content extremes, failure, permissions, and environments are handled.
Performant: the primary experience remains responsive and stable under realistic conditions.
Measurable: success and guardrails can be observed after release.
Maintainable: future contributors can understand the decisions and continue the system.
```

Never say "done" because the mockup looks polished or the code compiles. Finish when the real experience has been inspected, verified, and made ready to learn from.
