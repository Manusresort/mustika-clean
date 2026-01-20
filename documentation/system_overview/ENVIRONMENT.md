# ENVIRONMENT — Local Runtime Setup (authoritative)

This document is the source of truth for local dev/runtime environment setup.

## Mac (Apple Silicon) — quick setup

```bash
cd runtime
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-ui.txt
cd ui
npm install
```

## Run / stop (canonical)

```bash
cd runtime && ./scripts/dev_up.sh
cd runtime && ./scripts/dev_down.sh
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

- No active venv → `source runtime/.venv/bin/activate`
- `crewai` missing → `pip install -r runtime/requirements-ui.txt`
- Wrong Python version → recreate venv with Python 3.11
