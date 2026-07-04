---
name: forms-validation
description: Design forms, data entry, validation, review, submission, and recovery for clarity, efficiency, accessibility, and data integrity.
version: "1.0.0"
category: experience-design
phases: ["structure", "systemize", "verify"]
triggers: ["form design", "validation", "checkout form", "data entry"]
---

# Forms Validation

## Mission

Help people provide the minimum necessary accurate information with confidence and recover without loss.

## Use this skill when

- form design
- validation
- checkout form
- data entry

## Inputs

- data requirements
- user context/device
- risk/legal constraints
- backend validation and persistence

## Protocol

1. Question whether each field is necessary now; group by user intent, not database schema.
2. Choose appropriate native controls, input modes, autocomplete, formatting, defaults, and examples.
3. Use persistent labels; add concise help before the error when misunderstanding is predictable.
4. Validate at the least disruptive useful moment; distinguish formatting, completeness, business rule, server, and cross-field errors.
5. Preserve entered data and focus/announce errors accessibly; provide an error summary for long forms when appropriate.
6. Support save/resume, review/edit, back navigation, timeouts, duplicate submission, and partial failure based on risk.
7. Explain optionality, privacy/purpose, irreversible consequences, and what happens next.
8. Test mobile keyboard, zoom, password managers, paste, autofill, long/translated values, and assistive technology.

## Required outputs

- field/section model
- validation/error contract
- review/submission/recovery flow
- accessibility behavior
- test matrix

## Quality bar

- Data collection is minimized.
- Errors preserve work and move focus appropriately.
- Native semantics/autocomplete are used.
- Form structure follows user decisions.

## Failure modes to avoid

- Placeholder-only labels.
- Validation on every keystroke.
- Generic red text.
- Disabling paste.
- Splitting fields for visual symmetry.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
