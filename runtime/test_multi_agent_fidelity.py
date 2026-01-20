"""Thin CLI wrapper for the fidelity pipeline (module is in runtime/src/)."""

import argparse
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / "src"))

from pipeline_fidelity import run_pipeline, AGENTS_AVAILABLE


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
