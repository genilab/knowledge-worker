#!/usr/bin/env python3
"""Render scoped Knowledge-worker skill catalogs from managed metadata."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml


def status(qa: Path) -> str:
    """Return current QA status, retaining PENDING when evidence is absent."""
    if not qa.is_file():
        return "PENDING"
    match = re.search(r"(?:^Status:\s*|Overall status\s*\|\s*)([A-Z]+)", qa.read_text(), re.M)
    return match.group(1) if match else "PENDING"


def metadata(skill: Path) -> dict:
    """Read one skill's supported YAML front matter."""
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not front:
        raise ValueError(f"{skill.name}: missing front matter")
    data = yaml.safe_load(front.group(1))
    if not isinstance(data, dict) or data.get("name") != skill.name:
        raise ValueError(f"{skill.name}: folder and metadata name differ")
    if not isinstance(data.get("metadata", {}).get("action"), str):
        raise ValueError(f"{skill.name}: missing metadata.action")
    return data


def render(project: Path, scope: str = "core") -> str:
    """Return the table-only catalog for one confirmed skill scope."""
    skills = project / "skills" / scope
    rows = [f"# {scope.title()} Skills Index", "", "| Skill | Action | Status | Plan | QA |", "| --- | --- | --- | --- | --- |"]
    for skill in sorted(path for path in skills.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()):
        data = metadata(skill)
        rows.append(
            f"| [{skill.name}]({skill.name}/SKILL.md) | {data['metadata']['action']} | "
            f"{status(skill / 'docs/qa.md')} | [Plan]({skill.name}/docs/plan.md) | [QA]({skill.name}/docs/qa.md) |"
        )
    return "\n".join(rows) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path("."))
    parser.add_argument("--scope", choices=("core", "local"), default="core")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    output = render(args.project, args.scope)
    if args.write:
        (args.project / "skills" / args.scope / "INDEX.md").write_text(output, encoding="utf-8")
    else:
        print(output, end="")
