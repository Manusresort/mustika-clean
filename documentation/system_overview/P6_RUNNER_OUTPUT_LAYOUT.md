# Phase-6 — Runner Output Layout (Excerpt-Aware Runs)

Status: READY_FOR_IMPLEMENTATION — documentary, non-enforcing  
Related: P6_EXCERPT_BINDING_SPEC.md, P6_EXCERPT_AWARE_RUNNER_DESIGN.md,  
P6_EXCERPT_BINDING_RUNTIME_DESIGN.md, P6_CASE01_REAL_RUN_EXECUTION_PLAN.md

---

## 1. Purpose

This document defines a **standard home** for excerpt-aware runner outputs:

- where logs will live,
- where annotator/challenger/crew JSON artefacts will live,
- how runs for different excerpts and reruns for the same excerpt are separated,
- how rollback and comparison are made possible.

It is **design-only** and does not change runtime behavior by itself.  
Existing logs are not retrofitted; this layout applies to future excerpt-aware runs.

---

## 2. Concepts and Naming

We assume the following conceptual identifiers:

- `excerpt_id` — e.g. `sayur_052_066`, `lobak_0XX_0YY`
- `run_id` — a stable identifier per run, e.g. `RUN_SAYUR_CASE01_001`
- `run_timestamp` — ISO-like timestamp, e.g. `2026-01-05T15-49-46Z`

New excerpt-aware runs should:

- always record `excerpt_id` in filenames or directory paths,
- always record `run_id` and/or `run_timestamp` for uniqueness,
- avoid overloading legacy naming conventions.

---

## 3. Top-Level Locations

Phase-6 distinguishes between:

1. **Runtime logs** — under `sandbox/crew/run_logs/`
2. **Structured outputs (JSON)** — under a dedicated run output root, e.g.:

   `sandbox/crew/run_outputs/`

This document does not require immediate creation of these directories,  
but defines where a future excerpt-aware runner should write.

---

## Design contract (Phase-6)

- never overwrite: each run gets a new run_id (and timestamp)
- no retro-patching of past runs
- supersede instead of mutate (new run replaces old for review)
- excerpt_id must match the runtime propagation contract

---

## 4. Log Layout (Design)

For excerpt-aware runs, logs SHOULD follow this pattern:

- Base directory:

  `sandbox/crew/run_logs/{excerpt_id}/`

- Preferred filename pattern:

  `{run_id}_{timestamp}.log`

Example:

- `sandbox/crew/run_logs/sayur_052_066/RUN_SAYUR_CASE01_001_20260105T154946.log`

Requirements:

- `excerpt_id` must be visible in the filename,
- `run_id` may encode chapter/case (e.g. `SAYUR_CASE01`),
- timestamp can mirror existing practice.

Existing Phase-4/5 logs remain unchanged; this pattern applies to future excerpt-aware runs.

---

## 5. JSON Artefact Layout (Design)

JSON artefacts for a single run SHOULD live under a dedicated run root, e.g.:

- Run root:

  `sandbox/crew/run_outputs/{excerpt_id}/{run_id}/`

Within that directory, Phase-6 expects at minimum:

- `annotator_*.json`
- `challenger_*.json`
- `crew_provisional.json`
- `review_notes.md`
- `run_metadata.json` (optional but recommended)

Example structure:

```text
sandbox/crew/run_outputs/
  sayur_052_066/
    RUN_SAYUR_CASE01_001/
      annotator_raw.json
      challenger_raw.json
      crew_provisional.json
      review_notes.md
      run_metadata.json
```

Rules:

All files in a run root MUST refer to the same excerpt_id.

run_metadata.json (if present) MUST repeat excerpt_id/source/version
so it can be cross-checked against logs and artefacts.

6. Metadata Requirements Inside JSON
Each JSON artefact SHOULD include:

json
Copy code
{
  "excerpt_id": "…",
  "excerpt_source": "…",
  "excerpt_version": "…",
  "…": "other fields"
}
Consistency rules:

Values MUST match the locked excerpt selection document.

annotator/challenger/crew files MUST carry identical excerpt metadata.

If metadata differs between files, the run is considered misaligned and
must not be trusted without Human Review.

This mirrors P6_EXCERPT_BINDING_RUNTIME_DESIGN.md but adds a concrete file layout.

## Example tree (sample run)

```text
sandbox/crew/run_logs/
  sayur_052_066/
    RUN_SAYUR_CASE01_001_20260105T154946.log

sandbox/crew/run_outputs/
  sayur_052_066/
    RUN_SAYUR_CASE01_001/
      annotator_raw.json
      challenger_raw.json
      crew_provisional.json
      review_notes.md
      run_metadata.json
```

7. Multiple Runs for the Same Excerpt
Multiple runs for the same excerpt are handled by distinct run_id (and/or timestamps):

text
Copy code
sandbox/crew/run_outputs/sayur_052_066/RUN_SAYUR_CASE01_001/…
sandbox/crew/run_outputs/sayur_052_066/RUN_SAYUR_CASE01_002/…
Rollback and comparison:

rollback does NOT delete old runs,

instead, a newer run is marked as the current one in human-facing documentation
(e.g. in evaluation or review notes),

old runs remain available for audit and comparison.

8. Rollback Expectations
Rollback for excerpt-aware runs means:

restoring the last coherent run root:

logs,

JSON artefacts,

and metadata that agree on excerpt_id/source/version.

It explicitly does NOT mean:

retroactively editing files inside an old run root,

silently patching JSON to match a different excerpt.

If a run is found to be misaligned, it should be:

documented,

left intact,

superseded by a new, correct run.

9. Governance and Boundaries
This layout:

does NOT give any agent more autonomy,

does NOT change lifecycle rules,

does NOT decide what is canonical.

It only ensures that:

when a future excerpt-aware runner is implemented,

its outputs already have a predictable, governed location.

If implementation deviates from this layout, a Phase-6 design update is required.

End of document.
