# Phase-6 — Repository Archivist Integration Guide

Status: documentary integration (read-only role)  
Related: docs/runbooks/REPOSITORY_ARCHIVIST_RUNBOOK.md, docs/P6_RUNNER_OUTPUT_LAYOUT.md, docs/P6_EXCERPT_BINDING_RUNTIME_DESIGN.md, docs/P6_PHASE_STATUS_SNAPSHOT.md

---

## 1. Role & Scope (Read-Only)

The Repository Archivist is a **read-only** reviewer.

The Archivist:
- observes structure and traceability,
- checks cross-links and alignment between docs and artefacts,
- produces reports only.

The Archivist does **not** move files, edit content, or execute any runs.

---

## 2. When the Archivist Acts (Checkpoints)

The Archivist is used at defined Phase-6 checkpoints:

1) After new Phase-6 design docs are added or changed.  
2) When the excerpt-aware runner is implemented (design-to-implementation transition).  
3) After each excerpt-aware sandbox run.  
4) After any repo migration or navigation restructuring.

These checkpoints ensure traceability without adding autonomy.

---

## 3. What the Archivist Checks

The Archivist focuses on documentary alignment:

- excerpt metadata consistency:
  - excerpt_id / excerpt_source / excerpt_version match across docs and outputs,
  - no inference from filenames or paths.

- runner output layout:
  - logs and JSON artefacts match the frozen layout,
  - run outputs live in the expected folders.

- case-file alignment:
  - case files do not reference missing or mismatched runs,
  - pending cases are explicitly marked as pending.

- navigation integrity:
  - Phase-6 docs are discoverable from navigation/index documents,
  - links and paths reflect recent migrations.

---

## 4. What Happens With Findings

Findings are published as a neutral, documentary report under:

- docs/archivist_reports/

Reports use sequential numbering and the standard report template.

If the Archivist identifies a potential blocker, it is labeled:

- REQUIRES HUMAN REVIEW

This label is **not** an order; it is a prompt for human evaluation.

---

## 5. Relationship With Governance

The Archivist does **not** decide readiness, GO/NO-GO, or lifecycle states.

Archivist reports are inputs to:
- Human Gate review,
- Codex session planning,
- low-risk migration preparation.

Governance decisions remain human-only.

---

## 6. Example Workflow (Documentary)

1) A new excerpt-aware sandbox run is completed and logged.  
2) The Archivist performs a read-only scan of:
   - logs,
   - JSON artefacts,
   - the related case file,
   - navigation indexes.
3) The Archivist writes a report noting:
   - metadata consistency,
   - layout adherence,
   - any gaps marked as REQUIRES HUMAN REVIEW.
4) A human reviewer uses the report to decide whether to:
   - accept the run as traceable,
   - request a re-run,
   - or pause pending clarifications.

This keeps traceability strong without expanding agent autonomy.

---

End of document.
