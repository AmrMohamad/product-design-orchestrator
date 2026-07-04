# Deep analysis of the uploaded design-skill archives

I treated the four uploaded archives as the full target set and inspected their markdown skills, commands, metadata, datasets, and key scripts directly from the ZIPs so nothing depended on fragile extraction state.

## 1) What these repos are really built on

- In Anthropic’s model, a **Skill** is a markdown-based unit of reusable knowledge/workflow that Claude can invoke directly or load automatically when relevant.

- A **plugin** is the packaging layer that groups skills (and optionally hooks, subagents, or MCP servers) into a reusable installable unit.

- A **command** is the verb surface: an entrypoint that chains skills or encodes a repeated workflow.

- A **DESIGN.md** file, in the Google Stitch framing, is an agent-friendly markdown representation of design rules that can be exported/imported across tools.


This matters because the uploads are not all the same thing: one is a classic skill pack, one is a plugin marketplace, one is closer to a design-retrieval product, and one is mostly an index of external design-rule documents.

## 2) Inventory at a glance

| Archive | What it actually is | Local skill count | Other executable artifacts | Observed posture |
|---|---:|---:|---:|---|
| `designer-skills-main.zip` | Compact sequential design workflow pack | 8 skills | 0 commands | Process-first, artifact-first |
| `designer-skills-main.zip 14-26-37-568.zip` | Modular Claude Code plugin marketplace | 63 skills | 27 commands across 8 plugins | Breadth-first, composable |
| `ui-ux-pro-max-skill-main.zip` | Productized design-intelligence toolkit | 7 skills | CLI, search engine, datasets, templates, scripts | Retrieval-first, systemized |
| `awesome-design-md-main.zip` | Catalog of external DESIGN.md references | 0 local skills | 59 brand README stubs + root index | Inspiration/index layer |


## 3) Archive-by-archive analysis

### A. `designer-skills-main.zip` — the sequential design operating system

**What it is:** a tight 8-skill workflow with one orchestrator (`design-flow`) and seven subordinate skills.

**Core operating model:** interrogation -> brief -> structure -> tokens -> tasks -> implementation -> review.

**Why it feels coherent:** every phase writes durable artifacts into `.design/<feature-slug>/`, so the system remembers what was decided and keeps later phases grounded.

**Mindset:** design quality comes from disciplined sequencing, persistent artifacts, and explicit visual doctrine. This pack distrusts vague brainstorming and generic output.

#### The eight skills

##### `brief-to-tasks`

- **How it works:** A planning skill that converts the brief and IA into a build order of independently reviewable vertical slices.

- **Mindset behind it:** Its mindset rejects fake setup work. A task should produce something shippable-looking and testable, not just file scaffolding.

- **Observed structure:** Example prompts, Process, Task List Template, Foundation, Core UI, Interactions & States, Responsive & Polish, Review, Rules.

- **Notable implementation detail:** it defines tasks as vertical slices that must include structure, style, and interaction rather than fake setup tasks.



##### `design-brief`

- **How it works:** A structured discovery-and-synthesis skill that interviews the user, inspects the codebase, and turns goals into a formal brief saved under `.design/<feature-slug>/DESIGN_BRIEF.md`.

- **Mindset behind it:** Its mindset is that good UI direction is born from context: product intent, existing code patterns, component inventory, responsive behavior, and accessibility all belong in the brief.

- **Observed structure:** Example prompts, Process, File Output, Brief Template, Problem, Solution, Experience Principles, Aesthetic Direction, Existing Patterns, Component Inventory, Key Interactions, Responsive Behavior, Accessibility Requirements, Out of Scope.

- **Notable implementation detail:** it actively explores the codebase for existing themes, components, storybook/docs, tokens, pages, dependencies, and fonts, then tries to extend rather than replace existing language.



##### `design-flow`

- **How it works:** The orchestration skill that sequences all other skills, pauses between phases, and manages the `.design/<slug>/` workspace as a persistent project memory.

- **Mindset behind it:** Its mindset is process control. It treats design as a staged workflow with checkpoints, artifacts, and explicit handoffs between thinking modes.

- **Observed structure:** Example prompts, The Sequence, Rules, Phase Details, ### Phase 1: Grill Me, ### Phase 2: Design Brief, ### Phase 3: Information Architecture, ### Phase 4: Design Tokens, ### Phase 5: Brief to Tasks, ### Phase 6: Frontend Design, ### Phase 7: Design Review (on request only), Project Files Structure, If the Designer Returns Mid-Flow.

- **Notable implementation detail:** it explicitly requires the assistant to announce phases, read each child skill fully, wait for confirmation between phases, and keep artifacts inside `.design/<slug>/`.



##### `design-review`

- **How it works:** A QA/critique skill that compares the built interface against the brief, the codebase, and screenshots at multiple breakpoints and states.

- **Mindset behind it:** Its mindset is that visual quality cannot be inferred from code alone; screenshots are mandatory because many design failures are only visible on the rendered surface.

- **Observed structure:** Example prompts, Process, Review Checklist, ### Visual Hierarchy, ### Consistency, ### Aesthetic Fidelity, ### Component Quality, ### States and Interactions, ### Responsive Behavior, ### Accessibility, ### Typography, ### Dark Mode, ### Mobile-First, Output Format, Screenshots Captured, Summary, Must Fix, Should Fix, Could Improve, What Works Well.

- **Notable implementation detail:** it requires screenshots at desktop, tablet, and mobile sizes plus state/dark-mode captures; code review alone is considered insufficient.



##### `design-tokens`

- **How it works:** A system-foundation skill that translates the chosen direction into colors, type, spacing, layout, motion, and breakpoint tokens with light and dark mode support.

- **Mindset behind it:** Its mindset is architectural: styling decisions should be encoded in semantic tokens before components proliferate.

- **Observed structure:** Example prompts, Process, Token Categories, ### Color, ### Spacing, ### Typography, ### Layout, ### Motion, ### Responsive Breakpoints, Dark Mode, Output.

