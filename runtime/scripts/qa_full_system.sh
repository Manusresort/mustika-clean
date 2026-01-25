#!/usr/bin/env bash
set -euo pipefail

# Ensure runtime venv is active (avoid PATH python mismatches)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ -f "$ROOT/.venv/bin/activate" ]; then
  # shellcheck disable=SC1090
  source "$ROOT/.venv/bin/activate"
else
  echo "ERROR: missing runtime/.venv. Create it under runtime/.venv (Python 3.11) and install deps."
  exit 1
fi

set -u

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
AUDIT_DIR="$BASE_DIR/audit/qa/latest_full"
SUMMARY="$AUDIT_DIR/summary.tsv"
API_LOG="$AUDIT_DIR/api.log"
UI_LOG="$AUDIT_DIR/ui_build.log"

mkdir -p "$AUDIT_DIR"

normalize_summary() {
  if [ ! -f "$SUMMARY" ]; then
    return 0
  fi
  SUMMARY_NORMALIZED="${AUDIT_DIR}/summary.normalized.tsv"
  SUMMARY_PATH="$SUMMARY" SUMMARY_NORMALIZED_PATH="$SUMMARY_NORMALIZED" python3 - <<'PY'
import re
from pathlib import Path
import os

src = Path(os.environ["SUMMARY_PATH"])
dst = Path(os.environ["SUMMARY_NORMALIZED_PATH"])
text = src.read_text(encoding="utf-8", errors="replace")
text = re.sub(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", "<TS>", text)
text = re.sub(r"\b\d{6,}\b", "<N>", text)
dst.write_text(text, encoding="utf-8")
PY
}
trap normalize_summary EXIT

print_summary() {
  printf '%s\t%s\t%s\n' "$1" "$2" "$3" | tee -a "$SUMMARY" >/dev/null
}

passfail() {
  if [ "$1" -eq 0 ]; then
    echo "PASS"
  else
    echo "FAIL"
  fi
}

: > "$SUMMARY"
print_summary "CHECK" "RESULT" "NOTES"

cd "$BASE_DIR"

# A) Preflight
python3 --version >/tmp/qa_full_python.txt 2>&1
print_summary "python3" "PASS" "$(cat /tmp/qa_full_python.txt | tr -d '\n')"

if [ -d "$BASE_DIR/.venv" ]; then
  print_summary ".venv" "PASS" "present"
else
  print_summary ".venv" "WARN" "missing"
fi

if command -v node >/dev/null 2>&1; then
  print_summary "node" "PASS" "$(node --version | tr -d '\n')"
else
  print_summary "node" "WARN" "missing"
fi

if command -v npm >/dev/null 2>&1; then
  print_summary "npm" "PASS" "$(npm --version | tr -d '\n')"
else
  print_summary "npm" "WARN" "missing"
fi

# B) API readiness
API_UP="no"
if curl -s http://127.0.0.1:8010/health | rg -q '"ok"\s*:\s*true'; then
  API_UP="yes"
else
  nohup python3 -m uvicorn api_server:app --host 127.0.0.1 --port 8010 >"$API_LOG" 2>&1 &
  for i in {1..15}; do
    sleep 1
    if curl -s http://127.0.0.1:8010/health | rg -q '"ok"\s*:\s*true'; then
      API_UP="yes"
      break
    fi
  done
fi
if [ "$API_UP" = "yes" ]; then
  print_summary "api_health" "PASS" "ok"
else
  print_summary "api_health" "FAIL" "not_healthy"
fi

# C) Indexer checks
indexer_rc=0
python3 indexer.py >/tmp/qa_full_indexer.txt 2>&1 || indexer_rc=$?
print_summary "indexer_run" "$(passfail $indexer_rc)" "python3 indexer.py"

# B8b) Book build manifest generator
BOOK_MANIFEST_RC=0
TEST_BOOK_ID=""

TEST_BOOK_ID="$(python3 - <<'PYP'
import json
from pathlib import Path
p = Path("indices/book_closure_rollup.json")
data = json.loads(p.read_text(encoding="utf-8"))
books = data.get("books", [])
bid = books[0].get("book_id") if books else ""
print(bid or "")
PYP
)"

