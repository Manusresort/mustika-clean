# Production Guardrails — Autonomy Matrix (Phase 5)

Status: documentation (guidance).  
Purpose: helder maken welke actoren welke beslissingen
mogen nemen — individueel, als crew, via Codex/meta, of via Human Gate.

Dit document werkt SAMEN met:
- P5_DECISION_LIFECYCLE.md
- P5_USER_PREFERENCES.md
- CANONICAL_INDEX.md

> Core principle:
> Agents PREPARE.  
> Crews DECIDE provisionally.  
> Meta ORCHESTRATES.  
> Humans decide when consequences become real.

---

## 1. Decision Lifecycle (reference)

Zie: **P5_DECISION_LIFECYCLE.md**.

Kernstaten:

1) CANDIDATE_TRANSLATION — agent-voorstel  
2) CREW_PROVISIONAL — voorlopig bevestigd, reopenable  
3) READY_FOR_HUMAN_REVIEW — mogelijk gevoelig / impactvol  
4) CANONICAL — alleen na Human Gate

Alle provisionele beslissingen zijn:
- traceable
- challenge-baar
- reversibel

---

## 2. Autonomy Matrix — Who May Do What

### A) Individual Agents

**MAY**
- candidate translations voorstellen
- annoteren, labelen, ambiguïteit signaleren
- risico’s markeren (INFO/WARNING/BLOCKER)
- issues escaleren naar “crew discussion”

**MUST NOT**
- iets “definitief” verklaren
- repo-structuur wijzigen
- andere agents overrulen buiten crew-proces

Output is altijd: *voorstel*.

---

### B) Crew (multi-agent)

**MAY**
- consensus vertaalkeuzes maken (CREW_PROVISIONAL)
- annotaties harmoniseren
- translation-issues sluiten met rationale
- items markeren als READY_FOR_HUMAN_REVIEW

**CONDITIONS**
- reasoning + alternatieven gelogd
- beslissingen reopenable
- geen bron / repo structuur wijzigen
- geen directe publicatie-consequentie

Output is: *provisionally binding* (voor werk).

---

### C) Codex / Meta-Agent

**MAY**
- beslissingen clusteren en ordenen
- zwakke rationale laten heropenen
- bepalen of iets richting READY_FOR_HUMAN_REVIEW gaat
- defaults toepassen o.b.v. prefs & guardrails
- éérst docs lezen, dán pas vragen

**MUST NOT**
- CANONICAL zetten
- governance wijzigen
- paden/structuur veranderen
- “human approval” impliceren zonder bewijs

Rol: *regisseur & vraag-compressor*.

---

### D) Human Gate

**Required for**
- publicatie-nabije vertalingen
- structurele repo-aanpassingen
- safety / cultural-harm / legal risico’s
- normatieve/historische oordelen
- acties met onomkeerbare gevolgen

Humans beslissen **wanneer impact reëel wordt**.

---

## 3. Escalation Rules

Agents / crews escaleren ALLEEN wanneer:

- publicatie-impact vermoed  
- veiligheid / harm risico  
- structurele repo-effecten  
- onoplosbare inhoudelijke impasse

Niet escaleren voor:
- normale onzekerheid
- woordkeuze-nuance
- interne werkbeslissingen

---

## 4. Logging Expectations

Elke promotie in de lifecycle bevat:

- decision_status
- decision_origin (agent/crew/meta/human)
- rationale_logged: true
- challenge_open / reopen_possible (ja/nee)

Zonder log = beslissing telt niet.

---

## 5. Relationship to Governance

Deze guardrails:
- beschrijven praktijkgedrag (Phase 5),
- vervangen géén governance-policies,
- en worden pas normatief na Human Gate-goedkeuring.

> Reversibility before speed.  
> Clarity before cleverness.

End of document.