- **Notable implementation detail:** it insists on semantic token naming, extension of existing systems when present, and light + dark mode from the outset.



##### `frontend-design`

- **How it works:** The main implementation style skill. It builds real UI while forcing the model to choose and inhabit a clear aesthetic philosophy instead of drifting into generic AI design.

- **Mindset behind it:** Its mindset is anti-blandness: strong design comes from explicit visual doctrine, mobile-first discipline, and intentional dark-mode behavior.

- **Observed structure:** Example prompts, Before You Write Any Code, Aesthetic Philosophies, ### Dieter Rams (Functionalist), ### Swiss / International Typographic, ### Japanese Minimalism (Ma), ### Brutalist / Raw, ### Scandinavian, ### Art Deco / Geometric, ### Neo-Memphis, ### Editorial / Magazine, Implementation Guidelines, Mobile-First, Dark Mode.

- **Notable implementation detail:** it encodes eight named aesthetic philosophies (Dieter Rams, Swiss, Japanese Minimalism, Brutalist, Scandinavian, Art Deco, Neo-Memphis, Editorial) and explicitly forbids generic AI aesthetics.



##### `grill-me`

- **How it works:** A confrontational discovery skill that forces the user to sharpen intent, clarify trade-offs, and expose assumptions before design work begins.

- **Mindset behind it:** It is deliberately tiny because its power is behavioral, not procedural: it tries to prevent weak premises from contaminating the rest of the workflow.

- **Observed structure:** Example prompts, Instructions.

- **Notable implementation detail:** even this small skill tells the assistant to inspect the project for answers instead of asking the user things the codebase already reveals.



##### `information-architecture`

- **How it works:** A structural planning skill that turns the brief into a navigation/content/page-flow blueprint, again saved as a durable artifact.

- **Mindset behind it:** Its mindset is that visual design should sit on top of a clear structural skeleton; otherwise teams end up polishing the wrong structure.

- **Observed structure:** Example prompts, Process, IA Document Template, Site Map, Navigation Model, Content Hierarchy, ### [Page Name], User Flows, ### [Flow Name] (e.g., "New user onboarding" or "Create a project"), Naming Conventions, Component Reuse Map, Content Growth Plan, URL Strategy.

- **Notable implementation detail:** it looks at routes, navigation, content hierarchy, user flows, URL strategy, naming conventions, and component reuse before visual design.



#### Why v1 works so well

- It uses **state**: `.design/<slug>/` acts like a project memory.

- It uses **phase separation**: discovery, structure, tokenization, planning, build, and QA are distinct mental modes.

- It uses **visual accountability**: screenshot-based review is built in, not optional.

- It uses **anti-generic doctrine**: the pack would rather be opinionated than bland.


#### Hidden assumptions and limits

- The workflow assumes a codebase and a feature context exist or will exist soon.

- It is strongest for feature/page work, not broad design-organization management.

- It assumes the user can tolerate a staged process with checkpoints rather than freeform ideation.

- It has breadth only where it serves the central build loop; outside that loop it is intentionally sparse.


### B. `designer-skills-main.zip 14-26-37-568.zip` — the modular plugin marketplace

**What it is:** 8 plugins, 63 skills, and 27 commands packaged in Claude Code marketplace format.

**Core operating model:** skills are nouns (capabilities/frameworks); commands are verbs (chained workflows).

**Mindset:** instead of forcing one canonical design process, this repo decomposes design practice into atomic expert modules that can be mixed and matched.

**What changed relative to v1:** this pack sacrifices v1’s persistent project-state and strict sequencing in exchange for breadth, composability, and plugin-packaging.


#### Plugin: `design-research`

This plugin is the discovery/synthesis layer. Its skills move from raw evidence, to structured sensemaking, to planned validation. The pattern is intentionally research-method agnostic but artifact-heavy: each skill translates ambiguous fieldwork into a designer-usable model.

- **Coverage:** 10 skills, 4 commands.

##### Skills

- `affinity-diagram` — Synthesizes raw notes into emergent themes through bottom-up clustering. **Mindset:** Starts from evidence, not pre-made categories; meaning should emerge from observed data. **Structure cues:** Context, Instructions.

- `card-sort-analysis` — Interprets card-sorting outputs into navigation and IA recommendations. **Mindset:** Uses users’ grouping behavior to challenge designer-imposed information structures. **Structure cues:** Context, Instructions.

- `diary-study-plan` — Designs longitudinal studies with prompts, cadence, capture methods, and analysis plans. **Mindset:** Assumes some behaviors only reveal themselves over time and in real context. **Structure cues:** Context, Instructions.

- `empathy-map` — Maps what users say, think, do, and feel around a situation. **Mindset:** Prioritizes holistic human context over feature-level requirements. **Structure cues:** Context, Domain Context, Instructions, Further Reading.

- `interview-script` — Builds moderated interview guides with warm-up, exploration, and wrap-up sections. **Mindset:** Treats research quality as a function of interviewing discipline rather than improvisation. **Structure cues:** Context, Domain Context, Instructions, Further Reading.

- `jobs-to-be-done` — Frames user needs as jobs, forces, outcomes, and hiring/firing criteria. **Mindset:** Looks past demographics to causal motivation and progress-seeking behavior. **Structure cues:** Context, Domain Context, Instructions.

- `journey-map` — Maps end-to-end phases, touchpoints, emotions, pain points, and opportunities. **Mindset:** Assumes experience problems are distributed across time, not isolated to single screens. **Structure cues:** Context, Domain Context, Instructions, Further Reading.

- `summarize-interview` — Turns transcripts into participant summaries, key themes, quotes, and action items. **Mindset:** Assumes raw interviews are too noisy to drive decisions until structured. **Structure cues:** Context, Instructions.

- `usability-test-plan` — Creates test goals, participant criteria, tasks, metrics, moderation guide, and logistics. **Mindset:** Treats usability testing as a designed study, not just ‘watch someone use it’. **Structure cues:** Context, Instructions, Further Reading.

