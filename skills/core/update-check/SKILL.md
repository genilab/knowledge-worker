---
name: update-check
description: Compare configured Knowledge-worker core material with a local project and reconcile approved applicable updates.
metadata:
  source: core
  action: Check configured core updates and reconcile approved applicable changes.
---

# Check Updates

## Scope

Use this external skill when the user says `Check updates` for Knowledge-worker
or a project derived from it. It compares the local project with the configured
`CORE_REPOSITORY_URL` and `CORE_VERSION` in `AGENTS.md`, regardless of
the local project's own GitHub repository. It first produces an
evidence-based update assessment and reconciliation plan, then applies only
the user-confirmed scope. User activation command: `Check updates`.
Primary agent role: update-agent.

## Workflow

1. Read `docs/plan.md`, the local project's `AGENTS.md` configuration block,
   and its local framework records. Confirm the target root, configured core
   repository, local repository, and adopted core version.
2. Inspect the configured core repository's available releases, tags, and relevant
   changes without changing the local project, its remotes, its branch, or its
   working tree. Treat the configured core repository as the update source even
   when a child project uses another repository for its own implementation.
3. Compare the configured adopted core version with the relevant core release and
   classify each change as applicable, optional, incompatible, or requiring a
   user decision. Compare only `AGENTS.md`, core actions and workflows, and
   `skills/core/`; do not propose replacing child-project product code,
   knowledge, runtime material, or `skills/local/`.
4. Present the evidence, recommended target version, affected areas,
   prerequisites, risks or conflicts, and ordered reconciliation steps.
5. Ask the user to confirm the exact reconciliation scope. After confirmation,
   apply only the approved core changes, validate them, and update
   `CORE_VERSION` in `AGENTS.md`. Use `github-maintain` only if the user
   separately requests a GitHub publication.

## Constraints

- Never pull, merge, rebase, switch branches, alter remotes, install
  dependencies, or synchronize a repository while checking for an update.
- Never treat a local project's GitHub repository, product code, knowledge base,
  configuration, or runtime-local content as a replacement for canonical
  framework evidence.
- Never assess, replace, or publish `skills/local/` as part of a core update.
- Do not recommend blind copying. Escalate an unknown baseline, a dirty or
  divergent target, an unavailable canonical source, conflicts, or any change
  whose project-specific effect cannot be determined.
- Non-goals include creating a release, modifying a repository, and deciding
  unresolved product behavior. After confirmation, a bounded reconciliation
  may modify only the approved core framework files.

## Dependencies

- `skill-validate`
