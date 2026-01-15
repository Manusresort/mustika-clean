[CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL]

Title: Crew-AI Shakedown Plan — SAYUR / Mistral / Ollama

Status:
RUNTIME TEST PLAN — NOT A GOVERNANCE DECISION

Purpose:
Controleren of de crew-ai + Ollama + Mistral stack technisch werkt
voor het annoteren van SAJUR-A, zonder inhoudelijke beslissingen.

Scope:

- Single-agent run: annotator_mistral
- Corpus: 3–5 regels uit SAJUR-A excerpt
- Task: alleen labels (HISTORICAL / GLOSSARY / SAFETY / OCR / NONE)
- Geen vertaling, geen herschrijving, geen glossary-besluiten.

What we test:

- Kan de crew de juiste modelconfig vinden (Mistral via Ollama)?
- Volgt de agent de JSON-outputvorm?
- Zijn latency en foutmeldingen acceptabel?
- Respecteert de agent de beperkingen (geen beslissingen, geen normalisatie)?

Manual steps (outside Codex):

1) Kies 3–5 regels uit SAJUR-A in je lokale omgeving.
2) Voer de crew-ai shakedown-run uit met deze YAML-config
   volgens je lokale crew-ai/Codex integratie.
3) Inspecteer de JSON-output:
   - valide JSON?
   - labels logisch?
   - geen vertaling of normalisatie?

Stop rules:

- Als output geen JSON is -> STOP, config/debug eerst.
- Als agent tekst herschrijft -> STOP, autonomie aanscherpen.
- Als Mistral niet bereikbaar is -> STOP, platform debuggen.

Reminder:
Dit plan beschrijft een ECHTE technische test.
Codex voert die test NIET uit; een mens start de crew-run buiten dit plan.

---

## Shakedown Data & JSON Contract (Phase-4 sandbox)

### Expected JSON Output Schema (STRICT)

The Mistral annotator MUST output valid JSON only.

Each reply MUST be a JSON array of objects, with EXACTLY these keys:

- "line"   → integer (1-based index of the line in the excerpt)
- "span"   → string (exact substring copied from the input line)
- "label"  → one of:
  ["HISTORICAL", "GLOSSARY", "SAFETY", "OCR", "NONE"]
- "reason" → short neutral explanation (1–2 sentences max)

Forbidden:
- extra fields
- Markdown, comments, or prose outside the JSON
- rewriting, translating, normalising, or deciding meanings

Preferred fallback behaviour:
- If in doubt between labels, choose "NONE" and explain uncertainty in "reason".

### Mini-Excerpt (SAJUR-A pilot subset)

Source mapping: see `data/source_imports/sayur_groente_001/EXCERPT_MAP.md` (ID: SAJUR-A)

For this shakedown we will use 3–5 consecutive lines
from the SAJUR-A range described there.

This excerpt MUST:

- come from SAJUR-A only,
- include at least one glossary-candidate term
  (examples: sajuran, lalab, seupan, lobak),
- remain unmodified (historical spelling preserved),
- be logged with an EvidenceRef linking back to EXCERPT_MAP.

NOTE:
The exact line numbers will be written down at run-time
in the session log entry for the shakedown RUN-ID.

---

## Shakedown Run Recipe & Observability

### How the run is started (sandbox only)

This shakedown is executed manually, with human gating at every step.

The run is triggered from the Codex CLI using a crew command
(e.g. `crew run` or project equivalent), pointing to:

- config: `sandbox/crew/shakedown_sayur_mistral.yaml`
- model host: Ollama (local), model `mistral`
- input: the mini-excerpt defined at run-time (SAJUR-A only)

No pipelines, no automation, no chained agents.

### What MUST be logged for this shakedown

For each shakedown attempt we log:

- RUN-ID (e.g. RUN-P4-SAYUR-A-0001 or derived)
- timestamp
- config reference (path + commit hash if available)
- excerpt reference (EvidenceRef to EXCERPT_MAP + local excerpt text)
- full system prompt (hash or link)
- full JSON output from the agent (verbatim)
- evaluation notes (OK / Soft-stop / Governance-stop)

