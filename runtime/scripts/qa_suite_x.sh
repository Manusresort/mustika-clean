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

PYTHON_BIN="$ROOT/.venv/bin/python"
[ -x "$PYTHON_BIN" ] || { echo "ERROR: expected $PYTHON_BIN" >&2; exit 1; }

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUNTIME_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="$(cd "$RUNTIME_ROOT/.." && pwd)"
if [[ ! -f "${RUNTIME_ROOT}/api_server.py" || ! -f "${RUNTIME_ROOT}/indexer.py" ]]; then
  echo "ERROR: runtime root missing api_server.py or indexer.py: ${RUNTIME_ROOT}" >&2
  exit 1
fi
QA_ROOT="${RUNTIME_ROOT}/audit/qa"
TS="$(date +%Y%m%dT%H%M%S)"
RUN_DIR="${QA_ROOT}/runs/${TS}"
LATEST_DIR="${QA_ROOT}/latest"
SUMMARY="${RUN_DIR}/summary.tsv"

mkdir -p "${RUN_DIR}"
mkdir -p "${QA_ROOT}"
echo -e "test_id\tstatus\tcommand\tlog_path" > "${SUMMARY}"

run_test() {
  local test_id="$1"
  local cmd="$2"
  local log_path="${RUN_DIR}/${test_id}.log"
  echo "== ${test_id} ==" | tee -a "${log_path}"
  echo "CMD: ${cmd}" | tee -a "${log_path}"
  echo "START: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" | tee -a "${log_path}"
  if bash -lc "${cmd}" >> "${log_path}" 2>&1; then
    echo "END: PASS" | tee -a "${log_path}"
    echo -e "${test_id}\tPASS\t${cmd}\t${log_path}" >> "${SUMMARY}"
  else
    echo "END: FAIL" | tee -a "${log_path}"
    echo -e "${test_id}\tFAIL\t${cmd}\t${log_path}" >> "${SUMMARY}"
  fi
  return 0
}

skip_test() {
  local test_id="$1"
  local reason="$2"
  local log_path="${RUN_DIR}/${test_id}.log"
  echo "== ${test_id} ==" > "${log_path}"
  echo "SKIPPED: ${reason}" >> "${log_path}"
  echo -e "${test_id}\tSKIPPED\t-\t${log_path}" >> "${SUMMARY}"
}

cd "${RUNTIME_ROOT}"

API_UP="no"
if curl -s http://127.0.0.1:8010/health >/dev/null 2>&1; then
  API_UP="yes"
else
  # Attempt to start API (no reload)
  nohup uvicorn api_server:app --host 127.0.0.1 --port 8010 > "${RUN_DIR}/api_start.log" 2>&1 &
  for _ in {1..10}; do
    if curl -s http://127.0.0.1:8010/health >/dev/null 2>&1; then
      API_UP="yes"
      break
    fi
    sleep 1
  done
fi

## L0 checks (contracts / entrypoints)
run_test "L0_OCR_CONTRACTS" "rg -n 'page_sources/ocr_txt|page_sources/ocr_tsv|OCR Correction Contract' \"${REPO_ROOT}/documentation/operator\""
run_test "L0_OCR_CORRECTION_CONTRACT" "rg -n 'page_ocr_corrected|manifests/<page_id>.json' \"${REPO_ROOT}/documentation/operator/OCR_CORRECTION_CONTRACT.md\""
run_test "L0_DEFINITIVE_SOURCE_CONTRACT" "rg -n 'definitive_source|builds/<BUILD_ID>/source_nl.txt' \"${REPO_ROOT}/documentation/operator/DEFINITIVE_SOURCE_BUILD_CONTRACT.md\""
run_test "L0_TRANSLATION_ENTRYPOINTS" "rg -n 'run_pipeline|Translation → Readability → Fidelity' test_multi_agent_fidelity.py mustikarasa_codex_cli.py"
run_test "L0_RUNNER_V2_CONTRACT" "rg -n 'create_run_directory|outputs/final.txt|output_contract_checks.txt' src/runner_v2/runner.py"
run_test "L0_VALIDATOR_CONTRACT" "rg -n 'overall_status|CHECK_RESULTS|PASS|FAIL' \"${REPO_ROOT}/sandbox/tools/phase8_output_contract_validator.sh\""
run_test "L0_INDEXER_RULES" "rg -n 'validator_fail|blocking_gate|challenger_issues|proposal_open|required_closure' indexer.py"
run_test "L0_REVIEW_PACK_API" "rg -n 'review_pack' api_server.py"
run_test "L0_PROPOSAL_SCHEMA" "rg -n 'proposal.md|status.json|required_closure.json' indexer.py"
run_test "L0_CLOSURE_SCHEMA" "rg -n 'class ClosureCreate|create_closure' api_server.py"
run_test "L0_AUDIT_LOGS" "rg -n 'ensure_audit_log' api_server.py"
run_test "L0_MIGRATION_SCRIPT" "rg -n 'DRY_RUN|migration_reports' scripts/migrate_to_clean_repo.sh"