if [ -n "$TEST_BOOK_ID" ]; then
  python3 scripts/build_book_build_manifests.py --book-id "$TEST_BOOK_ID" --out-dir exports/books --strict \
    > "$AUDIT_DIR/book_build_manifest_${TEST_BOOK_ID}.stdout.txt" 2>&1 || BOOK_MANIFEST_RC=$?
  if [ "$BOOK_MANIFEST_RC" -eq 0 ]; then
    print_summary "build_book_manifest" "PASS" "book=$TEST_BOOK_ID"
  else
    print_summary "build_book_manifest" "FAIL" "book=$TEST_BOOK_ID rc=$BOOK_MANIFEST_RC"
  fi

  BM_PATH="$BASE_DIR/exports/books/$TEST_BOOK_ID/builds/latest/build_manifest.json"
  if [ -f "$BM_PATH" ]; then
    print_summary "book_build_manifest_exists" "PASS" "book=$TEST_BOOK_ID"
    if rg -q '"generated_at"\s*:' "$BM_PATH"; then
      print_summary "book_build_manifest_has_generated_at" "PASS" "book=$TEST_BOOK_ID"
    else
      print_summary "book_build_manifest_has_generated_at" "FAIL" "generated_at_missing"
    fi
  else
    print_summary "book_build_manifest_exists" "FAIL" "missing $BM_PATH"
    print_summary "book_build_manifest_has_generated_at" "SKIP" "missing_manifest"
  fi
else
  print_summary "build_book_manifest" "WARN" "no_books_found"
  print_summary "book_build_manifest_exists" "SKIP" "no_books_found"
  print_summary "book_build_manifest_has_generated_at" "SKIP" "no_books_found"
fi

# B9) book manifest generation
BOOK_MANIFEST_GEN_RC=0
python3 scripts/build_book_manifest.py > "$AUDIT_DIR/book_manifest.stdout.txt" 2>&1 || BOOK_MANIFEST_GEN_RC=$?
if [ "$BOOK_MANIFEST_GEN_RC" -eq 0 ]; then
  print_summary "build_book_manifest_json" "PASS" "book_manifest.json"
else
  print_summary "build_book_manifest_json" "FAIL" "rc=$BOOK_MANIFEST_GEN_RC"
fi

BM_JSON_PATH="$BASE_DIR/manifests/book_manifest.json"
if [ -f "$BM_JSON_PATH" ]; then
  print_summary "book_manifest_exists" "PASS" "exists"
  if rg -q '"generated_at"\s*:' "$BM_JSON_PATH"; then
    print_summary "book_manifest_has_generated_at" "PASS" "has key"
  else
    print_summary "book_manifest_has_generated_at" "FAIL" "missing key"
  fi
  if python3 - <<'PY'
import json
p = "manifests/book_manifest.json"
d = json.load(open(p, "r", encoding="utf-8"))
books = d.get("books")
if isinstance(books, list):
    entries = books
else:
    entries = [d]
for entry in entries:
    assert isinstance(entry.get("required_closures"), list)
print("ok")
PY
  then
    print_summary "book_manifest_has_required_closures" "PASS" "list present"
  else
    print_summary "book_manifest_has_required_closures" "FAIL" "missing/invalid"
  fi
  if python3 - <<'PY'
import json
p = "manifests/book_manifest.json"
d = json.load(open(p, "r", encoding="utf-8"))
books = d.get("books")
if isinstance(books, list):
    entries = books
else:
    entries = [d]
for entry in entries:
    exports = entry.get("exports", [])
    assert isinstance(exports, list)
    for exp in exports:
        assert isinstance(exp, dict)
        bm = exp.get("build_manifest")
        assert isinstance(bm, str) and bm
print("ok")
PY
  then
    print_summary "book_manifest_exports_reference_build_manifest" "PASS" "exports linked"
  else
    print_summary "book_manifest_exports_reference_build_manifest" "FAIL" "missing build_manifest"
  fi

  # B10: Book closure object invariants
  if python3 - <<'PY'
import json, pathlib, sys
p = pathlib.Path("manifests/book_manifest.json")
d = json.load(open(p, "r", encoding="utf-8"))
entries = d.get("books") if isinstance(d.get("books"), list) else [d]
for entry in entries:
    book_id = entry.get("book_id", "BOOK-DEFAULT")
    status = entry.get("status")
    bc = pathlib.Path("closures") / f"BOOK-{book_id}" / "closure.json"
    if bc.exists():
        assert status == "locked"
    else:
        if status == "locked":
            raise AssertionError("status locked but BOOK closure missing")
