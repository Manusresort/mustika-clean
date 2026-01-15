# Phase-4 Sandbox Closure Checklist — SAYUR (Draft, non-binding)

Purpose: This checklist is documentary only.  
It helps verify whether Phase-4 sandbox goals were *demonstrated*,
not whether work should continue.  
No item in this list implies new backlog or approvals.

---

## 1) Runtime + reproducibility

- [ ] Single-agent runs produce valid JSON (schema-checked).
- [ ] Multi-agent (annotator → challenger) runs complete without breaking the pipeline.
- [ ] Logs consistently contain markers:
      ---ANNOTATIONS--- / ---CHALLENGE_REPORT--- / ---OPTIONAL_AGENT_STEPS---.
- [ ] Runs can be repeated on the same excerpt with consistent behaviour.

Evidence reference:
- sandbox/crew/run_logs/* (Phase-4 SAYUR)

---

## 2) Governance behaviour

- [ ] Soft-stop and governance-stop rules are visible in docs and runners.
- [ ] No agent writes to source or canonical documents.
- [ ] Agents signal and annotate — humans decide on meaning/culture/safety.
- [ ] Challenger raises issues without enforcing decisions.

Evidence reference:
- docs/WORKFLOW.md
- docs/10-governance/*
- HUMAN_GATE_LOG.md

---

## 3) Failure-mode learning (documented, not fixed)

- [ ] Translation-expectation bias observed and documented.
- [ ] Occasional challenger overreach recognised as governance issue.
- [ ] JSON-fencing / contract issues identified and traced to prompts.
- [ ] All such findings are recorded as “proposal-only”.

Evidence reference:
- P4_CONSOLIDATION_REPORT_SAYUR_SANDBOX.md
- MICROPILOT logs (SAYUR)

---

## 4) Traceability + rollback

- [ ] Every run has a corresponding log file.
- [ ] Rollback process exists and has been table-top tested.
- [ ] Any deviations are logged, not silently corrected.

Evidence reference:
- ROLLBACK_TESTPLAN_P4_SANDBOX.md
- CODEX_SESSION_LOG.md

---

## 5) What stays intentionally unresolved (Phase-5 territory)

- [ ] Whether challengers should classify translation-expectation differently.
- [ ] Whether agent outputs should be merged into a single JSON object.
- [ ] Whether learning-style feedback loops should become active.

These are **explicitly deferred** and do not block Phase-4 closure.

---

## Status

This checklist tracks understanding only.  
It does **not** determine GO / NO-GO.  
That remains a Human-Gate decision documented elsewhere.

End of file.
