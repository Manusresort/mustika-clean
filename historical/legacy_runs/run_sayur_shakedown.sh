#!/usr/bin/env bash
set -euo pipefail

# Ga naar de projectroot (Crew-AI/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
cd "${PROJECT_ROOT}"

# Activeer de virtuele omgeving als die bestaat
if [ -f ".venv/bin/activate" ]; then
  # shellcheck source=/dev/null
  source ".venv/bin/activate"
fi

# Voer de shakedown-runner uit
python3 sandbox/crew/shakedown_sayur_mistral_runner.py
