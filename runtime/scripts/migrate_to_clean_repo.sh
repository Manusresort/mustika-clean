#!/usr/bin/env bash
set -euo pipefail

# SAFE, COPY-ONLY migration from MVP repo to clean repo
# Default is DRY_RUN=1 (print actions only)

DRY_RUN="${DRY_RUN:-1}"
SOURCE_DIR="/Users/vwvd/Millway/AI-folder/Crew-AI/cursor/codex cli project repo copy"
TARGET_DIR="/Users/vwvd/Millway/AI-folder/Crew-AI/mustika-rasa-clean"
PARENT_ARCH_DOCS="/Users/vwvd/Millway/AI-folder/Crew-AI/Architecture docs"

TIMESTAMP="$(date +%Y%m%dT%H%M%S)"
REPORT_DIR="$SOURCE_DIR/migration_reports"
REPORT_PATH="$REPORT_DIR/${TIMESTAMP}.md"

mkdir -p "$REPORT_DIR"

RSYNC_BASE_OPTS=("-a" "--stats" "--human-readable")
EXCLUDES=(
  "--exclude" "node_modules"
  "--exclude" "__pycache__"
  "--exclude" ".DS_Store"
  "--exclude" ".venv"
)

if [[ "$DRY_RUN" == "1" ]]; then
  RSYNC_BASE_OPTS+=("-n")
fi

log_cmd() {
  echo "- $*" >> "$REPORT_PATH"
}

run_rsync() {
  local desc="$1"
  local src="$2"
  local dst="$3"
  mkdir -p "$dst"
  echo "\n## $desc" >> "$REPORT_PATH"
  echo "Source: $src" >> "$REPORT_PATH"
  echo "Target: $dst" >> "$REPORT_PATH"
  echo "Command:" >> "$REPORT_PATH"
  echo "rsync ${RSYNC_BASE_OPTS[*]} ${EXCLUDES[*]} \"$src\" \"$dst\"" >> "$REPORT_PATH"
  rsync "${RSYNC_BASE_OPTS[@]}" "${EXCLUDES[@]}" "$src" "$dst"
}

cat << EOF_REPORT > "$REPORT_PATH"
# Migration Report

- Timestamp: $TIMESTAMP
- Source: $SOURCE_DIR
- Target: $TARGET_DIR
- Dry run: $DRY_RUN

EOF_REPORT

# Runtime-critical code and runtime assets
run_rsync "Runtime code (src)" "$SOURCE_DIR/src/" "$TARGET_DIR/runtime/src/"
run_rsync "Runtime scripts" "$SOURCE_DIR/scripts/" "$TARGET_DIR/runtime/scripts/"
run_rsync "API server" "$SOURCE_DIR/api_server.py" "$TARGET_DIR/runtime/"
run_rsync "Indexer" "$SOURCE_DIR/indexer.py" "$TARGET_DIR/runtime/"
run_rsync "UI" "$SOURCE_DIR/ui/" "$TARGET_DIR/runtime/ui/"

# Runtime inputs and filesystem-first artifacts
run_rsync "Runtime data" "$SOURCE_DIR/data/" "$TARGET_DIR/runtime/data/"
run_rsync "Runs" "$SOURCE_DIR/runs/" "$TARGET_DIR/runtime/runs/"
run_rsync "Proposals" "$SOURCE_DIR/proposals/" "$TARGET_DIR/runtime/proposals/"
run_rsync "Closures" "$SOURCE_DIR/closures/" "$TARGET_DIR/runtime/closures/"
run_rsync "Indices (derived)" "$SOURCE_DIR/indices/" "$TARGET_DIR/runtime/indices/"
run_rsync "Canonical (read-only)" "$SOURCE_DIR/canonical/" "$TARGET_DIR/runtime/canonical/"
run_rsync "Audit logs" "$SOURCE_DIR/audit/" "$TARGET_DIR/runtime/audit/"

if [[ -d "$SOURCE_DIR/promotion" ]]; then
  run_rsync "Promotion" "$SOURCE_DIR/promotion/" "$TARGET_DIR/runtime/promotion/"
else
  echo "\n## Promotion" >> "$REPORT_PATH"
  echo "TODO: promotion/ not found in source; skipping" >> "$REPORT_PATH"
fi

# Prompts (copy if present; runner does not load prompts by default)
if [[ -d "$SOURCE_DIR/prompts" ]]; then
  run_rsync "Prompts" "$SOURCE_DIR/prompts/" "$TARGET_DIR/runtime/prompts/"
  echo "TODO: runner does not currently load prompts; copied for completeness" >> "$REPORT_PATH"
else
  echo "\n## Prompts" >> "$REPORT_PATH"
  echo "TODO: prompts/ not found in source; skipping" >> "$REPORT_PATH"
fi

# Requirements / package files
for f in requirements.txt requirements-dev.txt pyproject.toml poetry.lock package.json package-lock.json pnpm-lock.yaml; do
  if [[ -f "$SOURCE_DIR/$f" ]]; then
    run_rsync "Config file: $f" "$SOURCE_DIR/$f" "$TARGET_DIR/runtime/"
  fi
done

# Documentation
run_rsync "Docs" "$SOURCE_DIR/docs/" "$TARGET_DIR/documentation/system_overview/"

# Architecture PDFs from parent
if [[ -d "$PARENT_ARCH_DOCS" ]]; then
  run_rsync "Architecture PDFs" "$PARENT_ARCH_DOCS/" "$TARGET_DIR/documentation/architecture_sources/"
else
  echo "\n## Architecture PDFs" >> "$REPORT_PATH"
  echo "TODO: Architecture docs path not found; skipping" >> "$REPORT_PATH"
fi

# Historical materials (explicitly legacy in REPO_CLASSIFICATION)
run_rsync "Legacy: sandbox/phase8_runs" "$SOURCE_DIR/sandbox/phase8_runs/" "$TARGET_DIR/historical/legacy_runs/"
run_rsync "Legacy: sandbox/phase9_runs" "$SOURCE_DIR/sandbox/phase9_runs/" "$TARGET_DIR/historical/legacy_runs/"
run_rsync "Legacy: sandbox/crew" "$SOURCE_DIR/sandbox/crew/" "$TARGET_DIR/historical/legacy_runs/"
run_rsync "Legacy: sandbox/workflows" "$SOURCE_DIR/sandbox/workflows/" "$TARGET_DIR/historical/legacy_runs/"

# Experimental / ambiguous (log only, do not copy unless explicitly requested)
if [[ -d "$SOURCE_DIR/sandbox/legacy_imports" ]]; then
  echo "\n## Ambiguous: sandbox/legacy_imports" >> "$REPORT_PATH"
  echo "TODO: legacy_imports present; classification unclear; not copied" >> "$REPORT_PATH"
fi

cat << EOF_REPORT_END >> "$REPORT_PATH"

---

## Summary

- This script is copy-only.
- Dry run default prevents changes unless DRY_RUN=0.
- Review TODOs above for ambiguous items.
EOF_REPORT_END

echo "Migration report written to: $REPORT_PATH"
