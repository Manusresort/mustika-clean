# Phase-6 — Production-oriented Workflow (SAYUR)

This document describes the end-to-end editorial workflow for the SAYUR material,
from historical source → scholarly edition → provisional reasoning → Human Gate → canonical editorial decisions,
with translation/publication as a later, governed stage.

It formalizes behaviour already observed in pilots,
but frames it for real editorial use (without changing runtime).

---

## 1. Principles

- Source is never overwritten. Every editorial layer is additive.
- Agents reason provisionally; humans make canonical decisions.
- Every transition produces an artefact that can be cited.
- Any step must be reversible (rollback possible).
- Human Gate sits between *provisional* and *canonical*.
- Translation comes only after canonical editorial work.

---

## 2. Major Stages

### 2.1 Source Ingest (read-only)
Input: scans, OCR text, import manifests  
Output: source files with provenance headers  
Rules: no edits; fixes are documented as proposals only.

### 2.2 Scholarly Edition Layer
Input: source text  
Output: lightly normalized scholarly text (structure, pagination markers, minimal corrections)  
Rules:
- corrections are logged with justification
- nothing becomes canonical without Human Gate approval
- source remains available for comparison

### 2.3 Annotation (Agents)
Input: scholarly edition excerpt  
Output: annotation candidates with labels (HISTORICAL, GLOSSARY, OCR, etc.)  
Lifecycle: CANDIDATE → CREW_PROVISIONAL  
Notes: agents describe, they do not decide.

### 2.4 Challenger Review (Agents)
Input: annotation candidates  
Output: challenge notes (risk, bias, governance concerns)  
Lifecycle: still provisional  
Notes: warnings are signals, not vetoes.

### 2.5 Crew Synthesis
Input: annotator + challenger outputs  
Output: crew_decisions_provisional.json  
Lifecycle fields:
- decision_status (CANDIDATE | CREW_PROVISIONAL | READY_FOR_HUMAN_REVIEW)
- decision_origin (agent/crew/human)
- rationale
Notes: READY_FOR_HUMAN_REVIEW marks items that require human judgement.

### 2.6 Human Gate (Editorial)
Input: items marked READY_FOR_HUMAN_REVIEW  
Output: canonical editorial decisions  
Lifecycle: CANONICAL  
Rules:
- every decision links back to evidence (source + logs)
- disagreements are logged, not hidden
- rollback path is always documented

### 2.7 Translation & Publication (later stage)
Input: canonical editorial text + glossary + commentary  
Output: public translation + notes  
Rules:
- translation follows canonical editorial layer, never leads it
- culturally sensitive decisions must trace back to Human Gate notes

---

## 3. Artefact Map (what exists after each stage)

- /sources/... (immutable inputs)
- /scholarly/... (normalized text, with change logs)
- /sandbox/workflows/... (provisional agent + crew artefacts)
- /editorial/decisions/... (Human Gate outputs)
- /canonical/... (approved text + notes)
- /public/translation/... (later)

Each directory is governed; movement across them reflects lifecycle transitions.

---

## 4. Logging & Traceability Requirements

Every decisionable item must be able to show:

- excerpt_id / excerpt_version  
- original span  
- who proposed what (agent vs crew vs human)  
- rationale text  
- lifecycle status  
- links to logs and evidence

Bias patterns (like translation-expectation) are recorded as signals.

---

## 5. Rollback Patterns

- rollback to previous lifecycle state is always allowed
- rollback never deletes history
- any rollback gets a short explanation entry (who/why/when)

Rollback is a governance action, not an agent one.

---

## 6. Boundaries of Autonomy

Agents may:
- annotate
- flag risk
- suggest interpretation (provisionally)

Agents may NOT:
- finalize glossary entries
- override human editorial judgement
- publish or rewrite canonical text
- change lifecycle beyond CREW_PROVISIONAL

---

## 7. Hand-offs and Checkpoints

- Agent Crew → Human Gate (mandatory checkpoint)
- Human Gate → Canonical (requires justification entry)
- Canonical → Translation (requires editorial readiness note)

Every checkpoint produces a file and a short log entry.

---

## 8. Phase-6 Implementation Strategy

This document is normative for design,
but execution remains incremental:

1) align pilots and future runs with this structure
2) adapt repo layout to match stages
3) only then consider cleanup/migration
4) translation remains deferred until canonical material stabilizes

---

End of document.
