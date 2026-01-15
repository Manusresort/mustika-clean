# Archivist Report — Phase-6 Navigation Grouping Candidates

[ARCHIVIST_REPORT]
Scope:
  Identify Phase-6 documents in docs/ that may be better grouped under docs/navigation/
  as navigation/overview/design references, without moving anything yet.

Findings:
  - Phase-6 docs in docs/ root include both navigation/design plans and workflow/case artefacts.
  - Navigation/design/overview candidates: migration plan, migration candidate list, production workflow overview, excerpt-binding spec/plan/runner design.
  - Workflow/case artefacts: internal case files (SAYUR Case-01, LOBAK Case-02) should remain outside navigation for now.
  - Ambiguous cases: production workflow and repo migration plan are design-level but influence long-term structure; moving them is feasible but should be deliberate and logged.

CandidatesTable:

| Path | Why navigation-like? | Current role | Risk if moved | Notes |
|------|----------------------|--------------|---------------|-------|
| docs/P6_REPO_ARCHITECTURE_MIGRATION_PLAN.md | repo layout plan, overview map | navigation/design plan | medium | Design doc; moving needs link updates + migration log. |
| docs/navigation/P6_MIGRATION_CANDIDATE_LIST.md | catalog of migration candidates | navigation/assessment | low | List-only; low risk to move. |
| docs/P6_PRODUCTION_WORKFLOW_SAYUR.md | end-to-end workflow overview | workflow design | medium | Design-level; not canonical, but referenced widely. |
| docs/P6_EXCERPT_BINDING_SPEC.md | policy-style spec for traceability | workflow design | medium | Spec doc; move only with link updates. |
| docs/P6_EXCERPT_BINDING_INTEGRATION_PLAN.md | integration map for metadata | workflow design | medium | Plan doc; move only with links updated. |
| docs/P6_EXCERPT_AWARE_RUNNER_DESIGN.md | runner design overview | workflow design | medium | Design doc; safe if links updated. |

NonCandidates (explicitly keep in place):
  - docs/P6_SAYUR_INTERNAL_WORK_CASE01.md — case file with workflow artefact paths; keep outside navigation to avoid confusion with design docs.
  - docs/P6_LOBAK_INTERNAL_WORK_CASE02.md — case file with placeholders; keep outside navigation until excerpt is chosen and case is active.

Risks:
  - Moving design/navigation-like Phase-6 docs is low to medium risk: links and references must be updated, and migration notes logged.
  - Case files are medium to high risk to move because they are workflow-bearing artefacts and can affect traceability if relocated.
  - Any move must follow P6_LOW_RISK_MIGRATION_CHECKLIST.md and be logged in MIGRATION_NOTES.md.

ProposedTasks:
  - id: PHASE6_NAV_GROUPING_LOW_RISK_MOVE_PLAN
    description: For each candidate listed in CandidatesTable, design a low-risk migration plan (per-doc), including updated references and rollback instructions, to be executed in a later Codex session.
    impact: improves navigation clarity; low to medium risk; requires P6_LOW_RISK_MIGRATION_CHECKLIST.md and MIGRATION_NOTES.md entries.
    suggested_phase: P6

  - id: PHASE6_NAV_GROUPING_DECISION_LOG
    description: Document a short decision for ambiguous Phase-6 docs (especially case files) on whether they stay in docs/ or ever move, and update docs/navigation/EDITORIAL_INDEX.md accordingly.
    impact: makes placement explicit and traceable; medium risk if moves are later approved.
    suggested_phase: P6

Notes:
  This report is advisory only. No files were moved, renamed, or deleted.
[/ARCHIVIST_REPORT]
