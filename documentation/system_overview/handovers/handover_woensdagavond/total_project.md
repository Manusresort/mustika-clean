# Mustikarasa Project — Totale Uiteenzetting (feitelijk)

Dit document beschrijft het huidige project zoals het in de repository is ingericht.
Alle uitspraken zijn gebaseerd op de aanwezige bestanden in deze repo en de expliciete instructies daarin.

## 1) Projectdoel en context

Het project bouwt een gecontroleerde, multi‑agent vertaal- en redactie‑workflow voor het Mustikarasa‑kookboek met CrewAI en Mistral via Ollama.
De kernpipeline draait als drie fasen: Translation → Readability → Fidelity.
De rol van de Codex‑laag is governance, organisatie en reproduceerbare uitvoering via de terminal.

## 2) Repository‑structuur (actuele bestandstoestand)

Top‑level (selectie):
- `mustikarasa_codex_cli.py`
- `test_multi_agent_fidelity.py`
- `mustikarasa_agents.py`
- `prompts/` (alle agent‑prompts)
- `docs/` (documentatie en governance)
- `data/` (input/output)
- `test_multi_agent.py` (multi‑agent test)
- `test_mistral_agent.py` (single‑agent test)
- `simple_agent_mistral.py` (leeg bestand)

Prompts‑map (actuele lijst):
- `prompts/annotation_agent.md`
- `prompts/book_structure_agent.md`
- `prompts/challenger_agent.md`
- `prompts/cohesion_agent.md`
- `prompts/continuity_agent.md`
- `prompts/cultural_historical_editor.md`
- `prompts/design_agent.md`
- `prompts/fidelity.md`
- `prompts/glossary_agent.md`
- `prompts/handover_agent.md`
- `prompts/image_agent.md`
- `prompts/methodology_archivist.md`
- `prompts/orchestrator.md`
- `prompts/readability.md`
- `prompts/recipe_editor.md`
- `prompts/repository_archivist.md`
- `prompts/research_agent.md`
- `prompts/table_editor.md`
- `prompts/technical_advisor.md`
- `prompts/template_agent.md`
- `prompts/translation.md`
- `prompts/troubleshooting_agent.md`

Docs‑map (actuele lijst):
- `docs/AGENTS.md`
- `docs/CODEX_META_PROMPT.md`
- `docs/CODEX_META_PROMPT.backup.1767359806`
- `docs/CODEX_SESSION_LOG.md`
- `docs/CODEX_TODO.md`
- `docs/CHAPTER_BATCH_WORKFLOW.md`
- `docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md`
- `docs/CONSOLIDATION_AUDIT_01.md`
- `docs/CONSOLIDATION_TODO.md`
- `docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md`
- `docs/GLOSSARY_PILOT_REPORT.md`
- `docs/10-governance/GOVERNANCE_INTEGRATION_DESIGN.md`
- `docs/10-governance/GOVERNANCE_TEST_SCENARIO_1.md`
- `docs/10-governance/GOVERNANCE_TEST_SCENARIO_2.md`
- `docs/10-governance/GOVERNANCE_TESTS_PLAN.md`
- `docs/PHASE3_FRAMING.md` (Phase-3 strategisch kader)
- `docs/PILOT_GLOSSARY_LOBAK.md`
- `docs/PILOT_GLOSSARY_LOBAK_RUN_P3_LOBAK_001.md`
- `docs/REQUIREMENTS.md`
- `docs/REQUIREMENTS_CHANGE_PROCESS.md`
- `docs/RESEARCH_GLOSSARY.md`
- `docs/RESEARCH_OCR_HISTORY.md`
- `docs/RESEARCH_OLD_REPO.md`
- `docs/VISION_AND_STRATEGY.md`
- `docs/CAPABILITY_AGENT_MAP.md` — overzicht wie welke capability draagt, inclusief gaps & overlaps (bron voor ontwerpbeslissingen)
- Editorial / Content Foundations
  - `docs/EDITORIAL_CAPABILITIES.md` — redactionele normenkaders voor vertaling en annotatie van Mustika Rasa.

Docs‑structuur en vindbaarheid worden ontworpen in `docs/navigation/DOCS_INFORMATION_ARCHITECTURE.md`;
nieuwe docs volgen dit ontwerp (geen moves zonder expliciete taak).

