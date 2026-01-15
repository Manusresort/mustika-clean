# Phase-4 Cross-Capability Structural Levers

## 1. Scope and Positioning

## Definition: What Counts as a Cross-Capability Structural Lever

A cross-capability structural lever is an analytical construct that:
- applies across two or more editorial capabilities,
- is independent of specific agents, tools, or implementations,
- introduces no executable behavior, workflow, or runtime logic,
- constrains or shapes allowable structures rather than prescribing actions,
- is necessary to enable M4-level maturity across affected capabilities.

Explicitly excluded from this document are:
- agent roles, responsibilities, or autonomy definitions,
- workflow steps, sequencing, or orchestration logic,
- validators, scripts, templates, or tooling,
- prioritization, phasing decisions, or implementation guidance.

This document is a Phase-4 analytical bridge between:
- docs/PHASE4_CAPABILITY_MATURITY_ANALYSIS.md
- the subsequent agent-gap derivation work (Phase-4.1)

It introduces no decisions, designs, or implementation plans. It only extracts cross-cutting patterns and analytical levers that appear across capabilities.

## 2. Recurrent Gap Patterns Across Capabilities

Across multiple capabilities, the following recurring patterns appear:
- lack of uniform structure for proposals and observations
- insufficient system-enforced governance of capability-specific rules
- reliance on manual editorial discipline to prevent drift
- fragmented handling of signals, risks, and escalation

## 3. Structural Levers (Analytical Hypotheses)

### 3.1 Canonical Proposal Model

Across multiple editorial capabilities, non-canonical observations, suggestions,
or findings are currently represented in heterogeneous and ad hoc ways.
This fragmentation makes cross-capability review, comparison, escalation,
and auditability inconsistent and largely dependent on manual discipline.

A canonical proposal model is identified as a cross-capability structural lever
because it provides a uniform analytical container for any non-canonical
editorial output, regardless of originating capability.

At an analytical level, such a model must make the following invariant aspects
explicit and visible:
- the epistemic status of the content (e.g. observation, hypothesis, suggestion),
- provenance and traceability (source material, run context, authorship),
- the capability context in which the proposal arises,
- the nature and location of potential impact if the proposal were acted upon,
- known risks, ambiguities, or uncertainty associated with the proposal.

The purpose of this lever is not to standardize decisions or outcomes,
but to ensure that all non-canonical content enters the system in a
structurally comparable, reviewable, and auditable form across capabilities.

This lever is pre-agent and pre-workflow: it constrains how proposals
are represented analytically, not how they are generated, evaluated,
or resolved.

### 3.2 Signal → Gate → Closure

Across multiple editorial capabilities, critical moments where
interpretation, risk, ambiguity, or potential impact arise are
handled inconsistently. Some signals lead to explicit review and
documentation, while others are implicitly resolved or silently
absorbed into downstream artefacts.

The Signal → Gate → Closure pattern is identified as a cross-capability
structural lever because it provides a uniform analytical framing for
how consequential situations are recognized, bounded, and concluded,
independent of the specific capability involved.

At an analytical level, this pattern distinguishes three conceptual
states that must be explicitly representable across capabilities:
- a signal: the recognition that something non-trivial, risky,
  ambiguous, or potentially impactful has occurred,
- a gate: the explicit acknowledgement that continuation requires
  review, judgement, or authority beyond routine handling,
- a closure: a documented outcome that explains how the signal was
  addressed, deferred, or intentionally left unresolved.

The value of this lever lies in making non-decisions visible.
Deferred judgement, unresolved ambiguity, and intentional restraint
become first-class, reviewable outcomes rather than invisible gaps.

This pattern does not prescribe who acts, how decisions are made,
or what constitutes acceptance. It only constrains that, across
capabilities, signals cannot disappear without an explicit
gate-aware closure being documented.

### 3.3 Capability-agnostic Diff & Impact Representation

Across editorial capabilities, changes, observations, or proposed
interventions often affect different aspects of the artefact:
wording, meaning, structure, cultural framing, safety interpretation,
or downstream reader perception. These impacts are currently
expressed implicitly or in capability-specific language, making
cross-capability comparison and review difficult.

