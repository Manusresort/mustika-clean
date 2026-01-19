# Repo Migration Verification (Target Repo)

This checklist validates that the clean repo works end‑to‑end **after** a
copy migration (DRY_RUN=0). It does not modify the source repo.

---

## A) Preconditions (minimal)

- **Python**: 3.x available (venv in `runtime/.venv` preferred)
- **Node/npm**: installed for UI (`runtime/ui/`)
- **Env (if using local models):**
  - `LITELLM_MODEL` (if required by your setup)
  - `OLLAMA_API_BASE` (if using Ollama)
- **Ports:**
  - API: `8000`
  - UI: `5173` (fallback `5174`)

---

## B) Verification Steps (copy/paste commands)

### 1) Confirm structure and key files exist (target)
```
cd /Users/vwvd/Millway/AI-folder/Crew-AI/mustika-rasa-clean
ls runtime/src runtime/scripts runtime/ui runtime/indexer.py runtime/api_server.py
ls runtime/runs runtime/proposals runtime/closures runtime/canonical runtime/indices runtime/audit
```

### 2) Run indexer + validate JSON
```
cd /Users/vwvd/Millway/AI-folder/Crew-AI/mustika-rasa-clean/runtime
python3 indexer.py
python3 -m json.tool indices/run_index.json >/dev/null
python3 -m json.tool indices/inbox_index.json >/dev/null
python3 -m json.tool indices/proposal_index.json >/dev/null
python3 -m json.tool indices/closure_index.json >/dev/null
```

### 3) Start API + verify endpoints
```
cd /Users/vwvd/Millway/AI-folder/Crew-AI/mustika-rasa-clean/runtime
python3 -m uvicorn api_server:app --host 127.0.0.1 --port 8010 --reload
```
Then in a new terminal:
```
curl http://127.0.0.1:8010/health
curl http://127.0.0.1:8010/inbox
```
Extract a run_id and test:
```
python3 - << 'PY'
import json
with open('indices/run_index.json','r') as f:
    runs = json.load(f).get('runs',[])
print(runs[0]['run_id'] if runs else '')
PY
curl http://127.0.0.1:8010/runs/<run_id>
```
If proposals exist:
```
python3 - << 'PY'
import json
with open('indices/proposal_index.json','r') as f:
    items = json.load(f).get('proposals',[])
print(items[0]['proposal_id'] if items else '')
PY
curl http://127.0.0.1:8010/proposals/<proposal_id>
```
If closures exist:
```
python3 - << 'PY'
import json
with open('indices/closure_index.json','r') as f:
    items = json.load(f).get('closures',[])
print(items[0]['closure_id'] if items else '')
PY
curl http://127.0.0.1:8010/closures/<closure_id>
```
Reindex via API:
```
curl -X POST http://127.0.0.1:8010/reindex
```

### 4) Start UI + verify
```
cd /Users/vwvd/Millway/AI-folder/Crew-AI/mustika-rasa-clean/runtime/ui
npm install
npm run dev
```
Manual checks:
- Inbox loads (no 500)
- Run detail loads for a known `run_id`

---

## C) Expected Outputs (what “good” looks like)

- `indices/*.json` are valid JSON and non‑empty.
- `GET /health` returns HTTP 200 with `ok: true`.
- `GET /inbox` returns HTTP 200 with `items` (possibly empty).
- `GET /runs/{run_id}` returns HTTP 200 with run details.
- Proposal/closure endpoints return HTTP 200 if IDs exist.

**Acceptable variation:**
- `generated_at` timestamps change.
- Inbox `items` may be empty if no review signals exist.

---

## D) Troubleshooting

**Port already in use**
- `lsof -i :8010`
- `lsof -i :5173`

**Missing venv / uvicorn**
- Activate venv or install deps in `runtime/.venv`.

**Missing indices**
- Run `python3 indexer.py` and recheck `indices/*.json`.

**API errors**
- Check `runtime/audit/api_actions.log` and API console output.

---

## E) Rollback

The source repo remains canonical. To rollback:
- Stop target API/UI processes
- Return to the source repo (`/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy`)
