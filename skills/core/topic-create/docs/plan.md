# Skill Plan — topic-create

## Summary

Create one complete, listed knowledge topic from a confirmed human-readable
topic name.

## Description

This skill provides the bounded entry point for new knowledge categories. It
creates the required topic artifacts and keeps the knowledge-base main info
discoverable without adding any subject-matter content.

## Script Requirements

- It must accept a topic name and optionally a short scope description.
- It must derive a stable lowercase-hyphenated topic slug and reject a collision.
- It must create `references/`, info, ideas, and refs records using that slug.
- It must add exactly one linked main-info entry for the created topic.
- It must ask for clarification when the topic is ambiguous or duplicates an
  existing topic.
- It must report the created topic and the available next learning action.

## Delegation to Code

No code portion is currently required. Topic naming, scope assessment, and
content-aware duplicate resolution require the user's and agent's judgment.

## Code Requirements

N/A
