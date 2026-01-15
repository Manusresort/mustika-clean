# Source of Truth — Mustika Rasa

## 1. Doel van dit document
Vastleggen welke bestanden in deze repo als source of truth gelden en welke alleen afgeleid, optioneel of archief zijn. Geen inhoudelijke wijzigingen.

## 2. Canonieke bronnen
- Indonesische brontekst:
  Pad: `SOURCE_CANON/step3_canonical/`
  Status: CANON (bevestigd)
  Opmerking: canonstatus is bevestigd.

## 3. Afgeleide maar bindende bronnen
- Step5 mechanische extractie:
  Pad: `DERIVED/step5_extraction/`
  Omvang (aantal RBs): 28 (RB-0001..RB-0028)
  Status: DERIVED
- Step6 annotatiepakket:
  Bestanden: `DERIVED/step6_annotations_frozen/handover_STEP6_ANNOTATION_20251222_135220.tar.gz` + `.sha256`
  Checksum: .sha256 aanwezig (verificatie niet uitgevoerd)
  Status: bevroren

## 4. Niet-canonieke / optionele lagen
- PhaseA Safety & Science:
  Pad: `OPTIONAL/phaseA_safety_science/`
  Status: OPTIONAL / bewust beëindigd en vervangen
  Toelichting: traject is bewust beëindigd ten gunste van de huidige canon/flow.
- Step6 working annotaties:
  Pad: `DERIVED/step6_annotation_working_optional/`
  Status: OPTIONAL (aanvullend)

## 5. Overige projectgovernance
- Governance:
  Pad: `WORK/governance/`
  Status: DERIVED (procesdocumenten, niet canoniek)

## 6. Gebruikregels
- Analyse, vertaling en publicatie mogen uitsluitend steunen op:
  - `SOURCE_CANON/step3_canonical/`
  - `DERIVED/step5_extraction/`
  - `DERIVED/step6_annotations_frozen/`
- Overige bestanden zijn ondersteunend of archief.
