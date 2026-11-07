# Knowledge-worker

```text
PROJECT_ROLE=core
CORE_REPOSITORY_URL=https://github.com/genilab/knowledge-worker.git
LOCAL_REPOSITORY_URL=https://github.com/genilab/knowledge-worker.git
CORE_VERSION=v0.1.9
```

This workspace is the `Knowledge-worker` base project. It holds the shared
skills and topic-based knowledge structure used by other agent-worker
projects.

## Navigation

- Start at [README.md](README.md).
- Use [DELIVERY.md](DELIVERY.md) as the current objective-to-release lifecycle
  record. Agent evidence and HITL decisions must be recorded there; release
  status is never inferred from a prior version.
- Read an invoked skill completely before using or changing it.
- Use [skills/core/INDEX.md](skills/core/INDEX.md) for update-managed core
  skills and [skills/local/INDEX.md](skills/local/INDEX.md) for local-project
  skills.
- Use [knowledge/INDEX.md](knowledge/INDEX.md) for the topic-based knowledge
  base.

## Workspace structure review

After a Dev workspace restructure, audit this file, public action guidance,
local workflow documentation, and skill packages before performing a
cross-workspace action. Resolve paths from the Knowledge-worker root and
update only verified path references. Do not change product behavior, source
material, or GitHub configuration as part of a path review.

## Multi-agent orchestration

Knowledge-worker is a graph-based multi-agent knowledge-maintenance project.
Its orchestrator interprets confirmed public actions, routes work to the
appropriate agent role and bounded skill, reviews the returned evidence, and
either completes the action, requests a decision, or makes an explicit
handoff. It does not authorize external, destructive, or ambiguous changes on
its own.

| Agent role | Responsibility | Skills | Handoffs |
| --- | --- | --- | --- |
| `structure-agent` | Maintain the approved project and agent-control structure. | `project-structure-manage`, `agents-file-manage` | Returns structural evidence to the orchestrator. |
| `skill-agent` | Create, document, and verify bounded reusable capabilities. | `skill-create`, `skill-validate`, `code-document` | Routes catalog changes to `information-agent`. |
| `information-agent` | Maintain and present knowledge dashboards and local navigation indexes. | `index-maintain`, `index-show` | Returns requested knowledge dashboards or routes knowledge work to `knowledge-agent`. |
| `knowledge-agent` | Create topics and maintain durable, attributed knowledge. | `topic-create`, `info-learn`, `knowledge-base-maintain` | Returns evidence to the orchestrator. |
| `asset-agent` | Classify, retain, and expose approved project-produced assets. | `asset-manage` | Routes public-documentation changes to `publication-agent`; escalates replacement or deletion. |
| `publication-agent` | Maintain external repository documentation and explicit GitHub operations. | `readme-maintain`, `github-maintain` | Escalates external writes and version decisions to the user. |
| `update-agent` | Show project lineage and reconcile approved core updates for a base or local project. | `project-info-show`, `update-check` | Returns project lineage, an evidence-based update assessment or reconciliation result to the orchestrator. |

The deliberation path is always **public action → orchestrator → agent role →
skill workflow → evidence → orchestrator**. The orchestrator may route a
confirmed handoff to another listed role; unclear requirements, conflicts, and
approval-gated work return to the user. These roles are capability nodes in
the project graph, not a claim that persistent external agents are already
running. See the transferable [graph-based multi-agent project model](skills/core/project-structure-manage/docs/multiagent_project_model.md).

## Knowledge actions

- `Show knowledge [ALL | {topic}]` presents the knowledge-base dashboard or a
  confirmed topic dashboard through [index-show](skills/core/index-show/SKILL.md).
- `Create topic {topic}` creates one structured knowledge topic through
  [topic-create](skills/core/topic-create/SKILL.md).
- `Learn info about {topic}` records attributable supplied material through
  [info-learn](skills/core/info-learn/SKILL.md).

## Update action

- `Show info` invokes [project-info-show](skills/core/project-info-show/SKILL.md)
  and reports the configured project version, repositories, and available
  knowledge and skill content.
- `Check updates` invokes [update-check](skills/core/update-check/SKILL.md).
  It compares the core `AGENTS.md`, actions, workflows, and `skills/core/` with
  the local project; after presenting an impact analysis, it applies only the
  user-confirmed reconciliation and records the adopted core version.

## Permanent structure

- `skills/core/` contains core-project skill packages. In a derived local
  project, they are maintained only through the confirmed reconciliation in
  `Check updates`.
- `skills/local/` contains local-project skill packages. They are created for
  local needs, are not replaced by core updates, and are never published back
  to the core repository by the update workflow.
