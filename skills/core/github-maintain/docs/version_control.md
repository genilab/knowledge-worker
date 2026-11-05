# Shared GitHub Version-Control Standard

This standard is the portable GitHub/version-control package for an
agent-worker project. A project adopts it only when its owner selects GitHub
versioning during structure setup.

## Public Actions

- `GitHub connect {repository-url}` attaches an existing GitHub repository to
  a local project and records it in `AGENTS.md`; it does not publish anything.
- `GitHub commit` creates the default patch release after verifying an
  existing local-project GitHub `origin`.
- `GitHub commit version` or `GitHub commit minor version` creates a minor
  release.
- `GitHub commit major version` creates a major release.
- `GitHub commit knowledge` creates a patch release that explicitly includes
  the confirmed local knowledge-base content.
- `GitHub synchronize` fetches and fast-forwards a clean, non-divergent local
  project only when no merge or rebase is required.

Repository status is an internal, read-only commit preflight, not a public
action. If no GitHub `origin` is attached to the local project, the workflow
stops and directs the user to create a repository and use `GitHub connect
{repository-url}`; it never creates a repository. Only that explicit action
may add or replace `origin` and update `PROJECT_ROLE` and
`LOCAL_REPOSITORY_URL` in `AGENTS.md`.

## Publication Scope

The default publication scope is the transferable project framework: control
documents, managed skills, approved public assets, and external documentation.
It excludes `knowledge/` and running-environment paths, even when a tracked
knowledge index has changed. `.gitignore` prevents new local knowledge and
environment files from appearing as ordinary candidates, but the commit
workflow must also omit modifications to tracked knowledge files.

`GitHub commit knowledge` is the sole standard action that includes knowledge.
It first reconciles the knowledge structure, previews every knowledge path,
and stages only the user-confirmed set. It may force-add ignored knowledge
files only after that explicit confirmation. Environment-local paths are never
published through either action.

## Version Rules

GitHub semantic tags and releases are the sole version authority. Tags use
`vMAJOR.MINOR.PATCH`. The default initial release is `v0.0.1`; an explicitly
requested initial version is permitted. Each commit action previews the changed
files, generated factual message, and next version before mutation. It then
commits, pushes, creates an annotated tag, pushes the tag, creates a
`{project-slug}_latest.zip` archive from the tag for direct extraction into the
destination folder, and creates a GitHub release with generated notes and that
attached archive.

## Safety Rules

Synchronization is manual. Never force-push, amend, reset, rebase, merge,
discard changes, or change branches. Stop for a dirty tree, divergence,
missing authentication, a different origin, a required merge, or an ambiguous
project root. Only `GitHub connect {repository-url}` may replace an origin.

## Transfer to Another Project

When GitHub versioning is selected during project setup, copy the complete
`github-maintain` package, including this reference, into the target's local
`skills/core/` folder. Add its row to `skills/core/INDEX.md`, add the `GitHub`
block to the target `AGENTS.md`, and describe the action in the target root
`README.md`. The target keeps its own remote, GitHub history, tags, releases,
and project-specific pre-commit reconciliation rules. Add the selected default
publication scope and local-runtime ignore rules to the target's `AGENTS.md`
and `.gitignore`.