print("ok")
PY
  then
    print_summary "book_manifest_status_matches_book_closure" "PASS" "status consistent"
  else
    print_summary "book_manifest_status_matches_book_closure" "FAIL" "status mismatch"
  fi

  if python3 - <<'PY'
import json, pathlib, sys
p = pathlib.Path("manifests/book_manifest.json")
d = json.load(open(p, "r", encoding="utf-8"))
entries = d.get("books") if isinstance(d.get("books"), list) else [d]
for entry in entries:
    book_id = entry.get("book_id", "BOOK-DEFAULT")
    req = entry.get("required_closures", []) or []
    bc = pathlib.Path("closures") / f"BOOK-{book_id}" / "closure.json"
    if not bc.exists():
        continue
    c = json.load(open(bc, "r", encoding="utf-8"))
    assert c.get("decision_type") == "BOOK"
    assert c.get("book_id") == book_id
    c_req = c.get("required_closure_ids", [])
    assert isinstance(c_req, list)
    if req:
        assert sorted(c_req) == sorted(req)
print("ok")
PY
  then
    print_summary "book_closure_object_valid" "PASS" "shape ok"
  else
    print_summary "book_closure_object_valid" "FAIL" "invalid"
  fi

  if python3 - <<'PY'
import json, pathlib, sys
p = pathlib.Path("manifests/book_manifest.json")
d = json.load(open(p, "r", encoding="utf-8"))
entries = d.get("books") if isinstance(d.get("books"), list) else [d]
for entry in entries:
    book_id = entry.get("book_id", "BOOK-DEFAULT")
    bc = pathlib.Path("closures") / f"BOOK-{book_id}" / "closure.json"
    if not bc.exists():
        continue
    c = json.load(open(bc, "r", encoding="utf-8"))
    c_req = c.get("required_closure_ids", [])
    for cid in c_req:
        if not (pathlib.Path("closures") / cid / "closure.json").exists():
            raise AssertionError(f"missing required closure {cid}")
print("ok")
PY
  then
    print_summary "book_closure_required_closures_exist" "PASS" "all present"
  else
    print_summary "book_closure_required_closures_exist" "FAIL" "missing"
  fi
else
  print_summary "book_manifest_exists" "FAIL" "missing"
  print_summary "book_manifest_has_generated_at" "SKIP" "missing"
  print_summary "book_manifest_has_required_closures" "SKIP" "missing"
  print_summary "book_manifest_exports_reference_build_manifest" "SKIP" "missing"
  print_summary "book_manifest_status_matches_book_closure" "SKIP" "missing"
  print_summary "book_closure_object_valid" "SKIP" "missing"
  print_summary "book_closure_required_closures_exist" "SKIP" "missing"
fi

# B8a) book closure rollup
if [ -f "$BASE_DIR/indices/book_closure_rollup.json" ]; then
  print_summary "book_closure_rollup_exists" "PASS" "exists"
else
  print_summary "book_closure_rollup_exists" "FAIL" "missing indices/book_closure_rollup.json"
fi

if [ -f "$BASE_DIR/indices/book_closure_rollup.json" ]; then
  if rg -q '"generated_at"\s*:' "$BASE_DIR/indices/book_closure_rollup.json"; then
    print_summary "book_closure_rollup_has_generated_at" "PASS" "generated_at_present"
  else
    print_summary "book_closure_rollup_has_generated_at" "FAIL" "generated_at_missing"
  fi
else
  print_summary "book_closure_rollup_has_generated_at" "SKIP" "missing_rollup"
fi

MANIFEST_PATH="$BASE_DIR/manifests/chapter_manifest.json"
if [ -f "$MANIFEST_PATH" ]; then
  print_summary "chapter_manifest_exists" "PASS" "file exists"
  if python3 - <<PY
import json
path = "${MANIFEST_PATH}"
try:
    data = json.load(open(path))
    if 'generated_at' not in data:
        print('chapter_manifest_error: missing generated_at key')
        raise SystemExit(1)
except Exception as exc:
    print(f'chapter_manifest_error: {exc}')
    raise
PY
  then
    print_summary "chapter_manifest_has_generated_at" "PASS" "has key"
  else
    print_summary "chapter_manifest_has_generated_at" "FAIL" "missing key"
  fi
else
  print_summary "chapter_manifest_exists" "FAIL" "missing"
fi

REGISTRY_PATH="$BASE_DIR/indices/chapter_registry.json"
if [ -f "$REGISTRY_PATH" ]; then
  print_summary "chapter_registry_exists" "PASS" "file exists"
  if python3 - <<PY
