# Phase-6 Human Review Workflow (Draft)

## Purpose
This document defines how AI-generated annotations move through the editorial lifecycle
without ever becoming canonical automatically. Phase-6 focuses on infrastructure,
traceability, and safe human control.

We treat AI output as evidence and proposals, never as decisions.

## Lifecycle States

### 1) CANDIDATE
Source: raw crew run (annotator/challenger JSON)

Characteristics:
- excerpt metadata present
- run metadata present
- payload may be null or partial
- no human has touched the content yet

Allowed actions:
- archive
- send to challenger
- move to CREW_PROVISIONAL

Not allowed:
- publishing
- rewriting original text

---

### 2) CREW_PROVISIONAL
Source: crew output after challenger or internal consistency checks.

Characteristics:
- machine commentary may exist
- disagreements documented
- still *not* authoritative

Allowed actions:
- human inspection
- flag issues
- move to READY_FOR_HUMAN_REVIEW

Not allowed:
- merging into scholarly edition
- overwriting earlier records

---

### 3) READY_FOR_HUMAN_REVIEW
This is the hand-off point.

Characteristics:
- excerpt binding verified
- run trace verified
- JSON structural sanity validated
- humans now explicitly responsible

Allowed actions:
- approve, reject, or annotate further
- escalate uncertainties
- propose edits in a separate layer

Not allowed:
- silently promote to canonical

---

### 4) CANONICAL (Human-Only Lane)
Only humans (editors) may declare something canonical.

Requirements:
- explicit review note
- cross-reference to governing excerpt
- justification that avoids speculation
- clear link to earlier states

No automation may enter this state.

---

## Rollback Model
Any state may be rolled back to an earlier state
as long as the reason is documented.

Canonisation must never occur silently,
and re-evaluation always creates *a new record* rather than editing history.

---

## Relationship to Excerpt Binding
Every artifact carries:

- excerpt_id
- excerpt_source
- excerpt_version

If any mismatch appears at any stage,
work stops and the issue is recorded.

Excerpt-binding remains a documentary guard,
not an automated enforcement mechanism.

---

## Human Review Participation Model

Human review in Mustikarasa is intentional, scheduled, and batch-based.

- Agents operate autonomously within safe lanes.
- They NEVER interrupt runs to ask humans for ad-hoc decisions.
- Instead, they mark uncertainty using signals such as:
  `[AUTO-OK]`, `[AMBIGUOUS]`, `[ESCALATE-HUMAN]`.

Decisions are handled later, in bundled review sessions
(per excerpt or per thematic batch). During these sessions:

1) reviewers examine the bundle,
2) low-risk items may be acknowledged quickly,
3) ambiguous or escalated items are discussed and documented,
4) only where appropriate, a canonical decision record is created.

Important principle:

> Human reviewers do not “chase” the workflow while it runs.
> They decide at defined editorial checkpoints — traceably and reproducibly.

This ensures scalability, preserves the autonomy envelope of agents,
and guarantees that canonical status only emerges from deliberate human judgment.

## Next Steps
- define minimal JSON checks for READY_FOR_HUMAN_REVIEW
- design review notes template
- connect human decisions to CANONICAL_INDEX

## Linking to the Canonical Index

When a human decision eventually promotes material into CANONICAL state,
the canonical entry must:

1. Reference the governing excerpt (id, source, version)
2. Link to the review note file
3. Link to the original crew run artifact
4. Include a short justification (editor-written)

The CANONICAL_INDEX never stores AI output itself — only stable,
human-approved editorial results with traceable provenance.

This creates a clean separation between:
- *proposals* (agents + review trail)
- *decisions* (editors, explicitly justified)
