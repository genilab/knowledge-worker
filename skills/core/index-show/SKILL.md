---
name: index-show
description: Present the Knowledge-worker knowledge-base dashboard or one topic dashboard without modifying records.
metadata:
  source: core
  action: Show the knowledge-base or one topic dashboard.
---

# Show Knowledge

## Scope

Use this skill when the user says `Show knowledge` or `Show knowledge {topic}`.
It reads the maintained knowledge indexes and topic records, then presents a
dashboard of available topics or the requested topic without changing the
workspace.
Primary agent role: information-agent.

## Workflow

1. Read `knowledge/INDEX.md`. For `Show knowledge`, present the available
   topics and their maintained navigation.
2. For `Show knowledge {topic}`, resolve the confirmed topic and present its
   information, ideas, references, and available source-material navigation.
3. State when the requested topic is absent or ambiguous; do not create,
   infer, or modify a topic while showing it.

## Constraints

- This is read-only.
- Do not create a root `INDEX.md` or substitute a local index for the project
  guide.
- Do not treat temporary migration records as durable Knowledge-worker indexes.
