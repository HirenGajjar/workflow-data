# Governance for workflow-data

This repository contains Clarvia's source-backed workflow data, schemas, provenance metadata, exports, and validation logic.

The repository is maintained by CLARVIA ASBL.

Clarvia provides administrative guidance based on official sources.

It does not provide individualized legal advice.

---

## Purpose of this repository

The purpose of `workflow-data` is to maintain reusable, structured workflow data for bereavement administration.

The repository should support:

- official-source-backed administrative workflows,
- clear provenance,
- review metadata,
- deterministic exports,
- validation,
- and reuse by public web interfaces or downstream tools.

---

## Publication standard

A workflow item should not be marked as `published` unless it has:

- at least one official or authoritative source,
- jurisdiction metadata,
- language metadata,
- an access date,
- provenance information,
- verification status,
- and maintainer review.

For high-impact workflow content, maintainers may require expert review before publication.

High-impact content includes:

- deadlines,
- required administrative steps,
- legal or tax-related administrative obligations,
- cross-border branching rules,
- inheritance or succession-related workflow logic,
- and content that could materially affect a bereaved person's next action.

---

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

---

## Source requirements

Every workflow-related object should include source references where applicable.

Source-backed objects include:

- `Task`
- `Deadline`
- `DocumentRequirement`
- `Condition`
- `Workflow`
- `Scenario`

A source reference should point to a `Source` object in `data/sources`.

---

## Review model

Workflow-data changes should be made through pull requests.

Maintainers may request:

- source clarification,
- access-date correction,
- language metadata,
- evidence locator details,
- schema changes,
- translation review,
- or expert review.

Maintainers may reject or defer changes that are:

- unsourced,
- too broad,
- difficult to verify,
- outside project scope,
- or likely to require expert review before publication.

---

## AI-assisted work

Clarvia may use AI-assisted workflows for:

- source discovery,
- first-pass extraction,
- translation drafts,
- documentation drafts,
- validation support,
- and issue drafting.

AI-generated output must not be published without human review.

AI-generated factual content must be checked against official or authoritative sources before publication.

---

## Corrections

Errors should be corrected promptly.

Corrections may be handled through:

- workflow correction issues,
- pull requests,
- changelog entries,
- review-status updates,
- or published correction notes.

Content may be marked `stale-review` or `superseded` when a source changes, a review expires, or a workflow item is no longer reliable.
