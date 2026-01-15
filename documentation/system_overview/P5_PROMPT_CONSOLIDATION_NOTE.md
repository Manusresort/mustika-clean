# Phase-5 Prompt Consolidation Note

Status: documentation — non-binding  
Scope: annotator & challenger prompts + AGENT_PROMPT_PATTERN_P5  
Purpose: vastleggen wat we geleerd hebben, zonder runtime-wijzigingen.

---

## 1. Context (waarom dit document bestaat)

Phase-4 heeft laten zien dat annotator en challenger technisch stabiel zijn,
en dat hun prompts de juiste discipline afdwingen: signaleren, niet beslissen.
Phase-5 focust niet op “tunen”, maar op beter begrijpen en navigeerbaar maken.

> Kernprincipe: zichtbaar gedrag > verborgen optimalisatie.  
> Alle wijzigingen blijven proposal-only en vereisen governance-review.

---

## 2. Wat werkt al goed

- Annotator:
  - strikt JSON, goed te valideren  
  - signaleert OCR/historical/glossary zonder beslissen  
  - houdt vertalen/moderniseren buiten scope

- Challenger:
  - controleert rule-violations i.p.v. inhoud  
  - hanteert issue_types (TRANSLATION / SAFETY / etc.)  
  - gebruikt INFO/WARNING/BLOCKER — eist niets

- Pipeline:
  - bias en failure-modes blijven zichtbaar in logs  
  - rollback en traceability functioneren zoals bedoeld

---

## 3. Waar we “needs-clarification” zagen

Niet fout — maar nog niet uniform volgens het nieuwe Phase-5 pattern:

- boundaries soms impliciet i.p.v. expliciet
- uncertainty/escaleer-regels niet altijd in een vaste sectie
- forbidden-lijst verschilt per prompt (inhoud wel correct)
- loggingverwachting niet overal in de prompt zelf benoemd
- rules verspreid over uitlegblokken i.p.v. compacte checklist

Dit zijn **harmonisatie-punten**, geen urgente problemen.

---

## 4. Wat we bewust NIET oplossen in Phase-5

- translation-expectation bias  
  → blijft **signaal**, geen bug.

- strengere annotator-interpretatie-regels  
  → pas aanpakken als we betere voorbeelden + evaluatie-criteria hebben.

- prompt-herformuleringen met gedragsimpact  
  → alleen na governance-review.

> Phase-5 = ordenen en expliciteren — niet herontwerpen.

---

## 5. Rol van het nieuwe Prompt Pattern

`docs/AGENT_PROMPT_PATTERN_P5.md` fungeert als:
- gemeenschappelijk sjabloon
- audit-houvast
- “alignment tool” zonder gedrag te wijzigen

Adoptieplan:
1) nieuwe prompts volgen het patroon,  
2) bestaande prompts krijgen labels:  
   `compliant / needs-clarification / defer-to-governance`.

---

## 6. Aanbevolen vervolgstappen (documentair)

- review uitbreiden naar 1–2 extra agents (optioneel)  
- concrete voorbeelden verzamelen van:
  - OK vs OVERREACH vs OUT-OF-BOUNDS  
- voorbereiden van een kleine Phase-5 pilot:
  **“Challenger clarity (no behavior change)”** —
  alleen formulering, geen tuning, log-gedreven evaluatie.

Alle acties blijven:
- traceable  
- reversibel  
- human-gated waar nodig.

---

## 7. Reminder

Dit document beschrijft observaties en afspraken in wording.
Het autoriseert **geen** nieuwe runs en **geen** prompt-aanpassingen.

Einde document.
