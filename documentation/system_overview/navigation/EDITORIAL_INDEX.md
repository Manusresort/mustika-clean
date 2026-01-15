# Editorial Index (Phase-6)

Status: living navigation document (must be maintained over time)  
Scope: human-readable catalog of key editorial/gov/workflow docs under `docs/`  
Location: docs/navigation/EDITORIAL_INDEX.md (primary navigation index path)

This index:

- does NOT replace `DOCS_INFORMATION_ARCHITECTURE.md`, `manifest_p5.yaml`, or `CANONICAL_INDEX.md`;
- extends them with a per-document view:
  - which documents exist,
  - what they do,
  - where they live,
  - how risky they are to move.

Machine-oriented maps:
- `manifest_p5.yaml` (machine-readable categories)
- `docs/CANONICAL_INDEX.md` (canonical set)
- `docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md` (category/zone design)

---

## 1. Maintenance & Usage

- Use this index as a starting point when you need to find “which doc does what”.
- When you create a new **governance / workflow / navigation / consolidation** doc under `docs/` via Codex, add a row to this table.
- When you move or rename such a doc, update:
  - this index,
  - `MIGRATION_NOTES.md`,
  - and any obvious references.

System-generated artefacts (run logs, JSON, sandbox/workflows output) are NOT listed per file here.
Instead, they are referenced at directory level (see “Generated Artefacts” at the bottom).

This document has no normative authority over governance; it is a navigation aid only.

---

## 2. Key Documents (initial subset)

| Path                                       | Category    | Phase | Role                                                        | Authority | Risk (move) | Notes |
|--------------------------------------------|-------------|-------|-------------------------------------------------------------|-----------|-------------|-------|
| docs/WORKFLOW.md                           | governance  | P3–P6 | High-level workflow & governance flow (when to stop, gate). | binding   | high        | Source for global workflow behaviour. |
| docs/PRODUCTION_GUARDRAILS_P5.md           | governance  | P5    | Autonomy matrix & escalation rules for agents/crews.        | binding   | high        | Do not move without governance review. |
| docs/P5_DECISION_LIFECYCLE.md              | governance  | P5    | Defines lifecycle: CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL. | binding | high | Core editorial lifecycle. |
| docs/CODEX_META_PROMPT.md                  | workflow    | P3–P6 | Rules for Codex as orchestrator (how to operate on repo).   | design    | high        | Changes affect how all Codex sessions behave. |
| docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md | navigation | P3–P6 | Category/zone design: canonical vs sandbox vs consolidation vs sources. | design | medium | Already moved into docs/navigation/. |
| docs/CANONICAL_INDEX.md                    | canonical   | P3–P6 | Source-of-truth list for canonical docs.                    | canonical | high        | Aligns with manifest_p5.yaml. |
| docs/P6_EDITORIAL_WORKFLOW_MINI.md | workflow | P6 | Generic editorial mini-workflow (roles, lifecycle, sequence). | design | medium | Used across chapters; no canonical actions. |
| docs/P6_WORKFLOW_SAYUR_MINI.md | workflow | P6 | First concrete application of the mini workflow to SAYUR. | design | medium | Historical reference; do not overwrite. |
| docs/P6_EXCERPT_BINDING_SPEC.md | workflow | P6 | Defines excerpt_id/source/version metadata discipline. | design | medium | Documentary only — prevents mismatched logs. |
| docs/P6_EXCERPT_BINDING_INTEGRATION_PLAN.md | workflow | P6 | Describes how excerpt metadata flows through logs and artefacts. | design | medium | Planning layer; not runtime-enforcing. |
| docs/P6_EXCERPT_AWARE_RUNNER_DESIGN.md | workflow | P6 | Design for future excerpt-aware runner (args + logging format). | design | medium | Design only; implementation deferred. |
| **P6_HUMAN_REVIEW_WORKFLOW.md** | workflow | P6 | Human-review lane specification (CANDIDATE → CANONICAL). | Draft | medium | Documents the human-only canonisation boundary and rollback behaviour. |
| **P6_ARCHIVE_ARCHITECTURE.md** | workflow | P6 | Archive architecture (Phase-6). | Active | medium | Defines directory layout and traceability rules for runs, outputs, reviews, and canonical references. |
| docs/P6_PRODUCTION_WORKFLOW_SAYUR.md | workflow | P6 | End-to-end design from source → scholarly → editorial → canonical. | design | high | Influences long-term structure. |
| docs/P6_REPO_ARCHITECTURE_MIGRATION_PLAN.md | navigation | P6 | Plan for gradual repo re-architecture with rollback + phases. | design | high | Consult before moving anything. |
| docs/navigation/P6_MIGRATION_CANDIDATE_LIST.md | navigation | P6 | Risk-classified list of potential migration targets. | info | medium | Input to planning, not permission. |
| docs/P6_LOW_RISK_MIGRATION_CHECKLIST.md | navigation | P6 | Safe procedure for small doc moves and renames. | binding (process) | medium | Required for Phase-6 migrations. |
| docs/runbooks/REPOSITORY_ARCHIVIST_RUNBOOK.md | runbook | P6 | Playbook for Archivist: scan → report → proposals (no moves). | info | medium | Works with Index + Migration Plan. |
| docs/navigation/PILOT_LOG_OVERVIEW.md | navigation | P4–P6 | Where pilot/micropilot logs live and how to read them. | info | low | Complements sandbox documentation. |
| docs/P6_SAYUR_INTERNAL_WORK_CASE01.md | workflow/case | P6 | Concrete application of generic editorial workflow to SAYUR excerpt (pending, excerpt-aware). | provisional | high | Bound to excerpt/logs. Placement governed by P6_CASEFILE_PLACEMENT_DECISION.md. |
| docs/P6_LOBAK_INTERNAL_WORK_CASE02.md | workflow/case | P6 | Second generic workflow rehearsal (LOBAK), excerpt not yet locked. | provisional | high | Remains in docs/ for traceability. Governed by P6_CASEFILE_PLACEMENT_DECISION.md. |
| docs/decisions/P6_CASEFILE_PLACEMENT_DECISION.md | decision | P6 | Documents why case files stay in docs/ and conditions for revisiting. | design (governance note) | high (if violated) | Decision is documentary but binding for migration planning.
| docs/P6_RUNNER_OUTPUT_LAYOUT.md | workflow/runtime | P6 | Standard layout for logs and JSON outputs of future excerpt-aware runs. | design | medium | Guides implementation; does not change governance or existing logs.

