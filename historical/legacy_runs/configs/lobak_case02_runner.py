"""
Wrapper runner for LOBAK Case-02.

Maps sandbox/crew/configs/lobak_case02.yaml to the LOBAK shakedown runner
so the excerpt-aware entrypoint can dispatch without error.

This is a minimal bridge; it does not change pipeline behavior.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the project root (Crew-AI/) is on sys.path
BASE_DIR = Path(__file__).resolve().parents[3]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from sandbox.crew.shakedown_lobak_mistral_runner import main


if __name__ == "__main__":
    main()
