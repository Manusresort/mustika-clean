import argparse
import sys
from pathlib import Path

from pipeline_fidelity import run_pipeline


def format_result_for_output(result) -> str:
    """
    Converteert de returnwaarde van run_pipeline(...) naar een eindstring.
    """
    if isinstance(result, dict):
        text = result.get("text", "")
        remarks = result.get("remarks", "")
        if remarks:
            return f"{text}\n\nOpmerkingen:\n{remarks}\n"
        return text
    return str(result)


def handle_recipe(args) -> int:
    english_path = Path(args.english)
    rough_nl_path = Path(args.rough_nl)

    if not english_path.is_file():
        print(f"Error: English input file not found: {english_path}", file=sys.stderr)
        return 1
    if not rough_nl_path.is_file():
        print(f"Error: rough NL input file not found: {rough_nl_path}", file=sys.stderr)
        return 1

    english_text = english_path.read_text(encoding="utf-8")
    rough_dutch_text = rough_nl_path.read_text(encoding="utf-8")

    result = run_pipeline(english_text, rough_dutch_text)
    output_text = format_result_for_output(result)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_text, encoding="utf-8")
    else:
        print(output_text)

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Mustikarasa multi-agent pipeline CLI (Translation \u2192 Readability \u2192 Fidelity)"
        )
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    recipe_parser = subparsers.add_parser(
        "recipe",
        help="Run the 3-phase pipeline on a single recipe (EN + rough NL).",
    )
    recipe_parser.add_argument(
        "--english",
        required=True,
        help="Path to the English source text file.",
    )
    recipe_parser.add_argument(
        "--rough-nl",
        required=True,
        help="Path to the rough Dutch translation file.",
    )
    recipe_parser.add_argument(
        "--output",
        required=False,
        help=(
            "Optional path to write the final Dutch text + remarks. If omitted, "
            "prints to stdout."
        ),
    )

    args = parser.parse_args()

    if args.command == "recipe":
        return handle_recipe(args)

    return 1


if __name__ == "__main__":
    sys.exit(main())