You can extend this table incrementally with other key documents (Phase-4 consolidation, Phase-5 pilot reports, Phase-6 workflows, etc.).
New Phase-6 design documents are considered “complete” only after they are listed here with path, role, and risk.

> Phase-6 documents added here remain design-level unless explicitly promoted via governance.  
> This index tracks location, role and risk — it does not grant authority.

> **Case files and navigation**  
> Case files are workflow-bearing artefacts and remain in `docs/` for traceability.  
> Navigation docs may link to them, but must not attempt to reorganize them.  
> See: `docs/decisions/P6_CASEFILE_PLACEMENT_DECISION.md`.

### Phase-6 supporting references

- `docs/pilots/P6_CASE01_REFLECTION.md` → human reflection on the first excerpt-aware run (sandbox, non-decisional)
- `docs/pilots/P6_CASE02_REFLECTION.md` → human reflection on the first excerpt-aware LOBAK run (sandbox, non-decisional)
- **P6_CASES_CONSOLIDATION.md**  
  Path: docs/pilots/P6_CASES_CONSOLIDATION.md  
  Role: Consolidation note (Case-01 + Case-02) — architectural reflection  
  Phase: P6  
  Status: Final  
  Risk: Low  
  Notes: Summarises excerpt-binding, runner resilience, and payload refinement across both cases.
- Phase-6 Closure — summary of what Phase-6 proved and what was explicitly deferred  
  docs/pilots/P6_PHASE_CLOSURE.md
- `docs/templates/P6_CASE_REFLECTION_TEMPLATE.md` → reusable template for human reflections after excerpt-aware runs
- **P6_REVIEW_NOTES_TEMPLATE.md**  
  Path: docs/templates/P6_REVIEW_NOTES_TEMPLATE.md  
  Role: Template — human review notes  
  Phase: P6  
  Status: Stable  
  Risk: Low  
  Notes: Standard form for documenting human evaluation without canonising content.
- `docs/pilots/P6_LOBAK_INTERNAL_WORK_CASE02.md` → internal Case-02 working file (LOBAK; excerpt exploration and structure)
- `docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md` → Case-02 (LOBAK) — Excerpt Selection (governing); locks excerpt for Case-02, documentary only; mismatch with run artefacts must stop the workflow
- `docs/P6_CASE02_READINESS_PLAN.md` → readiness conditions for starting the first excerpt-aware sandbox run (LOBAK)
- `docs/P6_CASE02_REAL_RUN_EXECUTION_PLAN.md` → execution plan for the first excerpt-aware sandbox run (LOBAK)
- `docs/P6_CASE02_VALIDATION_PLAN.md` → validation plan for the first excerpt-aware sandbox run (LOBAK)

### Reviews (Phase-6)

- **P6_REVIEW_LOBAK_CASE02_001.md**  
  Path: docs/reviews/P6_REVIEW_LOBAK_CASE02_001.md  
  Role: Human review note (simulation)  
  Phase: P6  
  Status: Complete  
  Risk: Low  
  Notes: First end-to-end test of human-review lane. Promoted to READY_FOR_HUMAN_REVIEW, no canonisation.
