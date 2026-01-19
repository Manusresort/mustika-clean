import argparse
import sys
from pathlib import Path

try:
    from crewai import Task, Crew
    CREWAI_AVAILABLE = True
except Exception:
    CREWAI_AVAILABLE = False

try:
    from mustikarasa_agents import (
        translation_quality_agent,
        readability_editor,
        fidelity_agent,
    )
    AGENTS_AVAILABLE = True
except Exception:
    AGENTS_AVAILABLE = False


def phase_1_translation_quality(english_text: str, rough_dutch: str):
    """Fase 1: taalkundige controle / verbetering van de vertaling."""
    task = Task(
        description=(
            "Je krijgt een Engelse brontekst én een ruwe Nederlandse vertaling.\n"
            "Fase 1 – Translation Quality:\n"
            "- Kijk of de Nederlandse tekst de betekenis van de Engelse tekst goed weergeeft.\n"
            "- Verbeter waar nodig grammatica, woordkeus en zinsbouw.\n"
            "- Behoud de betekenis van de Engelse tekst.\n"
            "- Schrijf in natuurlijk, modern Nederlands.\n\n"
            "GEEF ALLEEN de verbeterde Nederlandse tekst terug, zonder uitleg of commentaar.\n\n"
            "Engelse brontekst:\n"
            f"{english_text}\n\n"
            "Ruwe Nederlandse tekst:\n"
            f"{rough_dutch}\n"
        ),
        agent=translation_quality_agent,
        expected_output=(
            "Alleen de verbeterde Nederlandse tekst, zonder uitleg of commentaar."
        ),
    )

    crew = Crew(
        agents=[translation_quality_agent],
        tasks=[task],
        verbose=True,
    )

    print("\n=== FASE 1: Translation Quality ===\n")
    result = crew.kickoff()
    print("\n[FASE 1 RESULTAAT]\n", result, "\n")
    return str(result).strip()


def phase_2_readability(nl_text: str):
    """Fase 2: leesbaarheid / stijl oppoetsen."""
    task = Task(
        description=(
            "Je krijgt een Nederlandse tekst.\n"
            "Fase 2 – Readability Editor:\n"
            "- Maak de tekst vloeiend, helder en prettig leesbaar voor een moderne Nederlandse lezer.\n"
            "- Verander de betekenis niet.\n"
            "- Corrigeer eventuele overgebleven grammaticale of stilistische fouten.\n"
            "- Verwijder ALLE meta-uitleg, opmerkingen, Engelse zinnen en tekst tussen haakjes.\n\n"
            "GEEF ALLEEN de definitieve Nederlandse tekst terug, zonder uitleg of commentaar.\n\n"
            "Tekst:\n"
            f"{nl_text}\n"
        ),
        agent=readability_editor,
        expected_output=(
            "Alleen de definitieve, natuurlijke Nederlandse tekst zonder toelichting."
        ),
    )

    crew = Crew(
        agents=[readability_editor],
        tasks=[task],
        verbose=True,
    )

    print("\n=== FASE 2: Readability ===\n")
    result = crew.kickoff()
    print("\n[FASE 2 RESULTAAT]\n", result, "\n")
    return str(result).strip()


