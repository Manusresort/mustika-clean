[RUNBOOK_P4_SANDBOX_SAYUR_TABLETOP]

Title: Sandbox Runbook — SAYUR (Table-top rehearsal)

Status:
DESIGN / REHEARSAL — NOT AUTHORIZED FOR EXECUTION

Purpose:
- Test of het pilot-proces logisch, traceable en herhaalbaar is.
- Identificeer waar soft-stops, escalaties en logging onduidelijk worden.
- Oefen samenwerking tussen rollen zonder technische risico’s.

Scope:
- Alleen excerpt SAJUR-A + topregels SAJUR-B
- Geen nieuwe bronnen, geen glossaries, geen publicatie-artefacts

Participants (role-play):
- Orchestrator
- Translation agent (human)
- Annotation agent (human)
- Challenger
- Methodology Archivist
- Optional observer (captures process feedback)

Input materials:
- sayur_groente_excerpt_v1.txt
- EXCERPT_MAP.md
- CHAPTER_PREP_REPORT (Sayur)
- PILOT_TRANSLATION_PLAN_SAYUR

Expected outputs (simulation only):
- Draft translation (proposal-only)
- Annotation notes
- Glossary proposals (proposal-only)
- Soft-stop & escalation log
- Traceability notes (excerpt → proposal)
- Debrief notes: “what broke / what was unclear”

Execution steps:

1) ORCHESTRATOR — briefing
   - legt scope uit
   - wijst rollen toe
   - herhaalt stop-model (soft-stop → governance-stop → Human Gate)

Guideline timing (table-top rehearsal):
- Translation: max 15–20 min
- Annotation: max 15 min
- Challenger: max 10 min
- Debrief: 15–20 min
(Doel: proces oefenen, niet ‘perfecte’ inhoud maken.)

2) TRANSLATION — draft (proposal)
   - produceert concept-vertaling met [UNCERTAIN] tags
   - noteert EvidenceRef per claim

3) ANNOTATION — enrich
   - voegt HISTORICAL/GLOSSARY/SAFETY/OCR labels toe
   - verwijst naar EXCERPT_MAP + EvidenceRef

4) CHALLENGER — question
   - markeert: over-zelfverzekerde keuzes, gemiste ambiguïteit
   - zet SOFT-STOP wanneer lezer-betekenis kan verschuiven

5) ORCHESTRATOR — triage
   - verzamelt soft-stops en beslist:
     * documenteren en door
     * of ESCALATE (Human Gate nodig)

6) ARCHIVIST — log
   - logt beslissingspunten, onzekerheden en rationale
   - maakt rollback-notitie (wat zou verwijderd kunnen worden)

LOG FIELDS (template):
- Step:
- Role:
- EvidenceRef:
- Issue type (Ambiguity / OCR / Safety / Culture):
- Action (Document / Soft-stop / Escalate):
- Rationale (1–2 zinnen):

7) DEBRIEF — process review
   - wat werkte
   - wat vastliep
   - welke velden/rollen/regels ontbraken

Soft-stop examples (expected):
- lobak-ambiguïteit
- veiligheid/gezondheidsadvies
- OCR-symbolen (bv. “€”)
- dish-vs-method verwarring (tumis)

Example (documentary only):
- “sajuran” lijkt zowel categorie als gerecht — documenteren, NIET kiezen.

Human Gate triggers (simulation only):
- publicatie-impact
- culturele interpretatie
- veiligheid die gedrag kan beïnvloeden

Rollback model:
Alles wat tijdens de rehearsal wordt gemaakt,
wordt bewaard in een tijdelijke notitie — maar NIET in canon.
Rollback = niets publiceren / niets verplaatsen.

Metrics (qualitative):
- Was elke stap traceable?
- Werd het stop-model natuurlijk gebruikt?
- Werden agents over- of onder-autonoom gespeeld?
- Kon iemand anders het proces begrijpen uit dit document?

Failure conditions (process, not content):
- soft-stops werden genegeerd
- annotaties vervingen feitelijke besluitvorming
- rationale ontbrak in de log

Next:
Resultaten van de rehearsal worden samengevat
in een korte AFTER-ACTION NOTE (proposal-only).

Deze aanvullingen verbeteren rehearsal-duidelijkheid.
Ze autoriseren GEEN uitvoering en wijzigen geen governance-grenzen.

[/RUNBOOK_P4_SANDBOX_SAYUR_TABLETOP]
