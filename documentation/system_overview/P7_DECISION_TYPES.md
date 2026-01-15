# Phase-7 — Decision Types Matrix

## Purpose
This document classifies the different kinds of editorial decisions in Mustikarasa
and assigns each one to the correct decision lane:

- AGENT_AUTONOMOUS (low-risk, reversible, traceable)
- AGENT_PROVISIONAL → HUMAN REVIEW
- HUMAN ONLY (canonical judgment, interpretive, or cultural meaning)

This matrix does not make decisions.  
It only defines **who is allowed to decide, and when escalation is required**.

## Matrix (Draft — Phase-7 Work in Progress)

| DECISION TYPE | DESCRIPTION | DECISION LANE | ESCALATION RULE | NOTES |
|---------------|-------------|---------------|-----------------|-------|
| typographic | visual & spacing conventions | AGENT_AUTONOMOUS | escalate if it changes meaning or reader interpretation | |
| OCR-correction | fix obvious OCR noise | AGENT_AUTONOMOUS | escalate if correction is uncertain or affects meaning | |
| text-critical | which variant is chosen | AGENT_PROVISIONAL → HUMAN REVIEW | escalate whenever variant choice changes wording or structure | |
| glossary meaning | what a term *means* | HUMAN ONLY | always escalate — meaning is interpretive | |
| contextual / historical note | explanation for reader | HUMAN ONLY | always escalate — cultural/historical framing | |
| structural normalisation | headings, ordering, grouping | AGENT_PROVISIONAL → HUMAN REVIEW | escalate if it affects narrative flow or hierarchy | |

> Rule of thumb: if reader understanding, cultural meaning,
> or historical interpretation may change — agents must escalate.

At the end of Phase-7 this table must be complete and stable.