def phase_3_fidelity(english_text: str, nl_text: str):
    """Fase 3: Fidelity – bewaker van betekenis t.o.v. origineel."""
    task = Task(
        description=(
            "Je bent de Fidelity Agent: bewaker van het origineel.\n"
            "Je krijgt de Engelse brontekst en de huidige Nederlandse versie.\n\n"
            "Taken:\n"
            "1. Controleer of de Nederlandse tekst trouw is aan de Engelse tekst qua betekenis.\n"
            "2. Let extra op woorden die mogelijk een andere betekenis hebben gekregen "
            "(bijvoorbeeld 'receptie' vs 'recept', 'ceremony' vs 'gerecht', etc.).\n"
            "3. Corrigeer alleen als je met hoge zekerheid weet dat een woord fout is in deze context.\n"
            "4. Als je twijfelt, verander het woord niet, maar noem het als mogelijke kwestie.\n\n"
            "OUTPUT-FORMAT:\n"
            "- Plaats EXACT één lege regel tussen hoofdtekst en 'Opmerkingen:'.\n"
            "  Dit betekent dat je output letterlijk '\\n\\nOpmerkingen:' bevat.\n"
            "- Eerst: ALLEEN de Nederlandse tekst (geen Engels, geen bronzin).\n"
            "- Dan EXACT één lege regel.\n"
            "- Dan: 'Opmerkingen:'\n"
            "- Opmerkingen mogen alleen korte bulletpoints bevatten; geen herformuleringen van de hoofdtekst.\n"
            "- Als je twijfelt: laat hoofdtekst ongewijzigd; zet twijfel in Opmerkingen.\n"
            "- Gebruik nooit woorden als 'definitief' in labels; geef alleen de tekst zelf.\n"
            "- Self-check: Als je per ongeluk Engels hebt geschreven in het hoofdblok,\n"
            "  herschrijf dat blok naar Nederlands voor je antwoord afrondt.\n"
            "- Self-check: controleer dat je output '\\n\\nOpmerkingen:' bevat; zo niet,\n"
            "  voeg de lege regel toe.\n"
            "- Als er geen problemen zijn, schrijf 'Opmerkingen: (geen)'.\n\n"
            "Engelse brontekst:\n"
            f"{english_text}\n\n"
            "Huidige Nederlandse tekst:\n"
            f"{nl_text}\n"
        ),
        agent=fidelity_agent,
       expected_output=(
    "ALLEEN de hoofdtekst.\n"
    "\n"
    "Opmerkingen:\n"
    "- (optioneel) korte bulletpoints, of '(geen)'."
)
 ,
    )

    crew = Crew(
        agents=[fidelity_agent],
        tasks=[task],
        verbose=True,
    )

    print("\n=== FASE 3: Fidelity ===\n")
    result = crew.kickoff()
    print("\n[FASE 3 RESULTAAT]\n", result, "\n")
    return str(result).strip()


def run_pipeline(english_text: str, rough_dutch_text: str):
    """
    Voert de 3-fasen pipeline uit:
    Translation → Readability → Fidelity.
    Retourneert de finale tekst inclusief opmerkingen.
    """
    if not CREWAI_AVAILABLE or not AGENTS_AVAILABLE:
        text = (rough_dutch_text or "").strip()
        if not AGENTS_AVAILABLE:
            remarks = (
                "STUB: mustikarasa_agents missing; returned rough_nl without agent processing."
            )
        else:
            remarks = "STUB: crewai not installed; returned rough_nl without agent processing."
        return {"text": text, "remarks": remarks}

    nl_phase1 = phase_1_translation_quality(english_text, rough_dutch_text)
    nl_phase2 = phase_2_readability(nl_phase1)
    final_output = phase_3_fidelity(english_text, nl_phase2)

    return final_output


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Mustikarasa pipeline: Translation Quality → Readability → Fidelity."
        )
    )
    parser.add_argument(
        "--english",
        required=True,
        help="Pad naar de Engelse brontekst.",
    )
    parser.add_argument(
        "--rough-nl",
        required=True,
        help="Pad naar de ruwe Nederlandse vertaling.",
    )
    parser.add_argument(
        "--output",
        help="Optioneel pad om de finale tekst naar weg te schrijven.",
    )
    args = parser.parse_args()

    if not AGENTS_AVAILABLE:
        print("mustikarasa_agents missing; running stub mode")

    english_path = Path(args.english)
    rough_nl_path = Path(args.rough_nl)

    if not english_path.is_file():
        print(f"Fout: Engels bronbestand niet gevonden: {english_path}", file=sys.stderr)
        sys.exit(1)
    if not rough_nl_path.is_file():
        print(
            f"Fout: Ruwe NL-vertaling niet gevonden: {rough_nl_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    english_text = english_path.read_text(encoding="utf-8")
    rough_dutch_text = rough_nl_path.read_text(encoding="utf-8")

    final_output = run_pipeline(english_text, rough_dutch_text)

    if args.output:
        Path(args.output).write_text(final_output, encoding="utf-8")
    else:
        print("\n================ EINDE PIPELINE ================\n")
        print(final_output)


if __name__ == "__main__":
    main()
