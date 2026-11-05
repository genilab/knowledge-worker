# Plan

## Summary

Show the configured core/local repository relationship, adopted core version,
and available project content for one Knowledge-worker project.

## Description

The action provides lineage and content evidence before checking framework
updates. It reads the `AGENTS.md` configuration block, the root README, and
the knowledge and skill indexes, then reports mismatches without changing
repository state.

## Script Requirements

- Read the `KEY=value` configuration block in `AGENTS.md` at the confirmed project root.
- Compare `LOCAL_REPOSITORY_URL` with the GitHub `origin` when present.
- Report the configured role, both repository URLs, and `CORE_VERSION`.
- Summarize the available knowledge topics and core/local skills from their
  maintained indexes.

## Delegation to Code

No deterministic automation is required for this instruction-only workflow.

## Code Requirements

No code or test unit is required.
