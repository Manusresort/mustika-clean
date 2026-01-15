# GOVERNANCE — Mustika Rasa (MVP)

## Harde regels (MUST / MUST NOT)

MUST:
- human-in-the-loop expliciet (review_required, incident, closure_needed)
- signal → gate → closure is zichtbaar en traceerbaar
- indices zijn afgeleid van filesystem

MUST NOT:
- schrijven naar `canonical/`
- closures muteren (closures zijn immutable)
- auto-promotion naar canonical

---

## Human-in-the-loop (in deze repo)

Human-in-the-loop betekent dat relevante signalen zichtbaar worden in de inbox:
- `incident` (validator fail)
- `gate` (blocking gate)
- `review_required` (challenger issues of open proposal)
- `closure_needed` (required_closure.json)

ADDED: The inbox/review queue is a visibility aid. Its signals indicate items that require attention or review; only the presence of `closure_needed` marks an explicit decision requirement. Other signals do not imply urgency, priority, or mandatory resolution.

ADDED: Deze signalen geven zichtbaarheid in de Proposal en Decision fases (review_required betreft open proposals; closure_needed markeert decisions) en verplaatsen niets automatisch—de mens blijft verantwoordelijk.

ADDED: “Reproduceerbaar” betekent hier dat artefacten audit- en vergelijkbaar zijn voor interne beslissingen (run logs, index regressie, auditrapporten), niet dat exacte reruns identiek zijn of automatisch herhaald worden.

Deze items vereisen expliciete menselijke review of expliciete deferral.

### Required closure — as-built lifecycle consequence

- `required_closure.json` is presence-based.
- Zolang het bestand bestaat, verschijnt `closure_needed` in de inbox.
- Het bestaan van een closure verwijdert dit item niet automatisch.
- Beheer van dit bestand is operationele verantwoordelijkheid.

ADDED: Dit markeert de Decision-fasegrens; required closures documenteren een besluit zonder publicatie of canonical status te impliceren.

---

## Closures zijn immutable

- Closures worden als `closures/<closure_id>/closure.json` geschreven.
- Als `closure.json` al bestaat, mag hij niet worden overschreven.
- Immutability is onderdeel van de audit‑trail.

ADDED: Daardoor zijn closures Decision-fase artefacten binnen de MVP-Input → Proposal → Decision-keten.

---

## Canonical is read-only

- `canonical/` wordt niet door tooling geschreven.
- Canonical updates gebeuren buiten dit MVP en via expliciete governance.

ADDED: Canonical-eligible besluitvorming ligt buiten dit MVP en valt onder separaat governancewerk.

---

## Indices zijn afgeleid

- `indices/*.json` worden door `indexer.py` gegenereerd.
- UI en API lezen indices; ze schrijven niet direct naar filesystem.
- Als indices ontbreken of leeg zijn, is dat geen fout in de data, maar een afgeleide toestand.
