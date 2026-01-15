# SAYUR Internal Workflow — Case 01

This case file tracks the first real application of the
generic Phase-6 Editorial Mini-Workflow.

It is NOT a pilot. It is a normal internal workflow run
with full traceability and no publication impact.

---

## 1. Excerpt Selection

Lines 52–66 (SAYUR)

52  Ada sajuran jang tak tahan hudjan semasa tumbuhnja, seperti  
54  ketimun, lobak, labu, tomat, kentang, lombok, buntjis, kapri, kol bunga,  
56  katjang merah, katjang tunggak, ojong, bawang merah. Biasanja djenis?2  
58  sajuran ini ditanam pada achir musim hudjan jaitu bulan Maret dan April.  
64  Sajuran jang tahan hudjan dapat ditanam sepandjang tahun asal  
66  tjukup air dimusim kemarau. Dalam golongan ini termasuk bajem,

Source: SAYUR chapter (OCR excerpt, sandbox copy)

### Excerpt metadata (Phase-6)

excerpt_id: sayur_052_066  
excerpt_source: docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md  
excerpt_version: locked-2026-01-05  

These fields follow P6_EXCERPT_BINDING_SPEC.md and are documentary only.
They do not by themselves authorize or execute any run.

---

## 2. Why This Excerpt

- multiple annotation targets  
- low glossary risk  
- realistic agricultural / seasonal framing  
- likely to produce challenger signals without forcing escalation  
- appropriate as the first internal application of the generic workflow

---

## 3. Workflow Artefacts (will be filled during the run)

All artefacts for this case will live under (once the run is executed):

sandbox/workflows/sayur_internal/case01/

- annotator_raw.json → pending (no aligned log yet)  
- challenger_raw.json → pending (no aligned log yet)  
- crew_decisions_provisional.json  
- human_review_notes.md  
- session log references

## 3a. Planned runner invocation (design only)

Once an excerpt-aware runner exists and is approved, Case-01 is expected to run via a command in this shape (example):

```bash
python sandbox/crew/run_excerpt_workflow.py \
  --excerpt-id sayur_052_066 \
  --excerpt-source docs/pilots/P6_SAYUR_CASE01_EXCERPT_SELECTION.md \
  --excerpt-version locked-2026-01-05 \
  --config sandbox/crew/configs/sayur_case01.yaml
```

This example is derived from P6_EXCERPT_AWARE_RUNNER_DESIGN.md and does not by itself authorize or implement any run.

---

## 4. Notes

This case establishes the baseline pattern.
If the workflow feels too heavy or unclear,
we document friction here instead of changing rules ad-hoc.

Case-01 execution is deferred.
Existing MICROPILOT logs do not match the selected excerpt (lines 52–66),
and the current runner is not excerpt-aware.
Case-01 will only be executed once an excerpt-aware run is available.
This pending status remains until an excerpt-aware runner is implemented and explicitly approved via governance.

End of file.
