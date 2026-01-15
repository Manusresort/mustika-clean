[CREW_SHAKEDOWN_PLAN_LOBAK_MISTRAL]

Title: Crew-AI Shakedown Plan — LOBAK / Mistral / Ollama

Status:
RUNTIME TEST PLAN — NOT A GOVERNANCE DECISION

Purpose:
Validate a single-agent, annotation-only shakedown focused on glossary ambiguity
around "lobak" without making meaning decisions.

Excerpt selection rules:
- 3–5 lines from a locked excerpt (sandbox only)
- Must include "lobak" or a direct variant
- No recipe instructions; prefer taxonomy/definition context
- EvidenceRef required (EXCERPT_MAP ID + line range)

JSON contract (same as SAYUR):
- Output is a JSON array of objects
- Required keys: line, span, label, reason
- Labels: HISTORICAL / GLOSSARY / SAFETY / OCR / NONE
- No extra fields, no prose outside JSON

Governance stops:
- Human Gate required if meaning/safety/cultural interpretation could shift readers
- Soft-stop on ambiguity or any implicit meaning choice

Run recipe (manual only):
- Run via a local crew command using the shakedown YAML
- Manual gating per step
- Review logs in sandbox/crew/run_logs/

Evaluation checklist:
- JSON valid and schema-compliant
- "lobak" flagged as GLOSSARY (proposal-only)
- No translation or meaning choice
- No governance incidents; rollback remains trivial

### Selected Mini-Excerpt (locked for shakedown)

EvidenceRef:
- source: data/source_imports/sayur_groente_001/sayur_groente_excerpt_v1.txt
- lines: 52–55 (inclusive)

Verbatim:

52: Ada sajuran jang tak tahan hudjan semasa tumbuhnja, seperti
53:
54: ketimun, lobak, labu, tomat, kentang, lombok, buntjis, kapri, kol bunga,
55:

Rules:
- Text MUST remain unmodified.
- Any ambiguity MUST be handled in annotations.
- If the excerpt ever changes, record rationale here.

### Closure Note (Shakedown Complete)

- Status: **DONE**
- Behaviour confirmed stable (JSON + glossary signalling).
- Known limitation recorded:
  - Reasons may include light cultural framing.
  - Will be harmonised during Phase-5 human review.
- No governance incidents, rollback remains reversible.

[/CREW_SHAKEDOWN_PLAN_LOBAK_MISTRAL]