- `docs/P6_LOBAK_INTERNAL_WORK_CASE02.md` → internal Case-02 working file (LOBAK; excerpt exploration and structure)
- `docs/pilots/P6_LOBAK_CASE02_EXCERPT_SELECTION.md` → Case-02 (LOBAK) — Excerpt Selection (governing); locks excerpt for Case-02, documentary only; mismatch with run artefacts must stop the workflow
- `docs/P6_CASE02_READINESS_PLAN.md` → readiness conditions for starting the first excerpt-aware sandbox run (LOBAK)
- `docs/P6_CASE02_REAL_RUN_EXECUTION_PLAN.md` → execution plan for the first excerpt-aware sandbox run (LOBAK)
- `docs/P6_CASE02_VALIDATION_PLAN.md` → validation plan for the first excerpt-aware sandbox run (LOBAK)

### Phase-4 — Analysis (Non-canonical)

- `docs/PHASE4_CROSS_CAPABILITY_STRUCTURAL_LEVERS.md` → Cross-capability analysis identifying structural levers derived from Phase-4 capability maturity gaps. (Analysis / Non-canonical, Phase-4)

### Phase-4 — Structural Levers (Implemented, Documentary)

- `docs/PROPOSAL_RECORD.md` → Minimal documentary proposal record for non-canonical observations. (Documentary, Phase-4)
- `docs/SIGNAL_GATE_CLOSURE.md` → Documentary pattern for signal, gate, and closure visibility. (Documentary, Phase-4)
- `docs/DIFF_IMPACT_REPRESENTATION.md` → Capability-agnostic description of differences and potential impact. (Documentary, Phase-4)
- `docs/CAPABILITY_RISK_TAXONOMIES.md` → Capability-specific risk naming without scoring or enforcement. (Documentary, Phase-4)
- `docs/AGENTS_AS_SENSORS.md` → Analytical positioning of agents as sensors and proposal producers. (Documentary, Phase-4)

### Phase-7 — Canonical Decision Trails

Phase-7 introduces the canonical decision-trail architecture.
AI outputs remain provisional; humans create canonical decisions
through documented decision records with full traceability.

Key documents:

- P7_DECISION_TYPES.md
- P7_CANONICAL_TRAIL_SPEC.md  
- (upcoming) pilots/P7_CANONICAL_TRAIL_REHEARSAL_PLAN.md
- **Pilot complete:** first real canonical decision recorded — *“lobak” marked as glossary lemma (itemisation only; meaning/translation pending).*  
  See CANONICAL_INDEX.md for the full decision trail.

> See also: *Human Review Participation Model*  
  (P6_HUMAN_REVIEW_WORKFLOW.md, P7_CANONICAL_TRAIL_SPEC.md)

### Phase-7 Rehearsal — Canonical Trail (NOT canonical)

Rehearsal files exist only to test the lifecycle of canonical decision records.
They are part of the pilots archive, not part of the editorial history.

Location:

- decisions/rehearsal/  (Phase-7 dry-run records)

These artefacts should never be cited as evidence in real editorial work.

### Phase-8 — Meaning Preservation (COMPLETED — REWORK ACCEPTED)

- Output-contract v2 + gate vastgesteld; FAIL-signalen blijven diagnostisch en niet-canoniek.
- Geen auto-repair toegepast; governance-keuze blijft documentair.
- Artefacten (Phase-8 / sandbox / experimental / not-for-publication):
  - docs/pilots/P8_MEANING_PRESERVATION_PILOT_001.md
  - docs/pilots/runs/P8_MEANING_PRESERVATION_PILOT_001_RUN01.md
  - sandbox/tools/phase8_output_contract_validator.sh
  - sandbox/tools/phase8_run_with_gate.sh

---

## 3. Generated Artefacts (directory-level reference)

The following paths contain **system-generated** or **run-generated** artefacts
(JSON, logs, provisional outputs). They are not indexed per file here:

- `sandbox/workflows/` — annotator/challenger/crew JSON artefacts per run.
- `sandbox/crew/run_logs/` (or equivalent) — raw run logs.
- `sandbox/phase8_runs/` — Phase-8 agent-run artefacten:
  - run context (command, env)
  - provisional outputs
  - capability evaluation files
  - output-contract validation reports
  Deze artefacten zijn evaluatief en niet-canoniek; zij ondersteunen
  Phase-8 meaning-preservation testing en governance-leren.
  Runs kunnen PASS of FAIL zijn; beide blijven niet-canoniek.
- Any other future per-run directories defined in Phase-6 runner designs.

Consult the relevant workflow design documents (e.g. P6_EDITORIAL_WORKFLOW_MINI.md,
P6_EXCERPT_BINDING_INTEGRATION_PLAN.md, P6_EXCERPT_AWARE_RUNNER_DESIGN.md) for
details on how these artefacts are produced and used.

---

End of document.
