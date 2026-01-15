from datetime import datetime
import json
from pathlib import Path

from crewai import Agent, Task, Crew, Process, LLM


# Project root (Crew-AI/)
BASE_DIR = Path(__file__).resolve().parents[2]

SYSTEM_PROMPT_PATH = BASE_DIR / "sandbox" / "crew" / "prompts" / "shakedown_sayur_mistral_system.md"
EXCERPT_PATH = BASE_DIR / "data" / "source_imports" / "sayur_groente_001" / "sayur_groente_excerpt_v1.txt"
LOG_DIR = BASE_DIR / "sandbox" / "crew" / "run_logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def load_system_prompt() -> str:
    return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def load_locked_excerpt() -> str:
    """
    Lees de locked mini-excerpt regels (14–18) uit het lokale excerpt-bestand.

    In het plan zijn de lijnen 14–18 (1-based). Python is 0-based,
    dus we pakken indices 13 t/m 17 (eindindex exclusief).
    """
    lines = EXCERPT_PATH.read_text(encoding="utf-8").splitlines()
    start_idx = 13  # lijn 14
    end_idx = min(18, len(lines))  # tot en met 18 (1-based) als het kan
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


def validate_json_contract(text: str) -> tuple[bool, str]:
    try:
        data = json.loads(text)
    except Exception as e:
        return False, f"Output is not JSON: {e}"

    if not isinstance(data, list):
        return False, "Top-level value must be a JSON array."

    required = {"line", "span", "label", "reason"}

    for i, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            return False, f"Item {i} is not an object."
        missing = required - set(item.keys())
        if missing:
            return False, f"Item {i} missing keys: {', '.join(sorted(missing))}"

    return True, "OK"


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

    result = crew.kickoff()

    # Print naar stdout (zoals nu)
    print(result)

    # --- JSON contract validation (non-fatal) ---
    valid, msg = validate_json_contract(str(result))
    if valid:
        print("[SCHEMA] JSON is valid.")
    else:
        print(f"[SCHEMA WARNING] {msg}")

    # Log naar sandbox/crew/run_logs als tekst (JSON-achtig)
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    log_path = LOG_DIR / f"P4_SAYUR_MISTRAL_CREW_SHAKEDOWN_{timestamp}.json"

    try:
        # crewai kan een string of object teruggeven; we loggen tekst om drift te vermijden.
        log_path.write_text(str(result), encoding="utf-8")
    except Exception as e:
        # Logging mag geen harde failure veroorzaken tijdens shakedown.
        print(f"[WARN] Could not write log file {log_path}: {e}")


if __name__ == "__main__":
    main()