- `user-persona` — Creates evidence-based personas with goals, behaviors, pain points, and contexts. **Mindset:** Treats personas as synthesis artifacts tied to data and product decisions, not fictional profiles. **Structure cues:** Context, Domain Context, Instructions, Further Reading.

##### Commands

- `/discover` — Chains persona creation, empathy mapping, journey mapping, and synthesis. **Mindset:** Mindset: research artifacts should accumulate into a coherent model of the user, not remain isolated deliverables.

- `/interview` — Routes either to interview preparation or transcript synthesis depending on user need. **Mindset:** Mindset: the same research domain needs both pre-fieldwork and post-fieldwork workflows.

- `/synthesize` — Chains affinity clustering and JTBD framing into prioritized design implications. **Mindset:** Mindset: raw qualitative data becomes useful only after structured interpretation.

- `/test-plan` — Creates a complete usability test plan and connects it back to personas or later synthesis. **Mindset:** Mindset: validation should be planned as seriously as discovery.

##### Plugin reading

This plugin is deliberately front-loaded toward evidence synthesis. It does not assume research artifacts are inherently useful; it keeps converting them into higher-order models and then into future validation plans.


#### Plugin: `design-systems`

This plugin is the normalization layer. It is less about inventing pixels and more about turning repeated design decisions into names, tokens, specs, docs, and themes that survive scale.

- **Coverage:** 8 skills, 3 commands.

##### Skills

- `accessibility-audit` — Audits interfaces against WCAG/POUR principles and severity ratings. **Mindset:** Treats accessibility as a first-class systems requirement, not a polish pass. **Structure cues:** What You Do, WCAG 2.2 Principles (POUR), Severity Ratings, Issue Format.

- `component-spec` — Defines component anatomy, states, variants, behaviors, and edge cases. **Mindset:** Assumes reusable components fail when teams document visuals but not behavior. **Structure cues:** What You Do, Specification Structure, Best Practices.

- `design-token` — Defines token categories, layers, naming, and usage rules. **Mindset:** Treats tokens as the bridge between abstract design language and implementation. **Structure cues:** What You Do, Token Categories, Token Tiers, Naming Convention.

- `documentation-template` — Creates templates for component docs, patterns, and governance docs. **Mindset:** Assumes the design system only scales if knowledge is standardized. **Structure cues:** What You Do, Template Types, ### Component Docs, ### Pattern Docs.

- `icon-system` — Defines icon style, naming, delivery formats, and usage rules. **Mindset:** Treats icons as a system with semantics and consistency, not isolated art files. **Structure cues:** What You Do, Foundations, Naming, Delivery.

- `naming-convention` — Builds naming rules for components, tokens, patterns, and files. **Mindset:** Assumes many system failures are language failures: ambiguous names create ambiguous implementation. **Structure cues:** What You Do, Principles, Patterns, Common Pitfalls.

- `pattern-library` — Documents recurring UX/UI patterns and when to apply them. **Mindset:** Elevates reusable interaction or layout patterns above one-off components. **Structure cues:** What You Do, Pattern Entry Structure, Categories, Best Practices.

- `theming-system` — Designs architecture for themes, dark mode, brand variants, and overrides. **Mindset:** Assumes flexibility needs explicit rules for inheritance and variation. **Structure cues:** What You Do, Architecture, Theme Types, Dark Mode Considerations.

##### Commands

- `/audit-system` — Runs accessibility, naming, documentation, theming, and token checks across a system. **Mindset:** Mindset: design systems need regular health checks, not just expansion.

- `/create-component` — Chains component spec, naming, accessibility, and docs for a new system component. **Mindset:** Mindset: a component is only ‘ready’ when behavior, naming, and documentation are aligned.

- `/tokenize` — Builds or refactors token architecture, naming, theming, and governance. **Mindset:** Mindset: token work is an architectural foundation, not a cosmetic task.

##### Plugin reading

This plugin treats system quality as a naming/specification/governance problem as much as a visual one. The recurring theme is codification.


#### Plugin: `ux-strategy`

This plugin works one level above screens. It frames the problem, the future state, the opportunity space, the success metrics, and the stakeholder alignment required for a team to move coherently.

- **Coverage:** 8 skills, 3 commands.

##### Skills

- `competitive-analysis` — Benchmarks competitors, dimensions, opportunities, and differentiation gaps. **Mindset:** Treats external comparison as strategic framing, not copying. **Structure cues:** What You Do, Analysis Framework, ### 1. Competitor Identification, ### 2. Evaluation Dimensions.

- `design-brief` — Creates a concise strategic brief with problem, users, goals, constraints, and success measures. **Mindset:** Treats design work as hypothesis-driven and bounded by clear intent. **Structure cues:** What You Do, Brief Structure, Best Practices.

- `design-principles` — Defines product or team design principles and how to use them in decisions. **Mindset:** Assumes principles should guide trade-offs, not serve as decorative slogans. **Structure cues:** What You Do, Qualities of Strong Principles, Principle Structure, Process.

- `experience-map` — Maps broader ecosystem experiences across stages, actors, channels, and emotions. **Mindset:** Looks above single product touchpoints to the wider service context. **Structure cues:** What You Do, Structure, ### Horizontal Axis: Phases, ### Vertical Layers.

- `metrics-definition` — Defines success metrics using frameworks like HEART and ties them to behaviors. **Mindset:** Treats UX outcomes as measurable, not purely qualitative. **Structure cues:** What You Do, Metric Categories, HEART Framework, Metric Template.

- `north-star-vision` — Frames a long-term aspirational vision, time horizons, and strategic direction. **Mindset:** Assumes teams need a vivid future target to align day-to-day decisions. **Structure cues:** What You Do, Vision Components, Time Horizons, Process.

- `opportunity-framework` — Identifies and prioritizes opportunity spaces using impact/effort and evidence. **Mindset:** Treats problem framing as portfolio management, not just idea generation. **Structure cues:** What You Do, Opportunity Sources, Evaluation Frameworks, ### Impact-Effort Matrix.

