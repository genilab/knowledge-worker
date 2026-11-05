# Skill Plan — skill-validate

## Summary

Validate managed skills and refresh their QA evidence and catalog.

## Description

`skill-validate` is an internal skill used when one managed skill or the full
catalog needs current QA evidence. It selects named targets, runs format,
documentation, and executable-test checks, writes QA only from actual results,
and refreshes the skills catalog.

## Script Requirements

- It must run Codex's bundled skill validator and validate each selected
  skill's authoritative minimal format, local plan, QA structure, source
  documentation, and test evidence.
- It must validate the required trigger, responsibility, input, outcome, clarification, and non-goal statements for newly managed skills.
- It must write QA results from current checks and report PENDING or FAILED evidence without inventing a pass.
- It must accept `{skill}` or `all` and refresh the skills catalog after validation.
- It must reject a managed skill that does not use the authoritative minimal
  format, including the required `metadata.action` value and exactly one
  primary agent-role declaration in its Scope.
- It must reject a root `INDEX.md`; project-level guidance belongs in the root
  README and local areas retain their own INDEX documents.
- It must reject `skills/INDEX.md`; core and local skill catalogs are accessed
  directly from their scoped folders.

## Delegation to Code

- Delegate target selection, catalog discovery, validation execution, QA writing, and catalog refresh to code.
- Code must resolve one named selector or all skills, invoke the shared validator, write actual QA outcomes, and refresh the Skills Index.

## Code Requirements

- It must resolve one flat skill selector or discover every registered skill.
- It must invoke the shared validator and report each selected skill's format, documentation, and executable-test results.
- It must detect a missing or duplicate primary agent-role declaration.
- It must detect a prohibited root INDEX document.
- It must refresh the affected scoped catalog after every validation run without
  creating `skills/INDEX.md`.
- It must prove selector handling and index refresh with executable test units.
