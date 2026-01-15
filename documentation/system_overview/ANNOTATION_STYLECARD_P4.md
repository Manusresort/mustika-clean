[ANNOTATION_STYLECARD_P4]

Title: Annotation Stylecard — Phase-4 Pilots

Status:
GUIDELINE — NOT A RUNTIME APPROVAL

Purpose:
Zorgen dat annotaties betekenis beschermen,
ambiguiteit zichtbaar houden
en altijd herleidbaar blijven naar bronregels.

Scope:
Geldt voor Phase-4 pilot-werk (sandbox),
proposal-only outputs,
niet voor publicatie-tekst.

---

## Core rules (for all annotation types)

1) Document > decide
   Beschrijf, kies niet. Markeer onzekerheid expliciet.

2) Short & scoped
   max 3–5 regels. Geen essays.

3) EvidenceRef verplicht
   Altijd EXCERPT_MAP ID + line range vermelden.

4) Uncertainty tag
   Gebruik [UNCERTAIN] of [AMBIGUOUS] waar van toepassing.

5) No normalization
   Geen modernisering, geen herschrijven van bron.

6) Separate label from opinion
   Label = feitelijke classificatie; toelichting = beknopt, neutraal.

7) Soft-stop discipline
   Bij mogelijke betekenisverschuiving → log soft-stop, niet “fixen”.

---

## Label-specific guidance

### [HISTORICAL_NOTE]
- Doel: context, tijdsbeeld, intentie van bron.
- Vermijd oordeel (“fout”, “ouderwets”).
- Verwijs naar concrete passage(n).

### [GLOSSARY_NOTE]
- Doel: mogelijke betekenissen opsommen (proposal-only).
- Altijd alternatieven tonen, geen voorkeur kiezen.
- Markeer Human Gate triggers indien lezer-impact.

### [SAFETY_NOTE]
- Doel: historisch kaderen, niet adviseren.
- Formuleer: “historische bewering, geen aanbeveling”.
- Escaleren bij moderne veiligheidsimplicaties.

### [OCR_NOTE]
- Doel: ruis signaleren, niet corrigeren.
- Voeg classificatie toe: REVIEW_REQUIRED / DO_NOT_AUTOMATE.
- Beschrijf kort welk teken/woord onzeker is.

### [LINGUISTIC_NOTE]
- Doel: spelling/varianten duiden.
- Geen normalisatie; benoem vorm + mogelijke redenen (tijd/streek).

---

## Anti-patterns (avoid)

- “Waarschijnlijk betekent dit X.”  → te sturend
- “Beter zou zijn…”                → normatief
- “Hier moet eigenlijk…”           → beslissend
- Lange paragrafen → niet traceable
- Annotaties die brontekst vervangen.

---

## Logging expectation

Elke annotatie koppelt aan:
- EvidenceRef
- Annotatie-type
- Rationale (1–2 regels)
- (optioneel) Soft-stop ID

---

## Relationship to governance

- Bij twijfel → soft-stop.
- Bij lezer-impact → Human Gate.
- OCR-correcties → NOOIT door agent.
- Glossary-keuzes → proposal-only.

Reminder:
Deze stylecard beschrijft gedrag.
Het autoriseert geen sandbox-runs.

[/ANNOTATION_STYLECARD_P4]
