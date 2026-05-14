# Methodology

Clarvia builds source-backed workflow data for bereavement administration.

The methodology is designed to make administrative guidance:

- traceable,
- reviewable,
- reusable,
- multilingual,
- and suitable for human-readable and machine-readable outputs.

Clarvia provides administrative guidance based on official sources.

It does not provide individualized legal advice.

---

## Workflow production loop

Clarvia's workflow production loop is:

```text
find source
→ create source object
→ extract structured facts
→ attach provenance
→ validate schema
→ human review
→ publish
→ monitor for changes
```

## Source-first model

Every publishable workflow item should be traceable to an official or authoritative source.

Preferred sources include:

- government portals,
- official forms,
- statutes,
- regulations,
- administrative guidance,
- official institutional pages,
- and official service descriptions.

Unsourced administrative, legal, tax, or inheritance claims should not be published.

## Object model

Clarvia uses a small set of explicit objects:

- Source
- Institution
- DocumentRequirement
- Deadline
- Condition
- Task
- Workflow
- Scenario
- ReviewEvent

This model is intentionally conservative.

The goal is to support useful public outputs without building a heavy case-management or legal-advice system.

## Verification states

Clarvia uses the following verification states:

| State | Meaning |
|---|---|
| `discovered` | A source or claim has been identified but not yet structured. |
| `structured-from-source` | A fact has been extracted into structured data from a source. |
| `source-checked` | A human has checked the structured data against the source. |
| `expert-reviewed` | A qualified reviewer has reviewed the item. |
| `published` | A maintainer has approved the item for public output. |
| `stale-review` | The review is outdated or the source may have changed. |
| `superseded` | The item has been replaced or is no longer current. |

Only maintainers should mark content as `published`.

## Provenance requirements

Workflow objects should include:

- source references,
- jurisdiction,
- language,
- access date,
- verification status,
- and review metadata where applicable.

Public outputs should display:

- source citations,
- last-verified dates,
- correction pathways,
- and review or publication status where appropriate.

## Human review

Human review is required before workflow content is published.

Human review is especially important for:

- deadlines,
- administrative obligations,
- required documents,
- jurisdiction-specific branching,
- cross-border scenarios,
- and inheritance or succession-related workflow logic.

## AI use

AI systems may assist with:

- source discovery,
- metadata cleanup,
- first-pass extraction,
- translation drafts,
- issue drafting,
- documentation drafts,
- validation support,
- and changelog drafting.

AI output must be treated as draft material.

AI-generated factual content must be checked against official or authoritative sources before publication.

## Sensitive information

Clarvia does not intend to collect personal bereavement case data in phase one.

Do not add:

- identity documents,
- death certificates,
- family details,
- addresses,
- financial information,
- medical information,
- private correspondence,
- or personal case descriptions

to public repositories.

## Correction policy

If an error is found, Clarvia should:

1. identify the affected object;
2. check the relevant official source;
3. update the data or mark it as stale;
4. record the correction where appropriate;
5. rerun validation;
6. update generated outputs if needed.

Corrections should prioritize user safety, source accuracy, and transparency.