A capability-agnostic approach to representing differences and
potential impact is identified as a structural lever because it
decouples the visibility of change from the domain-specific judgement
of any single capability.

At an analytical level, this lever requires that any non-canonical
content can make explicit:
- what is observed as different or at risk,
- where that difference or risk manifests in the artefact,
- which dimensions of impact are potentially involved (e.g. semantic,
  cultural, safety-related, structural),
- whether the impact is actual, hypothetical, or uncertain.

By abstracting impact representation away from capability-specific
terminology, this lever enables coherent review across disciplines
without collapsing their distinct evaluative criteria.

This lever does not define how differences are computed, displayed,
or resolved. It only constrains that meaningful differences and
their potential impacts must be representable in a shared analytical
frame across capabilities.

### 3.4 Capability-specific Risk Taxonomies

Different editorial capabilities are sensitive to fundamentally
different kinds of risk. What constitutes a serious concern for
one capability (e.g. semantic drift, cultural flattening, or
historical misrepresentation) may be irrelevant or secondary for
another.

Across the current system, risks are often described implicitly,
mixed across domains, or flattened into generic notions of
\"quality\" or \"correctness.\" This obscures the nature of the
actual concern and makes cross-capability judgement dependent on
individual interpretation rather than shared structure.

Capability-specific risk taxonomies are identified as a structural
lever because they allow risks to be named, surfaced, and compared
without forcing uniform evaluation criteria across capabilities.

At an analytical level, this lever requires that:
- each capability can articulate its own categories of risk,
  grounded in its normative editorial intent,
- risks can be expressed without immediately implying severity,
  action, or resolution,
- multiple risk perspectives can coexist for the same proposal
  or signal without being prematurely reconciled.

By separating the identification of risk from its governance
handling, this lever preserves disciplinary nuance while enabling
system-wide visibility of where and why editorial caution arises.

This lever does not prescribe taxonomies, thresholds, or responses.
It only constrains that capability-relevant risks must be expressible
in a structured, non-flattened way across the system.

### 3.5 Agents as Sensors / Proposal Producers

Across editorial capabilities, many potential issues, ambiguities,
and opportunities for contextualisation are detectable before any
human judgement or canonical decision is appropriate. In the absence
of clear structural constraints, automated or semi-automated systems
risk drifting toward implicit resolution or silent normalization.

Positioning agents analytically as sensors and proposal producers
is identified as a cross-capability structural lever because it
establishes a consistent boundary between detection and decision
across the system.

At an analytical level, this lever constrains that:
- agents may surface signals, observations, and hypotheses arising
  within or across capabilities,
- agents may articulate proposals in a structured, non-canonical form,
- agents do not resolve ambiguity, select outcomes, or confer authority.

This separation ensures that increased system support does not
translate into increased decision-making power, preserving human
editorial authority while improving visibility and coverage of
potential issues.

By treating agents uniformly as signalers rather than actors,
this lever aligns capability maturity with traceability and
governance requirements, independent of specific agent
implementations or future tooling choices.

This lever does not define agent behavior, orchestration, or
interaction patterns. It only constrains the analytical role that
agents may occupy within a capability-driven system.
The following cross-capability levers are identified as analytical hypotheses:
- a canonical proposal model for all non-canonical content
- a uniform Signal → Gate → Closure pattern
- capability-agnostic diff and impact representation
- capability-specific risk taxonomies
- agents positioned as signalers/sensors rather than decision-makers

These are not implementation plans; they are structural directions suggested by the consolidated capability gaps.

## 4. Relation to Agents (Non-Normative)

Agents may later be mapped to these levers as supporting components (signal, detection, verification, logging), but this document does not assign roles, authority, or behavior. Authority remains human and governed by existing lifecycle constraints.

## 5. What This Document Explicitly Does Not Do

- No prioritisation
- No sequencing
- No architecture or tooling decisions
- No agent definitions

## 6. Consequences for Next Phases

This analysis constrains and informs later work by:
- framing how agent-gap derivation should target structural levers rather than ad hoc fixes
- indicating where capability maturity upgrades require uniform patterns across capabilities
- clarifying that future design choices should be consistent with the cross-capability levers identified here
