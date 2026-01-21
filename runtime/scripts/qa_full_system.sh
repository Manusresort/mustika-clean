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
  print_summary "api_health" "PASS" "already_running"
else
  print_summary "api_health" "WARN" "not_running_attempting_start"
  nohup uvicorn api_server:app --host 127.0.0.1 --port 8010 >"$API_LOG" 2>&1 &
  for i in {1..15}; do
    sleep 1
    if curl -s http://127.0.0.1:8010/health | rg -q '"ok"\s*:\s*true'; then
      API_UP="yes"
      break
    fi
  done
  if [ "$API_UP" = "yes" ]; then
    print_summary "api_health_after_start" "PASS" "api_started"
  else
    print_summary "api_health_after_start" "FAIL" "api_not_healthy"
  fi
fi

# C) Indexer checks
python3 indexer.py >/tmp/qa_full_indexer.txt 2>&1
print_summary "indexer_run" "$(passfail $?)" "python3 indexer.py"

for idx in run_index.json proposal_index.json closure_index.json inbox_index.json; do
  if [ -f "$BASE_DIR/indices/$idx" ]; then
    print_summary "index_$idx" "PASS" "exists"
  else
    print_summary "index_$idx" "FAIL" "missing"
  fi
done

# D) API endpoints
if [ "$API_UP" = "yes" ]; then
  if curl -s http://127.0.0.1:8010/health | rg -q '"ok"\s*:\s*true'; then
    print_summary "GET_/health" "PASS" "ok:true"
  else
    print_summary "GET_/health" "FAIL" "unexpected"
  fi

  if curl -s http://127.0.0.1:8010/inbox | rg -q '"items"\s*:\s*\['; then
    print_summary "GET_/inbox" "PASS" "items[]"
  else
    print_summary "GET_/inbox" "FAIL" "missing_items"
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
else
  print_summary "GET_/health" "SKIP" "api_not_running"
  print_summary "GET_/inbox" "SKIP" "api_not_running"
  print_summary "GET_/proposals/P-TEST" "SKIP" "api_not_running"
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
  print_summary "POST_/closures" "SKIP" "api_not_running"
  print_summary "proposal_status_closed" "SKIP" "api_not_running"
  print_summary "POST_/reindex" "SKIP" "api_not_running"
  print_summary "inbox_after_closure" "SKIP" "api_not_running"
fi

# F) UI build sanity
if command -v npm >/dev/null 2>&1; then
  (cd "$BASE_DIR/ui" && npm install && npm run build) >"$UI_LOG" 2>&1
  print_summary "ui_build" "$(passfail $?)" "npm run build"
else
  print_summary "ui_build" "SKIP" "npm_missing"
fi

printf '\nSummary written to %s\n' "$SUMMARY"
