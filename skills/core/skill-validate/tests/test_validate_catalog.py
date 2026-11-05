import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE = Path(__file__).parents[1] / "code/validate_catalog.py"
SPEC = importlib.util.spec_from_file_location("catalog", MODULE)
CATALOG = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CATALOG)


class ValidateCatalogTest(unittest.TestCase):
    def write_indexes(self, root: Path, core_rows: str) -> None:
        (root / "skills/local").mkdir(parents=True, exist_ok=True)
        (root / "skills/core/INDEX.md").write_text(core_rows)
        (root / "skills/local/INDEX.md").write_text(
            "# Local Skills Index\n\n| Skill | Action | Status | Plan | QA |\n"
            "| --- | --- | --- | --- | --- |\n"
        )

    def test_rejects_catalog_action_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / "skills/core/alpha-check"
            (skill / "docs").mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: alpha-check\ndescription: Check alpha.\nmetadata:\n  source: core\n  action: Check alpha.\n---\n\n## Scope\n\nPrimary agent role: alpha-agent.\n")
            (skill / "docs/plan.md").write_text("# Plan\n")
            (skill / "docs/qa.md").write_text("Status: PENDING\n")
            self.write_indexes(root, "# Core Skills Index\n\n| Skill | Action | Status | Plan | QA |\n| --- | --- | --- | --- | --- |\n| [alpha-check](alpha-check/SKILL.md) | Wrong. | PENDING | [Plan](alpha-check/docs/plan.md) | [QA](alpha-check/docs/qa.md) |\n")
            self.assertIn("alpha-check: catalog action mismatch", CATALOG.check(root))

    def test_rejects_missing_primary_agent_role(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / "skills/core/alpha-check"
            (skill / "docs").mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: alpha-check\ndescription: Check alpha.\nmetadata:\n  source: core\n  action: Check alpha.\n---\n")
            (skill / "docs/plan.md").write_text("# Plan\n")
            (skill / "docs/qa.md").write_text("Status: PENDING\n")
            self.write_indexes(root, "# Core Skills Index\n\n| Skill | Action | Status | Plan | QA |\n| --- | --- | --- | --- | --- |\n| [alpha-check](alpha-check/SKILL.md) | Check alpha. | PENDING | [Plan](alpha-check/docs/plan.md) | [QA](alpha-check/docs/qa.md) |\n")
            self.assertIn("alpha-check: requires exactly one primary agent role", CATALOG.check(root))

    def test_rejects_root_index_document(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "INDEX.md").write_text("# Retired root index\n")
            (root / "skills/core").mkdir(parents=True)
            self.write_indexes(root, "# Core Skills Index\n\n| Skill | Action | Status | Plan | QA |\n| --- | --- | --- | --- | --- |\n")
            self.assertIn("Root INDEX.md is not permitted", CATALOG.check(root))

    def test_rejects_skills_root_index_document(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "skills/core").mkdir(parents=True)
            self.write_indexes(root, "# Core Skills Index\n\n| Skill | Action | Status | Plan | QA |\n| --- | --- | --- | --- | --- |\n")
            (root / "skills/INDEX.md").write_text("# Retired skills index\n")
            self.assertIn("skills/INDEX.md is not permitted", CATALOG.check(root))