- `stakeholder-alignment` — Creates artifacts and rituals to align stakeholders on goals, scope, and decisions. **Mindset:** Assumes design friction often comes from organizational misalignment, not UI problems. **Structure cues:** What You Do, Alignment Artifacts, Common Challenges, Best Practices.

##### Commands

- `/benchmark` — Runs competitive analysis and strategic comparison to surface opportunities. **Mindset:** Mindset: seeing the market clearly helps teams choose what not to imitate.

- `/frame-problem` — Creates design brief, principles, and alignment around a problem space. **Mindset:** Mindset: many design failures start as framing failures.

- `/strategize` — Builds opportunity framework, experience vision, metrics, and alignment artifacts. **Mindset:** Mindset: strategy is a system of decisions, not a single north-star slide.

##### Plugin reading

This plugin frames design as organizational direction-setting. It is strongest when the problem is not ‘how should this look?’ but ‘what are we trying to optimize and why?’


#### Plugin: `ui-design`

This plugin handles the visual grammar of interfaces: grid, spacing, color, type, hierarchy, illustration, dark mode, data viz, and responsiveness. It is the closest thing in v2 to a classical UI craft toolkit.

- **Coverage:** 9 skills, 4 commands.

##### Skills

- `color-system` — Builds layered color palettes with brand, neutral, semantic, and usage roles. **Mindset:** Treats color as a system of relationships and roles, not just swatches. **Structure cues:** What You Do, Color System Layers, ### 1. Brand Palette, ### 2. Neutral Palette.

- `dark-mode-design` — Designs dark theme surface hierarchy, contrast, adaptation, and elevation rules. **Mindset:** Assumes dark mode is a distinct design problem, not a palette inversion. **Structure cues:** What You Do, Core Principles, Surface Hierarchy (Dark Mode), Color Adaptation.

- `data-visualization` — Selects chart types and visualization rules based on data relationships and readability. **Mindset:** Treats chart choice as an analytical decision tied to user tasks. **Structure cues:** What You Do, Chart Selection, ### Comparison, ### Trend Over Time.

- `illustration-style` — Defines illustration principles, color usage, shape language, and character rules. **Mindset:** Treats illustrations as brand-system assets that must cohere with product UI. **Structure cues:** What You Do, Style Definition, Color in Illustration, Character Design (if applicable).

- `layout-grid` — Defines grid structure, columns, gutters, rhythm, and responsive adaptations. **Mindset:** Treats layout as a governing scaffold, not a byproduct of placing elements. **Structure cues:** What You Do, Grid Anatomy, Grid Types, Responsive Behavior.

- `responsive-design` — Defines breakpoints, adaptation strategies, and responsive content priorities. **Mindset:** Assumes responsiveness is about information prioritization, not simple resizing. **Structure cues:** What You Do, Responsive Strategies, Common Breakpoints, Responsive Patterns.

- `spacing-system` — Creates spacing units, application rules, and structural rhythm. **Mindset:** Treats spacing as one of the main carriers of polish and hierarchy. **Structure cues:** What You Do, Base Unit, Spacing Types, Application Rules.

- `typography-scale` — Builds type scales, weights, line-height logic, and usage guidance. **Mindset:** Treats typography as interface architecture, not surface styling. **Structure cues:** What You Do, Scale Components, ### Size Scale, ### Weight Scale.

- `visual-hierarchy` — Organizes emphasis through size, weight, contrast, spacing, grouping, and sequencing. **Mindset:** Assumes users read interfaces by signals of priority, not by exhaustive inspection. **Structure cues:** What You Do, Hierarchy Tools, ### Size, ### Weight.

##### Commands

- `/color-palette` — Creates a color system and dark-mode guidance from brand/product context. **Mindset:** Mindset: palette decisions belong inside a role-based system, not standalone aesthetics.

- `/design-screen` — Combines layout, hierarchy, spacing, typography, and responsive rules for a screen. **Mindset:** Mindset: high-quality UI emerges from coordinated fundamentals, not one flashy visual move.

- `/responsive-audit` — Checks breakpoints, responsive patterns, spacing, and hierarchy across screens. **Mindset:** Mindset: responsiveness should be reviewed as a quality dimension of its own.

- `/type-system` — Builds a typography scale and hierarchy for a product. **Mindset:** Mindset: typography is an operating system for readability and brand tone.

##### Plugin reading

This plugin is a fundamentals library. It is less opinionated aesthetically than v1’s `frontend-design`, but more granular and reusable across many contexts.


#### Plugin: `interaction-design`

This plugin focuses on behavior over appearance. It decomposes motion, gestures, feedback, loading, errors, and state transitions so the interface behaves predictably under change.

- **Coverage:** 7 skills, 3 commands.

##### Skills

- `animation-principles` — Defines motion rules such as easing, duration, hierarchy, and continuity. **Mindset:** Treats motion as meaning-bearing feedback, not decoration. **Structure cues:** What You Do, Core UI Animation Principles, ### Easing, ### Duration.

- `error-handling-ux` — Designs prevention, detection, explanation, recovery, and escalation for errors. **Mindset:** Assumes the best error UX starts before the error happens. **Structure cues:** What You Do, Error Handling Hierarchy, ### 1. Prevention, ### 2. Detection.

- `feedback-patterns` — Maps appropriate feedback for actions, states, confirmations, and system responses. **Mindset:** Treats responsiveness and clarity as essential to user confidence. **Structure cues:** What You Do, Feedback Types, ### Immediate Feedback, ### Confirmation Feedback.

- `gesture-patterns` — Defines gestures, discoverability, constraints, and conflict handling. **Mindset:** Assumes touch interactions need stronger affordance and forgiveness than visible controls. **Structure cues:** What You Do, Core Gestures, Gesture Design Rules, ### Discoverability.

- `loading-states` — Chooses patterns like skeletons, progress indicators, and optimistic states. **Mindset:** Treats waiting as a designed experience that affects trust and perceived speed. **Structure cues:** What You Do, Loading Patterns, ### Skeleton Screens, ### Spinner/Progress.

