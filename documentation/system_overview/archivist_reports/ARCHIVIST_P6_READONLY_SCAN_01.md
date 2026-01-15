[ARCHIVIST_REPORT]
Scope:
  Phase-6 oriented scan of docs/ and docs/navigation/.
  Goal: detect navigation gaps, overlaps, misplaced docs (proposal-only).

Findings:
  - docs/navigation/EDITORIAL_INDEX.md exists but only lists a small subset; multiple Phase-6 workflow/spec docs live in docs/ and are not yet indexed (e.g., P6_EXCERPT_BINDING_SPEC.md, P6_EXCERPT_BINDING_INTEGRATION_PLAN.md, P6_EXCERPT_AWARE_RUNNER_DESIGN.md, P6_EDITORIAL_WORKFLOW_MINI.md).
  - docs/P6_REPO_ARCHITECTURE_MIGRATION_PLAN.md is still in docs/ root while other navigation/design docs are under docs/navigation/; candidate for navigation grouping (low-risk, documentary).
  - Phase-6 case files (docs/P6_SAYUR_INTERNAL_WORK_CASE01.md, docs/P6_LOBAK_INTERNAL_WORK_CASE02.md) live in docs/ root; unclear whether these should be grouped under docs/navigation/ or remain in docs/ (needs decision).
  - docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md provides category map but does not reflect the newer docs/navigation/ moves in its own examples consistently; potential follow-up to ensure navigation docs point to docs/navigation/ paths.
  - docs/manifest_p5.yaml and docs/CANONICAL_INDEX.md both provide canonical lists; EDITORIAL_INDEX could explicitly link to both to reduce redundancy.

Risks:
  - Moving Phase-6 workflow/spec docs from docs/ to docs/navigation/ is low to medium risk due to link updates; requires checklist and migration log.
  - Case files are medium risk because they are workflow-bearing; moving them could confuse lifecycle ownership and traceability.
  - Updating DOCS_INFORMATION_ARCHITECTURE.md references is low risk but must avoid rewriting historical notes.

ProposedTasks:
  - id: PHASE6_NAV_GROUPING_CANDIDATES
    description: Identify specific Phase-6 docs that may belong in docs/navigation/ but currently live in docs/.
    suggested_phase: P6
    impact: improves discoverability, low risk, requires logging + checklist.

  - id: PHASE6_INDEX_EXPANSION_PASS
    description: Expand EDITORIAL_INDEX.md with missing key Phase-6 workflow/governance docs.
    suggested_phase: P6
    impact: navigation clarity, zero runtime risk.

  - id: PHASE6_CASEFILE_PLACEMENT_DECISION
    description: Decide whether Phase-6 case files should remain in docs/ or be grouped under docs/navigation/; document the decision and update indexes accordingly.
    suggested_phase: P6
    impact: medium risk; affects traceability if moved, requires governance-aligned logging.

  - id: PHASE6_NAV_LINK_CONSISTENCY_PASS
    description: Review navigation docs for lingering references to pre-move paths and update where safe.
    suggested_phase: P6
    impact: low risk; improves consistency after navigation moves.

Notes:
  This scan is advisory only. No moves or structural changes were performed.
[/ARCHIVIST_REPORT]
