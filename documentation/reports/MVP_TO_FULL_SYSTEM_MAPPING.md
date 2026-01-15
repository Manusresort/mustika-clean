# MVP → Full System Mapping (Mustika Rasa)

This document maps the current MVP to the capabilities required for a full
end-to-end Mustika Rasa book translation workflow. It is based on the current
MVP as documented under `documentation/system_overview/` and the architecture
sources in `documentation/architecture_sources/`.

Constraints (carry forward):
- Filesystem-first
- Human-in-the-loop
- Immutable runs and closures
- No auto-promotion
- Canonical read-only

---

## What “full system” means (capabilities)

A full system is a repeatable, book-level workflow that can:

1) Ingest book source material
- Import chapters and metadata with traceable provenance.

2) Segment and manage text units
- Maintain stable excerpt/chapter alignment with line ranges.
- Track versions of excerpts and their locks.

3) Execute runs at scale
- Batch runs per chapter/excerpt with consistent run bundle layouts.

4) Produce review packs and editorial decisions
- Provide structured review material per excerpt/batch.
- Record proposals and closures with immutable trails.

5) Govern decisions and publication
- Gate decisions through human review.
- Ensure canonical publication remains explicit and manual.

6) Expose the workflow in UI
- Dashboard, inbox, run detail, and review UX for batch work.

7) Operate reliably
- Reindexing, logs, reproducibility, and backups.

---

## Gap analysis (by domain)

### A) Content pipeline (ingest, segment, excerpt management)
Missing or partial components:
- Chapter ingestion pipeline with provenance metadata.
- Stable excerpt registry with versioning and locks across the full book.
- Alignment between source chapters and excerpt IDs at scale.

### B) Editorial workflow (review packs, approvals, closures)
Missing or partial components:
- Batch review packs for chapter-level runs.
- Explicit review queues for multi-excerpt work (beyond single-run review).
- Closure lifecycle coverage at scale (batch closure management).

### C) Quality / validation
Missing or partial components:
- Regression checks across run outputs over time.
- Additional validators beyond output-contract checks.
- Validation coverage for excerpt completeness and chapter coverage.

### D) UI/UX
Missing or partial components:
- Book/chapter workflow screens (progress, coverage, gaps).
- Diff/compare view for run iterations and edits.
- Batch review UI with triage and filtering at book scale.

### E) Ops
Missing or partial components:
- Explicit backup/restore procedure documented (DONE: documentation/operator/BACKUP_AND_RESTORE_RUNTIME.md; evidence: runtime/audit/index_regression_report_latest.md; runtime/audit/api_actions.log).
- Standardized run logs collection across batch runs.
- Operational runbook for multi-day batch processing.

---

## Notes on constraints and decisions

- Editorial domain rules (translation choices, cultural interpretation) are
  intentionally not specified here. Those decisions remain editorial and
  should be defined via governance documents, not in this mapping.
- Canonical publication is out of scope for MVP; a full system still keeps
  human gating and explicit acceptance without auto-promotion.
