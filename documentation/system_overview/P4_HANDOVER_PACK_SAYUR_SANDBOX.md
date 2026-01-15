# P4 Handover Pack — SAYUR Sandbox (Agents & CrewAI)

Dit pakket is bedoeld voor de volgende GPT-sessie, met expliciete expertise in:
- LLM-agents & multi-agent frameworks (CrewAI-achtig)
- Werken met Ollama als modelhost
- Mistral-achtige modellen in tool/agent-setting
- Prompt-engineering voor JSON/structuur-output
- Governance-bewuste integratie in een redactionele workflow
- Werken via een Codex CLI-laag (GPT schrijft prompts; mens runt code)

## 1. Kern-overzicht

**Lees deze eerst:**

- `docs/total_project.md`  
  → Overzicht van het Mustikarasa-project, doelen, doc-structuur.

- `docs/P4_CONSOLIDATION_REPORT_SAYUR_SANDBOX.md`  
  → Samenvatting van wat Phase-4 sandbox voor SAYUR al heeft bewezen  
    (shakedowns, multi-agent micropilot, known limitations).

## 2. Governance & workflow

**Belangrijk voor elke agent-beslissing:**

- `docs/WORKFLOW.md`  
  → Stop-model (soft-stop → governance-stop → Human Gate) + pipeline.

- `docs/10-governance/HUMAN_GATE_POLICY_P4_SANDBOX.md`  
  → Wanneer Human Gate verplicht is (meaning, cultuur, safety, publicatie).

- `docs/10-governance/ROLLBACK_TESTPLAN_P4_SANDBOX.md`  
  → Hoe reversibility getest en gegarandeerd wordt in de sandbox.

## 3. Agents & autonomie

**Definiëren wat agents wél/niet mogen:**

- `docs/AGENTS.md`  
  → Beschrijving van agentrollen (annotator, challenger, orchestrator, etc.).

- `docs/AGENT_AUTONOMY_ENVELOPE.md`  
  → Harde grenzen van agent-autonomie (geen bron-edits, geen beslissingsmacht).

- `docs/ANNOTATION_STYLECARD_P4.md`  
  → Labeltypes (HISTORICAL / GLOSSARY / SAFETY / OCR / NONE) + EvidenceRef-stijl.

## 4. Backlog & sessies

**Waar je de feitelijke status vindt:**

- `docs/CODEX_TODO.md`  
  → Backlog met P4-items. Belangrijk:  
    - SAYUR shakedown: status `done`  
    - LOBAK shakedown: status `done`  
    - Multi-agent micropilot: gepland/gestart, zie ook session log.

- `docs/CODEX_SESSION_LOG.md`  
  → Historiek van runs & simulaties.  
    - Bevat RUN-ID’s, wat echt is gedraaid, en wat alleen ontwerp was.

## 5. Shakedown-plannen & micropilots

**De patronen die al werken:**

- `docs/crew/CREW_SHAKEDOWN_PLAN_SAYUR_MISTRAL.md`  
  → Plan + evaluatie voor de annotator-shakedown op SAJUR-A.

- `docs/crew/CREW_SHAKEDOWN_PLAN_LOBAK_MISTRAL.md`  
  → Plan + evaluatie voor de LOBAK-glossary-shakedown.

- `docs/crew/CREW_MICROPILOT_SAYUR_MULTI_MISTRAL.md`  
  → Multi-agent micropilot-plan (annotator + challenger, JSON-only).

## 6. Belangrijke sandbox-code & prompts

**Niet om zelf te runnen door GPT, maar als referentie:**

- Annotator prompts (SAYUR/LOBAK):  
  - `sandbox/crew/prompts/shakedown_sayur_mistral_system.md`  
  - `sandbox/crew/prompts/shakedown_lobak_mistral_system.md`

- Multi-agent prompts (micropilot):  
  - `sandbox/crew/prompts/micropilot_sayur_annotator_system.md`  
  - `sandbox/crew/prompts/micropilot_sayur_challenger_system.md`

- Runners (door mens gestart, via terminal):  
  - `sandbox/crew/shakedown_sayur_mistral_runner.py`  
  - `sandbox/crew/shakedown_lobak_mistral_runner.py`  
  - `sandbox/crew/micropilot_sayur_multi_runner.py`  
  - generieke wrappers:
    - `sandbox/crew/codex_crew_runner.py`
    - `sandbox/crew/codex_crew_runner_lobak.py`
    - (optioneel) `sandbox/crew/codex_micropilot_sayur_runner.py`

## 7. Wat de volgende GPT-sessie mag doen

- Bouwen op de bestaande shakedowns en micropilot.  
- Multi-agent gedrag tunen (vooral challenger: issue_types, geen vertaling eisen).  
- Eventueel een eerste “learning agent” ontwerpen die logs leest en  
  *voorstellen* doet, maar nooit zelf prompts/config wijzigt zonder Human Gate + Codex.

- ALTIJD:
  - via Codex prompts werken,
  - expliciet terminal-commando’s geven als er een run nodig is,
  - en alles wat besluitvormend is in CODEX_TODO / sessielogs laten landen.

Einde handover-pack index.
