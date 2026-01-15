# Analyst Template — P5 Micropilot: Provisional Translation Discipline

Purpose:
Houvast geven bij het analyseren van P5_MICROPILOT_PROVISIONAL_*.log
zodat lifecycle en guardrails systematisch beoordeeld worden.

---

## 1. Run metadata

- Log file: `sandbox/crew/run_logs/...`
- Date/time:
- Runner: `codex_p5_micropilot_provisional_runner.py`
- Excerpts used:

---

## 2. Lifecycle sanity-check

Voor elk case / term / passage:

- decision_status: CANDIDATE / CREW_PROVISIONAL / READY_FOR_HUMAN
- decision_origin: agent / crew / meta / human
- rationale_logged: yes/no
- reopen_possible: yes/no
- challenge_open: yes/no

Checklist:

- [ ] Zijn er CANDIDATEs die nooit bekeken zijn door de crew?
- [ ] Zijn er CREW_PROVISIONAL beslissingen zonder rationale?
- [ ] Is READY_FOR_HUMAN alleen gebruikt bij risk / impasse / high impact?

Korte notities:

---

## 3. Escalatie-gedrag

- Aantal escalaties naar READY_FOR_HUMAN:
- Redenen (kort):

Markeer:

- [ ] Escalaties voornamelijk bij echte risico’s
- [ ] Geen escalatie bij normale onzekerheid / woordnuance
- [ ] Geen ongedocumenteerde “hard stops”

Observaties:

---

## 4. Agent vs Crew gedrag

Annotator:

- Neiging tot:
  - [ ] te voorzichtig
  - [ ] te stellig
  - [ ] ongeveer goed

Challenger:

- Neiging tot:
  - [ ] translation-expectation bias (INFO)
  - [ ] overreach (afdwingen van vertaling)
  - [ ] helpende signalering

Crew:

- Sluit beslissingen meestal op niveau:
  - [ ] CANDIDATE (te voorzichtig)
  - [ ] CREW_PROVISIONAL (gewenst)
  - [ ] READY_FOR_HUMAN (te vaak?)

Korte voorbeelden (case labels + 1 zin):

---

## 5. Meta / Codex gedrag

- Heeft meta:
  - [ ] eerst docs/guardrails geraadpleegd (af te leiden uit gedrag)?
  - [ ] onnodige vragen “geëxporteerd” naar de human?
  - [ ] clustering gedaan i.p.v. losse micro-vragen?

Notities:

---

## 6. Bias & Patterns (niet fixen, alleen signaleren)

- translation-expectation patterns:
- under/over-confident crew decisions:
- verrassende failure-modes:

---

## 7. Overall judgement

- [ ] Lifecycle wordt praktisch gevolgd
- [ ] Guardrails worden gerespecteerd
- [ ] Escalaties zijn zeldzaam en zinnig

Verdict:
- [ ] OK — geen actie nodig
- [ ] Needs follow-up (kleine clarificaties)
- [ ] Unclear — meer runs / meer context nodig

Aanbevolen vervolgstap (kort):

End of template.
