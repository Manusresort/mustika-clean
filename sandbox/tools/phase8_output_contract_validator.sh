#!/usr/bin/env bash
set -euo pipefail

run_dir="${1:-}"
if [[ -z "${run_dir}" ]]; then
  echo "usage: phase8_output_contract_validator.sh <run_dir>" >&2
  exit 2
fi
if [[ ! -d "${run_dir}" ]]; then
  echo "ERROR: run_dir not found: ${run_dir}" >&2
  exit 2
fi

eval_dir="${run_dir}/eval"
mkdir -p "${eval_dir}"
report_path="${eval_dir}/output_contract_checks.txt"

overall_status="PASS"
failed_list=()

# Check B: No governance terms like "definitieve" (scan final output if present)
final_txt="${run_dir}/outputs/final.txt"
status_b="PASS"
if [[ -f "${final_txt}" ]]; then
  if rg -n -i 'definitieve' "${final_txt}" >/dev/null 2>&1; then
    status_b="FAIL"
  fi
fi
if [[ "${status_b}" != "PASS" ]]; then
  failed_list+=("NO_GOVERNANCE_TERMS")
  overall_status="FAIL"
fi

{
  echo "overall_status: ${overall_status}"
  echo "check_id: NO_GOVERNANCE_TERMS"
  echo "status: ${status_b}"
  if [[ "${#failed_list[@]}" -gt 0 ]]; then
    echo "failed_checks: ${failed_list[*]}"
  fi
} > "${report_path}"

if [[ "${overall_status}" != "PASS" ]]; then
  exit 1
fi
exit 0