Data‑map (actuele inhoud):
- `data/origineel/hoofdstuk1.txt`
- `data/hoofdstuk1_rough_nl_dummy.txt`
- `data/output/hoofdstuk1_fidelity_run.txt`
- `data/output/hoofdstuk1_recipe_cli_prompts.txt`
- `data/output/hoofdstuk1_recipe_cli_todo_check.txt`
- `data/vertalingen/` (leeg)

## 3) Technische basis en runtime‑vereisten

### 3.1 CrewAI + Ollama
In `mustikarasa_agents.py`:
- De LLM wordt geconfigureerd als:
  - model: `ollama/mistral`
  - base_url: `http://localhost:11434`
  - temperature: `0.3`
- In comments staat: Ollama moet draaien met model `mistral` en `OPENAI_API_KEY` is een dummy‑key.

### 3.2 Python‑entrypoints

#### 3.2.1 Primair CLI‑entrypoint
`mustikarasa_codex_cli.py` biedt een `recipe`‑subcommand:
- Vereiste arguments:
  - `--english` (pad naar Engelse brontekst)
  - `--rough-nl` (pad naar ruwe NL‑vertaling)
- Optioneel:
  - `--output` (pad om finale output te schrijven; anders stdout)
- Gedrag:
  - controleert of input‑bestanden bestaan
  - leest teksten met UTF‑8
  - roept `run_pipeline(...)` uit `test_multi_agent_fidelity.py` aan
  - schrijft output naar bestand of stdout
  - maakt output‑parent‑dirs aan indien nodig
- Output formatting:
  - `format_result_for_output` accepteert zowel string als dict
  - dict‑fallback verwacht keys `text` en `remarks`

#### 3.2.2 Pipeline‑script (3 fasen)
`test_multi_agent_fidelity.py` bevat:
- `run_pipeline(english_text, rough_dutch_text) -> str`
- Fase 1: Translation Quality
- Fase 2: Readability
- Fase 3: Fidelity
- Fase 3 outputformat:
  - definitieve Nederlandse tekst
  - lege regel
  - `Opmerkingen:` met bullets of `(geen)`
- Er is ook een CLI‑modus in hetzelfde bestand, maar de primaire “hoofdknop” is `mustikarasa_codex_cli.py`.

#### 3.2.3 Test‑scripts
- `test_multi_agent.py`: demo met translation + readability en orchestrator.
- `test_mistral_agent.py`: single‑agent vertaaltest met CrewAI LLM.

## 4) Workflow (huidige 3‑fasen pipeline)

### 4.1 Fase‑keten (in code vastgelegd)
1. **Translation Quality**
   - Input: Engelse brontekst + ruwe NL‑vertaling
   - Output: verbeterde NL‑tekst (zonder uitleg)
2. **Readability**
   - Input: output van fase 1
   - Output: vloeiende, moderne NL‑tekst zonder meta‑uitleg
3. **Fidelity**
   - Input: Engelse brontekst + output van fase 2
   - Output: NL‑tekst + `Opmerkingen`‑sectie over mogelijke betekenisafwijkingen

### 4.2 Handover in de pipeline
- Fase 1 output wordt doorgegeven naar fase 2.
- Fase 2 output wordt doorgegeven naar fase 3.
- Fase 3 output is eindresultaat voor CLI‑output.

## 5) Prompt‑systeem (governance‑regel)

### 5.1 Prompt‑bron van waarheid
- Alle prompts staan in `prompts/*.md`.
- `mustikarasa_agents.py` leest alleen de secties `## Goal` en `## Backstory` via `load_prompt_sections(...)`.
- De code bevat geen inline promptstrings voor agents.

### 5.2 Promptformaten (per categorie)

#### 5.2.1 Kern‑agents met Goal/Backstory
Deze prompts bevatten alleen Goal + Backstory:
- `prompts/translation.md`
- `prompts/readability.md`
- `prompts/fidelity.md`
- `prompts/orchestrator.md` (plus extra gedrag‑secties)
- `prompts/cultural_historical_editor.md`
- `prompts/book_structure_agent.md`
- `prompts/annotation_agent.md`
- `prompts/recipe_editor.md`
- `prompts/table_editor.md`
- `prompts/image_agent.md`
- `prompts/cohesion_agent.md`
- `prompts/challenger_agent.md`
- `prompts/design_agent.md`
- `prompts/continuity_agent.md`

