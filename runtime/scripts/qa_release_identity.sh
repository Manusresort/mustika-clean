#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST="$ROOT/manifests/book_manifest.json"
EXPORTER="$ROOT/scripts/book_export.py"

cd "$ROOT"

if [ ! -x "$EXPORTER" ]; then
  echo "SKIP: missing exporter"
  exit 0
fi
if [ ! -f "$MANIFEST" ]; then
  echo "SKIP: missing book_manifest.json"
  exit 0
fi

BOOK_ID="$(python3 - <<'PY'
import json
from pathlib import Path
p = Path("manifests/book_manifest.json")
d = json.load(open(p, "r", encoding="utf-8"))
books = d.get("books")
entry = books[0] if isinstance(books, list) and books else d
print(entry.get("book_id") or "BOOK-DEFAULT")
PY
)"

python3 "$EXPORTER" --book-id "$BOOK_ID" --release-id latest >/tmp/qa_release_identity.stdout.txt 2>&1 || {
  echo "FAIL: export failed"
  exit 1
}

LATEST_JSON="$ROOT/exports/books/$BOOK_ID/releases/latest.json"
if [ ! -f "$LATEST_JSON" ]; then
  echo "FAIL: missing latest.json"
  exit 1
fi

export BOOK_ID
RELEASE_ID="$(python3 - <<'PY'
import json
import os
from pathlib import Path
book_id = os.environ.get("BOOK_ID", "")
p = Path("exports/books") / book_id / "releases" / "latest.json"
d = json.load(open(p, "r", encoding="utf-8"))
print(d.get("release_id") or "")
PY
)"

if [ -z "$RELEASE_ID" ]; then
  echo "FAIL: latest.json missing release_id"
  exit 1
fi

if [ "$RELEASE_ID" = "latest" ]; then
  echo "FAIL: release_id is literal latest"
  exit 1
fi

REL_DIR="$ROOT/exports/books/$BOOK_ID/releases/$RELEASE_ID"
if [ ! -d "$REL_DIR" ]; then
  echo "FAIL: release dir missing"
  exit 1
fi

MANIFEST_PATH="$REL_DIR/release_manifest.json"
if [ ! -f "$MANIFEST_PATH" ]; then
  echo "FAIL: release_manifest.json missing"
  exit 1
fi

export MANIFEST_PATH RELEASE_ID
if ! python3 - <<'PY'
import json
import os
from pathlib import Path
p = Path(os.environ["MANIFEST_PATH"])
d = json.load(open(p, "r", encoding="utf-8"))
assert d.get("release_id") == os.environ["RELEASE_ID"]
assert d.get("book_id")
print("ok")
PY
then
  echo "FAIL: release_manifest.json invalid"
  exit 1
fi

# Immutability check: re-run with explicit release_id should fail
if python3 "$EXPORTER" --book-id "$BOOK_ID" --release-id "$RELEASE_ID" >/tmp/qa_release_identity_rerun.stdout.txt 2>&1; then
  echo "FAIL: immutability not enforced"
  exit 1
fi

echo "PASS"