- `micro-interaction-spec` — Specs trigger, rules, feedback loop, and resulting state changes for micro-interactions. **Mindset:** Treats small interactions as tiny behavior systems, not animations layered on later. **Structure cues:** What You Do, Micro-Interaction Framework, ### 1. Trigger, ### 2. Rules.

- `state-machine` — Models UI state transitions explicitly for forms, async data, auth, or multi-step flows. **Mindset:** Assumes complexity is safest when represented as a finite set of states and transitions. **Structure cues:** What You Do, State Machine Components, Common UI State Machines, ### Form.

##### Commands

- `/design-interaction` — Chains state, micro-interaction, feedback, and motion considerations for a feature. **Mindset:** Mindset: interaction design is a layered behavior system, not a single animation pass.

- `/error-flow` — Builds robust error-handling flow with states, prevention, and recovery. **Mindset:** Mindset: broken flows should be designed as deliberately as happy paths.

- `/map-states` — Generates state-machine-style state maps for interactive features. **Mindset:** Mindset: explicit state modeling prevents accidental complexity.

##### Plugin reading

This plugin is strong because it views interaction as explicit stateful behavior. That helps prevent ‘pretty but brittle’ interfaces.


#### Plugin: `prototyping-testing`

This plugin converts design questions into validation tactics. It is less concerned with final polish and more with choosing the cheapest artifact or test that resolves uncertainty.

- **Coverage:** 8 skills, 4 commands.

##### Skills

- `a-b-test-design` — Builds hypotheses, variants, metrics, guardrails, and interpretation plans for experiments. **Mindset:** Treats experimentation as disciplined decision-making, not random variant comparison. **Structure cues:** What You Do, Test Structure, ### 1. Hypothesis, ### 2. Variants.

- `accessibility-test-plan` — Plans layered accessibility testing across automation, manual QA, and assistive tech. **Mindset:** Assumes accessibility testing needs multiple methods because no single check catches enough. **Structure cues:** What You Do, Testing Layers, ### 1. Automated Testing, ### 2. Manual Testing.

- `click-test-plan` — Creates click-test studies to validate findability, first-click success, and label clarity. **Mindset:** Assumes information architecture can be validated before full implementation. **Structure cues:** What You Do, Test Types, Test Plan Structure, ### 1. Objective.

- `heuristic-evaluation` — Reviews interfaces through Nielsen’s heuristics with severity scoring and issue logs. **Mindset:** Uses expert inspection as a fast structured proxy when user testing is not yet available. **Structure cues:** What You Do, Nielsen's 10 Usability Heuristics, Evaluation Process, Issue Documentation.

- `prototype-strategy` — Selects prototype fidelity, tools, and goals for the stage of work. **Mindset:** Assumes the ‘right’ prototype is the cheapest one that answers the current question. **Structure cues:** What You Do, Fidelity Spectrum, ### Low Fidelity, ### Medium Fidelity.

- `test-scenario` — Writes realistic user scenarios and tasks for research or validation. **Mindset:** Assumes test quality depends heavily on scenario framing, not only on tasks. **Structure cues:** What You Do, Scenario Structure, ### Context Setting, ### Task.

- `user-flow-diagram` — Builds flow diagrams showing steps, decisions, branches, and exceptions. **Mindset:** Treats flow clarity as foundational before screen-level design. **Structure cues:** What You Do, Flow Diagram Elements, Flow Types, Creating Effective Flows.

- `wireframe-spec` — Documents wireframes with content blocks, annotations, and interaction notes. **Mindset:** Treats wireframes as structured communication artifacts rather than vague grayscale sketches. **Structure cues:** What You Do, Wireframe Components, ### Content Blocks, ### Annotations.

##### Commands

- `/evaluate` — Runs heuristic and accessibility evaluation to produce issues and improvements. **Mindset:** Mindset: expert review can create a fast quality baseline before or alongside user testing.

- `/experiment` — Creates an A/B test design around a hypothesis and metrics. **Mindset:** Mindset: product changes should compete through evidence, not preference.

- `/prototype-plan` — Chooses prototype fidelity, format, and validation goals. **Mindset:** Mindset: prototyping should answer a question at the cheapest acceptable fidelity.

- `/test-plan` — Builds usability or click-test plans depending on the product question. **Mindset:** Mindset: testing method should fit the uncertainty being resolved.

##### Plugin reading

This plugin continually asks what question needs answering, then picks the prototype or evaluation method that best answers it. It is uncertainty-management in plugin form.


#### Plugin: `design-ops`

This plugin operationalizes design as team practice: critique, QA, review gates, handoff, workflow, versioning, and sprint structure. Its mindset is managerial and delivery-oriented rather than purely creative.

- **Coverage:** 7 skills, 3 commands.

##### Skills

- `design-critique` — Structures critique sessions into preparation, facilitation, feedback capture, and follow-through. **Mindset:** Treats critique as a designed process whose job is to turn subjective reactions into actionable decisions. **Structure cues:** What You Do, Critique Framework, ### Before the Critique, ### During the Critique.

- `design-qa-checklist` — Builds implementation QA checklists across visual accuracy, layout, interaction, responsiveness, and accessibility. **Mindset:** Assumes quality comes from systematic verification, not last-minute eyeballing. **Structure cues:** What You Do, QA Categories, ### Visual Accuracy, ### Layout.

- `design-review-process` — Defines gated reviews from concept through final QA, with criteria at each checkpoint. **Mindset:** Treats review as governance: different stages need different standards, stakeholders, and evidence. **Structure cues:** What You Do, Review Gates, ### Gate 1: Concept Review, ### Gate 2: Design Review.

- `design-sprint-plan` — Plans a structured design sprint from framing to prototype and test. **Mindset:** Assumes speed only works when the week is tightly scaffolded and decision-makers are aligned. **Structure cues:** What You Do, Sprint Structure (5-Day Classic), ### Day 1: Understand, ### Day 2: Diverge.