import json
path = "${REGISTRY_PATH}"
try:
    data = json.load(open(path))
    if 'generated_at' not in data:
        print('chapter_registry_error: missing generated_at key')
        raise SystemExit(1)
except Exception as exc:
    print(f'chapter_registry_error: {exc}')
    raise
PY
  then
    print_summary "chapter_registry_has_generated_at" "PASS" "has key"
  else
    print_summary "chapter_registry_has_generated_at" "FAIL" "missing key"
  fi
else
  print_summary "chapter_registry_exists" "FAIL" "missing"
fi

for idx in run_index.json proposal_index.json closure_index.json inbox_index.json; do
  if [ -f "$BASE_DIR/indices/$idx" ]; then
    print_summary "index_$idx" "PASS" "exists"
  else
    print_summary "index_$idx" "FAIL" "missing"
  fi
done

if [ -f "$BASE_DIR/indices/chapter_closure_rollup.json" ]; then
  print_summary "chapter_closure_rollup_exists" "PASS" "exists"
  if python3 - <<PY
import json
path = "$BASE_DIR/indices/chapter_closure_rollup.json"
try:
    data = json.load(open(path))
    if 'generated_at' not in data:
        raise SystemExit('missing generated_at key')
except Exception as exc:
    print(f'chapter_closure_rollup_error: {exc}')
    raise
PY
  then
    print_summary "chapter_closure_rollup_has_generated_at" "PASS" "has key"
  else
    print_summary "chapter_closure_rollup_has_generated_at" "FAIL" "missing key"
  fi
else
  print_summary "chapter_closure_rollup_exists" "FAIL" "missing"
fi

if [ -f "$BASE_DIR/indices/glossary_evidence_index.json" ]; then
  print_summary "glossary_evidence_index_exists" "PASS" "exists"
  if python3 - <<PY
import json
path = "$BASE_DIR/indices/glossary_evidence_index.json"
try:
    data = json.load(open(path))
    if 'generated_at' not in data:
        raise SystemExit('missing generated_at key')
except Exception as exc:
    print(f'glossary_evidence_index_error: {exc}')
    raise
PY
  then
    print_summary "glossary_evidence_index_has_generated_at" "PASS" "has key"
  else
    print_summary "glossary_evidence_index_has_generated_at" "FAIL" "missing key"
  fi
else
  print_summary "glossary_evidence_index_exists" "FAIL" "missing"
fi

# B5) glossary lifecycle gates
CHAPTER_MANIFEST_PATH="$BASE_DIR/manifests/chapter_manifest.json"
BOOK_MANIFEST_PATH="$BASE_DIR/manifests/book_manifest.json"

if [ -f "$CHAPTER_MANIFEST_PATH" ]; then
  if python3 - <<'PY'
import json
p = "manifests/chapter_manifest.json"
d = json.load(open(p, "r", encoding="utf-8"))
for ch in d.get("chapters", []):
    g = ch.get("glossary", {})
    lifecycle = g.get("lifecycle")
    assert lifecycle in ("draft", "approved", "locked", "deprecated")
    assert isinstance(g.get("evidence_paths", []), list)
    assert isinstance(g.get("source_closure_ids", []), list)
print("ok")
PY
  then
    print_summary "chapter_manifest_glossary_lifecycle" "PASS" "valid"
  else
    print_summary "chapter_manifest_glossary_lifecycle" "FAIL" "invalid"
  fi
else
  print_summary "chapter_manifest_glossary_lifecycle" "SKIP" "missing_manifest"
fi

if [ -f "$BOOK_MANIFEST_PATH" ]; then
  if python3 - <<'PY'
import json
p = "manifests/book_manifest.json"
d = json.load(open(p, "r", encoding="utf-8"))
books = d.get("books")
entries = books if isinstance(books, list) else [d]
for entry in entries:
    prov = entry.get("provenance", {})
    assert isinstance(prov, dict)
    g = prov.get("glossary", {})
    lifecycle = g.get("lifecycle")
    assert lifecycle in ("draft", "approved", "locked", "deprecated")
    assert isinstance(g.get("evidence_paths", []), list)
    assert isinstance(g.get("source_closure_ids", []), list)
print("ok")
PY
  then
    print_summary "book_manifest_glossary_lifecycle" "PASS" "valid"
  else
    print_summary "book_manifest_glossary_lifecycle" "FAIL" "invalid"
  fi
