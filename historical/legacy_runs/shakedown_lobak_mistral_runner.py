from pathlib import Path

from crewai import Agent, Task, Crew, Process, LLM


# Project root (Crew-AI/)
BASE_DIR = Path(__file__).resolve().parents[2]

SYSTEM_PROMPT_PATH = BASE_DIR / "sandbox" / "crew" / "prompts" / "shakedown_lobak_mistral_system.md"
EXCERPT_PATH = BASE_DIR / "data" / "source_imports" / "sayur_groente_001" / "sayur_groente_excerpt_v1.txt"


def load_system_prompt() -> str:
    return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def load_locked_excerpt() -> str:
    """
    Lees de locked mini-excerpt regels (52–55) uit het lokale excerpt-bestand.

    Plan: lines 52–55 (1-based). Python is 0-based → indices 51–55 (eindindex exclusief).
    """
    lines = EXCERPT_PATH.read_text(encoding="utf-8").splitlines()
    start_idx = 51  # lijn 52
    end_idx = min(55, len(lines))  # tot en met 55 (1-based) als het kan
    selected = lines[start_idx:end_idx]

    numbered = []
    for i, text in enumerate(selected, start=start_idx + 1):
        numbered.append(f"{i}: {text}")
    return "\n".join(numbered)


def build_description(system_prompt: str, excerpt_block: str) -> str:
    return f"""{system_prompt}

Here is the excerpt (line numbers included):

{excerpt_block}

Return ONLY the JSON array as described above.
"""


def main() -> None:
    # LLM via Ollama (mistral)
    llm = LLM(
        model="ollama/mistral",
        base_url="http://localhost:11434",
    )

    system_prompt = load_system_prompt()
    excerpt_block = load_locked_excerpt()
    description = build_description(system_prompt, excerpt_block)

    annotator = Agent(
        role="Annotation helper (Mistral via Ollama, LOBAK)",
        goal=(
            "Classify short LOBAK-related text spans with labels "
            "HISTORICAL / GLOSSARY / SAFETY / OCR / NONE "
            "without rewriting or deciding meanings."
        ),
        backstory=(
            "You work in the Mustikarasa project. "
            "You ONLY signal and classify. You NEVER translate, "
            "normalise, or choose final glossary equivalents, "
            "especially not for 'lobak'."
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

    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
