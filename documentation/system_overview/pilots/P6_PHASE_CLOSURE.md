# Phase-6 Closure — Excerpt-Aware Editorial Workflows

## Purpose

Phase-6 had a single strategic objective:

> Build a safe, traceable path from source → provisional AI outputs → human review,  
> without ever letting AI silently shape the canonical text.

This phase was not about translation or publishing.  
It was about infrastructure, editorial discipline, and reproducibility.

---

## What Phase-6 Delivered

### 1) Excerpt-binding as a first-class principle
Every run must now declare:

- **excerpt_id**
- **excerpt_source** (governing document)
- **excerpt_version** (locked value)

Design rule:

> If excerpt metadata and content do not align → STOP, document, do not “fix quietly”.

This makes every proposal explainable later.

---

### 2) Excerpt-aware runner

Implemented entrypoint:

- accepts excerpt metadata explicitly,
- propagates it into logs + JSON outputs,
- avoids implicit assumptions about “current text”.

This was validated first on **Case-01 (SAYUR)** and then mirrored on **Case-02 (LOBAK)**.

---

### 3) Structured runner outputs (payload refinement)

Each agent output now has:

- `excerpt {…}`
- `run {…}`
- `raw_output` — full TUI stream, preserved for audit
- `payload` — parsed JSON (or `null` when parsing fails)

Design rule:

> Never retro-edit artefacts. Parsing failures are documented, not “cleaned up”.

---

### 4) Human review lane

Introduced:

- human review workflow,
- review template,
- review note stubs tied to specific runs,
- lifecycle alignment with decision stages  
  (CANDIDATE → CREW_PROVISIONAL → READY_FOR_HUMAN_REVIEW → CANONICAL).

AI proposes; humans decide — visibly.

---

### 5) Archive architecture

Defined stable locations for:

- run logs,
- JSON artefacts,
- review notes,
- canonical references.

Traceability is now structural — not ad-hoc.

---

## Phase-6 Proven (at handover time)

- excerpt-aware runner works on Case-01 (SAYUR) and Case-02 (LOBAK)
- artefacts are traceable end-to-end (CLI → logs → JSON → review → archive)
- human-review lane tested (simulation), no canonical promotion
- archive immutability validated in practice

---

## What Phase-6 Explicitly Did NOT Solve

These items are deferred by design (not failures):

- final glossary decisions,
- translations,
- canonical rewrites,
- large-scale batch processing,
- UI or publication tooling.
 - robust payload extractor (payload sometimes null),
 - generic runner-mapping conventions,
 - canonical decision trails (Phase-7 work).

All of these depend on Phase-6 foundations and belong to later phases.

---

## Case Evidence

- Case-01 (SAYUR) — demonstrated the end-to-end workflow in design and practice (happy-path).
- Case-02 (LOBAK) — tested resilience, revealed gaps, and validated fixes.
- Evidence files:
  - `docs/P6_CASE01_READINESS_PLAN.md`
  - `docs/P6_CASE01_REAL_RUN_EXECUTION_PLAN.md`
  - `docs/P6_CASE01_VALIDATION_PLAN.md`
  - `docs/P6_CASE02_READINESS_PLAN.md`
  - `docs/P6_CASE02_REAL_RUN_EXECUTION_PLAN.md`
  - `docs/P6_CASE02_VALIDATION_PLAN.md`
  - `docs/reviews/P6_REVIEW_LOBAK_CASE02_001.md`
  - `docs/pilots/P6_CASES_CONSOLIDATION.md`

Key lesson:

> Impediments are signals for design improvement, not “run failures”.

---

## Non-Negotiable Principles Going Forward

- excerpt-binding is mandatory and documentary — no silent fixes,
- AI produces proposals only (CANDIDATE / CREW_PROVISIONAL),
- every step leaves an artefact trail,
- people make canonical decisions,
- rollback = new artefacts, never overwrite,
- nothing important happens “off the books”.
ADDED: AI proposals represent the Proposal phase while humans document decisions through closures, and canonical determinations remain outside this MVP’s operational scope.


---

## Safe Next Steps (Phase-7 Direction)

- formalise canonical-decision trail,
- introduce structured human review queues,
- begin glossary decision workflows with explicit references back to excerpt + run.

ADDED: These Phase-7 intentions (canonical decision trails and structured review queues) are post-MVP work and remain outside the current system’s operational boundary.

All of this builds on Phase-6 — not beside it.

---

## Closing Note

Phase-6 proved the editorial spine of Mustikarasa:

> **We can use AI productively — without losing scholarly control.**

This phase is therefore **closed** — not because “everything is finished”,  
but because the system it needed to establish now exists, is documented, and works.
Phase-6 is CLOSED: infrastructure and traceability are proven.
Canonical decision-making intentionally remains future work (Phase-7).