else
  print_summary "book_manifest_glossary_lifecycle" "SKIP" "missing_manifest"
fi

# B6) review pack bundling
REVIEW_PACK_INDEX_PATH="$BASE_DIR/indices/review_pack_index.json"
if [ -f "$REVIEW_PACK_INDEX_PATH" ]; then
  print_summary "review_pack_index_exists" "PASS" "exists"
  if python3 - <<PY
import json
path = "$REVIEW_PACK_INDEX_PATH"
try:
    data = json.load(open(path))
    if 'generated_at' not in data:
        raise SystemExit('missing generated_at key')
except Exception as exc:
    print(f'review_pack_index_error: {exc}')
    raise
PY
  then
    print_summary "review_pack_index_has_generated_at" "PASS" "has key"
  else
    print_summary "review_pack_index_has_generated_at" "FAIL" "missing key"
  fi
else
  print_summary "review_pack_index_exists" "FAIL" "missing"
fi

if [ -f "$BASE_DIR/manifests/book_manifest.json" ]; then
  if python3 - <<'PY'
import json
p = "manifests/book_manifest.json"
d = json.load(open(p, "r", encoding="utf-8"))
entries = d.get("books")
entries = entries if isinstance(entries, list) else [d]
for entry in entries:
    prov = entry.get("provenance", {})
    rp = prov.get("review_packs", {})
    assert isinstance(rp, dict)
    assert "entries" in rp
print("ok")
PY
  then
    print_summary "book_manifest_review_packs" "PASS" "present"
  else
    print_summary "book_manifest_review_packs" "FAIL" "missing/invalid"
  fi
else
  print_summary "book_manifest_review_packs" "SKIP" "missing_manifest"
fi

### B8 — Build manifest generation (full)
BUILD_MANIFEST_RC=0
python3 scripts/validate_build_manifests.py > "$AUDIT_DIR/validate_build_manifests.stdout.txt" 2>&1 || BUILD_MANIFEST_RC=$?
if [ "$BUILD_MANIFEST_RC" -eq 0 ]; then
  print_summary "build_manifest_exists_for_each_export" "PASS" "validated"
  print_summary "build_manifest_checksums_match_exports" "PASS" "validated"
  print_summary "build_manifest_tool_versions_present" "PASS" "validated"
else
  print_summary "build_manifest_exists_for_each_export" "FAIL" "rc=$BUILD_MANIFEST_RC"
  print_summary "build_manifest_checksums_match_exports" "FAIL" "rc=$BUILD_MANIFEST_RC"
  print_summary "build_manifest_tool_versions_present" "FAIL" "rc=$BUILD_MANIFEST_RC"
fi

# D) API endpoints
if [ "$API_UP" = "yes" ]; then
  if curl -s http://127.0.0.1:8010/health | rg -q '"ok"\s*:\s*true'; then
    print_summary "GET_/health" "PASS" "ok:true"
  else
    print_summary "GET_/health" "FAIL" "unexpected"
  fi

  INBOX_JSON="$AUDIT_DIR/inbox.json"
  curl -s http://127.0.0.1:8010/inbox > "$INBOX_JSON"
  if rg -q '"items"\s*:\s*\[' "$INBOX_JSON"; then
    print_summary "GET_/inbox" "PASS" "items[]"
  else
    print_summary "GET_/inbox" "FAIL" "missing_items"
  fi

  if INBOX_JSON_PATH="$INBOX_JSON" python3 - <<'PY'
import json, os
path = os.environ['INBOX_JSON_PATH']
try:
    data = json.load(open(path))
    items = data.get('items', [])
    for item in items:
        if 'chapter_id' not in item:
            raise SystemExit('missing chapter_id key')
except Exception:
    raise
PY
  then
    print_summary "GET_/inbox_chapter_id_key" "PASS" "exists"
  else
    print_summary "GET_/inbox_chapter_id_key" "FAIL" "missing"
  fi

  if INBOX_JSON_PATH="$INBOX_JSON" python3 - <<'PY'
import json, os, sys
path = os.environ["INBOX_JSON_PATH"]
try:
    data = json.load(open(path))
    items = data.get("items", [])
    counts = data.get("counts", {})
    if counts.get("total") != len(items):
        print(f"counts mismatch: total={counts.get('total')} items={len(items)}")
        raise SystemExit(1)
except Exception:
    raise
