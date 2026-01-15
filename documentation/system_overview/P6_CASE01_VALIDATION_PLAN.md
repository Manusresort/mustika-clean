# Case-01 Validation Plan (Excerpt-Aware Sandbox Run)

Status: READY  
Scope: Case-01 — SAYUR (lines 52–66)  
Intent: Validate excerpt-awareness, logging, and artefact layout — NOT content quality.

---

## 1. Objectives (wat we willen bevestigen)

We beschouwen deze run geslaagd wanneer:

- [ ] excerpt-metadata (id/source/version) verschijnt **in CLI/config → log → JSON**
- [ ] logbestand wordt geplaatst onder het juiste pad
- [ ] JSON-output verschijnt onder het juiste excerpt/run pad
- [ ] STOP-regels werken zoals ontworpen
- [ ] niets buiten de sandbox wordt aangeraakt
- [ ] een reviewer kan de hele keten volgen zonder te raden

Geen enkele inhoudelijke beslissing wordt in deze run canoniek.

---

## 2. Preconditions (moet kloppen vóór we iets draaien)

- [ ] excerpt voor Case-01 is locked  
- [ ] runner is geïmplementeerd volgens implementation guide  
- [ ] sandbox-schrijfpad is leeg of voorbereid  
- [ ] er is één duidelijke config voor Case-01  
- [ ] readiness-checklist in P6_CASE01_READINESS_PLAN.md staat op “pre-run ready”  
- [ ] iemand is aangewezen als reviewer (rol, geen naam)

Als één van deze faalt → documenteer → niet draaien.

---

## 3. Single-run procedure (de run zelf)

1️⃣ Start runner met Case-01:

python sandbox/crew/run_excerpt_workflow.py
--config sandbox/crew/case01_config.yaml
--excerpt-id sayur_052_066
--excerpt-source docs/P6_SAYUR_INTERNAL_WORK_CASE01.md
--excerpt-version locked-XXXX-XX-XX

yaml
Copy code

2️⃣ Wacht tot exit.  
3️⃣ Noteer exit-code.  
4️⃣ Verzamel:

- logpad (zoals in CLI weergegeven)
- outputdirectory (excerpt_id + run_id)
- eventuele foutmeldingen

**NIETS verplaatsen of corrigeren.**  
Artefacts blijven precies zoals geproduceerd.

---

## 4. Expected artefacts

### 4.1 Log (mandatory)

Pad:

sandbox/crew/run_logs/sayur_052_066/{run_id}_{timestamp}.log

css
Copy code

Header bevat minstens:

mode: excerpt-aware
excerpt_id: sayur_052_066
status: (COMPLETED | SOFT-STOP | GOVERNANCE-STOP | ERROR)
cli_config_mismatch: true/false

shell
Copy code

### 4.2 JSON outputs (mandatory if no STOP)

sandbox/crew/run_outputs/sayur_052_066/{run_id}/
annotator_primary.json
challenger_primary.json
(optional) crew_provisional.json

yaml
Copy code

Elk bestand bevat:

excerpt.id / excerpt.source / excerpt.version
run.id / run.timestamp

yaml
Copy code

Als `excerpt` of `run` ontbreekt → **GOVERNANCE-STOP**.

---

## 5. Validation checklist (door reviewer)

Reviewer beantwoordt:

- [ ] metadata consistent van CLI → log → JSON?
- [ ] outputpaden exact zoals design?
- [ ] STOP-regels correct toegepast?
- [ ] log leesbaar en voldoende informatief?
- [ ] artefacts bruikbaar voor human review?
- [ ] geen onverwachte writes buiten sandbox?

Resultaatlabel:

- **GO** — systeem werkt zoals ontworpen  
- **REWORK** — technische fixes nodig, opnieuw draaien  
- **DESIGN-QUESTION** — documentatie aanpassing nodig

Label + korte uitleg worden vastgelegd in `review_notes.md`
(of in CODEX_SESSION_LOG, afhankelijk van workflow).

---

## 6. Rollback (alleen voor sandbox-artefacts)

Indien run wordt ongeldig verklaard:

- verwijder:
  - `sandbox/crew/run_outputs/sayur_052_066/{run_id}/`
  - bijbehorende log
- voeg een korte notitie toe in `CODEX_SESSION_LOG.md`:
  - reden + verwijzing naar review

Canonical/Docs blijven onaangeroerd.

---

## 7. Out-of-scope for this validation

- geen inhoudelijke beoordeling van annotaties
- geen glossary-promotie
- geen vertaling
- geen beslissingen over publicatie

Deze run valideert **alleen het systeem**.

---

## 8. Exit criteria (wanneer Case-01 validation “klaar” is)

Case-01 validation wordt als afgerond beschouwd wanneer:

- [ ] één run succesvol is uitgevoerd
- [ ] reviewer heeft een GO / REWORK / DESIGN-QUESTION afgegeven
- [ ] bevindingen zijn gelogd
- [ ] eventuele REWORK opnieuw succesvol is gevalideerd

Daarna mag Case-01 gebruikt worden als referentie voor volgende excerpts.
