[CHAPTER_PREP_REPORT_SANTAN]

- TermFocus:
  santan (incl. spellingvarianten)

- CandidateUses (Decision Cards)
  * ContextType: ingredient
    * EvidenceSnippet: “Common English mappings include: ‘coconut milk’ / ‘coconut cream’” (docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_001.md#Context)
    * EvidenceRef: docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_001.md (Context section)
    * PossibleInterpretations: coconut milk (thinner extraction); coconut cream (thicker extraction)
    * RisksForReaders: culinary outcome shifts; misleading simplification; historical authenticity drift
    * CandidateGloss: “santan (coconut milk/cream; extraction-dependent)” — proposal-only
    * HumanGateTriggers: if used in reader-visible text or publication drafts

  * ContextType: technique
    * EvidenceSnippet: “term could refer to thin coconut extraction … or a thicker coconut cream depending on stage and local practice” (docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_002.md#Scenario)
    * EvidenceRef: docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_002.md (Scenario section)
    * PossibleInterpretations: staged extraction; timing-sensitive ingredient use
    * RisksForReaders: wrong technique; recipe failure; loss of historical method
    * CandidateGloss: “santan (stage-dependent coconut extraction)” — proposal-only
    * HumanGateTriggers: if technique is normalized or simplified

  * ContextType: extract (thick vs thin)
    * EvidenceSnippet: “Some recipes distinguish between thin and thick coconut liquid by technique rather than explicit naming.” (docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_001.md#Examples)
    * EvidenceRef: docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_001.md (Examples section)
    * PossibleInterpretations: implicit thin/thick distinction; contextual extraction
    * RisksForReaders: misreading yields wrong fat/texture outcomes
    * CandidateGloss: “santan (thick/thin extraction; context decides)” — proposal-only
    * HumanGateTriggers: if glossary resolves to a single fixed meaning

  * ContextType: substitute / unknown
    * EvidenceSnippet: “Readers may assume a single equivalent (‘coconut milk’) even when fat content matters.” (docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_001.md#Examples)
    * EvidenceRef: docs/PILOT_GLOSSARY_SANTAN_RUN_P3_SANTAN_001.md (Examples section)
    * PossibleInterpretations: substitution assumed by reader; use of canned vs fresh
    * RisksForReaders: substitution error; loss of cultural method; reader confusion
    * CandidateGloss: “santan (coconut derivative; do not assume single equivalent)” — proposal-only
    * HumanGateTriggers: if substitution is presented as equivalent

- ExpectedAnnotations (with labels)
  * [GLOSSARY_NOTE]: santan proposal-only gloss; highlight stage dependence.
  * [HISTORICAL_NOTE]: cooking context where extraction method is historically specific.
  * [LINGUISTIC_NOTE]: spelling/term stability; avoid auto-normalization.
  * [SAFETY_NOTE]: only if health/consumption implications appear; otherwise defer.
  * SAFETY_NOTE — when required:
    - wanneer keuze tussen santan kental vs encer de kooktijd/temperatuur beïnvloedt
    - wanneer canned vs fresh santan plausibel andere risico’s introduceert
    - wanneer vet-/waterscheiding impliciet voedselveiligheid raakt
    (altijd historisch framen, nooit modern medisch advies; escalate bij twijfel)

- KnownAmbiguities
  * santan kental vs santan encer (thick vs thin extraction)
  * fresh vs canned coconut derivatives
  * region-dependent practice and timing in recipes

- RelatedTerms
  * kelapa
  * minyak kelapa
  * ampas santan
  * blondo

- OCRRiskSpots
  * santan spelling variants in source not yet validated (type: REVIEW_REQUIRED; reason: no direct excerpt evidence)
  * any OCR symbol noise near ingredient quantities (type: DO_NOT_AUTOMATE; reason: meaning shift risk)
  * Example triggers (documentary only):
    - "santam" vs "santan." (type: REVIEW_REQUIRED; reason: punctuation changing reading)
    - gebroken regels rondom hoeveelheden (bijv. "sa\\ntan" gesplitst) (type: DO_NOT_AUTOMATE; reason: line-break ambiguity)

- LikelySoftStops
  * whenever santan is used as a fixed, single equivalent
  * whenever extraction stage is implied but not explicit
  * when readability pushes to simplify without annotation

- OpenQuestions
  * Are there chapter-specific instances distinguishing santan kental/encer explicitly?
  * Do any recipes imply substitution practices that require Human Gate review?
  * Is there reliable historical context for how santan is produced in the relevant period?

Status reminder:
Dit document blijft proposal-only. De aanvullingen verduidelijken traceability
en agent-signalering, maar autoriseren géén inhoudelijke wijzigingen.

[/CHAPTER_PREP_REPORT_SANTAN]
