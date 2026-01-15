# Governance Classification: GOV-A, GOV-B, and BRIDGE

## 1. Purpose

This document defines how governance-related artefacts are classified in this repository.
It governs interpretation and structuring of the repository, not runtime enforcement.

## 2. GOV-A — Project Governance

GOV-A is governance over designing, building, and managing the system.
It covers design-time decisions, human authority, and non-runtime direction.
Typical artefacts include vision, strategy, TODO, workflow, and session logs.

## 3. GOV-B — System Governance

GOV-B is governance enforced by the system at runtime.
It relies on validators, gates, contracts, PASS/FAIL logic, and enforcement.
Typical artefacts include output contracts, validators, gates, and run artefacts.

## 4. BRIDGE — Governance Bridge Layer

BRIDGE is the set of design and policy documents that connect GOV-A intent
with GOV-B enforcement. BRIDGE documents are not themselves enforceable.
Typical artefacts include human gate policies, agent autonomy envelopes,
and governance integration designs.

## 5. Classification Decision Rule

a) If enforced at runtime → GOV-B
b) If governing project decisions → GOV-A
c) If human policy + reference to enforcement → BRIDGE

Ambiguity defaults to BRIDGE.

## 6. Normative Rules

- Each document has one primary governance label.
- BRIDGE is an explicit, allowed category.
- Classification precedes any refactoring or restructuring.
- GOV_LABEL_AUDIT.md is observational; this document is normative.
