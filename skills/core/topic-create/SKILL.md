---
name: topic-create
description: Create a complete, listed knowledge topic when the user asks to start a topic.
metadata:
  source: project
  action: Create one listed knowledge topic.
---

# Create Topic

## Scope

This is an external skill. Use it when the user says `Create topic {topic}` or
uses `$topic-create`. It is responsible only for creating one complete empty
topic and its main-info entry. Its input is a human-readable topic name and
an optional short description; it produces a slugged topic folder containing
the required records. User activation command: `Create topic {topic}`.
Primary agent role: knowledge-agent.

## Workflow

1. Read `docs/plan.md` and confirm the topic name is specific enough to become
   a durable knowledge category; ask for clarification if it duplicates an
   existing topic or its intended scope cannot be distinguished.
2. Derive a lowercase hyphenated slug from the confirmed name. Create
   `knowledge/{topic-slug}/references/` and the three Markdown records:
   `{topic-slug}_info.md`, `{topic-slug}_ideas.md`, and
   `{topic-slug}_refs.md`.
3. Seed the info record with the display name plus empty sections for key ideas,
   arguments, description, details, and open questions. Seed the ideas and refs
   records with their topic title and an explicit empty-state note.
4. Add one linked entry to `knowledge/INDEX.md`, replacing its empty-state line
   if this is the first topic. The entry must use the display name and the
   folder's relative link.
5. Produce the created folder and info outcome, and state that the next
   learning action can add information, ideas, or a reference.

## Constraints

- Do not create a topic without the complete prescribed schema or without the
  main-info entry.
- Do not put source content in the info record as though it had been learned,
  create a report, or add unrequested topic content; those are non-goals.
- Do not overwrite an existing topic. Escalate a slug collision for a user
  decision rather than silently merging topics.

## Dependencies

- `index-maintain`
