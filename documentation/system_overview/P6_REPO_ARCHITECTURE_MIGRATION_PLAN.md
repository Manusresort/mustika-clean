# Phase-6 — Repo Architecture Migration Plan (SAYUR)

This document describes how the repository should gradually evolve
to reflect the production workflow described in P6_PRODUCTION_WORKFLOW_SAYUR.md.

It is a planning document only — no files are moved by this plan.

---

## 1. Goals

- Align directories with lifecycle stages.
- Preserve provenance and reversibility.
- Avoid premature cleanup that hides useful evidence.
- Require Human Gate review when materials cross lifecycle boundaries.

---

## 2. Target Zones

### 2.1 /sources
Read-only ingestion outputs (scans, OCR, manifests).

### 2.2 /scholarly
Normalized scholarly editions with change logs.

### 2.3 /sandbox
Provisional experimentation (agents, pilots, logs, runners).

### 2.4 /editorial
Human Gate deliberation artefacts and decision logs.

### 2.5 /canonical
Approved text, commentary, and references.

### 2.6 /public
Publication-ready translations and front-matter.

Each zone maps to a lifecycle boundary.

---

## 3. Mapping Table (workflow → repo)

Source ingest → /sources  
Scholarly editing → /scholarly  
Annotation / Challenger / Crew → /sandbox/workflows  
Human review → /editorial/decisions  
Canonicalization → /canonical  
Translation → /public/translation

Rollback may move artefacts backward logically,
but history is kept in version control.

---

## 4. Movement Rules

- Moving from sandbox → editorial requires justification log.
- Moving from editorial → canonical requires Human Gate entry.
- Moving from canonical → public requires editorial readiness notes.
- Sandbox never deletes logs; archival only.

Repo movement follows lifecycle, not convenience.

---

## 5. Migration Phasing

Phase A — Document current reality (no moves).  
Phase B — Create empty target folders with README markers.  
Phase C — Move a limited set of artefacts with audit notes.  
Phase D — Broader migration once patterns are validated.

Each step must have rollback instructions.

---

## 6. Risks & Safeguards

- Risk: losing provenance → Mitigation: do not delete originals.  
- Risk: re-organizing too soon → Mitigation: migration phases.  
- Risk: unclear ownership → Mitigation: Human Gate checkpoints.

---

## 7. Next Actions (documentary)

1) Review this plan against P6_PRODUCTION_WORKFLOW_SAYUR.md  
2) Identify the first low-risk candidates for migration  
3) Draft migration checklists per directory

Execution happens only after explicit approval.

End of plan.
