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

```text
schemas/
  v0.1/
data/
  sources/
  institutions/
  document_requirements/
  deadlines/
  conditions/
  tasks/
  workflows/
  scenarios/
exports/
scripts/
tests/
```

## Core objects

The initial data model includes:

- Source
- Institution
- DocumentRequirement
- Deadline
- Condition
- Task
- Workflow
- Scenario
- ReviewEvent

Every publishable workflow item should be traceable to at least one source.

## Verification states

Workflow data may use the following verification states:

- `discovered`
- `structured-from-source`
- `source-checked`
- `expert-reviewed`
- `published`
- `stale-review`
- `superseded`

Only maintainers should mark workflow content as `published`.

## Current coverage

- **Luxembourg** — alpha source registry and workflow data in progress
- **France** — source mapping planned
- **Belgium** — jurisdiction modeling planned
- **Germany** — federal-core and state-overlay modeling planned
- **Portugal** — source mapping planned

## Contribution rules

Workflow-data contributions must include:

- source references,
- jurisdiction,
- language,
- access date,
- verification status,
- and enough context for review.

Do not add unsourced legal, tax, inheritance, or administrative claims.

Do not submit personal bereavement cases or sensitive personal information.

See [CONTRIBUTING.md](https://github.com/clarvia-org/.github/blob/main/CONTRIBUTING.md) for details.

## Validation

Install dependencies:

```sh
pip install -r requirements.txt
```

Validate data:

```sh
python scripts/validate.py
```

Export JSON:

```sh
python scripts/export_json.py
```

## License

Unless otherwise specified:

- workflow data, documentation, and source metadata are licensed under [Creative Commons Attribution 4.0 International](LICENSES/CC-BY-4.0.txt);
- code and tooling are licensed under [Apache License 2.0](LICENSES/Apache-2.0.txt).
