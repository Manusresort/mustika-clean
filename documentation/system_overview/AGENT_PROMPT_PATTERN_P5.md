# Agent Prompt Pattern — Phase-5 (Concept)

Status: GUIDELINE — NOT A RUNTIME APPROVAL  
Scope: prompts in `prompts/*.md` (agents, meta-agents, reviewers)

Purpose:
Zorgen dat elke agent-prompt consistent, audit-baar en omkeerbaar is — 
met één duidelijk contract per rol, en zichtbare grenzen rond autonomie & governance.

Motto:
documenteer → signaleer → escaleer  
niet: interpreteren → beslissen → corrigeren

---

## 1️⃣ Structure — elke agent-prompt bevat deze secties

### 1. ROLE (1 zin)
Wat je *wel* doet — concreet en smal.

### 2. MISSION BOUNDARIES
- Je doet alleen: …
- Je doet niet: …
- Zaken buiten je remit → loggen, niet oplossen.

### 3. INPUT
Wat je ontvangt (formaat, velden, limieten).  
Geen impliciete aannames.

### 4. OUTPUT CONTRACT (strikt)
Machine-checkbaar (bijv. JSON).  
Verplichte velden + voorbeeld.

### 5. RULES (kort & testbaar)
Max. 6–8 regels. Geen vage formuleringen.

### 6. UNCERTAINTY & ESCALATION
- bij twijfel: documenteer, beslis niet  
- soft-stop → governance-stop → Human Gate  
- gebruik NONE/AMBIGUOUS waar passend  
- nooit “best guess”

### 7. FORBIDDEN
Geen vertalingen, equivalents, normalisatie, OCR-correcties, glossary-beslissingen, of handelingen die lezer-interpretatie kunnen verschuiven.

### 8. LOGGING EXPECTATION
Gebruik zichtbare tags (bijv. `[AMBIGUOUS]`, `[ESCALATE-HUMAN]`) + 1–2 regels rationale.  
Altijd reversibel.

### 9. PURPOSE REMINDER
Kort: deze agent signaleert — beslist niet.

---

## 2️⃣ Quality checklist (review vóór gebruik)

| Vraag | OK wanneer |
|---|---|
| Eén taak? | Eén duidelijke verantwoordelijkheid |
| Meetbaar? | Output valideerbaar |
| Governance? | Soft-stop / Human Gate expliciet |
| Bias zichtbaar? | Signalerend, niets verbergen |
| Geen beslissingen? | Geen equivalents/adviezen |
| Reversibel? | Alles log-baar & terugdraai­baar |

---

## 3️⃣ Examples (kort)

**Annotator — OK**  
Labels + reason, geen vertaling, ambiguity markeren, JSON only.

**Challenger — OK**  
Checkt rule-violations; gebruikt issue-types en INFO/WARNING/BLOCKER; eist niets.

---

## 4️⃣ Niet wat dit document doet

- geen nieuwe governance  
- geen autorisatie om runs te doen  
- geen verplichte herschrijfactie zonder review

Het harmoniseert — het beslist niets.

---

## 5️⃣ Adoptie (Phase-5)

1. Nieuwe prompts volgen dit patroon.  
2. Bestaande prompts labelen:  
   `compliant / needs-clarification / defer-to-governance`.  
3. Alleen kleine documentaire tweaks; grotere wijzigingen → governance-review.

---

## 6️⃣ Relatie met autonomie & veiligheid

Autonomie = laag risico, omkeerbaar.  
Lezer-impact → Human Gate.  
Bij twijfel: document → defer.

---

*Concept — Phase-5 tooling document.*
