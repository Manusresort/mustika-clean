# Safety M4 — STOP Conditions (Safety-Aware Editorial Judgement)

## Purpose
This document defines explicit STOP conditions for the
Safety-Aware Editorial Judgement capability.

A STOP condition indicates that continuation of editorial work
without documented safety handling is not acceptable.

This document defines *when* the system must stop, not *how*
the stop is enforced.

---

## STOP Conditions

Continuation MUST STOP when any of the following conditions apply:

### 1. Unrecorded Safety Signal
A safety-relevant signal (as defined in
docs/SAFETY_M4_SIGNAL_DEFINITION.md) is detected but no
Canonical Proposal Record exists.

### 2. Missing Gate Acknowledgement
A safety signal has been identified, but no explicit gate
acknowledgement has been recorded.

### 3. Absent Closure
A safety signal has been gated, but no closure state
(accepted, deferred, rejected, or intentionally open)
has been documented.

### 4. Silent Resolution
A safety-relevant issue appears to have been resolved
implicitly (e.g. through text changes) without an
explicit proposal, gate, and closure trail.

---

## Scope of STOP

- STOP applies to further editorial progression on the
  affected material.
- STOP does not invalidate prior work.
- STOP may be lifted only by fulfilling the missing
  documentation requirements.

---

## Boundary Conditions

- STOP does not imply wrongdoing or error.
- STOP may be temporary and procedural.
- STOP applies only within the Safety-Aware Editorial
  Judgement capability.

---

## Non-Goals (Explicit)

- This document does not define enforcement mechanisms.
- This document does not assign responsibility.
- This document does not halt the entire system.
