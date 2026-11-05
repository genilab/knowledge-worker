---
name: project-info-show
description: Show configured project lineage, adopted core version, and available content for a Knowledge-worker project.
metadata:
  source: core
  action: Show configured project lineage, adopted core version, and available content.
---

# Show Project Info

## Scope

Use this external skill when the user says `Show info` for Knowledge-worker or
a project derived from it. It reads the `KEY=value` configuration block in
`AGENTS.md` and the local Git
repository without changing either. It reports the configured core repository,
local-project repository, last adopted core version, and available knowledge
and skill content.
Primary agent role: update-agent.

## Workflow

1. Read the `AGENTS.md` configuration block and confirm the target project root.
2. Check that the configured local repository matches the existing GitHub
   `origin`; report a mismatch or missing configuration rather than changing it.
   For a derived local project, also report when its configured local repository
   has not been separated from the core repository.
3. Read the root README and available knowledge and skill indexes. Present the
   project role, core repository URL, local repository URL, adopted core
   version, and available project content. For a core project, state that the
   two repositories are intentionally the same.

## Constraints

- This skill is read-only.
- Do not create, alter, connect, or synchronize a repository.
- Do not infer a missing version or replace project-specific configuration.
