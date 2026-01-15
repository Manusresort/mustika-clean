---
# Case-01 — Human Reflection (SAYUR 052–066)

This document is intentionally human-written and non-templated.

Scope of reflection:
- editorial behaviour of the agents on this excerpt
- patterns, risks, or biases we observed
- what this teaches us for future excerpt-aware runs
- notes that may inform later workflow or design adjustments

(Write reflections below. Do not turn this into a decision record;  
decisions, if any, should follow the normal lifecycle elsewhere.)
---

---

## Human reflection — editorial notes

### 1. Wat we zagen in de annotaties
De annotator herkende **“Sajuran”** correct als *GLOSSARY* (signaleren zonder beslissen).  
“Golongan VI” werd gelabeld als *HISTORICAL* — verdedigbaar, maar het wijst op een neiging
om classificatie-structuur snel als “historisch kader” te zien.

De volledige zin “Jang dinamakan sajuran …” werd als *HISTORICAL* gelabeld.
Dat lijkt eerder definitorisch dan historisch en toont lichte overreach:
bij twijfel had *NONE* beter gepast.

**Observatie:** de agent is voorzichtig, maar neigt bij definities te snel naar *HISTORICAL*.

### 2. Bias-signalen
- **Definition-bias:** definities worden geïnterpreteerd als “contextuitleg”.
- **Over-semantisering:** de agent probeert intentie te lezen i.p.v. alleen signalen te markeren.
- **Te weinig NONE:** de fallback-regel wordt niet altijd consequent toegepast.

Deze signalen zijn ontwerp-informatie, geen fouten.

### 3. Workflow-ervaring
**Sterk:**
- excerpt-binding + logs maken terugzoeken eenvoudig;
- outputs zijn consistent en reproduceerbaar;
- lifecycle-regels bleven intact.

**Minder:**
- payload bevat volledige console-output → ruis voor reviewers;
- geen snelle per-label review tooling.

### 4. Wat we leren
- definities → meestal GLOSSARY op kernterm, of NONE — niet automatisch HISTORICAL;
- runner kan later een schoon “annotations-only” veld toevoegen;
- reviewers documenteren twijfel i.p.v. corrigeren buiten lifecycle.

(End of reflection — no decisions taken.)

---
