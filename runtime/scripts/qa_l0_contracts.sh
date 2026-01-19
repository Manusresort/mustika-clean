#!/usr/bin/env bash
set -u

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
UMBRELLA_ROOT="$(cd "$BASE_DIR/../.." && pwd)"
SUBREPO="$UMBRELLA_ROOT/mustika-rasa-clean"

print_row() {
  printf '%-28s | %-32s | %-6s | %s\n' "$1" "$2" "$3" "$4"
}

run_check() {
  local pipeline="$1"
  local check="$2"
  local cmd="$3"
  local expected="$4"
  local result
  local notes

  eval "$cmd" >/tmp/qa_l0_out.$$ 2>/tmp/qa_l0_err.$$
  local status=$?

  if [ $status -eq 0 ]; then
    result="PASS"
  else
    result="FAIL"
  fi

  if [ "$expected" = "$result" ]; then
    notes="ok"
  else
    notes="expected $expected"
  fi

  print_row "$pipeline" "$check" "$result" "$notes"
}

printf '%-28s | %-32s | %-6s | %s\n' "PIPELINE" "CHECK" "RESULT" "NOTES"
printf '%-28s-+-%-32s-+-%-6s-+-%s\n' "----------------------------" "--------------------------------" "------" "------------------------------"

run_check "OCR ingestion" "contract presence" "rg -n \"page_sources/ocr_txt|page_sources/ocr_tsv\" \"$SUBREPO/documentation/operator/AGENT_USAGE_CONTRACT_PAGE_SOURCES.md\"" "PASS"
run_check "OCR ingestion" "entrypoint discovery" "ls scripts | rg -n \"ocr\"" "FAIL"

run_check "OCR correction" "contract presence" "rg -n \"OCR Correction Contract|page_ocr_corrected\" \"$SUBREPO/documentation/operator/OCR_CORRECTION_CONTRACT.md\"" "PASS"
run_check "OCR correction" "entrypoint discovery" "ls scripts | rg -n \"ocr.*correct|correct.*ocr\"" "FAIL"

run_check "Definitive source" "contract presence" "rg -n \"Definitive Source Build Contract|definitive_source\" \"$SUBREPO/documentation/operator/DEFINITIVE_SOURCE_BUILD_CONTRACT.md\"" "PASS"
run_check "Definitive source" "entrypoint discovery" "ls scripts | rg -n \"definitive|source_build\"" "FAIL"

run_check "Page-based validator" "contract presence" "rg -n \"Validator Contract — Page-Based Agent Outputs\" \"$SUBREPO/documentation/operator/VALIDATOR_CONTRACT_PAGE_BASED_OUTPUTS.md\"" "PASS"
run_check "Page-based validator" "entrypoint discovery" "ls scripts | rg -n \"page.*validator|validator.*page\"" "FAIL"

run_check "Review pack" "consumer presence" "rg -n \"review_pack\" api_server.py" "PASS"
run_check "Review pack" "entrypoint discovery" "ls scripts | rg -n \"review_pack\"" "FAIL"

run_check "Proposal generator" "consumer presence" "rg -n \"proposal.md|status.json|required_closure.json\" indexer.py" "PASS"
run_check "Proposal generator" "entrypoint discovery" "ls scripts | rg -n \"proposal\"" "FAIL"

run_check "Signals/gates (Runner V2)" "writer discovery" "rg -n \"signals.json|gates.json\" src/runner_v2/runner.py" "FAIL"

run_check "OCR signal scan (legacy)" "evidence log" "test -f \"$SUBREPO/documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/SCAN_SIGNALS/run_log.md\"" "PASS"
run_check "OCR signal scan (legacy)" "entrypoint discovery" "ls scripts | rg -n \"scan_signals|signal_scan\"" "FAIL"

run_check "Promotion pipeline" "promotion dir" "test -d promotion" "PASS"
run_check "Promotion pipeline" "spec discovery" "ls docs/implementation | rg -n \"PROMOTION|promotion\"" "FAIL"

rm -f /tmp/qa_l0_out.$$ /tmp/qa_l0_err.$$