- `assets/` contains durable project-produced assets. Store infographics in
  `assets/images/`, generated reports in `assets/reports/`, and add other
  clearly named asset subfolders only when their asset type requires one.
- Asset files must have descriptive stable names, retain applicable source or
  generation context with their request or report, and remain in `assets/`.
  Do not replace, relocate, or delete an existing asset without explicit
  approval. Public documentation may reference an approved asset only through
  the `asset-agent` to `publication-agent` handoff.
- Every core or local skill package uses the lowercase `{target}-{action}`
  naming convention; its folder name and `name` front-matter value must match.
- Every `SKILL.md` uses Codex-compatible top-level front matter: `name`,
  `description`, and optional supported fields only. Knowledge-worker routing
  data belongs in `metadata`; public actions are defined in `AGENTS.md` and
  `README.md`, not as custom Codex front-matter fields.
- Every core or local skill declares exactly one primary agent role in its `Scope`;
  that role must appear in the Agent graph above.
- The `KEY=value` configuration block at the top of this file records the core
  repository URL, local-project repository URL, and adopted core version. It is
  the shared configuration source for `Show info`, `Check updates`, and GitHub
  publication. A derived local project sets
  `PROJECT_ROLE=local` and a distinct `LOCAL_REPOSITORY_URL`.
- `knowledge/` contains durable topic-based knowledge only.
- Knowledge topics and their local records are running-environment content:
  they remain local by default and are not part of a normal GitHub release.
  `knowledge/INDEX.md` is the tracked structural stub; its local updates are
  also excluded from a default commit.
- `.env`, `.local/`, `local/`, `runtime/`, and `*.local` are local
  environment material and must never be staged by the GitHub workflow.
- The root `README.md` is the project-level guide. Root `INDEX.md` is not used.
  Local INDEX documents provide area navigation only.
- Local INDEX documents must follow the approved formats in [the index-format
  standard](skills/core/index-maintain/docs/index_format.md).

## Knowledge topics

Each topic lives at `knowledge/{topic-slug}/` and contains `references/`,
`{topic-slug}_info.md`, `{topic-slug}_ideas.md`, and
`{topic-slug}_refs.md`. Preserve source material in `references/`; record
attributed information in the info record and proposals or questions in the
ideas record.

## Boundaries

- Shared changes require a documented transfer decision; project-specific work
  remains in its owning project.
- Maintain the root `README.md` according to the repository-publication
  declaration below.

## Repository publication

- Repository visibility: `public`.
- GitHub repository: `https://github.com/genilab/knowledge-worker`.
- README profile: `public-release`.
- README maintenance: reconcile it before every explicitly requested GitHub
  commit using [readme-maintain](skills/core/readme-maintain/SKILL.md) and the
  [public-release template](skills/core/readme-maintain/docs/public_release_template.md).

## GitHub actions

- `GitHub {action}` invokes
  [github-maintain](skills/core/github-maintain/SKILL.md).
- Apply the shared [GitHub version-control standard](skills/core/github-maintain/docs/version_control.md).

Supported actions are `GitHub connect {repository-url}`, `GitHub commit`,
`GitHub commit version`, `GitHub commit minor version`, `GitHub commit major
version`, `GitHub commit knowledge`, and `GitHub synchronize`.

`GitHub connect {repository-url}` explicitly attaches an existing GitHub
repository to the local project, updates `PROJECT_ROLE` and
`LOCAL_REPOSITORY_URL` in `AGENTS.md`, and never creates a repository. Every
GitHub action performs a read-only preflight of the project root, GitHub
`origin`, branch, and working tree.

`GitHub commit` and its version variants publish only the approved framework
scope: control documents, managed skills, approved public assets, and external
documentation. `GitHub commit knowledge` is the separate explicit patch-release
action that may include `knowledge/` content and its INFO updates after a
preview. Environment-local paths are never included.

Every commit creates a generated message, a GitHub-controlled semantic release,
and a `{project-slug}_latest.zip` archive that extracts directly into a chosen
destination folder. `commit` defaults to a patch bump; `commit version` and
`commit minor version` use a minor bump; `commit major version` uses a major
bump.

`GitHub synchronize` fetches and fast-forwards only a clean, non-divergent
local project. GitHub synchronization is manual only. No action connects,
commits, pushes, pulls, or creates a repository unless the user explicitly
requests that action.

Before publication, a current `DELIVERY.md` for the requested release candidate
is required: all applicable requirements and Agent Verification must be
`PASSED`, and the user must have explicitly approved its HITL Verification.
TeamK summarizes this gate when it manages the project. This gate does not
replace the explicit `GitHub commit` request or its publication preflight.
