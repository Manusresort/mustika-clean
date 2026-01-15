# Micropilot — SAYUR Multi-Agent v2 (Annotator → Challenger → Troubleshooting)

Status:  
DESIGN-DRAFT (Phase-4 sandbox, reversible, proposal-only)

Related docs:  
- docs/crew/CREW_MICROPILOT_SAYUR_MULTI_MISTRAL.md  
- docs/crew/CHALLENGER_ISSUE_TYPES_P4.md  
- docs/10-governance/HUMAN_GATE_POLICY_P4_SANDBOX.md  
- docs/AGENT_AUTONOMY_ENVELOPE.md  

---

## 1. Purpose

Deze micropilot onderzoekt of we veilig kunnen werken met:

1) Annotator → signaleert (zonder vertalen/beslissen)  
2) Challenger → flagt rule-violations (zonder overreach)  
3) **Optionele** agent-stappen (Troubleshooting / Research / Template)  
   **vóór** escalatie naar Human Gate.

Doel: failure-modes zichtbaar maken — niet “mooie output”.

---

## 2. Hypotheses

- Annotator houdt zich aan labels + JSON-schema.  
- Challenger gebruikt Issue Types correct
  (TRANSLATION/EQUIVALENT/MEANING_DECISION/SAFETY/GOVERNANCE).  
- Ambiguïteit met lage impact → eerst agent-teamwerk (troubleshooting).  
- Alleen high-impact / onoplosbaar → Human Gate (met log-redenen).  
- Alles blijft traceable & reversible.

---

## 3. Scope (klein en gecontroleerd)

Source: SAYUR excerpt (locked) — regels 14–18.  
No edits to source, glossary, or canon.  
Sandbox only (no publication path).

---

## 4. Agents & roles

| Phase | Agent | Role | Must NOT |
|------:|-------|------|---------|
| 1 | Annotator | signaleren, labelen, EvidenceRefs | vertalen, corrigeren, beslissen |
| 2 | Challenger | rule-violations flaggen (JSON only) | oplossingen eisen, equivalents pushen |
| 3 (opt.) | Troubleshooting | verduidelijken, context verzamelen | beslissen, normaliseren |
| 4 (opt.) | Template Agent | JSON/contract valideren | inhoud wijzigen |
| 5 (if needed) | Human Gate | betekenis/cultuur/safety besluiten | overslaan van logs |

Meta-laag (Codex) analyseert achteraf en doet voorstellen — past niets live aan.

---

## 5. Possible paths
