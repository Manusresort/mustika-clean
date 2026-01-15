# Project Meta Registry (Facts Only)

Scope: scanned paths under `runtime/data/`, `documentation/system_overview/`,
`documentation/legacy_imports/`. Only files actually found are listed.

| artefact_id | type | origin | source_path | scope | notes | conflicts |
|---|---|---|---|---|---|---|
| README_SOURCE_IMPORT.md | PROJECT_META | CLEAN_REPO_STAGED | `runtime/data/source_imports/legacy_mr2026_alignment_spine/README_SOURCE_IMPORT.md` | batch | Alignment spine batch provenance. | none observed |
| README_SOURCE_IMPORT.md | PROJECT_META | CLEAN_REPO_STAGED | `runtime/data/source_imports/legacy_agentic_inputs/README_SOURCE_IMPORT.md` | batch | Agentic inputs batch provenance. | none observed |
| README_SOURCE_IMPORT.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/README_SOURCE_IMPORT.md` | batch | Project meta batch provenance. | none observed |
| CHECKSUMS.txt | PROJECT_META | CLEAN_REPO_STAGED | `runtime/data/source_imports/legacy_mr2026_alignment_spine/CHECKSUMS.txt` | batch | Checksums for alignment spine. | none observed |
| CHECKSUMS.txt | PROJECT_META | CLEAN_REPO_STAGED | `runtime/data/source_imports/legacy_agentic_inputs/CHECKSUMS.txt` | batch | Checksums for agentic inputs. | none observed |
| CHECKSUMS.txt | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/CHECKSUMS.txt` | batch | Checksums for project meta import. | none observed |
| SOURCE_OF_TRUTH.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/SOURCE_OF_TRUTH.md` | legacy-root | Canonical sources and derived layers defined. | CONFLICT: raw sources presence vs DECISIONS note |
| STEP3_BRONTEXT_STATUS.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/STEP3_BRONTEXT_STATUS.md` | legacy-root | OCR/canon status notes. | none observed |
| STATUS.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/STATUS.md` | legacy-root | Status tracking. | none observed |
| DECISIONS.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/DECISIONS.md` | legacy-root | Notes: raw sources not included. | CONFLICT with staged raw sources |
| MIGRATION_REPORT.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/MIGRATION_REPORT.md` | legacy-root | Migration notes. | none observed |
| readme_mustika_rasa_project.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/readme_mustika_rasa_project.md` | legacy-root | Project overview & staged plan. | none observed |
| SCAN_SIGNALS (collection) | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/SCAN_SIGNALS/` | legacy-root | Signals logs + summaries. | none observed |
| MANIFESTS/filelist_maxdepth3.txt | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/MANIFESTS/filelist_maxdepth3.txt` | legacy-root | Legacy manifest listing. | none observed |
| PROMPTS/prompt_current.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/PROMPTS/prompt_current.md` | legacy-root | Legacy prompt snapshot. | none observed |
| HANDOVERS/2025-12-24_1049_session_handover.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/HANDOVERS/2025-12-24_1049_session_handover.md` | legacy-root | Legacy handover memo. | none observed |
| KERNEL/SOURCE_OF_TRUTH.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/KERNEL/SOURCE_OF_TRUTH.md` | legacy-root | Kernel source-of-truth. | none observed |
| KERNEL/DECISIONS.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/KERNEL/DECISIONS.md` | legacy-root | Kernel decisions. | none observed |
| KERNEL/STATUS.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/KERNEL/STATUS.md` | legacy-root | Kernel status. | none observed |
| KERNEL/PLAN_MASTER.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/KERNEL/PLAN_MASTER.md` | legacy-root | Master plan. | none observed |
| KERNEL/BRON_LACUNES.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/KERNEL/BRON_LACUNES.md` | legacy-root | Source gaps. | none observed |
| KERNEL/BRON_DOCUMENT_RELEASE.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/KERNEL/BRON_DOCUMENT_RELEASE.md` | legacy-root | Release notes. | none observed |
| KERNEL/STEP3B_CLOSURE.md | PROJECT_META | CLEAN_REPO_STAGED | `documentation/legacy_imports/legacy_mr2026_project_meta/project_meta/KERNEL/STEP3B_CLOSURE.md` | legacy-root | Step3b closure. | none observed |
| README.md | PROJECT_META | CLEAN_REPO | `documentation/system_overview/handovers/handover_woensdagavond/README.md` | legacy bundle | Handover README. | none observed |
| README.md | PROJECT_META | CLEAN_REPO | `documentation/system_overview/handovers/handover_woensdagavond/addendum_handover/README.md` | legacy bundle | Handover addendum README. | none observed |
| P6_PHASE_STATUS_SNAPSHOT.md | PROJECT_META | CLEAN_REPO | `documentation/system_overview/P6_PHASE_STATUS_SNAPSHOT.md` | global | Status snapshot (documentation). | none observed |
| P6_PHASE_STATUS_SUMMARY.md | PROJECT_META | CLEAN_REPO | `documentation/system_overview/P6_PHASE_STATUS_SUMMARY.md` | global | Status summary (documentation). | none observed |
| README_QUICKSTART.md | PROJECT_META | CLEAN_REPO | `documentation/system_overview/implementation/README_QUICKSTART.md` | implementation | Quickstart documentation. | none observed |

Notes:
- All legacy meta files are staged under documentation/legacy_imports.
