---
name: asset-manage
description: Classify, add, inspect, or report on approved project assets without replacing or publishing them automatically.
metadata:
  source: core
  action: Maintain approved project assets.
---

# Manage Assets

## Scope

Use this external skill when the user says `Maintain assets {request}`. It
classifies, adds, inspects, or reports on approved project-produced assets.
Its inputs are the confirmed asset request, the supplied or existing asset,
its intended use, and any source or generation context. It produces an asset
in its approved location or an evidence-based inventory or gap report. User
activation command: `Maintain assets {request}`.
Primary agent role: asset-agent.

## Workflow

1. Read `docs/plan.md`, the project `AGENTS.md`, and the requested asset or
   existing asset path. Confirm the project root, the request, the asset type,
   intended use, and source or generation context; ask for clarification when
   any is absent or the destination is ambiguous.
2. Route infographics and other project images to `assets/images/`, generated
   reports to `assets/reports/`, and another asset type only to a clearly named
   subfolder under `assets/`.
3. Use a descriptive, stable filename. Preserve the approved source or
   generation context in the request, associated report, or other maintained
   record; do not represent an unverified asset as an approved public fact. For
   a public README infographic, also provide factual alt text and confirm that
   it is ready for centered placement after the catch phrase and before badges.
4. For inspection or inventory, report the current path, type, and any
   identifiable gap without modifying files.
5. Preserve existing assets. Escalate replacement, relocation, deletion,
   ambiguous ownership, or a request to publish. Hand an approved
   public-documentation request to `publication-agent` and `readme-maintain`;
   do not modify public documentation directly.

## Constraints

- Do not store durable project assets in `temp/`, a skill package, or an
  unrelated project.
- Do not create or imply a public asset reference without an explicit
  publication request and verified asset path.
- Do not invent provenance, licensing, or accessibility claims.
- Do not decide README wording, badge content, or release-package instructions;
  provide verified asset facts to `readme-maintain` through the approved
  handoff.
- Non-goals include generating an asset, editing an asset, publishing a
  release, or changing repository state.

## Dependencies

- `readme-maintain`
