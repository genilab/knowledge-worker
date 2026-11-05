#!/usr/bin/env python3
"""Validate scoped Knowledge-worker skill catalogs and their links."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml


ALLOWED = {"name", "description", "license", "allowed-tools", "metadata"}
ROLE = re.compile(r"^Primary agent role: ([a-z][a-z0-9-]*)\.$", re.M)


def check_scope(project: Path, scope: str) -> list[str]:
    """Return catalog-schema errors for one managed skill scope."""
    skills_root = project / "skills" / scope
    packages = sorted(path for path in skills_root.iterdir() if path.is_dir())
    errors, actions = [], {}
    if (project / "INDEX.md").exists():
        errors.append("Root INDEX.md is not permitted")
    for package in packages:
        skill, plan, qa = package / "SKILL.md", package / "docs/plan.md", package / "docs/qa.md"
        if not all(path.is_file() for path in (skill, plan, qa)):
            errors.append(f"{package.name}: missing SKILL.md, plan, or QA")
            continue
        source = skill.read_text()
        front = re.match(r"^---\n(.*?)\n---", source, re.S)
        data = yaml.safe_load(front.group(1)) if front else {}
        if not isinstance(data, dict) or set(data) - ALLOWED:
            errors.append(f"{package.name}: unsupported front matter")
            continue
        meta = data.get("metadata")
        if data.get("name") != package.name or not isinstance(meta, dict) or not meta.get("action"):
            errors.append(f"{package.name}: invalid name or metadata.action")
            continue
        if len(ROLE.findall(source)) != 1:
            errors.append(f"{package.name}: requires exactly one primary agent role")
            continue
        actions[package.name] = meta["action"]
    catalog = (skills_root / "INDEX.md").read_text() if (skills_root / "INDEX.md").is_file() else ""
    rows = dict(re.findall(r"^\| \[([^]]+)\]\([^)]*\) \| (.*?) \| [^|]+ \|", catalog, re.M))
    if list(rows) != list(actions): errors.append(f"{scope}: Skills Index does not list packages alphabetically")
    for name, action in actions.items():
        if rows.get(name) != action: errors.append(f"{name}: catalog action mismatch")
    return errors


def check(project: Path) -> list[str]:
    """Return errors for both core and local skill catalogs."""
    errors = []
    for scope in ("core", "local"):
        if not (project / "skills" / scope).is_dir():
            errors.append(f"skills/{scope}: missing scope directory")
            continue
        errors.extend(check_scope(project, scope))
    if (project / "skills" / "INDEX.md").exists():
        errors.append("skills/INDEX.md is not permitted")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path("."))
    args = parser.parse_args()
    errors = check(args.project)
    if errors:
        raise SystemExit("\n".join(errors))
    print("Knowledge-worker catalog is valid.")
