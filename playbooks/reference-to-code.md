# Playbook — Reference or design file to production code

1. Establish rights and the reference contract: source, approved frames, intended fidelity, responsive/state gaps, assets/fonts, and acceptable deviations.
2. Inspect the real stack and existing design system. Do not replace architecture to imitate a screenshot.
3. Decompose the reference into layout constraints, hierarchy, typography, spacing, color/material, assets, components, behavior, and responsive transformations.
4. Resolve missing behavior and states as product-design decisions; label inference and get approval where consequential.
5. Lock comparison conditions: viewport, DPR, browser/OS, fonts, assets, theme, locale, data, time/animation, network.
6. Implement in order: structure → geometry → typography → color/material → assets → behavior/states → responsive → polish.
7. Capture deterministic screenshots and compare side-by-side/overlay/diff.
8. Fix root causes in the same order. Avoid one-off coordinates that break nearby widths.
9. Verify semantics, keyboard/touch, accessibility, content extremes, and performance; fidelity never excuses broken UX.
10. Record any unavoidable rendering/platform deviation. Pixel-accurate completion requires approved evidence, not a claim.
