# Plan

## Summary

Create or reconcile one confirmed agent-worker project structure through a
single safe workflow.

## Description

This skill replaces the separate structure-creation and structure-maintenance
workflows. It first establishes whether the target structure is absent or
already present, then creates missing approved elements or reconciles existing
navigation without overwriting material.

## Script Requirements

- It must confirm project identity, role, required structure, and external
  README need before changing a target.
- For a public-release README profile, it must confirm the approved
  infographic, verifiable badges, clone destination, public actions,
  and release-package policy before publication content is maintained.
- It must establish the target's graph-based multi-agent orchestration
  contract: an orchestrator, necessary agent roles, skill ownership and
  handoffs, and escalation boundaries, using `multiagent_project_model.md`.
- It must create required folders, including `skills/core/` and `skills/local/`
  with scoped indexes, `AGENTS.md` with the multi-agent
  orchestration contract, a root `README.md` project guide, and local `INDEX.md`
  documents when the target structure is absent; root `INDEX.md` is prohibited.
- It must create `assets/images/` for approved infographics and
  `assets/reports/` for generated reports; other asset subfolders require a
  clearly named asset type.
- It must declare an `asset-agent` for the standard assets area, including
  ownership, skill routing, and the handoff to publication when a public asset
  reference is requested.
- It must reconcile missing required elements and stale navigation when the
  target structure exists.
- It must preserve unexpected or conflicting material and report it rather
  than deleting or overwriting it.
- It must ask whether the project adopts the shared GitHub/version-control
  package and, when selected, transfer its skill package into `skills/core/`,
  its core catalog row, AGENTS
  and INFO action declarations, and the `AGENTS.md` configuration variables without transferring
  another project's remote, history, tags, releases, or project-specific rules.
- It must record the owner-selected repository visibility and README profile
  in the target AGENTS file before README maintenance can occur.
- It must configure the portable default publication scope: framework material
  is published, while knowledge and environment-local content remain local
  until the owner explicitly invokes the knowledge-publication action.
- It must transfer the current `readme-maintain` package into `skills/core/`
  and its public README references when the target selects a public-release profile.

## Delegation to Code

No code is delegated. Structure decisions require project-specific inspection
and human confirmation when a conflict exists.

## Code Requirements

No deterministic code or test unit is required for this instruction-only
workflow.
