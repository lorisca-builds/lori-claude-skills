#!/usr/bin/env python3
"""Check that every skill in this repo is well formed.

For each folder that holds a SKILL.md:
  - the file opens with a frontmatter block between two --- lines
  - it has a name and a non-empty description
  - the name is lowercase-with-hyphens and matches the folder name
  - the description fits Claude's 1,024 character limit
  - the folder has a README.md for people browsing on GitHub
  - every references/... or scripts/... path the skill mentions exists
  - the root README lists the skill, so the gallery stays complete

Standard library only. Exit code 1 if anything fails.

Usage:
    python3 scripts/check_skills.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_DESCRIPTION = 1024
LOCAL_PATH_RE = re.compile(r"(?<![\w/.-])((?:references|scripts)/[\w./-]+\.(?:md|py|sh|json))")


def read_frontmatter(text):
    """Return the frontmatter as a dict of top-level keys, or None if absent.

    Handles plain values and YAML block scalars (>, >-, |, |-), which is all
    these files use. Not a general YAML parser, on purpose: no dependencies.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None

    data, key, block = {}, None, []
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m and not line.startswith(" "):
            if key is not None and block:
                data[key] = " ".join(b.strip() for b in block if b.strip())
            key, value = m.group(1), m.group(2).strip()
            block = []
            if value in (">", ">-", "|", "|-", ">+", "|+"):
                data[key] = ""
            else:
                data[key] = value.strip("\"'")
                key = None if value else key
        elif key is not None:
            block.append(line)
    if key is not None and block:
        data[key] = " ".join(b.strip() for b in block if b.strip())
    return data


def check_skill(folder, root_readme):
    problems = []
    skill_file = folder / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    meta = read_frontmatter(text)
    rel = folder.name

    if meta is None:
        return [f"{rel}: SKILL.md has no frontmatter block"]

    name = meta.get("name", "")
    description = meta.get("description", "")
    if not name:
        problems.append(f"{rel}: frontmatter has no name")
    elif not NAME_RE.match(name):
        problems.append(f"{rel}: name '{name}' should be lowercase words joined by hyphens")
    elif name != rel:
        problems.append(f"{rel}: name '{name}' does not match the folder name")

    if not description:
        problems.append(f"{rel}: frontmatter has no description")
    elif len(description) > MAX_DESCRIPTION:
        problems.append(f"{rel}: description is {len(description)} characters (limit {MAX_DESCRIPTION})")

    if not (folder / "README.md").exists():
        problems.append(f"{rel}: no README.md")

    mentioned = set(LOCAL_PATH_RE.findall(text))
    readme = folder / "README.md"
    if readme.exists():
        mentioned |= set(LOCAL_PATH_RE.findall(readme.read_text(encoding="utf-8")))
    for path in sorted(mentioned):
        if not (folder / path).exists():
            problems.append(f"{rel}: mentions {path}, which does not exist")

    if rel not in root_readme:
        problems.append(f"{rel}: not listed in the root README")
    return problems


def main():
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    folders = sorted(p.parent for p in ROOT.glob("*/SKILL.md"))
    if not folders:
        print("No skills found")
        return 1

    problems = []
    for folder in folders:
        problems += check_skill(folder, root_readme)

    if problems:
        print(f"{len(problems)} problem(s) across {len(folders)} skills:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"OK: {len(folders)} skills, frontmatter valid, names match folders, all referenced files exist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
