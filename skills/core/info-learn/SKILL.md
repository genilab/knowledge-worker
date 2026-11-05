---
name: info-learn
description: Absorb supplied knowledge, ideas, or references into one existing topic without losing provenance.
metadata:
  source: project
  action: Add attributed learning to a topic.
---

# Learn Information

## Scope

This is an external skill. Use it when the user says `Learn info about
{topic}`, `Absorb info about {topic}`, or uses `$info-learn`. It is responsible
only for adding supplied material to one existing topic. Its inputs are the
topic, supplied information and/or idea and/or source file or citation; it
produces appended, appropriately attributed topic records. User activation command:
`Learn info about {topic}`.
Primary agent role: knowledge-agent.

## Workflow

1. Read `docs/plan.md`, locate the topic in `knowledge/INDEX.md`, and confirm
   the supplied material belongs to it. Ask for clarification if no topic
   exists, the source cannot be identified, or the requested destination is
   ambiguous.
2. If a source file is supplied, copy it unchanged into that topic's
   `references/` folder using a collision-safe name. If a link, citation, or
   verbal source is supplied, retain the most precise provided identifier.
3. Append a dated, concise source entry to `{topic-slug}_refs.md` with its
   location or citation, type, and relevance note. Do not invent bibliographic
   details.
4. Append synthesized learning to `{topic-slug}_info.md` under the relevant
   key-ideas, arguments, description, or details section. Attribute source
   material and label uncertainty or interpretation.
5. Append proposals, hypotheses, questions, and brainstormed possibilities to
   `{topic-slug}_ideas.md`, never presenting them as confirmed information.
6. Produce the update outcome, naming affected records and any unresolved
   source or classification question.

## Constraints

- Do not create a missing topic, overwrite or alter an original source file,
  or silently remove earlier learning; these are non-goals.
- Do not claim source support that the supplied material does not establish,
  and do not turn an idea into information without clear evidence.
- Do not perform literature analysis, generate a report, or browse for sources
  unless separately requested. Escalate conflicting source claims or unclear
  topic classification for a user decision.

## Dependencies

- `index-maintain`