- `handoff-spec` — Creates developer-facing handoff documentation including visual specs, interaction behavior, assets, and QA notes. **Mindset:** Assumes design debt often begins at handoff, so ambiguity must be removed before engineering starts. **Structure cues:** What You Do, Handoff Contents, ### Visual Specifications, ### Interaction Specifications.

- `team-workflow` — Designs operating rhythms for teams: task management, rituals, collaboration, and decision flow. **Mindset:** Treats team process itself as a product that can be intentionally designed. **Structure cues:** What You Do, Workflow Components, ### Task Management, ### Collaboration Rituals.

- `version-control-strategy` — Defines what to version, how to branch, and how to name or archive design work. **Mindset:** Assumes design teams need the same traceability and change discipline as engineering teams. **Structure cues:** What You Do, What to Version, Versioning Approaches, ### Design Files.

##### Commands

- `/handoff` — Chains specs, QA criteria, review readiness, and versioning into a delivery package. **Mindset:** Mindset: shipping quality is the result of layered operational handoff, not tossing frames over the wall.

- `/plan-sprint` — Builds a sprint plan around challenge framing, team setup, activities, materials, and review criteria. **Mindset:** Mindset: compressed discovery needs explicit structure to stay honest and productive.

- `/setup-workflow` — Assembles team structure, rituals, critique, review gates, versioning, and QA into an operating model. **Mindset:** Mindset: process debt is real debt, so workflow design is part of design leadership.

##### Plugin reading

This plugin turns design maturity into repeatable process. It is for teams that want predictability, review quality, and cleaner delivery handoffs.


#### Plugin: `designer-toolkit`

This plugin packages the communication side of design work: explaining decisions, presenting them persuasively, documenting case studies, improving adoption, and auditing system hygiene.

- **Coverage:** 6 skills, 3 commands.

##### Skills

- `case-study` — Structures product/design case studies from challenge to impact. **Mindset:** Treats storytelling as a design skill: decisions need to be legible to hiring managers and stakeholders. **Structure cues:** What You Do, Case Study Structure, ### 1. Overview, ### 2. Challenge.

- `design-rationale` — Documents why a decision was made, which options were considered, and what trade-offs remain. **Mindset:** Assumes design maturity means preserving reasoning, not just final frames. **Structure cues:** What You Do, Rationale Structure, ### 1. Decision, ### 2. Context.

- `design-system-adoption` — Plans how a system will be socialized, trained, enabled, and measured across a team. **Mindset:** Treats adoption as an organizational change problem, not merely a documentation problem. **Structure cues:** What You Do, Adoption Strategy, ### Awareness, ### Education.

- `design-token-audit` — Audits token coverage, duplication, consistency, and implementation gaps. **Mindset:** Assumes tokens drift unless periodically inspected against reality. **Structure cues:** What You Do, Audit Scope, ### Token Coverage, ### Token Consistency.

- `presentation-deck` — Structures decks for stakeholder updates, reviews, or strategy communication. **Mindset:** Treats narrative sequencing as part of design work, not an afterthought. **Structure cues:** What You Do, Presentation Types, ### Stakeholder Update, ### Design Review.

- `ux-writing` — Guides UX copy for labels, errors, empty states, onboarding, and voice/tone. **Mindset:** Treats wording as interaction design: text changes comprehension and trust. **Structure cues:** What You Do, UX Writing Categories, ### Microcopy, ### Error Messages.

##### Commands

- `/build-presentation` — Creates a structured deck from design work and audience context. **Mindset:** Mindset: persuasion and clarity require intentional narrative packaging.

- `/write-case-study` — Turns a project into a case-study narrative from challenge to impact. **Mindset:** Mindset: portfolios should show thinking, trade-offs, and results, not just screenshots.

- `/write-rationale` — Produces a formal rationale artifact for a decision or direction. **Mindset:** Mindset: decisions should remain inspectable after the meeting ends.

##### Plugin reading

This plugin recognizes that design work also needs explanation, adoption, persuasion, and retrospection. It covers the social layer of design practice.


#### Why v2 is architecturally different from v1

- **Breadth over linearity:** nearly every design subdiscipline gets a dedicated micro-skill.

- **Commands replace orchestration monoliths:** instead of one `design-flow`, there are many smaller routes like `/discover`, `/design-screen`, `/evaluate`, and `/strategize`.

- **Less persistent state:** the pack is more conversation-oriented than file-system-oriented.

- **More reusable expertise:** the same skill can be invoked across unrelated projects without dragging along a whole end-to-end workflow.


#### Hidden assumptions and limits

- Many skills are concise expert scaffolds rather than heavyweight procedures; they rely on the model to do some of the orchestration.

- There is less emphasis on rendered screenshot review than in v1.

- Because the skills are atomized, quality depends more on choosing the right entrypoint and chaining the right companions.


### C. `ui-ux-pro-max-skill-main.zip` — the retrieval-driven design intelligence toolkit

**What it is:** not just a skill folder, but a product-like system: skills + CLI + search engine + curated CSV databases + templates + multi-platform installers.

**Core operating model:** generate a design system first, persist it, then retrieve supporting rules from curated domains (style, product, color, typography, chart, landing, UX, stack guidance).

**Mindset:** expert-system design. This repo tries to reduce randomness by making design decisions retrieval-backed, rules-first, and persistable.

#### The seven skills

##### `ui-ux-pro-max`

- **How it works:** The flagship skill: a rulebook plus retrieval front-end that tells the assistant when to search styles, products, colors, typography, UX rules, charts, or stack guidance, and to start by generating a design system.

- **Mindset behind it:** Its mindset is expert-system design. Rather than rely on fresh reasoning from scratch every time, it tries to constrain decisions through curated datasets, priority rules, and persisted design-system files.

- **Observed structure:** When to Apply, ### Must Use, ### Recommended, ### Skip, Rule Categories by Priority, Quick Reference, ### 1. Accessibility (CRITICAL), ### 2. Touch & Interaction (CRITICAL).

