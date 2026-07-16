#!/usr/bin/env python3
"""Validate the relex-legal skill pack against Anthropic's conventions.

Checks every skills/**/SKILL.md and commands/*.md / agents/*.md:
  * YAML frontmatter present, parseable, with exactly the allowed keys,
  * `name` <= 64 chars, lowercase-hyphen, matches its directory (skills),
  * `description` present, <= 1024 chars, no decimal-comma-in-number
    (breaks some selectors — the German pack's lesson),
  * no obvious skeleton markers left in the body.

Exit non-zero on any failure so CI can gate. No external deps beyond PyYAML.
"""
from __future__ import annotations

import pathlib
import re
import sys

try:
    import yaml
except Exception:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parent.parent / "plugin"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DECIMAL_COMMA_RE = re.compile(r"\d,\d")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SKILL_KEYS = {"name", "description", "user-invocable", "argument-hint"}

# Jurisdiction packs are reference files (NO frontmatter) under skills/jurisdictions/.
PACK_NAME_RE = re.compile(r"^([A-Z]{2}|_TEMPLATE)\.md$")
CANONICAL_DEADLINE_HEADING = (
    "## Limitation / deadline heuristics "
    "(orientation only — never finalize from memory)"
)
REQUIRED_PACK_HEADINGS = (
    "## Legal family",
    "## Citation",
    "## Discovery channels",
    "## Grounding availability",
    "## Compliance limits",
    "## Method notes",
    "## Community skills",
    "## Limitation / deadline heuristics",
)
PACK_MAX_BYTES = 6144
DESC_INFO_THRESHOLD = 350


def _frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1)) or {}


def check_skill(path: pathlib.Path, errors: list):
    fm = _frontmatter(path.read_text())
    rel = path.relative_to(ROOT)
    if fm is None:
        errors.append(f"{rel}: missing/!parseable YAML frontmatter")
        return
    extra = set(fm) - SKILL_KEYS
    if extra:
        errors.append(f"{rel}: unexpected frontmatter keys {sorted(extra)}")
    name = str(fm.get("name", ""))
    desc = str(fm.get("description", ""))
    if not NAME_RE.match(name):
        errors.append(f"{rel}: name '{name}' must be lowercase-hyphen")
    if len(name) > 64:
        errors.append(f"{rel}: name > 64 chars")
    if path.parent.name != name:
        errors.append(f"{rel}: name '{name}' != dir '{path.parent.name}'")
    if not desc:
        errors.append(f"{rel}: empty description")
    if len(desc) > 1024:
        errors.append(f"{rel}: description > 1024 chars ({len(desc)})")
    if DECIMAL_COMMA_RE.search(desc):
        errors.append(f"{rel}: decimal comma in description (selector hazard)")


def check_markdown_frontmatter(path: pathlib.Path, errors: list):
    fm = _frontmatter(path.read_text())
    rel = path.relative_to(ROOT)
    if fm is None:
        errors.append(f"{rel}: missing/!parseable YAML frontmatter")
        return
    if not str(fm.get("description", "")):
        errors.append(f"{rel}: empty description")


def check_pack(path: pathlib.Path, errors: list):
    """Validate one jurisdiction pack (stdlib only — packs carry no frontmatter)."""
    rel = path.relative_to(ROOT)
    name = path.name
    if not PACK_NAME_RE.match(name):
        errors.append(f"{rel}: pack filename must match ^([A-Z]{{2}}|_TEMPLATE)\\.md$")
    raw = path.read_bytes()
    if len(raw) > PACK_MAX_BYTES:
        errors.append(f"{rel}: pack > {PACK_MAX_BYTES} bytes ({len(raw)})")
    text = path.read_text()
    if FRONTMATTER_RE.match(text):
        errors.append(f"{rel}: pack must NOT have YAML frontmatter (it is a reference file)")
    lines = text.splitlines()
    title = lines[0] if lines else ""
    code = name[:-3]  # strip '.md'
    if code != "_TEMPLATE" and not title.startswith(f"# {code} — "):
        errors.append(f"{rel}: title line must start '# {code} — '")
    headings = [ln for ln in lines if ln.startswith("## ")]
    for req in REQUIRED_PACK_HEADINGS:
        if not any(h.startswith(req) for h in headings):
            errors.append(f"{rel}: missing required section heading '{req}'")
    if CANONICAL_DEADLINE_HEADING not in text:
        errors.append(
            f"{rel}: deadline heading must be exactly '{CANONICAL_DEADLINE_HEADING}'"
        )
    if "GET /research/sources" not in text:
        errors.append(f"{rel}: must reference the live registry 'GET /research/sources'")


def main() -> int:
    errors: list = []
    infos: list = []
    skills = sorted(ROOT.glob("skills/**/SKILL.md"))
    if not skills:
        print("no skills found", file=sys.stderr)
        return 2
    md_meta = sorted(ROOT.glob("commands/*.md")) + sorted(ROOT.glob("agents/*.md"))
    for p in skills:
        check_skill(p, errors)
    for p in md_meta:
        check_markdown_frontmatter(p, errors)

    packs = sorted(ROOT.glob("skills/jurisdictions/*.md"))
    for p in packs:
        check_pack(p, errors)

    # Non-failing: flag long frontmatter descriptions (a selector cost, not an error).
    for p in skills + md_meta:
        fm = _frontmatter(p.read_text()) or {}
        desc = str(fm.get("description", ""))
        if len(desc) > DESC_INFO_THRESHOLD:
            infos.append(
                f"{p.relative_to(ROOT)}: description {len(desc)} chars "
                f"(> {DESC_INFO_THRESHOLD} — informational)"
            )
    for i in infos:
        print("  ℹ", i)

    if errors:
        print(f"FAIL — {len(errors)} problem(s):")
        for e in errors:
            print("  •", e)
        return 1
    print(
        f"OK — {len(skills)} skills + {len(packs)} jurisdiction packs "
        f"+ commands/agents validated"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
