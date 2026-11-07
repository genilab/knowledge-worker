# Maintain GitHub Plan

## Summary

Connect, commit, or safely synchronize a confirmed local project with its
explicitly selected GitHub repository.

## Description

This workflow exposes explicit `GitHub` actions. It performs a read-only
preflight internally; repository status is not a public action. `GitHub connect
{repository-url}` attaches an existing local-project GitHub repository and
records it in `AGENTS.md`. Every commit generates a factual message and
creates a semantic GitHub release. `GitHub synchronize` fetches and
fast-forwards only when it is safe.

For Knowledge-worker normal commits, it applies the declared README profile
and excludes local knowledge content. Only `GitHub commit knowledge` reconciles and
previews the knowledge catalog before it is included.

Every project uses its candidate-current `DELIVERY.md` as the required HITL
release gate: applicable requirements and Agent Verification must be `PASSED`
and the user must have explicitly approved HITL Verification. TeamK summarizes
that gate when it manages the project; independently used core-project copies
retain the same portable project-local process.

## Script Requirements

- It must accept `GitHub connect {repository-url}`, `GitHub commit`, `GitHub
  commit version`, `GitHub commit minor version`, `GitHub commit major version`,
  `GitHub commit knowledge`, and `GitHub synchronize`.
- It must confirm the exact project root, read the `AGENTS.md` configuration
  variables, and perform
  a read-only preflight of the local Git root, `origin`, branch, upstream, and
  working tree.
- For `GitHub connect`, it must confirm the supplied GitHub repository exists,
  configure it as `origin`, set `PROJECT_ROLE=local`, and set
  `LOCAL_REPOSITORY_URL` in `AGENTS.md`; it must not commit, push, pull, or
  create a repository while connecting.
- For all other actions, it must verify that `origin` matches
  `LOCAL_REPOSITORY_URL` in `AGENTS.md`.
- It must require a derived local project's configured repository to differ
  from its core repository before publication.
- It must stop when no matching GitHub `origin` is attached and direct the user
  to create a GitHub repository, then use `GitHub connect {repository-url}`.
- It must stop when the candidate-current Delivery Record is absent, any
  applicable requirement or Agent Verification is not `PASSED`, or HITL
  Verification is not explicitly approved; it must direct the user to
  `Manage delivery for {project}` or `Verify all for {project}` rather than
  publishing.
- It must never initialize Git or create a GitHub repository. Only the explicit
  connect action may add or replace an origin.
- It must generate a concise factual commit message from the changed files.
- It must publish only framework material by default and exclude all knowledge
  and local-runtime changes, including tracked knowledge-index changes.
- It must include knowledge only for the explicit `GitHub commit knowledge` action,
  after reconciling and previewing the exact selected knowledge files.
- It must create a semantic GitHub release after a successful commit and push.
- It must create a `{project-slug}_latest.zip` archive from the release tag,
  for direct extraction into the destination folder, and attach it to the
  GitHub Release.
- It must default `commit` to a patch bump, use minor for `commit version` and
  `commit minor version`, and use major for `commit major version`.
- It must use GitHub releases and semantic tags as the sole version authority,
  with `v0.0.1` as the initial release when no prior release exists.
- It must refuse automatic synchronization and any destructive or
  history-rewriting operation.
- It must synchronize only on `GitHub synchronize`, with a clean,
  non-divergent branch that needs no merge or rebase.

## Delegation to Code

No code is delegated in this instruction-only workflow. Deterministic command
automation requires a separately approved implementation and validation plan.

## Code Requirements

No deterministic code or test unit is required for this instruction-only
workflow.
