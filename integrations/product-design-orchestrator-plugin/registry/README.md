# Skill registry

This registry lets an agent find a narrow skill without loading the whole ecosystem.

- `bundled-skills.json` — 67 original specialist skills included locally.
- `ui-skills-registry.tsv` — 110 entries mirrored from the UI Skills catalog on 2026-06-25.
- `taste-skills.json` — install metadata for the Taste Skill family.
- `all-skills.json` — normalized searchable index containing 192 entries across bundled, preserved, and external sources.

External entries are metadata, not an endorsement or a local installation. Inspect source, maintenance, license, assumptions, and conflicts before use. Use `python scripts/skill.py` for search and safe text-only acquisition.