#### 5.2.2 Agents met vaste output‑formats
Deze prompts definiëren expliciete output‑structuren:
- `prompts/template_agent.md` → `[TEMPLATE_DEFINITION]`
- `prompts/research_agent.md` → `[RESEARCH_REPORT]` + Reference Corpus
- `prompts/glossary_agent.md` → `[GLOSSARY_PROPOSALS]`
- `prompts/methodology_archivist.md` → `[METHODOLOGY_LOG]`
- `prompts/technical_advisor.md` → `[MODEL_ADVICE]`
- `prompts/troubleshooting_agent.md` → `[INCIDENT_REPORT]`

## 6) Agents: rollen, implementatie en status

### 6.1 Agents in code (geïmplementeerd in `mustikarasa_agents.py`)
Deze agents bestaan als `Agent(...)` in code en laden prompts uit `prompts/`:
- Orchestrator
- Translation Quality Agent
- Readability Editor
- Cultural‑Historical Editor
- Book Structure Agent
- Annotation Agent
- Recipe Editor
- Table Editor
- Image Agent
- Cohesion Agent
- Fidelity Agent
- Challenger Agent
- Design Agent
- Continuity Agent

### 6.2 Agents in `docs/AGENTS.md`
`docs/AGENTS.md` bevat:
- korte rolbeschrijvingen per agent
- verwijzingen naar promptbestanden
- een status‑tabel met prompt/code‑status

De status‑tabel vermeldt onder meer:
- **Actief (prompt + code)**: Translation, Readability, Fidelity, Orchestrator, Cultural/Historical, Annotation, Continuity/Cohesion, Design, Challenger.
- **Ontworpen (prompt aanwezig, nog niet geïntegreerd)**: Methodology Archivist, Technical Advisor, Troubleshooting Agent, Glossary / Terminology Manager, Research / Historical Knowledge Agent, Repository Archivist / Documentation Admin.
- **Concept**: OCR / Source Integrity Agent, Batch Governor, Meeting / Redaction Agent.

## 7) Governance‑lagen en handovers tussen agents

### 7.1 Orchestrator (governance‑laag)
`prompts/orchestrator.md` bevat:
- **Template‑aware behaviour**:
  - raadpleegt Template Agent eerst
  - behandelt `TEMPLATE_DEFINITION` als contract
  - stuurt agents aan om outputs in template‑structuur te plaatsen
  - bij overtreding: retry, daarna Troubleshooting Agent
  - logt template‑versies voor Methodology Archivist
- **Research‑aware behaviour**:
  - raadpleegt Research Agent voor `RESEARCH_REPORT`
  - gebruikt `RelevantFiles` voor Annotation Agent en Glossary Agent
  - gebruikt `KeyInsights`/`Recommendations` voor Methodology Archivist en Technical Advisor

### 7.2 Template Agent (structurele contracten)
`prompts/template_agent.md`:
- definieert `TEMPLATE_DEFINITION` met `Name`, `Version`, `Status`, `Sections`, `Guidance`, `BackwardCompatibility`, `ChangeProposal`.
- mag geen inhoud genereren, alleen structuur.

### 7.3 Research Agent (historische kennis)
`prompts/research_agent.md`:
- levert `RESEARCH_REPORT` met `Scope`, `Summary`, `RelevantFiles`, `KeyInsights`, `OpenQuestions`, `Recommendations`.
- verplicht Reference Corpus te raadplegen en expliciet te verwijzen naar bestaande reports.

### 7.4 Glossary Agent (terminologie)
`prompts/glossary_agent.md`:
- levert `GLOSSARY_PROPOSALS` met `Terms` en `Meta`.
- mag geen definitieve terminologiebeslissingen afdwingen.

### 7.5 Methodology Archivist (audit trail)
`prompts/methodology_archivist.md`:
- levert `METHODOLOGY_LOG` met context, beslissing, rationale, impact, human review, artifacts.

### 7.6 Technical Advisor (modelstrategie)
`prompts/technical_advisor.md`:
- levert `MODEL_ADVICE` met `Recommendation` en `Decision Status`.
- adviseert, voert niets door.