## L1 checks (smoke)
run_test "L1_TRANSLATION_PIPELINE" "printf \"EN test\" > /tmp/qa_en.txt && printf \"NL test\" > /tmp/qa_nl.txt && \"$PYTHON_BIN\" test_multi_agent_fidelity.py --english /tmp/qa_en.txt --rough-nl /tmp/qa_nl.txt"
run_test "L1_RUNNER_V2_SMOKE" "printf \"EN test\" > /tmp/qa_en.txt && printf \"NL test\" > /tmp/qa_nl.txt && \"$PYTHON_BIN\" scripts/mustika_run_excerpt.py --excerpt-id QA_EXCERPT --excerpt-source /tmp/qa_en.txt --excerpt-version v1 --english /tmp/qa_en.txt --rough-nl /tmp/qa_nl.txt"
run_test "L1_VALIDATOR_FAIL_SIM" "mkdir -p /tmp/qa_run/eval /tmp/qa_run/outputs && sandbox/tools/phase8_output_contract_validator.sh /tmp/qa_run || true && cat /tmp/qa_run/eval/output_contract_checks.txt"

# Indexer L1 requires manual run folder creation; skip to avoid hand-editing runs.
skip_test "L1_INDEXER_INBOX_SIM" "SKIP: would require manual run bundle creation under runs/ (not allowed)"

if [[ "${API_UP}" == "yes" ]]; then
  run_test "L1_REVIEW_PACK_API" "mkdir -p proposals/P-TEST-REVIEW/review_pack && printf \"dummy\" > proposals/P-TEST-REVIEW/review_pack/readme.txt && curl -s http://127.0.0.1:8010/proposals/P-TEST-REVIEW | \"$PYTHON_BIN\" -m json.tool | rg -n 'review_pack'"
  run_test "L1_PROPOSAL_API" "mkdir -p proposals/P-TEST && printf \"# P-TEST\\nbody\" > proposals/P-TEST/proposal.md && printf '{ \"status\": \"open\", \"severity\": \"info\" }' > proposals/P-TEST/status.json && curl -s http://127.0.0.1:8010/proposals/P-TEST | \"$PYTHON_BIN\" -m json.tool | rg -n 'proposal_md|status'"
  run_test "L1_CLOSURE_API" "mkdir -p proposals/P-TEST-CLOSE && printf '{ \"status\": \"open\", \"severity\": \"info\" }' > proposals/P-TEST-CLOSE/status.json && curl -s -X POST http://127.0.0.1:8010/closures -H 'Content-Type: application/json' -d '{\"proposal_id\":\"P-TEST-CLOSE\",\"run_id\":\"RUN_QA_SUITE_X\",\"decision_type\":\"qa_suite_x\",\"rationale\":\"QA suite X closure rationale\",\"evidence_paths\":[\"proposals/P-TEST-CLOSE/status.json\"],\"sign_off\":true,\"created_by\":\"qa\"}'"
  run_test "L1_AUDIT_REINDEX" "curl -s -X POST http://127.0.0.1:8010/reindex | \"$PYTHON_BIN\" -m json.tool | rg -n \"ok|generated_files\""
else
  skip_test "L1_REVIEW_PACK_API" "SKIP: API not reachable on http://127.0.0.1:8010"
  skip_test "L1_PROPOSAL_API" "SKIP: API not reachable on http://127.0.0.1:8010"
  skip_test "L1_CLOSURE_API" "SKIP: API not reachable on http://127.0.0.1:8010"
  skip_test "L1_AUDIT_REINDEX" "SKIP: API not reachable on http://127.0.0.1:8010"
fi

run_test "L1_MIGRATION_DRY_RUN" "./scripts/migrate_to_clean_repo.sh"

# Update latest folder
rm -rf "${LATEST_DIR}"
cp -R "${RUN_DIR}" "${LATEST_DIR}"

echo "Suite X complete: ${RUN_DIR}"
echo "Summary: ${SUMMARY}"
