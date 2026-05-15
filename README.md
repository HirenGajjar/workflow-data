# workflow-data

**Clarvia helps grieving families navigate the mountain of paperwork after losing a loved one.** Every small contribution here — a source check, a translation, a link fix — reduces that burden for someone in Luxembourg or across Europe.

🌐 [clarvia.org](https://clarvia.org) · 📋 [Good first issues](https://github.com/clarvia-org/workflow-data/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) · 📖 [How to contribute](https://github.com/clarvia-org/.github/blob/main/CONTRIBUTING.md)

---

Source-backed workflow data, schemas, provenance, exports, and validation for [Clarvia](https://clarvia.org).

This repository is the core data layer for Clarvia's open bereavement workflow infrastructure. It contains structured administrative workflow data that can be used to generate:

- human-readable checklists,
- machine-readable exports,
- review pipelines,
- and lightweight public API views.

---

## How to help in under 30 minutes

You don't need to be a developer. Many of our most valuable tasks require attention to detail, language skills, or domain knowledge — not code.

| Task | Time | Skills needed |
|---|---|---|
| [Verify a source URL is still current](https://github.com/clarvia-org/workflow-data/issues?q=is%3Aissue+is%3Aopen+label%3A%22type%3A+source%22+label%3A%22good+first+issue%22) | ~15 min | Browser + attention to detail |
| [Translate source descriptions to French or German](https://github.com/clarvia-org/workflow-data/issues?q=is%3Aissue+is%3Aopen+label%3A%22type%3A+translation%22) | ~20 min | French or German proficiency |
| [Review and mark a source as verified](https://github.com/clarvia-org/workflow-data/issues/23) | ~15 min | Attention to detail |
| [Write methodology documentation](https://github.com/clarvia-org/workflow-data/issues/21) | ~30 min | Clear writing in English |
| [Add a new official source record](https://github.com/clarvia-org/workflow-data/issues?q=is%3Aissue+is%3Aopen+label%3A%22type%3A+source%22+label%3A%22good+first+issue%22) | ~20 min | Basic YAML editing |

👉 **Browse all [good first issues](https://github.com/clarvia-org/workflow-data/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)** to find something that fits your skills.


---

## Project scope

Clarvia focuses on bereavement administration and related family support workflows.

The first service is being built and validated in Luxembourg. The data model is designed to recognise cross-border realities from the beginning, because many Luxembourg family situations involve neighbouring countries, foreign institutions, multilingual documents, or responsibilities outside one jurisdiction.

This repository models administrative workflows using official and authoritative sources.

Clarvia provides administrative guidance based on official sources.

It does not provide individualized legal advice.

The public data should not contain personal bereavement cases, private family information, or sensitive personal documents.

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

## Implementation path

- Luxembourg — first checklist and source-backed workflow foundation to build and validate
- France, Belgium, Germany — future or Luxembourg-relevant source mapping where cross-border situations require it
- Portugal and other European jurisdictions — possible future expansion after the model and review process mature

No jurisdiction should be treated as published guidance until its workflow data has appropriate sources, review status, and publication approval.

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