### 7.7 Troubleshooting Agent (incidenten)
`prompts/troubleshooting_agent.md`:
- levert `INCIDENT_REPORT` met severity, category, symptoms, likely cause, actions, escalation.

## 8) Documentatie en governance‑bestanden

### 8.1 `docs/CODEX_META_PROMPT.md`
Dit document definieert:
- rol van Codex als meta‑orchestrator
- fail‑safe protocol (STOP/rapporteren)
- sessie‑start‑ritueel
- “golden documents”
- beslisprincipes
- expliciete vermeldingen van Template Agent, Research Agent en Glossary Agent

### 8.2 `docs/CODEX_TODO.md`
Actuele TODO‑status (zoals vastgelegd):
- PHASE-1 foundations zijn afgerond; alle SYSTEM_* items staan op [x].
- PHASE-2 items staan in `docs/CODEX_TODO.md`; alle PHASE2_* items zijn gemarkeerd als [x].
- De kernsectie bevat nog één open item (basis chapter/batch‑workflow ontwerpen); workflow‑documentatie is [x].
Phase-3 bereidt gecontroleerde pilots voor, maar verandert (nog) niets aan productie-workflow.

### 8.3 `docs/CODEX_SESSION_LOG.md`
Bevat sessielog entries met datum en korte samenvatting van afgeronde acties.

## 9) Research‑rapporten (historische repo‑scan)

### 9.1 `docs/RESEARCH_OLD_REPO.md`
- Scope: `/Users/vwvd/Millway/AI-folder/mustika_archive`
- Focus: OCR_HISTORY, GLOSSARY, ANNOTATIONS, GENERAL
- Bevat `RelevantFiles` met paths + type/relevance/notes en vaste `KeyInsights`, `OpenQuestions`, `Recommendations`.

### 9.2 `docs/RESEARCH_OCR_HISTORY.md`
- Focus op OCR/scan‑bestanden
- `RelevantFiles` bevat geclassificeerde entries (IMAGE_SCAN, SCAN_PDF, OCR_LOG, UNKNOWN)
- `KeyInsights`/`OpenQuestions`/`Recommendations` gericht op OCR‑pijplijn reconstructie

### 9.3 `docs/RESEARCH_GLOSSARY.md`
- Focus: GLOSSARY / TERMINOLOGY
- `RelevantFiles` bevat tabellen en notities (tsv/csv/md/txt)
- `KeyInsights`/`OpenQuestions`/`Recommendations` gericht op terminologie‑beslissingen

## 10) Data‑stroom en outputs

- Inputvoorbeeld: `data/origineel/hoofdstuk1.txt`
- Ruwe NL‑input (dummy): `data/hoofdstuk1_rough_nl_dummy.txt`
- Outputs van eerdere runs staan in `data/output/` (meerdere bestanden).

## 11) Bekende handover‑punten (samengevat, feitelijk)

- **Pipeline‑faseoverdracht**: Phase 1 → Phase 2 → Phase 3 in `test_multi_agent_fidelity.py`.
- **Template‑contract**: Orchestrator behandelt `TEMPLATE_DEFINITION` als contract en stuurt bij via Troubleshooting.
- **Research‑overdracht**: Orchestrator gebruikt Research‑output om Annotation/Glossary te voeden en Methodology/Technical te informeren.
- **Glossary‑overdracht**: Glossary Agent levert voorstellen; finale terminologie blijft menselijk besluit.
- **Methodology‑overdracht**: Orchestrator logt template‑versies en belangrijke beslissingen als input voor Methodology Archivist.

## 12) Bewuste beperkingen en non‑goals (zoals gedocumenteerd)

`docs/CODEX_META_PROMPT.md` stelt expliciet:
- geen inline prompts in Python
- geen logicawijzigingen zonder opdracht
- geen workarounds bij fouten; eerst STOP en rapporteren
- governance‑documenten zijn leidend

## 13) Overige observaties uit repo‑inhoud

- `simple_agent_mistral.py` is leeg.
- De status‑tabel in `docs/AGENTS.md` is het centrale overzicht van implementatiestatus.
- `mustikarasa_codex_cli.py` is het primaire CLI‑entrypoint voor de pipeline.

## 14) Orchestrator‑mandaat en grenzen (geconsolideerd)

