---
name: github-maintain
description: Connect, commit, or safely synchronize one local project with its explicitly selected GitHub repository.
metadata:
  source: core
  action: Connect, commit, or safely synchronize one local project on explicit request.
---

# Maintain GitHub

## Scope

Use this skill when the user says `GitHub {action}` for one confirmed project.
Supported actions are `GitHub connect {repository-url}`, `GitHub commit`,
`GitHub commit version`, `GitHub commit minor version`, `GitHub commit major
version`, `GitHub commit knowledge`, and `GitHub synchronize`.
Every commit action generates a concise message from the changed files and
creates a GitHub-controlled semantic version release. It never synchronizes
automatically. Apply the portable
[version-control standard](docs/version_control.md).
Primary agent role: publication-agent.

## Workflow

1. Read `docs/plan.md`, the target project's `AGENTS.md` configuration block,
   and its root `README.md`. Confirm the exact project root and requested
   GitHub action.
2. For every action, perform an internal, read-only preflight: inspect the local Git root,
   existing `origin`, branch, upstream, and working-tree state. `origin` is
   the local project's GitHub repository, not the core-project source.
3. For `GitHub connect {repository-url}`, confirm that the supplied URL is an
   existing GitHub repository. On this explicit action, configure it as
   `origin`, set `PROJECT_ROLE=local`, and set `LOCAL_REPOSITORY_URL` to the
   supplied URL in the `AGENTS.md` configuration block. Never create a
   repository, commit, push, or pull while connecting.
4. For every other action, confirm that `origin` matches
   `LOCAL_REPOSITORY_URL` in `AGENTS.md`. If it is missing or mismatched, stop
   and direct the user to create and connect a GitHub repository for the local
   project. For `PROJECT_ROLE=local`, require that the local URL differs from
   `CORE_REPOSITORY_URL`.
5. Require a current project `DELIVERY.md` for the requested release candidate.
   Require every applicable requirement and Agent Verification to be `PASSED`
   and HITL Verification to record explicit user approval. Stop and direct the
   user to `Manage delivery for {project}` or `Verify all for {project}` when
   the record is missing, stale, incomplete, or not approved. This lifecycle
   gate is portable: independently used copies maintain their own Delivery
   Record even when TeamK is unavailable.
6. For a normal commit action, invoke `readme-maintain` only when the declared
   profile requires it. Stage and publish only the approved framework scope:
   control documents, managed skills, approved public assets, and external
   documentation. Exclude all `knowledge/` changes and ignored local-runtime
   paths, including a tracked `knowledge/INDEX.md` change.
7. For `GitHub commit knowledge`, first invoke `knowledge-base-maintain`, then
   preview the exact knowledge files to include. Stage the confirmed knowledge
   scope explicitly, including ignored topic files only when the user has
   confirmed their inclusion. Never include local-runtime paths.
8. For either commit action, confirm the branch and attached GitHub `origin`, inspect the
   selected files, and generate a concise factual commit message. Preview the
   proposed changed files, message, and next version before mutation. Commit
   and push the confirmed project changes, create and push an annotated
   semantic tag, create `{project-slug}_latest.zip` from that tag for direct
   extraction into the destination folder, attach it when creating the GitHub
   Release with generated notes, and remove the temporary archive after a
   successful upload.
9. Determine the requested version bump under the version-control standard.
   Use the latest GitHub semantic release/tag as the version authority; an
   explicitly requested initial version may override the default `v0.0.1`.
   Do not create a local VERSION file or changelog.
10. For `GitHub synchronize`, fetch and fast-forward only when the working tree
   is clean, the branch is non-divergent, and no merge or rebase is required.
11. Report factual resulting state, including any commit, version, release URL,
   or revision identifier,
   or escalate when the requested operation is unsafe or ambiguous.

## Constraints

- Never perform an action not explicitly named by the user.
- Never create a GitHub repository. Only explicit `GitHub connect {repository-url}`
  may add or replace `origin` and update the local-project configuration variables.
- Never amend, force-push, merge, rebase, reset,
  discard changes, or change branches.
- GitHub tags and releases are the authoritative version records; never create
  a local VERSION file or changelog.
- A normal commit stages only selected framework files after previewing them;
  it excludes `knowledge/` even when a tracked knowledge file is modified.
  `GitHub commit knowledge` stages knowledge only after an explicit preview and
  confirmation of its contents. Escalate an ambiguous or unsafe scope.
- Do not bypass an incomplete or unapproved Delivery Record. TeamK may present
  its active-gate summary, but project `DELIVERY.md` is the release evidence;
  the user must still explicitly request the GitHub action.
- Never synchronize automatically after local changes, a preflight, or on a
  schedule.
- Escalate missing authentication, insufficient permission, an ambiguous root,
  a different existing origin, unapproved files, a dirty tree, divergence, or
  any required merge or rebase.
