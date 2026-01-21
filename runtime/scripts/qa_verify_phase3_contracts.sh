#!/usr/bin/env bash
set -euo pipefail

API_BASE_URL="${API_BASE_URL:-http://127.0.0.1:8000}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pass() { echo "PASS: $*"; }
fail() { echo "FAIL: $*" >&2; exit 1; }

# 1) GET /health, require HTTP 200
health_code="$(curl -s -o /tmp/qa_health.json -w "%{http_code}" "$API_BASE_URL/health" || true)"
if [[ "$health_code" != "200" ]]; then
  fail "/health HTTP $health_code"
fi
pass "/health HTTP 200"

# 2) POST /reindex, require base_path_used ends with /runtime
reindex_code="$(curl -s -o /tmp/qa_reindex.json -w "%{http_code}" -X POST "$API_BASE_URL/reindex" || true)"
if [[ "$reindex_code" != "200" ]]; then
  fail "/reindex HTTP $reindex_code"
fi

base_path_used="$(python -c 'import json; import sys; p=json.load(open("/tmp/qa_reindex.json")); print(p.get("base_path_used",""))')"
if [[ -z "$base_path_used" ]]; then
  fail "base_path_used missing in /reindex response"
fi
if [[ "$base_path_used" != */runtime ]]; then
  fail "base_path_used does not end with /runtime: $base_path_used"
fi
pass "/reindex base_path_used=$base_path_used"

# 3) Choose proposal id deterministically
proposal_root="$ROOT_DIR/proposals"
proposal_id=""
if [[ -d "$proposal_root/P-001" ]]; then
  proposal_id="P-001"
else
  if [[ -d "$proposal_root" ]]; then
    proposal_id="$(ls -1 "$proposal_root" | sort | head -n 1)"
  fi
fi
if [[ -z "$proposal_id" ]]; then
  fail "No proposals found under $proposal_root"
fi
pass "proposal_id=$proposal_id"

# 4) GET /proposals/<id>, require proposal_md key exists
proposal_code="$(curl -s -o /tmp/qa_proposal.json -w "%{http_code}" "$API_BASE_URL/proposals/$proposal_id" || true)"
if [[ "$proposal_code" != "200" ]]; then
  fail "/proposals/$proposal_id HTTP $proposal_code"
fi
has_proposal_md="$(python -c 'import json; p=json.load(open("/tmp/qa_proposal.json")); print("proposal_md" in p)')"
if [[ "$has_proposal_md" != "True" ]]; then
  fail "proposal_md key missing in /proposals/$proposal_id"
fi
pass "/proposals/$proposal_id contains proposal_md"

# 5) Inbox rule proof for closed proposals
status_path="$proposal_root/$proposal_id/status.json"
status_val=""
if [[ -f "$status_path" ]]; then
  status_val="$(python -c 'import json; p=json.load(open("'"$status_path"'")); print(p.get("status",""))')"
fi

inbox_path="$ROOT_DIR/indices/inbox_index.json"
if [[ ! -f "$inbox_path" ]]; then
  fail "inbox_index.json missing at $inbox_path"
fi

if [[ "$status_val" == "closed" ]]; then
  has_bad="$(python -c 'import json; data=json.load(open("'"$inbox_path"'")); items=data.get("items",[]); pid="'"$proposal_id"'"; print(any(i.get("kind")=="closure_needed" and i.get("source_id")==pid for i in items))')"
  if [[ "$has_bad" == "True" ]]; then
    fail "closure_needed present for closed proposal $proposal_id"
  fi
  pass "no closure_needed for closed proposal $proposal_id"
else
  echo "NOTE: proposal $proposal_id status is '$status_val'; closure_needed rule not enforced for non-closed"
fi

pass "Phase 3 contracts OK"
