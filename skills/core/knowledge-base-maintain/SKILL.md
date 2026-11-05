---
name: knowledge-base-maintain
description: Reconcile a topic-based knowledge base and its local index from verified folders.
metadata:
  source: core
  action: Reconcile the knowledge-base structure and index.
---

# Maintain Knowledge Base

## Scope

Use this skill to reconcile one knowledge base's topic folders and
`knowledge/INDEX.md`. It receives the current topic structure and produces
accurate internal navigation without changing information, ideas, or source
content. It may supply verified topic facts to `readme-maintain` only when the
declared README profile requires them.
Primary agent role: knowledge-agent.

## Workflow

1. Read `docs/plan.md`, `knowledge/INDEX.md`, the target `AGENTS.md`, and the
   candidate topic folders.
2. Verify every topic follows the prescribed schema and identify missing or
   conflicting records.
3. Update the knowledge INDEX only from verified topic folders.
4. Provide verified topic names and concise descriptions to `readme-maintain`
   only when the declared README profile explicitly requires topic content.
   Do not add a Topics table to a public-release README unless that format is
   subsequently approved.
5. Report structure gaps as pending work.

## Constraints

- Do not manufacture topic content or provenance.
- Do not overwrite source material or merge colliding topics.
- Do not add internal workflow details, plans, QA evidence, or unverified
  descriptions to external documentation.
- Escalate ambiguous topic identity or a nonstandard topic schema.
