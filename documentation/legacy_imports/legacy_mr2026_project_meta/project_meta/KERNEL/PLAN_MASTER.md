# PLAN_MASTER — Mustika Rasa (Editie A)

## 0. Doel en functie van dit document

Dit document beschrijft het canonieke projectplan voor de academische editie
(Editie A) van *Mustika Rasa*.

Het PLAN_MASTER document:
- definieert projectfasen en hun onderlinge afhankelijkheden;
- legt vast welke stappen zijn afgerond, actief of gepland;
- fungeert als referentie voor consistente uitvoering en overdracht.

Dit document bevat geen uitvoeringslogs en geen inhoudelijke correcties.

---

## 1. Projectdoel (samenvattend)

Het doel van dit project is het realiseren van een wetenschappelijk
verantwoorde editie van *Mustika Rasa* met maximale bronintegriteit.

Kernprincipes:
- geen stille correcties;
- zichtbaarheid van onzekerheid;
- expliciete scheiding tussen bron, afleiding en interpretatie;
- file-based workflow, zonder verborgen context.

---

## 2. Bronhiërarchie en mappenstructuur (samenvatting)

### Canonieke bron
- `SOURCE_CANON/step3_canonical/`
  Canonieke Indonesische brontekst (Editie A-ID)

### Afgeleide lagen
- `DERIVED/step4_structure/`
- `DERIVED/step5_extraction/`
- `DERIVED/step6_annotations_frozen/`

### Projectgovernance en planning
- `project_meta/KERNEL/`
- `WORK/governance/`
- `WORK/logs/`
- `WORK/qc/`

### Archief en optioneel
- `ARCHIVE/`
- `OPTIONAL/phaseA_safety_science/`

---

## 3. Overzicht projectfasen

### Fase 1 — OCR
Status: afgerond  
Beschrijving: initiële OCR van bronmateriaal (PDF/scan).

---

### Fase 2 — OCR-vetting
Status: afgerond  
Beschrijving:
- identificatie van systematische OCR-fouten;
- vastlegging van risico’s en failure signatures;
- expliciete keuze om geen automatische correcties toe te passen.

---

### Fase 3 — Vastlegging canonieke brontekst
Status: afgerond  
Documentatie:
- `project_meta/STEP3_BRONTEXT_STATUS.md`

Beschrijving:
- stabilisatie van de Indonesische brontekst;
- plaatselijke correctie van ondubbelzinnige OCR-fouten;
- expliciete zichtbaarheid van onzekerheden;
- formele bevriezing van de tekst als Editie A-ID.

---

### Fase 3b — Brontekstconsolidatie & lacunedetectie
Status: gepland / actief

#### Doel
Het verhogen van de betrouwbaarheid en leesbaarheid van de canonieke
Indonesische brontekst door:
- verdere reductie van evidente OCR-ruis;
- inhoudelijke lezing op samenhang;
- expliciete detectie en documentatie van lacunes en bron-discrepanties.

Deze fase beoogt **geen reconstructie** van ontbrekende tekst.

#### Context en afhankelijkheden
Fase 3b is mogelijk en noodzakelijk geworden door inzichten uit:
- OCR-vetting (kennis van failure signatures);
- structurele extractie (Stap 4/5);
- annotatiefasen (Stap 6);
- vergelijking tussen scan/PDF en fysiek origineel.

#### Scope (wel / niet)
Wel:
- corrigeren van onmiskenbare OCR-fouten;
- signaleren van abrupte overgangen;
- markeren van mogelijke ontbrekende of verwisselde pagina’s;
- documenteren van scan ↔ boek-discrepanties.

Niet:
- invullen van ontbrekende tekst;
- normalisatie of modernisering;
- interpretatieve correcties;
- stilzwijgende bronwijzigingen.

#### Werkwijze (behapbaar)
- pagina-voor-pagina binnen `SOURCE_CANON/step3_canonical/`;
- correcties alleen bij absolute zekerheid;
- observaties vastleggen buiten de brontekst.

#### Vastlegging
- `project_meta/BRON_LACUNES.md`  
  (observaties over lacunes, volgordeproblemen, onzekerheden)

#### Stopcriterium
Fase 3b is afgerond wanneer:
- de tekst inhoudelijk leesbaar is zonder voortdurende OCR-ruis;
- alle opvallende lacunes expliciet zijn gedocumenteerd;
- verdere verbetering alleen mogelijk is via nieuw bronmateriaal.

---

### Fase 4 — Structurele en mechanische extractie
Status: afgerond  
Beschrijving:
- receptafbakening;
- structurele analyse;
- RB-extracts (RB-0001..RB-0028).

Geen herhaling gepland.

---

### Fase 5 — Annotaties (historisch / terminologisch)
Status: afgerond en bevroren  
Bron:
- `DERIVED/step6_annotations_frozen/`

Beschrijving:
- contextuele annotaties;
- terminologie en structuuraanduidingen;
- geen safety- of interpretatieve lagen.

---

### Fase 6 — Vertaling (Editie A)
Status: gepland (na afronding Fase 3b)

Beschrijving:
- wetenschappelijk verantwoorde vertaling;
- behoud van expliciete onzekerheden;
- geen stilzwijgende tekstcorrecties.

---

### Fase 7 — Eventuele nieuwe editie (optioneel)
Status: toekomstig / optioneel

Beschrijving:
- nieuwe OCR of her-scan;
- reconstructie van lacunes;
- resulteert in een **nieuwe editie**, niet in wijziging van Editie A.

---

## 4. Continuïteit en overdracht

- Projectkennis wordt vastgelegd in bestanden, niet in chatsessies.
- Elke werksessie eindigt met een handover-snapshot in:
  `project_meta/HANDOVERS/`
- Nieuwe sessies starten altijd vanuit:
  - `project_meta/KERNEL/`
  - laatste handoverbestand.

---

## 5. Slotopmerking

Dit PLAN_MASTER document is bindend voor uitvoering,
maar kan worden aangevuld of herzien via expliciete besluiten
die worden vastgelegd in `project_meta/KERNEL/DECISIONS.md`.

Zonder expliciet besluit worden eerdere fases niet heropend.
