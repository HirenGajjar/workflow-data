# workflow-data

Source-backed workflow data, schemas, provenance, exports, and validation for Clarvia.

This repository is the core data layer for Clarvia's open bereavement workflow infrastructure.

It contains structured administrative workflow data that can be used to generate:

- human-readable checklists,
- machine-readable exports,
- review pipelines,
- and lightweight public API views.

---

## Project scope

Clarvia focuses on bereavement administration, starting from Luxembourg and cross-border corridors in Europe.

This repository models administrative workflows using official and authoritative sources.

Clarvia provides administrative guidance based on official sources.

It does not provide individualized legal advice.

---

## Repository contents

Planned structure:

```text
schemas/
  v0.1/
data/
  sources/
  institutions/
  tasks/
  workflows/
  scenarios/
exports/
scripts/
tests/
```
