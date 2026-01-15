# Phase-6 — Excerpt Binding Runtime Design (Documentary)

Status: DESIGN — non-enforcing  
Related: P6_EXCERPT_BINDING_SPEC.md, P6_EXCERPT_AWARE_RUNNER_DESIGN.md, P6_EDITORIAL_WORKFLOW_MINI.md

---

## 1. Purpose

Excerpt binding exists to keep runs traceable, reproducible, and reversible across Phase-6 workflows.
It provides a clear link between the excerpt that was intended and the artefacts that were produced.
This is documentary first: it makes mismatches visible rather than silently corrected.
The goal is to prevent logs and decisions from drifting away from the source excerpt without notice.
Excerpt metadata is recorded so that rollback can restore the last coherent trio of excerpt + logs + artefacts.
No agent gains additional autonomy from these fields; they are informational only.

> “Excerpt metadata does not create runtime authority. Human review remains decisive.”

---

## 2. Required Metadata (recap)

- `excerpt_id` — stable identifier for the excerpt instance used in a run.
- `excerpt_source` — governing document or location that defines the excerpt text.
- `excerpt_version` — locked tag indicating which excerpt snapshot was used.

> “If one of these is missing, the run is allowed in sandbox — but it must be marked INCOMPLETE for evaluation purposes.”

---

## 3. CLI / Runner Contract

The runner accepts excerpt metadata via flags or config keys.
All three fields are optional in early Phase-6, but when provided they MUST be copied unchanged into logs.
If only some are provided, the run should be flagged as incomplete in evaluation notes.
Example (pseudocode only — NOT executable):

--excerpt-id sayur_052_066
--excerpt-source docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md
--excerpt-version locked-2026-01-05

> “The runner must never infer excerpt metadata from filenames.”

---

## 4. Logging Format (runtime logs)

A Phase-6 log should contain at minimum:

```json
{
  "run_metadata": {
    "excerpt_id": "...",
    "excerpt_source": "...",
    "excerpt_version": "...",
    "timestamp": "...",
    "runner_config": "reference only"
  }
}
```

Logs may add fields, but removing or renaming excerpt fields is not allowed without a design change.

5. Crew Artefacts (annotator/challenger/crew)

Excerpt metadata propagates as follows:

annotator_raw.json → includes excerpt block,

challenger_raw.json → copies it unchanged,

crew_decisions_provisional.json → embeds the same values.

If metadata differs between artefacts, mark the run for Human Review triage before any synthesis is trusted.

6. Human Gate & Review Notes

Reviewers check alignment between excerpt, logs, and artefacts.
They may override interpretations, but must not silently “fix” excerpt metadata.

“Corrections must be documented and produce a new run, not silently patched.”

7. Archive & Rollback

Excerpt metadata is the linking key that ties runs back to source text and workflow context.
It supports reconstruction of: which excerpt, which workflow design, and which artefacts were produced.

“Rollback = restore the last coherent trio: excerpt + logs + crew artefacts.”

8. Out of Scope (Phase-6 boundary)

- no automatic enforcement,
- no blocking of runs,
- no canonical approvals,
- no implicit glossary decisions.

“Excerpt binding improves visibility; governance remains human.”

---

## Runtime propagation contract (excerpt_id/source/version)

### Required fields

- excerpt_id
- excerpt_source
- excerpt_version

### Where these appear

- CLI flags for excerpt-aware runs:
  - --excerpt-id
  - --excerpt-source
  - --excerpt-version
- Log header (key:value lines at top of each log):
  - excerpt_id: <...>
  - excerpt_source: <...>
  - excerpt_version: <...>
  - mode: excerpt-aware
- JSON artefacts (annotator, challenger, crew):
  - metadata appears under a top-level "excerpt" object, e.g.:
    {
      "excerpt": {
        "id": "...",
        "source": "...",
        "version": "..."
      }
    }

### Behavioural rules

- If CLI flags and config disagree, config is the source of truth; log the discrepancy explicitly.
- If any excerpt_* field is missing at runtime:
  - SOFT-STOP: do not start the workflow; write a short log entry explaining the missing field and exit with a clear error.
- If an annotator/challenger JSON lacks excerpt metadata:
  - Governance-STOP for that artefact; mark the run invalid for review and require a re-run with proper metadata.
- Never infer excerpt_id from filenames or directories; only explicit metadata counts.

### Review & archive implications

- Human reviewers must be able to reconstruct:
  excerpt → run_id → artefacts (annotator/challenger/crew) → decision.
- Review/evaluation templates must include excerpt_id/source/version and link to the log/JSON for traceability.

### Backwards compatibility

- Existing non-excerpt-aware logs remain valid as historical records,
  but are NOT acceptable for Phase-6 excerpt-bound runs.
- Excerpt-aware runs must be tagged as such in the log header (mode: excerpt-aware).

End of document.
