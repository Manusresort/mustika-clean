# Phase-8 Capability Map — Editorial System Maturity

## 1. Purpose

Phase-8 designs capabilities first; agent roles are derived from those
capabilities, not the other way around. Governance remains unchanged:
canonical decisions are human-only, and rollback occurs via new records.

## 2. Capability Families

### 2.1 Text Acquisition & Integrity

- Good looks like: excerpt binding is consistent; OCR anomalies are flagged; missing sections are detected.
- What can go wrong: mismatched excerpt metadata, silent OCR drift, missing lines.
- Relation to canonical decisions: supports trustworthy evidence for later human decisions.

### 2.2 Structure & Navigation

- Good looks like: stable sectioning, consistent lists/tables, and traceable placement of artefacts.
- What can go wrong: misplaced sections, inconsistent headings, navigation drift.
- Relation to canonical decisions: keeps context stable for review, not a canonical decision itself.

### 2.3 Glossary & Knowledge Management

- Good looks like: lemma detection and variant tracking with provenance; research context linked.
- What can go wrong: meaning decisions slip in, or terms are promoted without review.
- Relation to canonical decisions: supports lemma inclusion decisions; meanings remain human-only.

### 2.4 Text-Critical / Variants

- Good looks like: variants are collected and exposed with uncertainty and evidence links.
- What can go wrong: hidden normalization, untracked variant choices.
- Relation to canonical decisions: provides evidence bundles for human variant choices.

### 2.5 Editorial Quality & Readability

- Good looks like: cohesive, stable editorial notes and anomaly flags (advisory only).
- What can go wrong: stylistic changes treated as authoritative edits.
- Relation to canonical decisions: advisory signals only; not a decision lane.

### 2.6 Trail & Reproducibility

- Good looks like: run → artefact → decision linkage is complete and verifiable.
- What can go wrong: missing artefact links, incomplete decision records.
- Relation to canonical decisions: required mechanical integrity before human gate.

### 2.7 Reviewer Support & Triage

- Good looks like: review-ready dossiers, risk tagging, and batch grouping.
- What can go wrong: overloaded reviewers, unclear escalation paths.
- Relation to canonical decisions: accelerates review without changing authority.

## 3. Maturity Model

- Level 0 — ad-hoc
- Level 1 — documented workflow
- Level 2 — agent-supported (provisional signals)
- Level 3 — tool/validator assisted (mechanical certainty)
- Level 4 — orchestration-aware collaboration (still human-only canonical)

Phase-8 typically aims for Level 2 → 3.

## 4. Capability × Maturity × Responsibility Matrix

| Capability | Current Maturity (estimate) | Phase-8 Target | Responsibility Model |
|-----------|-----------------------------|----------------|----------------------|
| Text Acquisition & Integrity | Level 1 | Level 3 | TOOL/VALIDATOR |
| Structure & Navigation | Level 1 | Level 2 | AGENT-SUPPORTED (provisional) |
| Glossary & Knowledge Management | Level 2 | Level 3 | HUMAN ONLY / AGENT-SUPPORTED (provisional) |
| Text-Critical / Variants | Level 1 | Level 2 | HUMAN ONLY |
| Editorial Quality & Readability | Level 1 | Level 2 | AGENT-SUPPORTED (provisional) |
| Trail & Reproducibility | Level 2 | Level 3 | TOOL/VALIDATOR |
| Reviewer Support & Triage | Level 1 | Level 3 | AGENT-SUPPORTED (provisional) |

## 5. Derived Role Implications (No Roles Yet)

- Text Acquisition & Integrity:
  - Possible roles: excerpt checker, OCR anomaly flagger.
  - Must NEVER: alter sources or override excerpt binding.
  - Phase-8 priority: validator-style checks before review.

- Structure & Navigation:
  - Possible roles: structure consistency reviewer, list/table checker.
  - Must NEVER: reorganize canonical content or declare canonical structure.
  - Phase-8 priority: provisional diagnostics only.

- Glossary & Knowledge Management:
  - Possible roles: lemma detector, variant tracker, research linker.
  - Must NEVER: assign meanings or promote canonically.
  - Phase-8 priority: clean lemma signals + provenance.

- Text-Critical / Variants:
  - Possible roles: variant collector, uncertainty bundler.
  - Must NEVER: choose a variant or decide canonical readings.
  - Phase-8 priority: evidence bundling for human review.

- Editorial Quality & Readability:
  - Possible roles: consistency checker, anomaly signaler.
  - Must NEVER: rewrite text or imply final editorial authority.
  - Phase-8 priority: advisory-only signals.

- Trail & Reproducibility:
  - Possible roles: trail preflight checker, linkage auditor.
  - Must NEVER: mark CANONICAL or modify records.
  - Phase-8 priority: mechanical completeness checks.

- Reviewer Support & Triage:
  - Possible roles: dossier builder, risk tagger, batch grouper.
  - Must NEVER: summarize as if a decision was made.
  - Phase-8 priority: reduce reviewer overhead without changing authority.

## 6. Alignment with Guardrails

- Canonical trail remains untouched.
- Agents only annotate, signal, cluster, and assemble dossiers.
- Validators help but do not gatekeep canonical promotion.
- Rollback always via new records, never overwrites.

## 7. Next Step from Capability Map

This map becomes the input for:

- P8_AGENT_ROLES_AND_PROMPTS.md
- orchestration patterns
- validation tooling

Capabilities drive roles, not the other way around.

---

- author: HumanGate-Editorial + Architecture
- date: 2026-01-07
- references:
  - docs/P8_PHASE_START_ARCHITECTURE.md
  - docs/P7_CANONICAL_TRAIL_SPEC.md
  - docs/P7_DECISION_TYPES.md
  - docs/AGENTS.md
