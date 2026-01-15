# Phase-5 Evidence — Translation-Expectation Patterns

Status: documentation — non-binding  
Scope: challenger behavior observed in Phase-4 (SAYUR micropilot & shakedowns)  
Purpose: voorbeelden bundelen zodat reviewers het gedrag sneller herkennen,
zonder nieuwe experimenten te draaien.

---

## 1. Waarom dit document bestaat

In Phase-4 zagen we een terugkerend patroon bij de Challenger:
het model verwacht soms dat er een vertaling/equivalent moet zijn —
ook wanneer dat **niet** tot de opdracht behoort.

Dat patroon is geen fout, maar een **signaal**:
het toont waar mogelijke glossarium-spanningen zitten,
zonder dat er beslissingen worden genomen.

> Policy: zichtbaar laten — niet weg-optimaliseren.

---

## 2. Typisch gedragsverloop (uit logs)

1) **SAFETY/BLOCKER**  
   “Lack of translation may confuse readers.”

2) **EQUIVALENT/INFO**  
   “No English equivalent is provided.”

3) **OTHER/INFO**  
   “No translation provided; may require review later.”

Interpretatie:
de Challenger leert “afremmen” en blijft signaleren
met lagere assertiviteit — precies wat we willen.

---

## 3. Voorbeeldcases (geanonimiseerd)

### Case A — term met culturele lading
- Annotator: labelt als GLOSSARY (proposal-only).
- Challenger: markeert initially als SAFETY → later INFO.

✔ Correct: signaal zichtbaar, geen decision-pressure.

---

### Case B — technisch kookbegrip
- Annotator: NONE (neutraal, puur beschrijvend).
- Challenger: vraagt of een equivalent nuttig zou zijn.

✔ Correct: dit is **INFO**, geen fout; review kan later beslissen.

---

### Case C — historisch label (Golongan)
- Annotator: HISTORICAL.
- Challenger: merkt op dat context ontbreekt.

✔ Correct: dit wijst reviewers naar mogelijke annotation-verrijking,
niet naar een vertaalbeslissing.

---

## 4. Wanneer dit wél een probleem zou zijn

- Challenger **eist** vertalingen of equivalents  
- Challenger **classificeert** meaning in plaats van te signaleren  
- Annotator-output wordt onterecht “gecorrigeerd”

> In die gevallen: markeren als OVERREACH en loggen.

Tot nu toe zagen we deze gevallen zelden en vooral in vroege runs.

---

## 5. Praktische richtlijnen voor reviewers

- Vraag niet: “Is dit juist?”  
  maar: **“Helpt dit signaal ons later beslissen?”**

- INFO/WARNING is meestal goed.  
- BLOCKER moet onderbouwd zijn — anders terugschalen naar INFO.

---

## 6. Wat we níet gaan doen (Phase-5)

- geen prompt-tuning om bias te verbergen  
- geen gedragswijzigingen in Challenger  
- geen “auto-equivalents”

We documenteren — we beslissen niet.

---

## 7. Mogelijke vervolgstap (optioneel)

Verzamelen van 5–10 “best exemplars” uit echte logs
en opnemen in een appendix — alleen als dit reviewers helpt
en zonder nieuwe runs.

Einde document.
