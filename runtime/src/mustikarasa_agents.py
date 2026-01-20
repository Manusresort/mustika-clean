"""
Minimal CrewAI agent definitions for the RunnerV2 translation pipeline.
"""

from __future__ import annotations

import os

from crewai import Agent, LLM


def _build_llm() -> LLM:
    model = os.getenv("LITELLM_MODEL") or os.getenv("OPENAI_MODEL")
    if not model:
        raise RuntimeError(
            "Missing model configuration: set LITELLM_MODEL or OPENAI_MODEL."
        )

    kwargs = {}
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        kwargs["api_key"] = api_key
    base_url = os.getenv("LITELLM_BASE_URL") or os.getenv("OPENAI_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url

    return LLM(model=model, **kwargs)


_LLM = _build_llm()

translation_quality_agent = Agent(
    role="Translation Quality Agent",
    goal="Improve rough Dutch translations while preserving meaning.",
    backstory="A careful editor focused on fidelity and grammar.",
    llm=_LLM,
    verbose=False,
)

readability_editor = Agent(
    role="Readability Editor",
    goal="Polish Dutch text for clarity and natural flow.",
    backstory="A stylist who improves readability without changing meaning.",
    llm=_LLM,
    verbose=False,
)

fidelity_agent = Agent(
    role="Fidelity Agent",
    goal="Ensure the Dutch output remains faithful to the English source.",
    backstory="A final checker who flags meaning drift and ambiguity.",
    llm=_LLM,
    verbose=False,
)
