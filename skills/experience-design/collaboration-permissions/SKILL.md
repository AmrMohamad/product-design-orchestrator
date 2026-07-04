---
name: collaboration-permissions
description: Design multi-user roles, sharing, permissions, presence, comments, approvals, conflicts, history, and accountability.
version: "1.0.0"
category: experience-design
phases: ["structure", "systemize", "verify"]
triggers: ["collaboration UX", "permissions", "roles", "sharing", "approval workflow"]
---

# Collaboration Permissions

## Mission

Make who can see, change, approve, and recover clear across collaborative work.

## Use this skill when

- collaboration UX
- permissions
- roles
- sharing
- approval workflow

## Inputs

- actors/roles
- objects and lifecycle
- permission model
- audit/security needs
- real-time/offline constraints

## Protocol

1. Map actors, goals, authority, object scopes, inherited permissions, and exceptional access.
2. Design invitations, requests, acceptance, expiry, removal, ownership transfer, and external guests.
3. Expose current access and consequence at the point of sharing or destructive change.
4. Define presence, comments/mentions, notifications, assignments, approvals, and resolved state without attention overload.
5. Handle simultaneous editing, optimistic updates, conflicts, locking, merge/recovery, and offline reconnection.
6. Provide history/audit, attribution, version restore, and export where consequences require it.
7. Test role transitions, revoked access, deleted users, hidden data, cross-tenant boundaries, and notification failure.
8. Ensure accessibility of real-time updates and avoid leaking private activity.

## Required outputs

- role/permission matrix
- sharing/invite flow
- collaboration state model
- conflict/history behavior
- security/a11y tests

## Quality bar

- Permission effects are visible before action.
- Least privilege is supported.
- Conflicts preserve work.
- Notifications are controllable and meaningful.

## Failure modes to avoid

- Role names without capability definitions.
- Security by hidden button only.
- Silent ownership transfer.
- Presence indicators that expose sensitive activity.

## Handoff

Record consequential decisions and pass only decision-relevant context to the next phase.
