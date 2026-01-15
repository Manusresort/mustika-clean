# Phase-7 — Canonical Decision Trail Specification

## Purpose
Define how a *proposal* becomes a *canonical editorial decision*,
with full traceability:

source → excerpt → run → AI proposal → human review → canonical decision.

Nothing becomes canonical silently.

## Canonical Decision Record (Draft Schema)

Every canonical decision must contain:

- decision_id
- decision_type (link to P7_DECISION_TYPES.md)
- excerpt { id, source, version }
- artefacts { run_id, json_paths, logs }
- reviewer (human identity)
- decision_status (approved / revised / rejected)
- rationale (short explanation, cite evidence)
- supersedes (optional link to earlier decision)
- created_at

## Lifecycle Overview

1. AI produces provisional proposal (CANDIDATE / CREW_PROVISIONAL)
2. Item is marked READY_FOR_HUMAN_REVIEW
3. Human creates a canonical decision record
4. Record is indexed and becomes part of the canonical trail
5. Rollback happens by creating a *new* decision (never overwriting)

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

## NO AUTO-PROMOTION (Human Gate Guarantee)

Canonical status may NEVER be assigned automatically.

- Agents only produce provisional proposals.
- Runners and scripts cannot promote anything to CANONICAL.
- Only a human reviewer, through a recorded canonical decision,
  can create canonical status.

If any tool attempts automatic promotion, it is treated as an incident:
restore previous valid state and document the issue.

## Rollback Principle

Rollback = new decision record.  
Previous records remain in the archive as historical trace.
