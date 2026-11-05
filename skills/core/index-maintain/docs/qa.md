# QA — index-maintain

Status: VERIFIED

- `tests/test_render_skills_index.py` passed against an isolated skill fixture.
- `code/render_skills_index.py --project . --scope core` reproduced
  `skills/core/INDEX.md` exactly.
- The renderer reads supported metadata, preserves evidence-based status, and
  emits only the approved table-only Skills Index format.
