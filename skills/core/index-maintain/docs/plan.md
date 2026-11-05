# Skill Plan — index-maintain

## Summary

Maintain approved Knowledge-worker local INDEX formats from current project
records and skill evidence.

## Description

`index-maintain` is an internal skill used after project records, managed
skills, or QA evidence change. It maintains `skills/core/INDEX.md`,
`skills/local/INDEX.md`, knowledge,
and topic-local INDEX documents from authoritative records without modifying
the evidence that supplies them. The durable formats are defined in
`index_format.md`.

## Script Requirements

- It must not create or maintain a root INDEX document; the README is the
  project-level guide.
- It must render each scoped catalog as one table with Skill, Action, Status,
  Plan, and QA columns; `skills/INDEX.md` is not used.
- It must display recorded validation status or PENDING without inventing a pass.
- It must link each listed skill, plan, and QA record using existing paths.

## Delegation to Code

- Future replacement code may automate record discovery, metadata extraction,
  status derivation, and Markdown rendering only after it implements the
  approved formats and has passing current validation.

## Code Requirements

- It must generate local INDEX documents from current maintained records.
- It must render no retired sections or columns.
- It must read each skill's action and current QA status from its package.
- It must prove that missing evidence remains PENDING and no passing status is manufactured.
