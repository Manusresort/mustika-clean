# ARCHIVIST REPORT — Cleanup Preparation Proposal (002)

[ARCHIVIST_REPORT]

Scope:
- Volledige documentstructuur, met nadruk op:
  canonical docs, governance, pilots/sandbox, phase-5 consolidatie,
  prompts, crew-runners en log-sporen.
- Doel: een VOORSTEL maken voor een latere “controlled cleanup”
  (Phase-6), zonder nu fysieke wijzigingen door te voeren.

Findings:
  - De repo bevat duidelijke categorieën (canonical / sandbox / consolidation),
    maar historische documenten en pilots lopen soms inhoudelijk door elkaar.
  - Sommige documenten functioneren in de praktijk als policy,
    terwijl ze formeel “consolidatie/uitleg” zijn.
  - Pilots, run-logs en rapporten zijn verspreid te vinden en vereisen
    vaak kennis van context om te begrijpen.
  - Prompts en agent-rollen staan goed beschreven, maar hun “thuisbasis”
    is niet altijd intuïtief voor nieuwe lezers.

Risks:
  - Reorganisatie zonder plan kan paden breken, tooling verwarren
    en reproduceerbaarheid verminderen.
  - Phase-5 documentatie kan per ongeluk beleidsstatus krijgen.
  - Logs en pilots kunnen uit beeld verdwijnen als ze niet zichtbaar
    worden gearchiveerd.

ProposedTasks:

  - id: CLEANUP_MAP_CANONICAL
    description: Maak één heldere index-pagina die *alle* canonical docs
                 beschrijft (met korte toelichting waarom ze canonical zijn).
    impact: verhoogt duidelijkheid en voorkomt verkeerd gebruik
    suggested_phase: P5 (documentair)

  - id: CLEANUP_ARCHIVE_STRATEGY
    description: Definieer een lichte “archive/” structuur voor oude pilots
                 en verouderde consolidatie-docs — alleen als governance
                 expliciet toestaat.
    impact: maakt ruimte zonder historische sporen te verliezen
    suggested_phase: P6 (governance-gated)

  - id: SAFE_MIGRATION_PLAN
    description: Voor elke toekomstige verplaatsing: documenteer
                 (a) oud pad, (b) nieuw pad, (c) reden, (d) update manifest,
                 (e) noteer in HUMAN_GATE_LOG.
    impact: volledige traceability van cleanup-acties
    suggested_phase: P6

  - id: PROMPTS_HOME_CLARITY
    description: Maak korte README in prompts-map die uitlegt welke
                 prompts productie-adjacent zijn en welke sandbox/test.
    impact: minder verwarring voor nieuwe contributors
    suggested_phase: P5

  - id: PILOT_LOG_DISCOVERY
    description: Voeg een overzichtsdocument toe dat wijst naar
                 alle pilots + bijbehorende logs.
    impact: betere vindbaarheid zonder structuur te wijzigen
    suggested_phase: P5

  - id: GOVERNANCE_BOUNDARIES_NOTE
    description: Korte notitie: wat mag nooit autonoom worden
                 verplaatst/verwijderd zonder Human Gate.
    impact: voorkomt riskante “opruimacties”
    suggested_phase: P5

MigrationPrinciples:
- geen fysieke verplaatsingen in Phase-5
- alles voorstel-only en human-gated
- elke verplaatsing in Phase-6 krijgt:
  manifest-update, README-redirect, log-entry, rollback-pad

[/ARCHIVIST_REPORT]

Note:
Dit document is signalerend en voorbereidend.
Er worden GEEN bestanden verplaatst, hernoemd of verwijderd.
