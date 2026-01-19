"""
LLM Client Interface - Model-agnostic LLM wrapper
"""

from abc import ABC, abstractmethod
from typing import Optional
from pathlib import Path
import json


class LLMClient(ABC):
    """Abstract base class for LLM clients."""
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text from prompt."""
        pass


class OllamaMistralClient(LLMClient):
    """Ollama/Mistral client using CrewAI."""
    
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "ollama/mistral", temperature: float = 0.3):
        try:
            from crewai import LLM
            self.llm = LLM(
                model=model,
                base_url=base_url,
                temperature=temperature,
            )
        except ImportError:
            raise ImportError("CrewAI not installed. Install with: pip install crewai")
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate using CrewAI LLM."""
        # CrewAI LLM doesn't have a direct generate method in this version
        # This is a placeholder - actual implementation depends on CrewAI API
        # For now, we'll use the agents directly via mustikarasa_agents
        raise NotImplementedError("Use agents via mustikarasa_agents instead")


def create_llm_client(config_path: Optional[Path] = None) -> LLMClient:
    """
    Create LLM client from config file or defaults.
    
    Config file format (JSON):
    {
        "type": "ollama_mistral",
        "base_url": "http://localhost:11434",
        "model": "ollama/mistral",
        "temperature": 0.3
    }
    """
    if config_path and config_path.exists():
        config = json.loads(config_path.read_text(encoding="utf-8"))
        client_type = config.get("type", "ollama_mistral")
        
        if client_type == "ollama_mistral":
            return OllamaMistralClient(
                base_url=config.get("base_url", "http://localhost:11434"),
                model=config.get("model", "ollama/mistral"),
                temperature=config.get("temperature", 0.3),
            )
        else:
            raise ValueError(f"Unknown LLM client type: {client_type}")
    
    # Default: Ollama/Mistral
    return OllamaMistralClient()
