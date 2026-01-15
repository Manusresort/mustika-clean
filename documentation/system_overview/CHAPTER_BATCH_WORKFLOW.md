# Chapter / Batch Workflow Design

## Purpose
Legt vast hoe meerdere recepten/hoofdstukken veilig, traceerbaar en reproduceerbaar
verwerkt kunnen worden, zonder individuele kwaliteitscontrole te verliezen.

## Scope
- Batch = set van recepten (of een hoofdstuk)
- Alleen ontwerp & governance — geen runtime implementatie
- Geldt bovenop bestaande single-recipe pipeline

## Overview
1. Batch ingeven (lijst recepten / hoofdstukdefinitie)
2. Voorbereiding (metadata, expected outputs, logging-ID)
3. Per item:
   - Translation
   - Readability
   - Fidelity
   - Review & comments
4. Batch-level summary
5. Logging & artifacts

## Governance Touchpoints
- Orchestrator grijpt in bij inconsistenties tussen items, scope-drift of escalaties.
- Governance-agents worden automatisch geraadpleegd bij triggers zoals in WORKFLOW.md.
- STOP → governance-stop → human gate geldt per item en kan batch-breed escaleren als
  meerdere items hetzelfde risico tonen.
- Individuele fouten breken de batch niet automatisch; ze worden geïsoleerd en gelogd.

## Failure & Recovery
- retry limited
- mark item as pending review
- never silently drop items
- herstarten vereist expliciete logregel met reden en referentie naar eerdere run-ID
- partial batches blijven traceerbaar met duidelijke status per item

## Audit Trail
- per item: input-referenties, outputs, opmerkingen, status, escalaties
- per batch: batch-ID, itemlijst, samenvatting, exceptions, governance-notities
- relatie met CODEX_SESSION_LOG: batch-events worden gelogd als sessie-artefacten

## Risks / Non-Goals
- geen automatische publicatie
- geen automatische definitieve glossary-wijzigingen
- mensen beslissen — agents signaleren

## Alignment
- docs/WORKFLOW.md
- docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md
- docs/CODEX_META_PROMPT.md
