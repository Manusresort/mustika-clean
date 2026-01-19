#!/usr/bin/env bash
set -euo pipefail

run_dir="${1:-}"
if [[ -z "${run_dir}" ]]; then
  echo "usage: phase8_run_with_gate.sh <run_dir> [english_txt] [rough_nl_txt]" >&2
  exit 2
fi

sandbox/tools/phase8_output_contract_validator.sh "${run_dir}"
validator_rc=$?

if [[ "${validator_rc}" -ne 0 ]]; then
  echo "PHASE8_GATE_FAIL: output contract validation failed for ${run_dir}" >&2
  exit "${validator_rc}"
fi

echo "PHASE8_GATE_PASS: output contract validation passed for ${run_dir}"
exit 0