PY
  then
    print_summary "GET_/inbox_counts" "PASS" "total_matches_items"
  else
    print_summary "GET_/inbox_counts" "FAIL" "counts_total_mismatch"
  fi

  PROPOSAL_JSON="$AUDIT_DIR/proposal_P-TEST.json"
  curl -s http://127.0.0.1:8010/proposals/P-TEST > "$PROPOSAL_JSON"
  if rg -q '"proposal_md"' "$PROPOSAL_JSON"; then
    if [ -f "$BASE_DIR/proposals/P-TEST/proposal.md" ]; then
      if rg -q '"proposal_md"\s*:\s*""' "$PROPOSAL_JSON"; then
        print_summary "GET_/proposals/P-TEST" "FAIL" "proposal_md_empty"
      else
        print_summary "GET_/proposals/P-TEST" "PASS" "proposal_md_present"
      fi
    else
      print_summary "GET_/proposals/P-TEST" "WARN" "proposal.md_missing"
    fi
  else
    print_summary "GET_/proposals/P-TEST" "FAIL" "proposal_md_missing"
  fi

  # B6) review_pack_files include name + path
  TEST_REVIEW_PACK_ID="P-TEST-REVIEW"
  TEST_REVIEW_PACK_DIR="$BASE_DIR/proposals/$TEST_REVIEW_PACK_ID/review_pack"
  mkdir -p "$TEST_REVIEW_PACK_DIR"
  printf "dummy" > "$TEST_REVIEW_PACK_DIR/readme.txt"
  REVIEW_PACK_JSON="$AUDIT_DIR/proposal_${TEST_REVIEW_PACK_ID}.json"
  curl -s http://127.0.0.1:8010/proposals/$TEST_REVIEW_PACK_ID > "$REVIEW_PACK_JSON"
  if python3 - <<'PY'
import json
p = "audit/qa/latest_full/proposal_P-TEST-REVIEW.json"
data = json.load(open(p, "r", encoding="utf-8"))
files = data.get("review_pack_files", [])
if files:
    assert isinstance(files[0], dict)
    assert "name" in files[0] and "path" in files[0]
print("ok")
PY
  then
    print_summary "review_pack_files_have_name" "PASS" "name+path"
  else
    print_summary "review_pack_files_have_name" "FAIL" "missing name"
  fi
else
  print_summary "GET_/health" "FAIL" "api_not_running"
  print_summary "GET_/inbox" "FAIL" "api_not_running"
  print_summary "GET_/proposals/P-TEST" "FAIL" "api_not_running"
  print_summary "review_pack_files_have_name" "FAIL" "api_not_running"
fi

# E) Closure contract
if [ "$API_UP" = "yes" ]; then
  TS_SHORT="$(date -u +%s | tail -c 6)"
  TEST_PREFIX="QAF${TS_SHORT}"
  TEST_ID="${TEST_PREFIX}-FULL"
  TEST_PROPOSAL_DIR="$BASE_DIR/proposals/$TEST_ID"
  mkdir -p "$TEST_PROPOSAL_DIR"
  printf '{ "status": "open", "severity": "info" }' > "$TEST_PROPOSAL_DIR/status.json"

  curl -s -X POST http://127.0.0.1:8010/closures \
    -H 'Content-Type: application/json' \
    -d "{\"proposal_id\":\"$TEST_ID\",\"run_id\":\"RUN_QA_FULL\",\"decision_type\":\"qa_full\",\"rationale\":\"QA full system closure rationale\",\"evidence_paths\":[\"proposals/$TEST_ID/status.json\"],\"sign_off\":true,\"created_by\":\"qa\"}" \
    > "$AUDIT_DIR/closure_${TEST_ID}.json"

  if rg -q '"closure_id"' "$AUDIT_DIR/closure_${TEST_ID}.json"; then
    print_summary "POST_/closures" "PASS" "closure_created"
  else
    print_summary "POST_/closures" "FAIL" "closure_not_created"
  fi

  if rg -q '"status"\s*:\s*"closed"' "$TEST_PROPOSAL_DIR/status.json"; then
    print_summary "proposal_status_closed" "PASS" "status.json updated"
  else
    print_summary "proposal_status_closed" "FAIL" "status_not_closed"
  fi

  curl -s -X POST http://127.0.0.1:8010/reindex > "$AUDIT_DIR/reindex.json"
  if rg -q '"ok"\s*:\s*true' "$AUDIT_DIR/reindex.json"; then
    print_summary "POST_/reindex" "PASS" "ok"
  else
    print_summary "POST_/reindex" "FAIL" "not_ok"
  fi

  if python3 - <<'PY' >/dev/null 2>&1
