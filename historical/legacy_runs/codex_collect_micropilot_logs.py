"""
Utility script — documentary only.

Lists available MICROPILOT logs and prints their paths,
so humans can copy-paste them into the meta-synthesis prompt.

No parsing, no modification, no automation.
"""

import os

LOG_DIR = "sandbox/crew/run_logs"


def list_micropilot_logs():
    files = sorted(
        [
            f
            for f in os.listdir(LOG_DIR)
            if f.startswith("MICROPILOT_SAYUR_")
        ]
    )
    for name in files:
        print(os.path.join(LOG_DIR, name))


if __name__ == "__main__":
    list_micropilot_logs()
