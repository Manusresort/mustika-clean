# ARCHIVIST REPORT — Phase 5 Alignment Check (001)

[ARCHIVIST_REPORT]

Scope:
- Phase-5 documenten, manifest_p5.yaml, en docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md.
- Doel: controleren of nieuwe consolidatie-documenten logisch zijn ingepast
  zonder structurele drift of ongeplande duplicatie.

Findings:
  - Phase-5 docs volgen de categorie "consolidation_phase5" en verwijzen niet
    naar zichzelf als beleid (correct).
  - Manifest en informatie-architectuur zijn consistent: canonical vs sandbox
    vs consolidatie zijn duidelijk onderscheiden.
  - Prompt-pattern, behaviour-criteria en evidence-doc zijn complementair
    (geen inhoudelijke duplicatie, wel duidelijke rolverdeling).
  - Archivist-rol zelf is nog niet expliciet genoemd in de architectuurkaart,
    maar functioneert feitelijk als ondersteunende governance-tool.

Risks:
  - Zonder periodieke alignment kan opnieuw document-sprawl ontstaan
    rond toekomstige pilots of Phase-6 voorbereidingen.
  - Phase-5 documenten zouden per ongeluk als "beleid" geïnterpreteerd kunnen
    worden als ze buiten hun context worden gelezen.
  - Nieuwe rapporten of analyses zouden verspreid kunnen raken wanneer geen
    vaste plek (archivist_reports/) wordt aangehouden.

ProposedTasks:
  - id: ARCHIVIST_NOTE_IN_ARCHITECTURE
    description: Vermeld Repository Archivist expliciet in docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md
                 als ondersteunende rol/documentcategorie (zonder structuur te wijzigen).
    impact: verbetert navigeerbaarheid en governance-transparantie
    suggested_phase: P5 (documentair)

  - id: PERIODIC_ALIGNMENT_CHECK
    description: Elke nieuwe pilot/consolidatie-set voorzien van één korte archivist-check
                 zodat document-sprawl vroeg wordt gesignaleerd.
    impact: voorkomt latere herstructureringslast
    suggested_phase: P5–P6 transition

  - id: CONSOLIDATION_TAG_CONVENTION
    description: Introduceer een lichte tag-conventie (bijv. "P5-CONSOL")
                 in front-matter van nieuwe documenten voor snelle herkenning.
    impact: verhoogt vindbaarheid zonder fysieke herstructurering
    suggested_phase: P5 (optioneel)

[/ARCHIVIST_REPORT]

Note:
Dit rapport is signalerend. Er worden GEEN bestanden verplaatst, hernoemd of
verwijderd en er worden GEEN inhoudelijke wijzigingen uitgevoerd.
