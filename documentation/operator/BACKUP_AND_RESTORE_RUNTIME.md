# Backup and Restore Workflow (Runtime)

## Purpose

Provide a copy-only backup and restore workflow for runtime artefacts referenced in the operator runbook.

## What is considered immutable

- runtime/runs/
- runtime/proposals/
- runtime/closures/

## Backup procedure (copy-only, step-by-step)

1) Choose a backup location outside the repo.
2) Copy these directories in full, preserving structure and contents:
   - runtime/runs/
   - runtime/proposals/
   - runtime/closures/
   - runtime/audit/
3) If you require an exact filesystem snapshot for debugging, also copy:
   - runtime/indices/

## Restore procedure (step-by-step)

1) Stop any processes that might write to runtime.
2) Copy the backed-up directories back to their original locations:
   - runtime/runs/
   - runtime/proposals/
   - runtime/closures/
   - runtime/audit/
3) If you backed up runtime/indices/, copy it back as well.

## Safety notes

- This is copy-only; do not modify contents during backup or restore.
- Restore overwrites existing files; ensure you want to replace current runtime data.
- This workflow does not write to runtime/canonical/.

## What this does NOT cover

- No index rebuilds.
- No partial restores.
- No conflict resolution.
