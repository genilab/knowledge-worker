# Knowledge-worker Index Format

This is the authoritative format for Knowledge-worker local INDEX documents.
`index-maintain`, `skill-create`, and `skill-validate` apply it whenever they
create, revise, or check a local index. Root `INDEX.md` is not used; the root
`README.md` is the project-level guide.

## Skills Catalogs

`skills/INDEX.md` is not used. The two scoped catalogs are
`skills/core/INDEX.md` and `skills/local/INDEX.md`.

Each scoped catalog contains exactly the title below and one table, with no
description before the table and no content after it:

```md
# Core Skills Index

| Skill | Action | Status | Plan | QA |
| --- | --- | --- | --- | --- |
| [skill-name](skill-name/SKILL.md) | Bounded action. | PENDING | [Plan](skill-name/docs/plan.md) | [QA](skill-name/docs/qa.md) |
```

For the local catalog, use `# Local Skills Index`. List every skill in its own
scope once, alphabetically by its folder name. Core skills belong only in
`skills/core/`; local-project skills belong only in `skills/local/`. The
Status value is evidence-based (`VERIFIED`, `PENDING`, `FAILED`, or another
documented current state); it is never inferred from a missing or stale QA
record. The Action value comes from the corresponding package's
`metadata.action` value; it does not define or activate a public user action.
