# P4 Consolidation Report — SAYUR Sandbox

## Status Summary
- Phase: P4 (sandbox, non-publication)
- Scope: SAYUR excerpt (SAJUR-A)
- Pilots completed:
  - Shakedown (annotator-only, Mistral/Ollama)
  - LOBAK glossary shakedown (signal-only)
  - Multi-agent micropilot (annotator + challenger)
- Overall outcome: **WORKFLOW PROVEN — SAFE TO CONTINUE (sandbox)**

## What We Proved
- CrewAI + Ollama + Mistral operate reliably under JSON constraints.
- Agents respect autonomy limits when prompts are explicit.
- Challenger pattern successfully flags rule-breaches without self-fixing.
- Rollback is reversible and documented.
- Goverance stop-model (soft-stop → human gate) works in practice.

## Evidence References
- docs/CODEX_SESSION_LOG.md entries for SAYUR runs
- sandbox/crew/run_logs/ selected logs
- docs/crew/CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md (closure note)
- docs/crew/CREW_SHAKEDOWN_PLAN_LOBAK_MISTRAL.md (closure note)
- sandbox/crew/micropilot_sayur_multi_runner.py

## Agent Behaviour Notes
- Annotator: stable JSON, tends to under-decide (preferred).
- Challenger: effective escalation but occasionally overreaches
  (requested translations where governance forbids decisions).

## Known Limitations
- Definition sentences sometimes marked HISTORICAL as whole lines.
- Challenger sometimes mislabels issues as SAFETY instead of GOVERNANCE.
- Reasons occasionally reference cultural knowledge instead of text-evidence.
- Observability for multi-agent runs required extra logging wrapper.

### KNOWN LIMITATION — “Helpful translation” framing (OTHER/INFO)

In later SAYUR micropilot runs, the Challenger agent occasionally
produced entries like:

- issue_type: OTHER
- severity: INFO
- comment along the lines of:
  "No translation or equivalent is provided, and it may be
   helpful for understanding in an English context."

Interpretation:

- This is not a rules violation. Annotators are explicitly NOT
  expected to provide translations in Phase-4.
- The message reflects a mild model bias toward assuming that
  untranslated terms are incomplete or suboptimal.
- Compared to earlier runs (EQUIVALENT/INFO), the tone is softer,
  but the underlying assumption is similar.

Governance stance:

- treat as signal, not as error
- severity remains INFO
- keep documented so humans understand the pattern

This behaviour is intentionally NOT suppressed in Phase-4,
because observing these biases is part of the learning goal.

## Governance Checkpoints
- No glossary or meaning decisions made automatically.
- All BLOCKER-type issues route to Human Gate.
- All modifications traceable & reversible.
- No runtime changes made by agents themselves.

## Components Ready For Re-Use
- JSON annotation contract
- Codex runner wrappers + log structure
- Annotator prompt baseline (SAYUR/LOBAK)
- Multi-agent runner pattern (annotator + challenger)
- Schema validation hook

## Next Safe Steps (Recommendation)
1. Tune challenger issue-types (add GOVERNANCE / MEANING_DECISION).
2. Add automatic JSON merge (`{ annotations, challenge_report }`) post-run.
3. Re-run multi-agent pilot on second excerpt (confirm repeatability).
4. Only then consider a learning-agent prototype (documentary, not self-editing).

## Decision
- Status: **CONSOLIDATED**
- Ready to proceed: **YES — sandbox only, controlled expansion**

## KNOWN LIMITATION — Translation Bias in Challenger (EQUIVALENT/INFO)

In multiple Phase-4 SAYUR micropilot runs, the Challenger agent
consistently produced the following pattern:

- issue_type: EQUIVALENT
- severity: INFO
- comment similar to:
  "No English translation provided for ‘Sajuran’."

Interpretation:

- This does NOT indicate a rules violation by the annotator
  (annotators are not expected to provide translations in Phase-4).
- It reflects a mild model bias toward assuming that untranslated
  terms are incomplete.
- The Challenger no longer demands translation (previous overreach),
  but still treats “no translation present” as noteworthy.

Governance stance (Phase-4):

- treat this as signal, not error
- severity remains INFO
- requires human interpretation rather than automatic suppression
- documented here for transparency and reproducibility

This bias should be revisited in later phases, but no additional
runtime constraints are added in Phase-4 to suppress it. Documentation
and human context are preferred over over-engineering prompts.

### Expected generalisation (Phase-4 stance)

Based on repeated micropilot observations, we expect the
“translation-expectation” bias to generalise across chapters and
content types (e.g., SAYUR, SANTAN and similar sections).  
In Phase-4 this bias is **documented and monitored, not eliminated**.  
When it reappears in other excerpts, it should be treated as an
**expected recurrence**, not as a new problem, unless it begins to
affect safety, meaning, or publication-impact decisions (Human Gate).
