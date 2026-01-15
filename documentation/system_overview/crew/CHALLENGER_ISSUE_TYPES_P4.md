# Challenger Issue Types — Phase-4 Sandbox (SAYUR Micropilot)

Status:  
DESIGN GUIDELINE — NOT A RUNTIME CONSTRAINT  

Scope:  
Phase-4 sandbox micropilots (SAYUR-A annotator + challenger).

Purpose:  
Deze notitie verduidelijkt hoe de challenger zijn `issue_type` en `severity`
moet gebruiken bij het beoordelen van annotator-output, zodat:

- challengers **alleen signaleren** en geen beslissingen nemen,
- overreach (bv. “needs translation”) zichtbaar wordt als GOVERNANCE-issue,
- SAFETY alleen wordt gebruikt waar echte veiligheidsinhoud speelt.

De JSON-structuur blijft hetzelfde; dit document definieert de semantiek.

---

## 1. Canonieke issue_types

De challenger mag de volgende `issue_type`-waarden gebruiken:

- `TRANSLATION`  
  Gebruik wanneer de annotator (of een andere agent) feitelijk een vertaling uitvoert
  of expliciet stelt “X means Y”, in plaats van alleen te signaleren.

- `EQUIVALENT`  
  Gebruik wanneer er een “beste equivalent” of vaste vertaling wordt geclaimd
  (bijv. “X is just Y” of “X should be translated as Y”), in strijd met de
  glossary-governance (proposal-only).

- `MEANING_DECISION`  
  Gebruik wanneer de annotator impliciet een interpretatie kiest uit meerdere
  plausibele betekenissen, zonder dit als twijfel/ambiguiteif te markeren.

- `SAFETY`  
  Gebruik **alleen** wanneer er echte veiligheidsinhoud speelt:
  gezondheid, conservering, reiniging, gevaarlijke handelingen, etc.  
  **Niet** gebruiken voor glossary-/betekenisdiscussies, tenzij de inhoud zelf
  als advies/safety claim gelezen zou kunnen worden.

- `GOVERNANCE`  
  Gebruik wanneer gedrag of output duidelijk de governance-regels schendt, bijv.:

  - “needs translation” / “provide equivalent” wordt geëist,
  - een term wordt als “gewone” vertaling gepusht i.p.v. als glossary-casus,
  - SAFETY wordt als drukmiddel gebruikt bij betekenis-/glossary-kwesties,
  - autonomie-envelope / Human Gate policy wordt genegeerd.

- `OTHER`  
  Voor issues die niet netjes in bovenstaande categorieen passen,
  maar wel het loggen waard zijn.

---

## 2. Severity: INFO / WARNING / BLOCKER

- `INFO`  
  Lichte observaties, lage risico’s — vooral documentair.

- `WARNING`  
  Duidelijke schending met beperkte impact.

- `BLOCKER`  
  Alleen wanneer een mens **moet ingrijpen** voor verdere stappen:
  echte safety, harde glossary-/meaning-beslissingen, of negeren van
  autonomie-/Human Gate-regels.

> Praktische regel: liever `INFO` of `WARNING` dan te snel `BLOCKER`.

---

## 3. SAYUR-voorbeeld (sajuran-case)

Voorbeeld uit de micropilot:

```json
{
  "line": 14,
  "span": "Sajuran",
  "issue_type": "SAFETY",
  "severity": "BLOCKER",
  "comment": "needs translation"
}
```