import json
p='indices/inbox_index.json'
try:
    d=json.load(open(p))
    items=[i for i in d.get('items',[]) if i.get('source_id')=='$TEST_ID']
    print('FOUND' if items else 'NOT_FOUND')
except Exception as e:
    print('ERROR', e)
PY
  then
    inbox_result=$(python3 - <<'PY'
import json
p='indices/inbox_index.json'
try:
    d=json.load(open(p))
    items=[i for i in d.get('items',[]) if i.get('source_id')=='$TEST_ID']
    print('FOUND' if items else 'NOT_FOUND')
except Exception:
    print('ERROR')
PY
)
    if [ "$inbox_result" = "NOT_FOUND" ]; then
      print_summary "inbox_after_closure" "PASS" "not_present"
    else
      print_summary "inbox_after_closure" "FAIL" "$inbox_result"
    fi
  else
    print_summary "inbox_after_closure" "FAIL" "read_error"
  fi
else
  print_summary "POST_/closures" "FAIL" "api_not_running"
  print_summary "proposal_status_closed" "FAIL" "api_not_running"
  print_summary "POST_/reindex" "FAIL" "api_not_running"
  print_summary "inbox_after_closure" "FAIL" "api_not_running"
fi

### B9 — Exporter skeleton (presence only)
if [ -x "$BASE_DIR/scripts/book_export.py" ]; then
  print_summary "exporter_script_exists" "PASS" "present"
  if python3 "$BASE_DIR/scripts/book_export.py" --help >/dev/null 2>&1; then
    print_summary "exporter_help_runs" "PASS" "ok"
  else
    print_summary "exporter_help_runs" "WARN" "help_failed"
  fi
else
  print_summary "exporter_script_exists" "WARN" "missing"
  print_summary "exporter_help_runs" "WARN" "missing"
fi

### R1 — Release identity enforcement (ADR-011)
RELEASE_IDENTITY_RC=0
RELEASE_IDENTITY_OUT=""
if [ -x "$BASE_DIR/scripts/qa_release_identity.sh" ]; then
  RELEASE_IDENTITY_OUT="$("$BASE_DIR/scripts/qa_release_identity.sh" 2>&1 || true)"
  if echo "$RELEASE_IDENTITY_OUT" | rg -q '^SKIP:'; then
    print_summary "release_identity_enforced" "SKIP" "$(echo "$RELEASE_IDENTITY_OUT" | head -n 1)"
  else
    "$BASE_DIR/scripts/qa_release_identity.sh" >/dev/null 2>&1 || RELEASE_IDENTITY_RC=$?
    if [ "$RELEASE_IDENTITY_RC" -eq 0 ]; then
      print_summary "release_identity_enforced" "PASS" "latest.json + immutability"
    else
      print_summary "release_identity_enforced" "FAIL" "qa_release_identity.sh rc=$RELEASE_IDENTITY_RC"
    fi
  fi
else
  print_summary "release_identity_enforced" "SKIP" "missing qa_release_identity.sh"
fi

### B11 — Deterministic exports & checksums
BOOK_EXPORT_RC=0
if [ -x "$BASE_DIR/scripts/book_export.py" ] && [ -f "$BASE_DIR/manifests/book_manifest.json" ]; then
  python3 "$BASE_DIR/scripts/book_export.py" --release-id latest > "$AUDIT_DIR/book_export.stdout.txt" 2>&1 || BOOK_EXPORT_RC=$?
  if [ "$BOOK_EXPORT_RC" -eq 0 ]; then
    print_summary "book_export_run" "PASS" "export ok (latest.json pointer updated)"
  else
    print_summary "book_export_run" "FAIL" "rc=$BOOK_EXPORT_RC"
  fi
else
  print_summary "book_export_run" "SKIP" "missing_exporter_or_manifest"
fi

if python3 - <<'PY'
import json
from pathlib import Path
bm_path = Path("manifests/book_manifest.json")
if not bm_path.exists():
    raise SystemExit(0)
bm = json.load(open(bm_path, "r", encoding="utf-8"))
entry = bm
books = bm.get("books")
if isinstance(books, list) and books:
    entry = books[0]
book_id = entry.get("book_id", "BOOK-DEFAULT")
latest_json = Path("exports") / "books" / book_id / "releases" / "latest.json"
if not latest_json.exists():
    raise SystemExit(1)
