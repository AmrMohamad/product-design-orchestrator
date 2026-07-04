# Any-stack design-to-code adapter

The orchestrator is technology-neutral; implementation must be technology-specific.

## Detection before recommendation

Inspect manifests, lockfiles, build/deploy config, framework/runtime versions, route/layout model, rendering mode, styling, component primitives, tokens/themes, state/data, localization, tests, previews, and platform targets. Current official documentation is the authority for version-sensitive APIs.

## Translation contract

Translate each approved design decision into the stack's native mechanisms:

| Design concern | Web | Native mobile/desktop | Embedded/other |
|---|---|---|---|
| Semantics | semantic HTML first; ARIA only when needed | platform accessibility roles/traits/actions | platform input/output semantics |
| Layout | intrinsic CSS grid/flex/container queries | platform layout primitives/safe areas | device constraints |
| Navigation | URL/history/deep link/focus/title | navigation stack/deep links/lifecycle | native routing/state |
| State | explicit domain/async state; server/client boundaries | lifecycle, offline, background/foreground | operational state model |
| Tokens | CSS variables/generated types/theme provider | resource/theme/token codegen | platform constants |
| Motion | transform/opacity, WAAPI/CSS/library where justified | native/compositor animation | performance budget |
| Tests | unit/component/e2e/a11y/visual | unit/UI/snapshot/accessibility | simulator/hardware evidence |

## Foundation policy

- Extend the installed coherent system before inventing another.
- Prefer official platform/design-system packages when the product context calls for them.
- Do not import a second primitive library for one visual effect.
- Do not hand-code an imitation of an official component when the official package is required.
- Do not force web conventions into native UI or native conventions into the web.

## Missing stack expertise

Use `python scripts/skill.py recommend --stack <stack> --phase implement --task "..."`. Prefer the narrow official/framework skill, then verify every recommendation against the installed version and repository constraints.
