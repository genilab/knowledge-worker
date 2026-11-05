# Plan

## Summary

Compare a Knowledge-worker base or child project with the canonical framework,
then reconcile only the approved applicable updates.

## Description

`update-check` gives every project derived from Knowledge-worker one canonical
framework-update source: `https://github.com/genilab/knowledge-worker`. It
inspects canonical releases, tags, and relevant changes; establishes the local
project's adopted baseline where possible; and explains which changes apply.
The resulting assessment distinguishes core `AGENTS.md`, public actions,
workflows, and `skills/core/` changes from child-project product, knowledge,
`skills/local/`, configuration, and runtime-local material. It presents the
impact before any change, asks for confirmation, then applies and validates
only the approved reconciliation. It never synchronizes a repository.

## Script Requirements

- It must accept the public action `Check updates` for Knowledge-worker or a
  confirmed derived local project.
- It must read the `AGENTS.md` configuration block and use its configured core
  repository and adopted core version as the framework-update source, irrespective of the
  local project's GitHub repository.
- It must inspect available releases, tags, and relevant change evidence
  without changing local or remote state.
- It must establish a verifiable local framework baseline or request direction
  when the baseline cannot be determined.
- It must classify discovered changes as applicable, optional, incompatible,
  or requiring a user decision.
- It must exclude `skills/local/` from comparison and proposed updates.
- It must present a recommended target, affected areas, prerequisites, risks,
  and ordered reconciliation steps, then stop for explicit approval.
- After approval, it must apply only the confirmed core framework changes,
  run the relevant validation, and update `CORE_VERSION` in `AGENTS.md`.
- It must not pull, merge, rebase, switch branches, change remotes, install
  dependencies, or invoke GitHub synchronization. It must not edit files
  before the reconciliation is explicitly approved.

## Delegation to Code

No deterministic code is delegated initially. Update applicability depends on
the project lineage and evidence that must be reviewed before automation is
introduced.

## Code Requirements

No deterministic code or test unit is required for this instruction-only
workflow.
