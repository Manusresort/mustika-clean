# Phase-6 Note — SAYUR Runner and Excerpt Locking

## Summary
Pilot 03 was designed as a glossary-critical test using the locked lines 118–132 excerpt.  
However, the resulting logs and JSON outputs match the earlier Golongan VI / Sajuran excerpt used in Pilot 01.

## Observation
The SAYUR runner did not execute against the Pilot-03 excerpt.  
The crew pipeline instead reused an earlier excerpt, producing identical lifecycle behaviour:
- 1 item
- CREW_PROVISIONAL only
- no READY_FOR_HUMAN_REVIEW
- translation-expectation WARNING (bias-signal only)

## Interpretation
This is not an agent failure.  
It is a workflow binding issue: the runner currently does not take an explicit excerpt-ID or excerpt-path as governed input.

## Implication for Phase-6
Before glossary-critical pilots can be meaningfully executed,
the SAYUR workflow should accept an explicit excerpt reference and log it
so that excerpt → run → decision remains traceable.

## Next step (documentary only)
Design a small change to the workflow specification:
- introduce an `excerpt_id` or `excerpt_path` field,
- record it in logs,
- verify that crew inputs match the locked excerpt.

No runtime changes yet — design first.

End of note.