- **Key behavioral pattern:** always start with `--design-system`, then optionally deepen with `--domain` and `--stack`, and optionally persist outputs into a master/page override structure under `design-system/`.



##### `ui-styling`

- **How it works:** An implementation-oriented styling skill built around a specific stack layering: shadcn/ui for components, Tailwind CSS for styling, and Canvas assets/utilities for richer visual treatment.

- **Mindset behind it:** Its mindset is pragmatic composability: use proven component primitives, then layer system styling and brand expression on top.

- **Observed structure:** Reference, When to Use This Skill, Core Stack, ### Component Layer: shadcn/ui, ### Styling Layer: Tailwind CSS, ### Visual Design Layer: Canvas, Quick Start, ### Component + Styling Setup.

- **Key behavioral pattern:** it assumes a specific stack preference (shadcn/ui + Tailwind) and includes helper scripts to add shadcn components and generate Tailwind config.



##### `design-system`

- **How it works:** A design-system-and-slides skill that formalizes primitive/semantic/component token layers and extends the same token rigor into presentation generation and validation.

- **Mindset behind it:** Its mindset is that one source of truth should power both product UI and slideware, with BM25-backed search and token validation keeping outputs consistent.

- **Observed structure:** When to Use, Token Architecture, ### Three-Layer Structure, Quick Start, References, Component Spec Pattern, Scripts, Templates.

- **Key behavioral pattern:** it extends beyond app UI into slide generation, token validation, and slide search, which makes it more than a normal token skill.



##### `design`

- **How it works:** A meta-router and umbrella production skill that coordinates brand, UI styling, slides, banners, logo/CIP/icon workflows, and scripts.

- **Mindset behind it:** Its mindset is breadth through routing: the assistant should not solve every design request from zero, but should dispatch into the right specialized workflow and fix scripts when they break.

- **Observed structure:** When to Use, Sub-skill Routing, Logo Design (Built-in), ### Logo: Generate Design Brief, ### Logo: Search Styles/Colors/Industries, ### Logo: Generate with AI, CIP Design (Built-in), ### CIP: Generate Brief.

- **Key behavioral pattern:** it is a dispatcher. Instead of deepening one craft domain, it routes across logos, CIP, banners, slides, icon workflows, and supporting scripts.



##### `brand`

- **How it works:** A brand-governance skill focused on syncing brand guidelines into tokens, validating assets, and keeping tone/identity consistent across outputs.

- **Mindset behind it:** Its mindset is synchronization: brand is a living source document that should propagate into implementation artifacts.

- **Observed structure:** When to Use, Quick Start, Brand Sync Workflow, Subcommands, References, Scripts, Templates, Routing.

- **Key behavioral pattern:** it references scripts for injecting brand context, syncing brand guidelines to tokens, validating assets, and extracting colors.



##### `banner-design`

- **How it works:** A campaign-asset workflow for generating banners across channels and sizes, blending creative direction, web/HTML mockups, AI visuals, and image export.

- **Mindset behind it:** Its mindset is production realism: banners are multi-format deliverables with hard dimensions, brand constraints, and iteration loops.

- **Observed structure:** When to Activate, Workflow, ### Step 1: Gather Requirements (AskUserQuestion), ### Step 2: Research & Art Direction, ### Step 3: Design & Generate Options, ### Step 4: Export Banners to Images, ### Step 5: Present Options & Iterate, Banner Size Quick Reference.

- **Key behavioral pattern:** it turns banner work into a production pipeline: requirements -> art direction -> generation -> exact-dimension export -> presentation/iteration.



##### `slides`

- **How it works:** A thin routing skill that points the assistant to slide-specific references and subcommands rather than trying to be the whole slide system itself.

- **Mindset behind it:** Its mindset is minimal surface area: keep the entrypoint simple and delegate the real work to the deeper slide resources.

- **Observed structure:** When to Use, Subcommands, References (Knowledge Base), Routing.

- **Key behavioral pattern:** it mainly serves as a thin entrypoint into the deeper slide references and commands rather than containing the whole slide craft itself.



#### Core architecture that makes this repo different

- **Search engine:** `src/ui-ux-pro-max/scripts/core.py` implements BM25-style ranking plus regex/keyword scoring against domain-specific CSV datasets.

- **Design-system generator:** `design_system.py` combines product, style, color, landing, typography, and `ui-reasoning.csv` logic into a single recommendation object with anti-patterns and decision rules.

- **Persistence model:** the main skill recommends `design-system/MASTER.md` plus per-page overrides, which is a stronger memory pattern than most lightweight skill packs.

- **Multi-platform installer:** `cli/` and template JSON files can generate platform-specific skill installs for Claude, Cursor-like tools, Copilot-like tools, and many others.

- **Data-backed breadth:** the repo includes large CSV assets for styles, colors, typography, products, UX rules, charts, icons, Google Fonts, app/web interface guidance, and stack-specific implementation guidance.

#### Dataset profile I verified locally

- `styles.csv`: 84 rows

- `colors.csv`: 161 rows

- `typography.csv`: 73 rows

- `charts.csv`: 25 rows

- `products.csv`: 161 rows

- `ux-guidelines.csv`: 99 rows

- `google-fonts.csv`: 1923 rows

- `icons.csv`: 105 rows

- `app-interface.csv`: 30 rows

- Stack CSVs present for: react, nextjs, vue, svelte, astro, swiftui, react-native, flutter, nuxtjs, nuxt-ui, html-tailwind, shadcn, jetpack-compose, threejs, angular, laravel.

#### The strongest idea inside ui-ux-pro-max

The strongest idea is that **design recommendations should be retrieved and reasoned over, not invented from scratch every time**. That shows up everywhere: domain search, stack search, anti-pattern tables, design-system persistence, and decision-system CSVs.

#### The biggest inconsistencies I found

- The generated main skill still says **React Native is the project’s only tech stack** in places, but the code and metadata expose many stacks.

