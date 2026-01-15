# Safety M4 — Gate and Closure Rules (Safety-Aware Editorial Judgement)

## Purpose
This document defines the minimum requirements for gating and closure
of safety-relevant signals within the Safety-Aware Editorial Judgement
capability.

The intent is to prevent silent continuation while preserving
editorial discretion and historical integrity.

---

## Gate Requirement

A **gate** is REQUIRED whenever a safety-relevant signal has been
identified.

The gate consists of an explicit acknowledgement that:
- a safety-relevant signal exists,
- continuation without recognition would be inappropriate,
- human judgement is required or intentionally deferred.

The presence of a gate does not imply approval, rejection, or change.

---

## Acceptable Closure States

Every gated safety signal MUST eventually have one of the following
closure states documented:

### 1. Accepted (with Rationale)
The signal is acknowledged and addressed through annotation,
contextualisation, or other explicit editorial handling.

### 2. Deferred (Explicit)
The signal is acknowledged, but handling is postponed due to
uncertainty, scope limits, or pending evidence.

### 3. Rejected (with Explanation)
The signal is acknowledged, but determined not to require editorial
action, with an explanation recorded.

### 4. Left Open (Intentional)
The signal is acknowledged and intentionally left unresolved, with
the uncertainty itself documented.

---

## Closure Requirements

- Closure must be explicit and written.
- Closure must reference the associated proposal record.
- Closure may be provisional and revisited.
- Absence of closure is itself non-compliant once gating has occurred.

---

## Boundary Conditions

- Closure does not imply correctness or finality.
- Closure does not require modification of the source text.
- Multiple closures over time are permitted, provided each is logged.

---

## Non-Goals (Explicit)

- This document does not assign decision authority.
- This document does not define escalation paths.
- This document does not implement workflow or enforcement.
