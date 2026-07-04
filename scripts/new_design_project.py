#!/usr/bin/env python3
"""Initialize a durable .design/<slug>/ workspace without overwriting work."""
from __future__ import annotations
import argparse
import re
import shutil
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
TEMPLATES = PACKAGE / "templates"
MODE_FILES = {
    "patch": ["PROJECT_CONTEXT.md", "DECISIONS.md", "VISUAL_QA.md", "RELEASE_REVIEW.md"],
    "component": ["PROJECT_CONTEXT.md", "DESIGN_BRIEF.md", "COMPONENT_CONTRACTS.md", "DESIGN_SYSTEM.md", "IMPLEMENTATION_PLAN.md", "VISUAL_QA.md", "RELEASE_REVIEW.md"],
    "feature": ["PROJECT_CONTEXT.md", "DESIGN_BRIEF.md", "EVIDENCE_LEDGER.md", "ASSUMPTIONS.md", "DECISIONS.md", "IA_AND_FLOWS.md", "SCREEN_CONTRACTS.md", "COMPONENT_CONTRACTS.md", "DESIGN_SYSTEM.md", "IMPLEMENTATION_PLAN.md", "SKILL_LEDGER.md", "VISUAL_QA.md", "RELEASE_REVIEW.md"],
    "redesign": ["PROJECT_CONTEXT.md", "DESIGN_BRIEF.md", "EVIDENCE_LEDGER.md", "ASSUMPTIONS.md", "DECISIONS.md", "DIRECTIONS.md", "IA_AND_FLOWS.md", "DESIGN_SYSTEM.md", "SCREEN_CONTRACTS.md", "IMPLEMENTATION_PLAN.md", "SKILL_LEDGER.md", "VISUAL_QA.md", "RELEASE_REVIEW.md"],
    "greenfield": [p.name for p in TEMPLATES.glob("*.md") if p.name != "README.md"],
    "research": ["PROJECT_CONTEXT.md", "RESEARCH_PLAN.md", "EVIDENCE_LEDGER.md", "ASSUMPTIONS.md", "RESEARCH_SYNTHESIS.md", "DECISIONS.md", "SKILL_LEDGER.md"],
    "system": ["PROJECT_CONTEXT.md", "DESIGN_BRIEF.md", "DECISIONS.md", "DESIGN_SYSTEM.md", "COMPONENT_CONTRACTS.md", "IMPLEMENTATION_PLAN.md", "VISUAL_QA.md", "RELEASE_REVIEW.md"],
    "live": ["PROJECT_CONTEXT.md", "EVIDENCE_LEDGER.md", "ASSUMPTIONS.md", "DECISIONS.md", "RESEARCH_PLAN.md", "LIVE_LEARNING.md", "RELEASE_REVIEW.md"],
}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--mode", choices=sorted(MODE_FILES), default="feature")
    p.add_argument("--root", default=".")
    p.add_argument("--force", action="store_true")
    args = p.parse_args()
    slug = re.sub(r"[^a-z0-9-]+", "-", args.slug.lower()).strip("-")
    if not slug:
        raise SystemExit("Invalid slug")
    dest = Path(args.root).resolve() / ".design" / slug
    dest.mkdir(parents=True, exist_ok=True)
    for sub in ("renders", "references", "research", "tests"):
        (dest/sub).mkdir(exist_ok=True)
    copied = []
    for name in MODE_FILES[args.mode]:
        src = TEMPLATES/name
        target = dest/name
        if target.exists() and not args.force:
            continue
        text = src.read_text(encoding="utf-8").replace("{{PROJECT_SLUG}}", slug).replace("{{MODE}}", args.mode)
        target.write_text(text, encoding="utf-8")
        copied.append(name)
    readme = dest/"00_READ_ME.md"
    if not readme.exists() or args.force:
        readme.write_text(f"# {slug}\n\nMode: `{args.mode}`\n\nRead repository-level `DESIGN.md` before using these artifacts. Update status headers; do not fill templates speculatively. Empty sections should be removed or marked not applicable with a reason.\n", encoding="utf-8")
    print(f"Workspace: {dest}\nCreated/updated {len(copied)} template(s).")

if __name__ == "__main__":
    main()
