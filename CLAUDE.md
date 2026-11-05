# Knowledge-worker

```text
PROJECT_ROLE=local
CORE_REPOSITORY_URL=https://github.com/genilab/knowledge-worker.git
LOCAL_REPOSITORY_URL=
CORE_VERSION=v0.1.8
```

Graph-based knowledge base for the AMZN_Account project, maintained by an
orchestrator, agent roles, and bounded skills. Knowledge is organized by topic
under `knowledge/`. Derived from the Knowledge-worker core project.

The `KEY=value` block above is the single configuration source for
`Show info`, `Check updates`, and GitHub actions. `LOCAL_REPOSITORY_URL` stays
empty until `GitHub connect {repository-url}` sets it. Keep the block as the
first code block in this file.

## Public actions

Match the user's request to an action, then read the skill's `SKILL.md`
completely before acting.

| Action | Skill |
| --- | --- |
| `Show knowledge [ALL \| {topic}]` | `index-show` |
| `Create topic {topic}` | `topic-create` |
| `Learn info about {topic}` (PDF, URL, text, file) | `info-learn` |
| `Show info` | `project-info-show` |
| `Check updates` | `update-check` |
| `GitHub {action}` | `github-maintain` |

Skills live in `skills/core/{skill}/SKILL.md`; local skills in `skills/local/`.
Each skill package has `docs/plan.md` and `docs/qa.md`. Indexes:
[core skills](skills/core/INDEX.md), [local skills](skills/local/INDEX.md),
[knowledge](knowledge/INDEX.md).

## Multi-agent orchestration

This project is graph-based and multi-agent. The orchestrator interprets each
confirmed public action, routes it to the agent role that owns the skill,
reviews the returned evidence, and then completes the action, requests a
decision, or makes an explicit handoff. It never authorizes external,
destructive, or ambiguous changes on its own.

| Agent role | Responsibility | Skills | Handoffs |
| --- | --- | --- | --- |
| `structure-agent` | Maintain the approved project and agent-control structure. | `project-structure-manage`, `agents-file-manage` | Returns structural evidence to the orchestrator. |
| `skill-agent` | Create, document, and verify bounded reusable capabilities. | `skill-create`, `skill-validate`, `code-document` | Routes catalog changes to `information-agent`. |
| `information-agent` | Maintain and present knowledge dashboards and local navigation indexes. | `index-maintain`, `index-show` | Returns dashboards or routes knowledge work to `knowledge-agent`. |
| `knowledge-agent` | Create topics and maintain durable, attributed knowledge. | `topic-create`, `info-learn`, `knowledge-base-maintain` | Returns evidence to the orchestrator. |
| `asset-agent` | Classify, retain, and expose approved project-produced assets. | `asset-manage` | Routes public-documentation changes to `publication-agent`; escalates replacement or deletion. |
| `publication-agent` | Maintain external repository documentation and explicit GitHub operations. | `readme-maintain`, `github-maintain` | Escalates external writes and version decisions to the user. |
| `update-agent` | Show project lineage and reconcile approved core updates. | `project-info-show`, `update-check` | Returns lineage, update assessment, or reconciliation result to the orchestrator. |

Deliberation path: public action → orchestrator → agent role → skill workflow
→ evidence → orchestrator.

- Route an action to the one role that owns its skill; the orchestrator may
  route a confirmed handoff to another listed role.
- Ask the user when requirements are unclear, conflicting, external,
  irreversible, or approval-gated.
- Roles are capability nodes. They are not continuously running external
  agents.

Model details: @skills/core/project-structure-manage/docs/multiagent_project_model.md

## Structure

```text
knowledge/{topic-slug}/   one folder per topic
knowledge/INDEX.md        topic navigation
skills/core/              core skills; change only via `Check updates`
skills/local/             local skills; never replaced by core updates
assets/images/            infographics
assets/reports/           generated reports
```

Each topic folder contains `references/`, `{topic-slug}_info.md`,
`{topic-slug}_ideas.md`, `{topic-slug}_refs.md`.

- Put source material in `references/`.
- Put attributed information in `_info.md`.
- Put proposals and questions in `_ideas.md`.
- Keep `knowledge/` for durable topic knowledge only. It is local
  running-environment content, excluded from normal GitHub releases.
- Add other `assets/` subfolders only when an asset type requires one.

## Rules

- Skill folders are lowercase `{target}-{action}`; the folder name must equal
  the `name` front-matter value.
- Every `SKILL.md` has top-level front matter `name`, `description`, and
  optionally supported fields. Put routing data under `metadata`. Define
  public actions in this file and `README.md`, not as custom front matter.
- Every skill declares exactly one primary agent role in its `Scope`, and that
  role must appear in the Agent table above.
- Local `INDEX.md` files follow
  @skills/core/index-maintain/docs/index_format.md. No root `INDEX.md`.
- Assets get descriptive, stable names and keep their source or generation
  context. Public docs reference an asset only through the `asset-agent` →
  `publication-agent` handoff.
- Shared changes need a documented transfer decision; project-specific work
  stays in its owning project.
- Keep this file for operating rules and navigation, not durable knowledge or
  INDEX content.

## Repository publication

- Repository visibility: not set. Declare it, with a README profile
  (`public-release` or `private`), before running `readme-maintain`.
- GitHub repository: see `LOCAL_REPOSITORY_URL` in the config block.
- Reconcile the root `README.md` with `readme-maintain` before every
  explicitly requested GitHub commit.

## GitHub actions

`GitHub {action}` invokes `github-maintain` and the shared
[version-control standard](skills/core/github-maintain/docs/version_control.md).

Supported: `connect {repository-url}`, `commit`, `commit version`,
`commit minor version`, `commit major version`, `commit knowledge`,
`synchronize`.

- `connect` attaches an existing repository, sets `PROJECT_ROLE` and
  `LOCAL_REPOSITORY_URL` in the config block, and never creates a repository.
- Every action starts with a read-only preflight of project root, `origin`,
  branch, and working tree.
- `commit` and its version variants publish only framework scope: control
  documents, managed skills, approved public assets, and external
  documentation. Default bump is patch; `version`/`minor` bump minor; `major`
  bumps major.
- `commit knowledge` is the only action that may include `knowledge/`, and
  only after a preview.
- Every commit creates a generated message, a semantic release, and a
  `{project-slug}_latest.zip` archive.
- `synchronize` fast-forwards only a clean, non-divergent project.

## Never

- Replace, move, or delete an existing asset without explicit approval.
- Edit `skills/core/` outside the confirmed `Check updates` reconciliation.
- Connect, commit, push, pull, or create a repository unless the user asks for
  that GitHub action.
- Stage `.env`, `.env.*`, `.local/`, `local/`, `runtime/`, `*.local`, or
  `.DS_Store`.
- Keep migration material outside `temp/`, which is deleted after migration
  acceptance.
- Invent product behavior, workflows, or operating rules.

## Maintaining this file

- Keep it short; move detail into skill docs and link or `@`-import it.
- After a workspace restructure, fix only verified path references. Do not
  alter behavior, source material, or GitHub configuration.
