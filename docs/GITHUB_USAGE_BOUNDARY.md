# GitHub Usage Boundary

## Purpose

This document defines the explicit boundary for using GitHub within the
Mustika Rasa repository.

GitHub is adopted as a secondary coordination and tracking layer.
It is not a source of truth for runtime state, canonical data, or derived artefacts.

## Canonical Source of Truth

The following remain authoritative and filesystem-first:

- runtime/
- runtime/indices/
- runtime/audit/
- Immutable runs and closures
- Governance rules defined in AS_BUILT_ARCH.md and GOVERNANCE.md

GitHub does not replace, generate, or mutate these sources.

## What GitHub Is Used For

- Backlog tracking (Issues)
- Planning and dependency visibility
- Design discussion and decision logging
- Verification tracking
- Code review coordination (Pull Requests)

## What GitHub Is NOT Used For

- Creating or modifying runtime artefacts
- Writing to canonical or derived data
- Auto-promotion or closure
- Autonomous decision-making
- Replacing operator-triggered workflows

## Automation Boundary

GitHub automation is limited to non-mutating verification checks.
Any automation introducing new runtime behavior requires an explicit architecture decision.

## Relationship to Other Documents

This document is subordinate to:
- documentation/system_overview/AS_BUILT_ARCH.md
- documentation/system_overview/GOVERNANCE.md
- docs/REPO_FREEZE.md
- docs/REPO_MIGRATION_VERIFICATION.md

In case of conflict, filesystem-first governance takes precedence.

## Status

Formalized during GitHub adoption migration.
