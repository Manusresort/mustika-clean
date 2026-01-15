# PHASE-3 FRAMING — Pilots, Safety & Learning

## 1. What Phase-3 really is
Phase-3 is de eerste **gecontroleerde interactie** tussen agents en echte content.
Niet om een product te maken — maar om te begrijpen hoe agents zich gedragen:

- hoe ze signaleren
- hoe governance ingrijpt
- hoe risico’s zichtbaar worden
- hoe logs en lifecycle samenwerken

Phase-3 is nadrukkelijk géén automatische productiestap.
Het is een observatiefase met tanden:

> Agents mogen fouten maken —  
> **maar alleen op manieren die we kunnen zien, uitleggen en terugdraaien.**

Geen onomkeerbare acties, geen stille wijzigingen,
geen output die automatisch “waar” wordt.

## 2. Objectives of Phase-3
Phase-3 heeft leerdoelen, geen productie-doelen.
We willen aantonen dat:

- agents de strategie, lifecycle en beperkingen respecteren
- governance-triggers afgaan waar dat hoort
- incidenten leiden tot governance-stop (en niet tot “doorgaan”)
- rollbacks daadwerkelijk bruikbaar zijn
- annotaties en signalen redactie ondersteunen — niet vervangen
- failure-modes zichtbaar worden in plaats van verborgen

We meten niet “hoeveel content klaar is”,
maar: **hoe goed het systeem zichzelf uitlegt**.

## 3. Scope & Boundaries
### In scope
- kleine, gecontroleerde pilot-batches
- documentair testen
- intentional failure cases
- glossary & terminology pilots
- OCR restoration pilots
- governance trigger validation

### Out of scope
- volledige boekbewerking
- automatisering zonder menselijke audit
- gebruik van Phase-3 output als eindproduct
- definitieve design- of publicatiebeslissingen
- “we hebben toch al 50 recepten — laten we ze gebruiken”

Phase-3 mag inzichten genereren,
maar **legt niets definitief vast**.

## 4. Data & Artefact Handling
Principes:
- pilots gebruiken **altijd kopieën**
- pilots draaien in **afgesloten sandboxes**
- pilots mogen **nooit canonical bronnen overschrijven**
- alle pilot-outputs zijn: **EXPERIMENTAL — NOT FOR PUBLICATION**

Concreet:
- elke pilot krijgt een eigen: `/sandbox/<pilot-id>/`
- elk artefact krijgt metadata: origin, step, pilot-id, timestamp, rollback-note
- canonical bronnen zijn read-only
- elke mutatie moet omkeerbaar én gelogd zijn

Phase-3 mag experimenteren — maar alleen met veilig, herleidbaar materiaal.

## 5. Pilot types
### 5.1 Translation + Fidelity Pilot
Doel: Fidelity signaleert afwijkingen, logt en corrigeert NIET.

### 5.2 Glossary Lifecycle Pilot
Doel: glossary blijft proposal-only en volgt lifecycle.

### 5.3 OCR Restoration Pilot
Doel: herstel blijft reversibel en gedocumenteerd.

### 5.4 Governance-Failure Simulation
Doel: aantonen dat soft-stop → governance-stop → human-gate werkt.

- **Glossary Pilot 1 — Lobak**  
  (proposal-only, lifecycle-driven, governance-stop demonstratie)

## Failure Notebook (verplicht)
Elke pilot bevat minimaal:
- één bewust opgewekte failure case
- expected vs actual
- lessons learned
- governance-evaluatie
- log-referenties

Doel: bewijzen dat **falen veilig en uitlegbaar is.**

## 6. Risk model for Phase-3
Content / Technical / Process / Human risk.
Mitigaties: labels, disclaimers, red-team, governance-triggers.

## 7. Human involvement model
Editors contextualiseren, governance besluit bij risico,
red-team daagt aannames uit,
human-gate = laatste escalatie.

## 8. Exit criteria
Phase-3 slaagt wanneer:
- governance-stops optreden waar verwacht
- niets ongedocumenteerd gebeurt
- rollbacks echt gebruikt worden
- pilots inzichten + failures opleveren
- we weten wat moet verbeteren vóór opschaling

> Phase-3 eindigt met **kennis, niet met een product.**

## 9. After Phase-3
Consolidatie → mogelijk aangepaste requirements →
veilige integratie-ontwerpen → gecontroleerde opschaling.

## Addendum — Phase-3 Status (Documentary)

Phase-3 has generated enough pilot evidence to support reflection and
readiness discussions. This does NOT mean Phase-3 is closed, and it does
NOT authorize Phase-4.

Phase-3 remains available as a learning space that can be reopened
whenever new risks, terminology conflicts, or governance uncertainties
appear. Its purpose remains unchanged: observe, document, and keep all
changes reversible.

Status framing:  
**LEARNING COMPLETE — NOT CLOSED — MAY REOPEN IF NEEDED.**

[METHODOLOGY_LOG]
Status note added for clarity. No phase transition declared.
[/METHODOLOGY_LOG]
