# Phase-6 Archive Architecture (Runs, Artefacts, Reviews)

## 1. Purpose

This document explains how Phase-6 artefacts are laid out on disk and
how they relate to each other over time. It focuses on:

- excerpt-aware crew runs
- JSON outputs (annotator / challenger / crew)
- human review notes
- reflections and consolidation docs
- canonical index entries (later phases)

The goal is to make it possible to reconstruct editorial decisions
from archived files, without guessing or reverse-engineering ad hoc paths.

---

## 2. High-level structure

At Phase-6, the relevant zones are:

- `sandbox/crew/run_logs/`          → per-excerpt run logs
- `sandbox/crew/run_outputs/`       → per-excerpt JSON artefacts
- `docs/pilots/`                    → reflections and consolidation notes for cases
- `docs/reviews/`                   → human review notes (per artefact)
- `CANONICAL_INDEX.md`              → canonical editorial entries (later, human-only)
- `docs/navigation/EDITORIAL_INDEX.md`              → navigation layer tying these together

Each zone has a defined role and is not interchangeable.

---

## 3. Run logs (per excerpt)

Path pattern:

- `sandbox/crew/run_logs/{excerpt_id}/RUN_{excerpt_id}_{timestamp}_{timestamp}.log`

Example (LOBAK Case-02):

- `sandbox/crew/run_logs/lobak_034_048/RUN_lobak_034_048_20260106T220558_20260106T220558.log`

Properties:

- header records excerpt metadata:
  - `excerpt_id`
  - `excerpt_source`
  - `excerpt_version`
- header records run metadata:
  - `run_id`
  - `started_at`
  - `status` (PENDING / ERROR / etc.)
- pipeline output section contains:
  - crew TUI
  - warnings (e.g. JSON parse warnings)
  - traceback if any

Logs are append-only artefacts. They MUST NOT be rewritten to “hide”
earlier failure states. New runs create new log files.

---

## 4. Run outputs (per excerpt, per run)

Path pattern:

- `sandbox/crew/run_outputs/{excerpt_id}/{run_id}/`

Example:

- `sandbox/crew/run_outputs/lobak_034_048/RUN_lobak_034_048_20260106T220558/`

Within each run output directory we expect JSON files such as:

- `annotator_primary.json`
- `challenger_primary.json`
- optionally: `crew_provisional.json`, `run_metadata.json`, etc.

Each JSON file follows the Phase-6 runner output contract:

```json
{
  "excerpt": {
    "id": "...",
    "source": "...",
    "version": "..."
  },
  "run": {
    "id": "...",
    "timestamp": "..."
  },
  "raw_output": "<full TUI / console trace as string>",
  "payload": null or "<structured JSON value>"
}
```

Notes:

raw_output is the full mixed output including TUI frames.

payload holds structured JSON if the runner can safely extract it;
otherwise it is null and a warning is written in the log.

This layout is forward-only: we can evolve parsing strategies
without changing historical files.

## 5. Reflections and consolidation docs
Path patterns:

docs/pilots/P6_CASE01_REFLECTION.md

docs/pilots/P6_CASE02_REFLECTION.md

docs/pilots/P6_CASES_CONSOLIDATION.md

Role:

capture human perspective on agent behaviour, bias signals,
workflow experience, and design implications.

do NOT act as canonical decision logs.

may reference multiple runs and artefacts by path.

These documents help future maintainers understand why certain design
choices were made, without being part of the canonical textual edition.

6. Human review notes
Path pattern:

docs/reviews/P6_REVIEW_<CASE>_<ID>.md

Example:

docs/reviews/P6_REVIEW_LOBAK_CASE02_001.md

Each review note:

references exactly one primary artefact (JSON file)

includes excerpt metadata and run id

states lifecycle state at review time

records a human assessment and issues noticed

records a target lifecycle state when promoting (e.g. READY_FOR_HUMAN_REVIEW)

Review notes are append-only: new assessments create new notes,
they do not overwrite earlier reviews.

7. Linking the chain
A typical chain from run to potential canonical decision looks like:

Run log:

sandbox/crew/run_logs/{excerpt_id}/{run_id}_{timestamp}.log

Run outputs:

sandbox/crew/run_outputs/{excerpt_id}/{run_id}/annotator_primary.json

sandbox/crew/run_outputs/{excerpt_id}/{run_id}/challenger_primary.json

Review note:

docs/reviews/P6_REVIEW_<CASE>_<ID>.md

links back to JSON and excerpt metadata

Canonical index entry (later phase):

CANONICAL_INDEX.md entry referencing:

excerpt_id / source / version

path to review note

path to original JSON artefact

short human-written justification

This chain is unidirectional (from runs towards canonical) but traceable
in reverse (from canonical back to runs).

8. Immutability and rollback
Phase-6 archive rules:

Run logs and JSON outputs are immutable once written.

Review notes are immutable records of a point-in-time assessment.

Rollback is performed by:

adding new runs

adding new review notes

updating indices to reference newer material

We do NOT delete or rewrite history to “tidy up” failed runs or
unwanted outputs. Instead, we document and supersede.

9. Interaction with EDITORIAL_INDEX and CANONICAL_INDEX
docs/navigation/EDITORIAL_INDEX.md lists all relevant docs by path and role:

cases, reflections, workflow specs, templates, reviews.

CANONICAL_INDEX.md is reserved for human-approved,
canonical editorial entries (later phases).

The archive architecture ensures that for every canonical entry
there is a clear trail back to:

the governing excerpt

the crew run(s)

the review note(s)

any design reflections that informed the decision

10. Next steps
Ensure new cases and runs follow the same path conventions.

Extend documentation if additional artefact types are introduced
(e.g. crew_provisional.json, run_metadata.json).

Use this architecture as a reference when designing future phases
and migration plans.

End of document.
