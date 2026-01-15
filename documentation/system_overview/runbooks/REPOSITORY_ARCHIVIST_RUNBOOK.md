# Repository Archivist Runbook (Phase-6)

Status: runbook skeleton (can be extended, but not overridden)  
Related: prompts/repository_archivist.md, docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md, docs/navigation/EDITORIAL_INDEX.md, docs/P6_LOW_RISK_MIGRATION_CHECKLIST.md

---

## 1. Purpose

De Repository Archivist bewaakt de documentatiestructuur, naming conventions en vindbaarheid
van `docs/` en `prompts/`, zonder zelf bestanden te verplaatsen of te verwijderen.

Dit runbook beschrijft:

- wanneer de Archivist ingezet wordt,
- welke vragen hij beantwoordt,
- hoe zijn output wordt omgezet in menselijke acties (Codex + editor),
- hoe EDITORIAL_INDEX.md en DOCS_INFORMATION_ARCHITECTURE.md daarbij worden gebruikt.

---

## 2. When to use the Archivist

Gebruik de Repository Archivist in deze situaties:

1. **Wildgroei-signaal**  
   - De repo voelt “vol” of onoverzichtelijk (veel losse docs in `docs/`).
   - Er zijn meerdere vergelijkbare documenten (bijv. meerdere workflow-overzichten).

2. **Voorbereiding op migratie**  
   - Voorafgaand aan low-risk moves volgens P6_LOW_RISK_MIGRATION_CHECKLIST.md.
   - Wanneer je twijfelt of een doc in de juiste map/category zit.

3. **Nieuwe Phase-6 documenten**  
   - Bij introductie van nieuwe governance/workflow-docs:
     - vraag de Archivist of er overlap is,
     - en of de EDITORIAL_INDEX moet worden bijgewerkt.

De Archivist wordt niet automatisch gedraaid; hij wordt bewust ingeschakeld
via een Codex-sessie die zijn prompt gebruikt.

---

## 3. Archivist Behaviour (summary)

De Repository Archivist:

- leest alleen (geen moves, geen deletes),
- vergelijkt docs met de categorieën in DOCS_INFORMATION_ARCHITECTURE.md,
- signaleert:
  - duplicatie,
  - wildgroei,
  - docs die in een andere map logischer zouden zijn,
- produceert een rapport in het vaste template:

  ```text
  [ARCHIVIST_REPORT]
  Scope:
  Findings:
    - ...
  Risks:
    - ...
  ProposedTasks:
    - id:
      description:
      impact:
      suggested_phase:
  [/ARCHIVIST_REPORT]
  ```

Output is ALTIJD een voorstel, nooit een directe wijziging.

## 4. Standard Questions for the Archivist

Wanneer je een Archivist-run draait, richt de analyse op minstens:

Locatie vs. categorie

Past dit document in zijn huidige map volgens DOCS_INFORMATION_ARCHITECTURE.md?

Overlap

Bestaan er al docs met een vergelijkbare rol/naam?

Moeten deze worden samengevat of geclusterd?

Risico bij verplaatsen

Is dit doc low / medium / high risk bij migratie?

Moet een eventuele verplaatsing via low-risk checklist of via governance?

Index en navigatie

Moet EDITORIAL_INDEX.md een extra rij krijgen?

Moet een navigatie-doc (in docs/navigation/) worden bijgewerkt?

## 5. Handoff: From Archivist to Human Action

Typische flow:

Archivist-run

Codex draait de Archivist prompt met een duidelijke Scope
(bijv. “alle Phase-6 docs in docs/ root”).

Resultaat: één [ARCHIVIST_REPORT].

Interpretatie

Een menselijke editor bekijkt het rapport.

Bepaalt welke ProposedTasks:

direct als TODO-item in docs/CODEX_TODO.md moeten,

of vertaald worden naar een low-risk migratie-sessie.

Actie via Codex

Low-risk moves gebeuren via aparte Codex-sessies
(die P6_LOW_RISK_MIGRATION_CHECKLIST.md volgen).

Elke move wordt gelogd in docs/MIGRATION_NOTES.md en in docs/CODEX_SESSION_LOG.md.

Index-bijwerking

Na significante docs-wijzigingen:

update docs/navigation/EDITORIAL_INDEX.md (path/role/risico),

zo nodig DOCS_INFORMATION_ARCHITECTURE.md (categorie/zone).

De Archivist voert zelf nooit stap 3 of 4 uit; hij levert alleen input.

## 6. Boundaries & Non-Goals

De Repository Archivist:

doet NIET:

bestanden verplaatsen, hernoemen of verwijderen,

TODO’s aanpassen zonder expliciete opdracht,

beslissen wat canonical is,

runtime- of promptgedrag wijzigen.

doet WEL:

inconsistenties signaleren,

tekstuele voorstellen doen,

migratie-ideeën formuleren met risico-inschatting,

verwijzen naar de juiste ontwerpbronnen
(DOCS_INFORMATION_ARCHITECTURE, EDITORIAL_INDEX, manifest_p5.yaml).

## 7. Minimal Invocation Pattern (example)

Een typische Codex-sessie om de Archivist te gebruiken kan er zo uitzien:

Scope: "analyseer alle Phase-6 documenten onder docs/ en de navigatie in docs/navigation/."

Input: Archivist prompt + deze runbookreferentie.

Output: één [ARCHIVIST_REPORT] dat:

een korte Scope geeft,

Findings opsomt,

Risks benoemt (voor moves),

ProposedTasks voorstelt met passende Phase (P3/P4/P5/P6).

De concrete Codex-prompt blijft buiten dit document, maar moet altijd:

expliciet READ-ONLY zijn voor scans,

of expliciet beschrijven welke migraties in een vervolgsessie overwogen worden.

End of document.
