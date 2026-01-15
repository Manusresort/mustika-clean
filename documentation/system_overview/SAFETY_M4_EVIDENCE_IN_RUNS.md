# Safety M4 — Evidence in Runs (Safety-Aware Editorial Judgement)

## Purpose
This document defines what constitutes sufficient evidence that
the Safety-Aware Editorial Judgement capability operates at M4
maturity level.

Evidence must demonstrate that safety handling is no longer
optional or implicit, but structurally unavoidable.

---

## Required Evidence Types

To justify an M4 upgrade, evidence MUST include all of the following:

### 1. Presence of Safety Signals
Runs or reviews show explicit identification of safety-relevant
signals as defined in docs/SAFETY_M4_SIGNAL_DEFINITION.md.

### 2. Mandatory Proposal Records
Each identified safety signal is associated with a Canonical
Proposal Record, including cases of non-action or deferral.

### 3. Gate Acknowledgement
Evidence shows that safety signals are explicitly gated before
editorial continuation.

### 4. Explicit Closure States
Each gated safety signal has a documented closure state
(accepted, deferred, rejected, or intentionally open).

### 5. Demonstrated STOP Behavior
At least one instance demonstrates that progression was halted
until missing safety documentation was supplied.

---

## Acceptable Evidence Sources

Evidence may be drawn from:
- run logs
- session logs
- review artefacts
- proposal records
- documented STOP events

Synthetic or illustrative examples are not sufficient for M4.

---

## Evaluation Criteria

- Evidence must span multiple instances, not a single anecdote.
- Evidence must show consistency across time or contributors.
- Absence of silent safety handling is critical.

---

## Boundary Conditions

- M4 status is capability-specific.
- Evidence may be partial for other capabilities.
- Loss of evidence invalidates M4 claims.

---

## Non-Goals (Explicit)

- This document does not execute validation.
- This document does not define auditing procedures.
- This document does not grant M4 status by itself.
