---
name: project-structure-manage
description: Create or reconcile one confirmed agent-worker project structure without overwriting existing material.
metadata:
  source: core
  action: Create or reconcile one standard project structure.
---

# Manage Project Structure

## Scope

Use this skill when the user asks to create, complete, or reconcile an
agent-worker project's standard structure. It receives a confirmed project
identity, role, and required local areas. It produces the missing required
folders and control documents, or an evidence-based report of conflicts.
Primary agent role: structure-agent.

## Workflow

1. Read `docs/plan.md`, the target `AGENTS.md` if it exists, the transferable
   [graph-based multi-agent project model](docs/multiagent_project_model.md),
   and relevant INDEX documents. Confirm project identity, role, expected
   permanent structure, its orchestrator and required agent-role graph,
   including an `asset-agent` when the standard `assets/` area is present,
   repository visibility, README profile (`public-release`, `private`, or
   none), and whether the project owner selects the shared GitHub/version-control
   package and its default knowledge-publication scope. For a public-release profile, confirm the public README contract: approved
   infographic, verifiable badges, clone destination, public actions,
   and the stable `{project-slug}_latest.zip` package when GitHub releases are
   selected.
2. Inspect the target filesystem. If the expected structure is absent, create
   the required folders, including `skills/core/`, `skills/local/`, their
   scoped `INDEX.md` files, `assets/images/` for infographics and
   `assets/reports/` for generated reports, `AGENTS.md` including the
   multi-agent orchestration contract, local `INDEX.md` documents, and a root
   `README.md` as the project-level guide. Do not create a root `INDEX.md`.
3. If the structure already exists, add only missing required elements and
   reconcile stale navigation. Preserve extra or conflicting material and
   report it for a user decision.
4. Do not create topic content, product code, or local skills outside the
   confirmed scope. When GitHub versioning is selected, transfer the complete
   `github-maintain` package and its version-control reference under
   `skills/core/`, add its Core Skills Index entry, add the portable GitHub action block to `AGENTS.md` and root
   `README.md`, and add the `KEY=value` configuration block to `AGENTS.md` with
   the configured core URL, local-project URL, and adopted core version. Configure `.gitignore` so knowledge and environment-local paths
   stay local by default; record the selected repository visibility, README
   profile, and optional knowledge-publication action in `AGENTS.md`. For a
   `public-release` profile, transfer the complete current `readme-maintain`
   package into `skills/core/` and its public README references. Report the resulting structure,
   changes made, and open decisions.

## Constraints

- Do not overwrite, delete, or reclassify existing material without explicit
  authorization.
- Do not infer a project role or treat README as internal navigation.
- Do not invent persistent external agents. Record agent roles as capability
  nodes and require user confirmation before an external agent is deployed or
  given a new authority.
- Keep migration material only under the target project's `temp/` directory.
- Keep durable project-produced assets under `assets/`; use `assets/images/`
  for infographics and `assets/reports/` for generated reports.
- Assign asset classification and retention to an `asset-agent`; reference an
  asset in public documentation only after an explicit handoff to the
  publication role.
- Do not create a public README, release-package link, or badge that cannot be
  supported by the confirmed repository, approved asset, or published release.
- Escalate an ambiguous project identity, ownership conflict, or incompatible
  existing structure.
