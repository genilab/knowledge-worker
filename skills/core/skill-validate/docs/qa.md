# QA — skill-validate

Status: VERIFIED

- `tests/test_validate_catalog.py` passed against an isolated invalid fixture.
- `code/validate_catalog.py --project .` passed for the current catalog.
- Codex's bundled `quick_validate.py` passed for all managed skill packages.
- The validator rejects unsupported front matter and detects catalog-action
  mismatches.
- The validator rejects a missing or duplicate `Primary agent role` declaration
  and the current catalog routes every skill to one declared AGENTS graph role.
- The validator rejects a prohibited root `INDEX.md`.

## Executed Test Units

- `tests/test_validate_skills.py`: PASSED — Actual checks passed.
