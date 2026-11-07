---
name: index-maintain
description: Rebuild local project and skills index documents when maintained records or QA evidence change.
metadata:
  source: core
  action: Rebuild maintained index documents.
---

# Maintain Index

## Scope

This is an internal skill. Use it after Knowledge-worker project records,
managed skills, or QA evidence change. It is responsible only for maintaining
approved local INDEX formats from authoritative records. Its inputs are current
`AGENTS.md`, maintained skill definitions, topic folders, and QA records; it
produces refreshed skills, knowledge, or topic-local `INDEX.md` files. It has
no user activation command; a calling workflow invokes it.
Primary agent role: information-agent.

## Workflow

1. Read the relevant maintained records and confirm each entry has a verified
   source; ask for clarification when ownership or scope is ambiguous.
2. Select the local index to maintain: core skills, local skills, knowledge, or a topic-local
   document. Apply the exact applicable format in
   [index_format.md](docs/index_format.md).
3. For `skills/core/INDEX.md` and `skills/local/INDEX.md`, retain only the
   required title and five-column skill table. Do not create or maintain
   `skills/INDEX.md` or a project-root `INDEX.md`; project-level guidance
   belongs in `README.md`.
4. Check that every linked target exists; derive each scoped skills-table Action from
   the package's `metadata.action` value and derive status, plan, and QA links
   from its managed package. Report missing evidence as `PENDING`, rather than
   inferring a result.
5. Produce the refreshed local index from the current approved formats.

## Constraints

- Do not edit a requirement, plan, skill definition, or QA record to make an
  index look complete.
- Do not manufacture a passing status; an index reports recorded evidence only.
- Do not add core skills to the local catalog or local skills to the core
  catalog. Do not add retired metadata to scoped skill indexes.
- Non-goals include creating skills, changing project behavior, and deciding
  missing source facts.