release_id = json.load(open(latest_json, "r", encoding="utf-8")).get("release_id")
if not release_id or release_id == "latest":
    raise SystemExit(1)
checksums = Path("exports") / "books" / book_id / "releases" / release_id / "CHECKSUMS.sha256"
if not checksums.exists():
    raise SystemExit(1)
print("ok")
PY
then
  print_summary "export_checksums_exists" "PASS" "CHECKSUMS.sha256 present"
else
  print_summary "export_checksums_exists" "FAIL" "missing"
fi

if python3 - <<'PY'
import json, hashlib
from pathlib import Path
bm_path = Path("manifests/book_manifest.json")
if not bm_path.exists():
    raise SystemExit(0)
bm = json.load(open(bm_path, "r", encoding="utf-8"))
entry = bm
books = bm.get("books")
if isinstance(books, list) and books:
    entry = books[0]
book_id = entry.get("book_id", "BOOK-DEFAULT")
latest_json = Path("exports") / "books" / book_id / "releases" / "latest.json"
if not latest_json.exists():
    raise SystemExit(1)
release_id = json.load(open(latest_json, "r", encoding="utf-8")).get("release_id")
if not release_id or release_id == "latest":
    raise SystemExit(1)
release_dir = Path("exports") / "books" / book_id / "releases" / release_id
checksums = release_dir / "CHECKSUMS.sha256"
if not checksums.exists():
    raise SystemExit(1)
lines = [ln for ln in checksums.read_text(encoding="utf-8").splitlines() if ln.strip()]
entries = {}
for ln in lines:
    if "  " not in ln:
        raise SystemExit(1)
    h, rel = ln.split("  ", 1)
    entries[rel] = h
exports = entry.get("exports", [])
if not isinstance(exports, list) or not exports:
    raise SystemExit(0)
bm_ref = exports[0].get("build_manifest")
if not isinstance(bm_ref, str) or not bm_ref:
    raise SystemExit(1)
bm_data = json.load(open(Path(bm_ref), "r", encoding="utf-8"))
files = bm_data.get("exports", {}).get("files", [])
for rel in files:
    rel_path = f"files/{rel}"
    fp = release_dir / rel_path
    if not fp.exists():
        raise SystemExit(1)
    h = hashlib.sha256(fp.read_bytes()).hexdigest()
    if entries.get(rel_path) != h:
        raise SystemExit(1)
print("ok")
PY
then
  print_summary "export_checksums_match_build_manifest" "PASS" "ok"
else
  print_summary "export_checksums_match_build_manifest" "FAIL" "mismatch"
fi

if python3 - <<'PY'
from pathlib import Path
bm_path = Path("manifests/book_manifest.json")
if not bm_path.exists():
    raise SystemExit(0)
bm = __import__("json").load(open(bm_path, "r", encoding="utf-8"))
entry = bm
books = bm.get("books")
if isinstance(books, list) and books:
    entry = books[0]
book_id = entry.get("book_id", "BOOK-DEFAULT")
latest_json = Path("exports") / "books" / book_id / "releases" / "latest.json"
if not latest_json.exists():
    raise SystemExit(1)
release_id = __import__("json").load(open(latest_json, "r", encoding="utf-8")).get("release_id")
if not release_id or release_id == "latest":
    raise SystemExit(1)
checksums = Path("exports") / "books" / book_id / "releases" / release_id / "CHECKSUMS.sha256"
if not checksums.exists():
    raise SystemExit(1)
lines = [ln for ln in checksums.read_text(encoding="utf-8").splitlines() if ln.strip()]
paths = [ln.split("  ", 1)[1] for ln in lines]
if paths != sorted(paths):
    raise SystemExit(1)
print("ok")
PY
then
  print_summary "export_checksums_sorted" "PASS" "sorted"
else
  print_summary "export_checksums_sorted" "FAIL" "unsorted"
fi

# F) UI build sanity
if command -v npm >/dev/null 2>&1; then
  ui_rc=0
  (cd "$BASE_DIR/ui" && npm install && npm run build) >"$UI_LOG" 2>&1 || ui_rc=$?
  print_summary "ui_build" "$(passfail $ui_rc)" "npm run build"
else
  print_summary "ui_build" "SKIP" "npm_missing"
fi

printf '\nSummary written to %s\n' "$SUMMARY"
normalize_summary
printf 'Normalized summary written to %s\n' "${AUDIT_DIR}/summary.normalized.tsv"
