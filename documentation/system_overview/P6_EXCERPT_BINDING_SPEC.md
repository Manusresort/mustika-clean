# Phase-6 Specification — Excerpt Binding & Traceability

## 1. Background
Pilot 03 revealed that glossary-critical testing could not be properly evaluated,
because the SAYUR runner reused an earlier excerpt instead of the locked one.

This is not an agent or lifecycle failure.
It is a workflow binding gap: the workflow did not explicitly carry
a governed excerpt reference from design → run → decision → evaluation.

## 2. Goal
Ensure that every workflow execution can answer, with evidence:

- Which excerpt was used?
- Where did it come from?
- Which version of the excerpt was intended?

Without changing runtime behaviour, we introduce documentary rules and fields
that make excerpt usage explicit and traceable.

## 3. Required Metadata Fields

Required fields for any excerpt-based run (sandbox, pilots, scholarly):

excerpt_id     = short stable identifier (example: sayur_118_132)
excerpt_source = path to the governing excerpt document
excerpt_version = version tag (example: v1 or locked-2026-01-05)

These fields are documentary and reproducibility-oriented.
They do not grant agents autonomy and do not create runtime enforcement.

### Re-excerpting policy (documentary only)

ADDED: Re-excerpting means deliberately redefining the governed excerpt scope (segment boundaries) rather than editing content.
ADDED: Agents may log or mention input mismatches in logs/eval/proposal notes to provide visibility, but the signals do not auto-change the excerpt metadata.
ADDED: Humans decide whether re-excerpting is required.
ADDED: Allowed forms are bumping excerpt_version under the same excerpt_id with an updated governing document, or introducing a new excerpt_id/document.
ADDED: MUST NOT silently reuse an older excerpt or patch existing run/proposal/closure artefacts to match a different excerpt.
ADDED: Operational rule: metadata/content mismatch → STOP, document the mismatch, and then follow one allowed form to start new work.

## 4. Where These Fields Must Appear

### 4.1 Pilot planning documents
Each pilot must explicitly declare excerpt_id, excerpt_source, and excerpt_version.

### 4.2 Run notes / collected logs
When run logs are summarized or collected,
the excerpt metadata must be included in the summary context.

### 4.3 Crew decision artefacts
When crew_decisions_provisional.json is generated,
each decision record MUST include the following fields
with identical values across that run:

excerpt_id
excerpt_version

### 4.4 Evaluation reports
Evaluation files should restate the excerpt metadata in the context section.

## 5. Example (SAYUR mini workflow)

Example metadata:

excerpt_id: sayur_118_132
excerpt_source: docs/pilots/P6_PILOT03_EXCERPT_SELECTION.md
excerpt_version: v1

Example crew decision entry:

term_id: lalab@line118
excerpt_id: sayur_118_132
excerpt_version: v1
decision_status: CREW_PROVISIONAL
decision_origin: crew
rationale: Glossary-relevant culinary term with cultural nuance.
ready_for_human_review: true

## 6. Governance Boundary
Excerpt metadata improves traceability only.

It does NOT:
- change agent autonomy,
- introduce automatic validation,
- authorize text edits,
- advance lifecycle states.

Human Gate remains the only authority to canonize decisions.

## 7. Next Step (documentary only)
Update pilot templates and workflow docs so that excerpt metadata
is explicitly declared everywhere it is logically needed.

No code changes yet; implementation discussion is deferred.

End of specification.