Het Orchestrator‑mandaat is expliciet vastgelegd in:
- `prompts/orchestrator.md` (sectie “Mandate and Boundaries”)
- `docs/AGENTS.md` (Orchestrator‑sectie)
- `docs/WORKFLOW.md`

De Orchestrator mag:
- workflow coördineren en agents aansturen;
- templates en formats bewaken en governance‑triggers activeren;
- outputs laten loggen bij Methodology Archivist.

De Orchestrator mag niet:
- nieuwe agents of rollen uitvinden buiten `docs/AGENTS.md`;
- eindbeslissingen over terminologie/publicatie nemen;
- Python‑code of runtime‑configuratie wijzigen.

STOP/escalatie voor de Orchestrator is vastgelegd via het Autonomy/Soft‑Stop/HARD‑Stop model
en wordt verder beschreven in `docs/AGENTS.md` en `docs/WORKFLOW.md`.

## 15) Glossary Decision Lifecycle (terminologie‑beslisstraat)

`docs/10-governance/GLOSSARY_DECISION_LIFECYCLE.md` beschrijft de volledige beslis‑lifecycle:
Proposal → Context → Risk Review → Human Gate → Versioning → Rollback.

Rollen in deze lifecycle:
- Glossary Agent (voorstellen)
- Research Agent (evidence)
- Orchestrator (proces)
- Methodology Archivist (audit trail)
- Human Reviewer / Editorial Board (definitieve beslissing)

De Glossary Agent en Research Agent verwijzen expliciet naar deze lifecycle in hun prompts.
Definitieve terminologiebeslissingen lopen altijd via een Human Gate.

## 16) Governance‑triggers (Methodology, Technical, Troubleshooting)

Er is expliciet vastgelegd wanneer governance‑agents automatisch worden aangeroepen:
- Methodology Archivist: nieuwe workflows, lifecycle‑wijzigingen en SYSTEM_* beslissingen.
- Technical Advisor: modelkeuze, kosten/performance, lokaal vs cloud.
- Troubleshooting Agent: pipeline‑fouten, STOP‑criteria, inconsistent gedrag.

Deze triggers staan in:
- `prompts/orchestrator.md` (sectie “Governance Triggers”)
- `prompts/methodology_archivist.md`
- `prompts/technical_advisor.md`
- `prompts/troubleshooting_agent.md`
- `docs/AGENTS.md` en `docs/WORKFLOW.md`

De governance‑agents zijn adviserend/loggend en voeren geen code‑wijzigingen door.

## 17) Autonomy, Soft‑Stop, Governance‑Stop en Human Gate

Per agent is nu een sectie “Autonomy, Soft‑Stop & Escalation” aanwezig in de prompts,
o.a. voor Orchestrator, Translation, Readability, Fidelity, Glossary, Research en Troubleshooting.

Het drietrapsmodel is:

1) Soft‑Stop / self‑healing: agent probeert zelf opnieuw en vraagt context of cross‑check.
2) Governance‑Stop: inzet van governance‑agents om te analyseren en te loggen.
3) Hard‑Stop / Human Gate: alleen bij high‑risk situaties (gezondheid, veiligheid, zwaar betwiste betekenis,
   project‑brede glossary‑impact, governance‑conflicten).

Dit model borgt maximale autonomie met governance vóór menselijke escalatie.
Zie `docs/AGENTS.md` (Autonomy & Escalation‑bullets) en `docs/WORKFLOW.md` (stop‑model tabel).

## 18) Governance testplan

`docs/10-governance/GOVERNANCE_TESTS_PLAN.md` bevat het testplan voor governance‑mechanismen (niet taalkwaliteit).
Belangrijkste categorieën:
- template compliance
- lifecycle enforcement (Glossary)
- governance‑triggers (Methodology/Technical/Troubleshooting)
- soft‑stop vs self‑healing
- hard‑stop / human gate

Het plan is documentair en bedoeld als basis voor toekomstige testscripts/CLI‑scenario’s.

## 19) Handover Agent (sessie-overdracht)

Er is een Handover Agent die handover-templates en concrete handover-notes
voor nieuwe ChatGPT- en Codex CLI-sessies maakt.
Deze agent werkt strikt repo-gebaseerd en voorkomt contextverlies tussen sessies.

Verwijzingen:
- prompts/handover_agent.md
- docs/AGENTS.md
- docs/CODEX_META_PROMPT.md
