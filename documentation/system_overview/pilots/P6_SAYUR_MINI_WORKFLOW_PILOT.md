# P6 Pilot — SAYUR Mini Workflow

## 1. Pilot Goal
Verifiëren dat de meeste items eindigen op CREW_PROVISIONAL en slechts
selectief escaleren naar READY_FOR_HUMAN_REVIEW.

## 2. Materials
- excerpt source reference: <source_path_or_id>
- existing runners (reference only):
  - `sandbox/crew/micropilot_sayur_multi_runner.py`
  - `sandbox/crew/codex_p5_micropilot_provisional_runner.py`
- workflow doc: `docs/P6_WORKFLOW_SAYUR_MINI.md`

## 3. Run Steps (Manual)
1) Kies excerpt en leg provenance vast (document-first).
2) Run annotator + challenger via bestaande runner(s) (geen codewijzigingen).
3) Verzamel JSON outputs en maak crew-synthese (provisional only).
4) Markeer READY_FOR_HUMAN_REVIEW uitsluitend bij criteria uit P6 workflow.
5) Log run-id, inputs, outputs en evaluatie.

## 4. Collected Outputs
- annotator JSON: <path>
- challenger JSON: <path>
- crew_decisions_provisional.json: <path>
- human_review_notes (if any): <path_or_none>

## 5. Evaluation Template
- total_items: <n>
- crew_provisional_count: <n>
- ready_for_human_review_count: <n>
- % provisional: <pct>
- % escalated: <pct>
- bias notes: translation-expectation / over-escalation / other

## 6. Observations & Follow-ups
Korte notities over waargenomen patronen; geen policy-wijzigingen hier.
