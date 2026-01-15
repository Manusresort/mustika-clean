# Phase-6 — Excerpt-Aware Practice Run (Case-01, SAYUR 052–066)

Status: PRACTICE ONLY — no real execution  
Related: P6_SAYUR_INTERNAL_WORK_CASE01.md, P6_EXCERPT_BINDING_SPEC.md,  
P6_EXCERPT_BINDING_RUNTIME_DESIGN.md, P6_EXCERPT_AWARE_RUNNER_DESIGN.md,  
P6_CASE01_READINESS_PLAN.md

---

## 1. Goal of This Practice Run

This document describes a **fictional**, excerpt-aware run for Case-01:

- it shows what CLI arguments, logs, and JSON artefacts *should* look like,
- it does not correspond to any real execution,
- it is used as a target/blueprint for future implementation.

No agents or crews were actually run for this practice run.

---

## 2. Assumed Excerpt Metadata

We assume the following locked excerpt metadata (for design purposes):

- excerpt_id: `sayur_052_066`
- excerpt_source: `docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md`
- excerpt_version: `locked-2026-01-05`

These values must match:

- the governing excerpt document,
- the internal case file (P6_SAYUR_INTERNAL_WORK_CASE01.md),
- and all runtime artefacts once a real run exists.

---

## 3. Expected CLI Invocation (Design-Only)

An excerpt-aware run for Case-01 is expected to be invoked like:

```bash
python sandbox/crew/run_excerpt_workflow.py \
  --excerpt-id sayur_052_066 \
  --excerpt-source docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md \
  --excerpt-version locked-2026-01-05 \
  --config sandbox/crew/configs/sayur_case01.yaml
```

Notes:

This command is not a record of a past run.

It is a shape example derived from the runner design.

A real execution must be logged separately once it exists.

4. Expected Runtime Log Header (Practice)
A future excerpt-aware log for Case-01 should begin with a header
containing (at minimum) the following fields:

text
Copy code
RUN_ID: RUN_P6_SAYUR_CASE01_001
TIMESTAMP: 2026-01-05T15:49:46Z
EXCERPT_ID: sayur_052_066
EXCERPT_SOURCE: docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md
EXCERPT_VERSION: locked-2026-01-05
MODE: sandbox
The exact RUN_ID and timestamp will differ in reality.
What matters is:

consistency of excerpt_id/source/version,

the fact that the log clearly identifies this run as Case-01.

5. Expected Artefact Skeletons (JSON)
These JSON examples are skeletons for a future real run.

5.1 annotator_raw.json (practice shape)
json
Copy code
{
  "excerpt_id": "sayur_052_066",
  "excerpt_source": "docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md",
  "excerpt_version": "locked-2026-01-05",
  "items": [
    {
      "line_id": "052",
      "text": "Ada sajuran jang tak tahan hudjan semasa tumbuhnja, seperti",
      "label": "HISTORICAL",
      "notes": "Seasonal framing; agriculture context."
    }
  ]
}
This is an illustrative fragment; a real run will likely contain many more items.

5.2 challenger_raw.json (practice shape)
json
Copy code
{
  "excerpt_id": "sayur_052_066",
  "excerpt_source": "docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md",
  "excerpt_version": "locked-2026-01-05",
  "issues": [
    {
      "issue_type": "GOVERNANCE",
      "severity": "WARNING",
      "span": "bajem",
      "comment": "Glossary pressure; no escalation required yet."
    }
  ]
}
Again, this is a minimal example; real issues may differ in content and count.

5.3 crew_decisions_provisional.json (practice shape)
json
Copy code
[
  {
    "term_id": "bajem@line066",
    "excerpt_id": "sayur_052_066",
    "excerpt_source": "docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md",
    "excerpt_version": "locked-2026-01-05",
    "decision_status": "CREW_PROVISIONAL",
    "decision_origin": "crew",
    "rationale": "Seasonal leafy vegetable; glossary-relevant but not escalated.",
    "ready_for_human_review": false
  }
]
Here, (term_id, excerpt_id, excerpt_version) together form a stable reference
for this decision in this specific run.

6. Validation Checklist for a Real Run
When a real Case-01 run is available, compare it against this practice design:

 CLI includes the same excerpt_id/source/version values.

 Runtime log header contains consistent excerpt metadata.

 annotator_raw.json includes the correct excerpt metadata block.

 challenger_raw.json copies the metadata unchanged.

 crew_decisions_provisional.json embeds the same metadata for all entries.

 No artefact refers to a different excerpt (e.g. Golongan VI lines 14–17).

 Human reviewer can trace from decision → JSON → log → excerpt selection.

If any box remains unchecked, the run is not considered excerpt-aware complete.

7. What This Practice Run Does NOT Do
This document:

does NOT indicate that any real run took place,

does NOT provide canonical or glossary decisions,

does NOT change readiness status for Case-01 by itself,

does NOT authorize execution — it only describes a desired shape.

Case-01 remains pending until:

a real run with excerpt-aware logs exists,

it passes the readiness plan checks,

and any issues are triaged via Human Review.

End of document.