- The main skill/search help mentions a **`prompt` domain**, but the actual `CSV_CONFIG` in `core.py` does not include a `prompt` dataset, so the documentation and executable config are out of sync.

- Metadata is stale across files: `skill.json`/plugin metadata say version `2.5.0`, while `.claude-plugin/marketplace.json` still advertises `2.2.1` and older dataset counts.

- The template source contains mixed-language examples (e.g. Chinese example prompts) and other copy artifacts, suggesting the skill file is template-generated and not fully normalized.

- The flagship skill says 67 styles, but the local `styles.csv` currently contains 84 rows, which again suggests stale marketing metadata or an evolved dataset.

- Some workflows reference external/non-local skills or tools such as `frontend-design`, `ai-artist`, `ai-multimodal`, or browser tooling, so the repo implicitly expects a wider ecosystem.

#### Bottom-line reading of ui-ux-pro-max

This is the most ambitious pack in the uploads. It is not merely instructive; it tries to become a **design intelligence substrate** with datasets, scoring, persistence, installers, and platform templates. Its main risk is not lack of depth but **configuration/documentation drift**.


### D. `awesome-design-md-main.zip` — the DESIGN.md index, not a skill pack

**What it is:** a curated index of design-rule references inspired by many brands/products, organized as README stubs under `design-md/<brand>/README.md`.

**What it is not:** it is not a local skill library in the same sense as the other uploads. There are no `SKILL.md` files.

**Mindset:** inspiration transfer. The repo assumes that a brand’s look/feel can be partially captured as a reusable DESIGN.md-style rule document that AI tools can consume.

**Local limitation:** almost every brand folder is only a 3-line stub pointing to an external `getdesign.md/.../design-md` page, so the local archive is mostly a catalog, not the design rules themselves.

#### Brand coverage by category

- **AI & LLM Platforms** (12): Claude, Cohere, ElevenLabs, Minimax, Mistral AI, Ollama, OpenCode AI, Replicate, RunwayML, Together AI, VoltAgent, xAI

- **Developer Tools & IDEs** (7): Cursor, Expo, Lovable, Raycast, Superhuman, Vercel, Warp

- **Backend, Database & DevOps** (8): ClickHouse, Composio, HashiCorp, MongoDB, PostHog, Sanity, Sentry, Supabase

- **Productivity & SaaS** (7): Cal.com, Intercom, Linear, Mintlify, Notion, Resend, Zapier

- **Design & Creative Tools** (6): Airtable, Clay, Figma, Framer, Miro, Webflow

- **Fintech & Crypto** (7): Binance, Coinbase, Kraken, Mastercard, Revolut, Stripe, Wise

- **E-commerce & Retail** (5): Airbnb, Meta, Nike, Shopify, Starbucks

- **Media & Consumer Tech** (11): Apple, IBM, NVIDIA, Pinterest, PlayStation, SpaceX, Spotify, The Verge, Uber, Vodafone, WIRED

- **Automotive** (6): BMW, Bugatti, Ferrari, Lamborghini, Renault, Tesla

#### Best way to understand this archive

- Treat it as an inspiration map or lookup index.

- The real value is the taxonomy of brands and the implied design-language descriptions in the root README.

- To use it seriously, you would need to visit the external linked DESIGN.md pages, because the local repo has already moved the details out.


## 4) Cross-repo comparison: how each system thinks

| Axis | v1 `designer-skills-main` | v2 `designer-skills` plugins | `ui-ux-pro-max` | `awesome-design-md` |

|---|---|---|---|---|

| Main unit | Sequential skill workflow | Atomic skills + slash commands | Skill + search engine + datasets | Brand reference stub |

| Statefulness | High (`.design/<slug>/`) | Medium/low | High (`design-system/MASTER.md` + page overrides) | Low |

| Strength | Coherent end-to-end feature design | Breadth of design disciplines | Retrieval-backed design system generation | Inspiration and style sampling |

| Weakness | Narrower coverage outside the main build loop | Less persistent memory and weaker rendered QA emphasis | Documentation/config drift | Most local content is missing |

| Review philosophy | Screenshot-heavy visual QA | Depends on chosen plugin/command | Rule-check + retrieval guidance | Not applicable |

| Design philosophy | Opinionated anti-generic craft | Modular expert library | Data-backed expert system | Brand-inspired style transfer |

| Best use case | Designing/building a feature in a real codebase | Calling specialist workflows on demand | Creating consistent systems across many UI tasks/stacks | Borrowing inspiration from known brands |


## 5) The deeper mindset behind all four uploads

Across the uploads, I see **three different theories of how AI should do design work**:

1. **Process theory (v1):** design quality comes from sequencing the right conversations and artifacts in the right order.

2. **Capability theory (v2):** design quality comes from having a broad library of specialized mental tools and chaining them well.

3. **Retrieval/system theory (ui-ux-pro-max):** design quality comes from constraining choices with structured data, search, and persisted rules.

The fourth archive (`awesome-design-md`) is not a fourth full theory of execution; it is an **inspiration substrate** for the other three.

## 6) My judgment on which pack is strongest for what

- **Best for one real product feature from idea to polished UI:** `designer-skills-main.zip` (v1).

- **Best for broad design-organization coverage:** `designer-skills-main.zip 14-26-37-568.zip` (v2).

- **Best for repeatable design-system-backed recommendations across many contexts:** `ui-ux-pro-max-skill-main.zip`.

- **Best as a style/reference companion:** `awesome-design-md-main.zip`.

## 7) If I had to combine them into one superior system

I would use:

- v1’s **workflow and artifact persistence** as the backbone,

- v2’s **specialist plugin library** as on-demand advisors during each phase,

- ui-ux-pro-max’s **search, datasets, and persisted design-system generation** as the recommendation engine,

- awesome-design-md’s **brand references** only as inspiration inputs.

That hybrid would be much stronger than any single archive on its own.

## 8) Machine-readable coverage note

I also generated a JSON inventory that lists every inspected skill/command with headings, line counts, and extracted snippets. That file is useful if you want an audit trail or want to compare packs mechanically.