All logging is documentary; no persistent runtime artefacts are created.

### OK / KO Criteria

**OK (pass)**
- valid JSON
- only allowed labels used
- no translations, rewrites or “best equivalents”
- doubts handled via "NONE" + explanation

**SOFT-STOP**
- ambiguous terms where the model appears to “choose”
- inconsistent labelling between lines
- behaviour that suggests hidden normalisation

In soft-stop:
- we pause,
- we document,
- we DO NOT rerun until reviewed.

**GOVERNANCE-STOP**
- anything that touches culture, safety, or historical meaning
  in a way that could mislead readers,
- attempts to silently “fix” the text,
- repeated template violations.

In governance-stop:
- freeze the run,
- log the incident,
- hand over via the sandbox incident playbook.

---

## Selected Mini-Excerpt (locked for shakedown)

**EvidenceRef**

- SectionID: SAJUR-A
- Source file: canonical_concat.txt
- Range (per EXCERPT_MAP): 3400–3555
- Local excerpt file: data/source_imports/sayur_groente_001/sayur_groente_excerpt_v1.txt
- Local excerpt lines used: 14–18

**Excerpt (verbatim)**

Golongan VI : Sajuran.



18: Jang dinamakan sajuran adalah bahan makanan jang dibikin sajur

Rules:
- Text MUST remain unmodified.
- Any ambiguity MUST be handled in annotations, not by rewriting.
- If the excerpt ever changes, this section MUST record the change and rationale.

---

## GO Note — Shakedown (Sandbox)

RUN-Scope: RUN-P4-SAYUR-A-0001 (shakedown variant)
Area: SAJUR-A (annotation-only)
Excerpt: Selected Mini-Excerpt (locked)

Decision: GO (sandbox, single-run)
Conditions:
- manual gating at every step
- no reruns without review
- JSON-only; any violation = STOP
- rollback rehearsal after evaluation

Rationale:
Small scope, clear rollback, strong observability.
Goal is technical validation, not content decisions.

Recorder: Codex (documentary only)
Date: 2026-01-04 23:25

### Evaluation Note — Direct Mistral Shakedown 01

- Result: JSON OK, no translation/normalisation.
- Minor issues:
  - Leading whitespace before "[" (parser can trim).
  - "Sajuran" labelled HISTORICAL instead of GLOSSARY (tuning needed).
- Decision: treat as technical PASS; follow-up is prompt/stylecard tuning,
  not a governance incident.

### Evaluation Note — Crew Shakedown 01

- Runner: sandbox/crew/shakedown_sayur_mistral_runner.py (single agent, no tools).
- Result: technical PASS.
  - JSON valid and schema-compliant.
  - "Sajuran" correctly labelled as GLOSSARY.
  - "Golongan VI" labelled as HISTORICAL (accepted as taxonomy heading).
- No governance incident; follow-up is optional tuning, not rollback.

### Verified Runtime Path (Phase-4)

- Runner: `sandbox/crew/shakedown_sayur_mistral_runner.py`
- Shortcut script: `sandbox/crew/run_sayur_shakedown.sh`
- Logs saved to: `sandbox/crew/run_logs/`
- Result: PASS — JSON clean, GLOSSARY behaviour acceptable.
- Remaining work: prompt tuning for label consistency (later phase).

### Stability Note (Phase-4)

- Runs: 3 (annotation-only, sandbox)
- Result: **STABLE**
  - JSON clean, reproducible
  - GLOSSARY behavior consistent for “sajuran”
  - Span rule respected (no full-sentence labels)
- Next allowed step: expand to +1 excerpt line (still annotation-only, gated).

### Closure Note (Shakedown Complete)

- Status: **DONE**
- Behaviour confirmed stable (JSON + spans + glossary).
- Known limitation recorded:
  - Definition lines may be annotated as HISTORICAL on the whole sentence.
  - Address later during human annotation consolidation.
- No governance incidents, rollback remains reversible.

[/CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL]
