# ENVIRONMENT — Local Runtime Setup (authoritative)

This document is the source of truth for local dev/runtime environment setup.

## Python venv (required)

```bash
cd runtime
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

## Python deps install

`runtime/requirements-ui.txt` contains backend/runtime deps plus translation pipeline deps (incl. `crewai`).

```bash
cd runtime
pip install -r requirements-ui.txt
```

## UI deps install

```bash
cd runtime/ui
npm install
```

## Run / stop (canonical)

```bash
cd runtime && ./scripts/dev_up.sh
cd runtime && ./scripts/dev_down.sh
```

## QA (full system)

```bash
cd runtime && ./scripts/qa_full_system.sh
```

## Health checks

```bash
curl http://127.0.0.1:8010/health
curl http://127.0.0.1:8010/inbox
```

## Required environment variables

- `OPENAI_API_KEY` (required for OpenAI-compatible backends)
- `OPENAI_MODEL` or `LITELLM_MODEL` (model selection)
- Optional: `OPENAI_BASE_URL` or `LITELLM_BASE_URL` (local gateway)

## Repo invariants (CI enforced)

- `runtime/` code is tracked
- State directories are generated and must not be committed:
  - `runtime/indices/`
  - `runtime/runs/`
  - `runtime/audit/`
  - `runtime/proposals/`
  - `runtime/closures/`
  - `runtime/.venv*`
  - top-level `indices/`

## Troubleshooting

- No active venv → `cd runtime && source .venv/bin/activate`
- `crewai` missing → `cd runtime && pip install -r requirements-ui.txt`
- Wrong Python version → recreate venv with Python 3.11
