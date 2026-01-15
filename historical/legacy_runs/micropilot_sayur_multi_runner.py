from pathlib import Path

from crewai import Agent, Task, Crew, Process, LLM


# Project root (Crew-AI/)
BASE_DIR = Path(__file__).resolve().parents[2]

ANNOTATOR_PROMPT_PATH = BASE_DIR / "sandbox" / "crew" / "prompts" / "micropilot_sayur_annotator_system.md"
CHALLENGER_PROMPT_PATH = BASE_DIR / "sandbox" / "crew" / "prompts" / "micropilot_sayur_challenger_system.md"
EXCERPT_PATH = BASE_DIR / "data" / "source_imports" / "sayur_groente_001" / "sayur_groente_excerpt_v1.txt"


def load_system_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_locked_excerpt() -> str:
    """
    Lees de locked mini-excerpt regels (14–17) uit het lokale excerpt-bestand.

    In het plan zijn de lijnen 14–17 (1-based). Python is 0-based,
    dus we pakken indices 13 t/m 16 (eindindex exclusief).
    """
    lines = EXCERPT_PATH.read_text(encoding="utf-8").splitlines()
    start_idx = 13  # lijn 14
    end_idx = min(17, len(lines))  # tot en met 17 (1-based) als het kan
    selected = lines[start_idx:end_idx]

    numbered = []
    for i, text in enumerate(selected, start=start_idx + 1):
        numbered.append(f"{i}: {text}")
    return "\n".join(numbered)


def run_annotator(llm: LLM, excerpt_block: str) -> str:
    system_prompt = load_system_prompt(ANNOTATOR_PROMPT_PATH)
    description = f"""{system_prompt}

Here is the excerpt (line numbers included):

{excerpt_block}

Return ONLY the JSON array as described above.
"""

    annotator = Agent(
        role="Annotation helper (Mistral via Ollama)",
        goal=(
            "Classify short SAJUR-A text spans with labels "
            "HISTORICAL / GLOSSARY / SAFETY / OCR / NONE "
            "without rewriting or deciding meanings."
        ),
        backstory=(
            "You work in the Mustikarasa project. "
            "You ONLY signal and classify. You NEVER translate, "
            "normalise, or choose final glossary equivalents."
        ),
        llm=llm,
        allow_delegation=False,
        verbose=True,
        tools=[],
    )

    task = Task(
        description=description,
        expected_output=(
            "A valid JSON array of objects with keys: "
            "line (int), span (string), label (string), reason (string)."
        ),
        agent=annotator,
        async_execution=False,
        human_input=False,
    )

    crew = Crew(
        agents=[annotator],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )

    return crew.kickoff()


def run_challenger(llm: LLM, excerpt_block: str, annotations_json_text: str) -> str:
    system_prompt = load_system_prompt(CHALLENGER_PROMPT_PATH)
    description = f"""{system_prompt}

Here is the excerpt (line numbers included):

{excerpt_block}

Here is the annotator JSON output:

{annotations_json_text}

Return ONLY the JSON array as described above.
"""

    challenger = Agent(
        role="Challenger (Mistral via Ollama)",
        goal=(
            "Check annotation output for rule violations: translations, "
            "equivalents, meaning decisions, unsafe claims."
        ),
        backstory=(
            "You work in the Mustikarasa project. "
            "You ONLY flag potential overreach; you do not propose fixes."
        ),
        llm=llm,
        allow_delegation=False,
        verbose=True,
        tools=[],
    )

    task = Task(
        description=description,
        expected_output=(
            "A valid JSON array of objects with keys: "
            "line (int or null), span (string), issue_type (string), "
            "severity (string), comment (string)."
        ),
        agent=challenger,
        async_execution=False,
        human_input=False,
    )

    crew = Crew(
        agents=[challenger],
        tasks=[task],
        process=Process.sequential,
        verbose=True,
    )

    return crew.kickoff()


def main() -> None:
    llm = LLM(
        model="ollama/mistral",
        base_url="http://localhost:11434",
    )

    excerpt_block = load_locked_excerpt()

    annotations = run_annotator(llm, excerpt_block)
    challenges = run_challenger(llm, excerpt_block, str(annotations))

    print("---ANNOTATIONS---")
    print(annotations)
    print("---CHALLENGE_REPORT---")
    print(challenges)
    print("---OPTIONAL_AGENT_STEPS---")
    # For this micropilot v2 design, we do not yet run
    # extra agents (troubleshooting/template). We still
    # emit an explicit marker so logs have a stable shape.
    # When optional agents are added later, their JSON
    # output can be printed here instead of this placeholder.
    print("[]")


if __name__ == "__main__":
    main()
