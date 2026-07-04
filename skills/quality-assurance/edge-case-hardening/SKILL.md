---
name: edge-case-hardening
description: Make a product production-ready across empty, slow, error, partial, stale, offline, permission, lifecycle, content, volume, and abuse edge cases.
version: "1.0.0"
category: quality-assurance
phases: ["implement", "verify"]
triggers: ["harden UI", "edge cases", "production readiness", "empty error loading states"]
---

# Edge Case Hardening

## Mission

Protect the real experience from assumptions encoded by ideal sample data and perfect networks.

## Use this skill when

- harden UI
- edge cases
- production readiness
- empty error loading states

## Inputs

- journey and data model
- API/error contracts
- roles/lifecycle
- content/locales
- operational incidents

## Protocol

1. Create an edge matrix by data, network, permission, account/object lifecycle, content, volume, environment, and misuse.
2. Prioritize by likelihood × consequence × detectability and include known production/support evidence.
3. Design and implement meaningful empty states, partial success, stale data, retries, offline/reconnect, and degraded dependencies.
4. Handle deletion, archival, expired links, revoked access, duplicate/stale writes, conflicts, and object ownership changes.
5. Stress zero/one/many/huge items, long/short/missing/malformed content, locale/RTL, and date/time boundaries.
6. Prevent duplicate submission, data loss, leakage, unsafe defaults, and inaccessible recovery.
7. Add observability, failure injection, support/audit information, and safe fallback.
8. Retest the complete journey after hardening.

## Required outputs

- edge matrix
- prioritized hardening changes
- fallback/recovery behavior
- tests/observability
- retest report

## Quality bar

- Edge states preserve user work and agency.
- Failures explain real system status.
- Sensitive data remains protected.
- High-volume/content extremes are tested.

## Failure modes to avoid

- "Something went wrong" everywhere.
- Empty states as illustrations only.
- Catching errors without recovery.
- Ignoring stale/partial data.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
