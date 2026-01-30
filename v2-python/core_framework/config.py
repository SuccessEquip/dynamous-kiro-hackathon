"""Configuration management for CORE Framework AI integration"""

import os
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from enum import Enum


class AIProvider(str, Enum):
    OPENROUTER = "openrouter"
    OLLAMA = "ollama"
    DISABLED = "disabled"


class OpenRouterModel(str, Enum):
    CLAUDE_SONNET = "anthropic/claude-3.5-sonnet"
    CLAUDE_HAIKU = "anthropic/claude-3-haiku"
    GPT4_TURBO = "openai/gpt-4-turbo"
    GPT4O = "openai/gpt-4o"
    LLAMA_70B = "meta-llama/llama-3.1-70b-instruct"


class OllamaModel(str, Enum):
    LLAMA3 = "llama3"
    MISTRAL = "mistral"
    CODELLAMA = "codellama"
    GEMMA = "gemma"


class AIConfig(BaseModel):
    """AI configuration settings"""
    
    # Provider settings
    provider: AIProvider = AIProvider.DISABLED
    fallback_provider: AIProvider = AIProvider.DISABLED
    
    # OpenRouter settings
    openrouter_api_key: Optional[str] = None
    openrouter_model: OpenRouterModel = OpenRouterModel.CLAUDE_HAIKU
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    
    # Ollama settings
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: OllamaModel = OllamaModel.LLAMA3
    
    # Rate limiting
    max_requests_per_minute: int = 20
    max_retries: int = 3
    retry_delay: float = 1.0
    
    # Response settings
    max_tokens: int = 1000
    temperature: float = 0.7
    timeout: float = 30.0
    
    # Caching
    enable_cache: bool = True
    cache_ttl: int = 3600  # 1 hour


def load_config() -> AIConfig:
    """Load AI configuration from environment variables"""
    
    # Determine provider based on available configuration
    provider = AIProvider.DISABLED
    fallback_provider = AIProvider.DISABLED
    
    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    ollama_available = check_ollama_availability()
    
    if openrouter_key:
        provider = AIProvider.OPENROUTER
        if ollama_available:
            fallback_provider = AIProvider.OLLAMA
    elif ollama_available:
        provider = AIProvider.OLLAMA
    
    return AIConfig(
        provider=provider,
        fallback_provider=fallback_provider,
        openrouter_api_key=openrouter_key,
        openrouter_model=OpenRouterModel(
            os.getenv("OPENROUTER_MODEL", OpenRouterModel.CLAUDE_HAIKU.value)
        ),
        ollama_model=OllamaModel(
            os.getenv("OLLAMA_MODEL", OllamaModel.LLAMA3.value)
        ),
        ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        max_requests_per_minute=int(os.getenv("AI_MAX_REQUESTS_PER_MINUTE", "20")),
        max_retries=int(os.getenv("AI_MAX_RETRIES", "3")),
        timeout=float(os.getenv("AI_TIMEOUT", "30.0")),
        temperature=float(os.getenv("AI_TEMPERATURE", "0.7")),
    )


def check_ollama_availability() -> bool:
    """Check if Ollama is available locally"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        return response.status_code == 200
    except:
        return False


# Phase-specific AI prompts
PHASE_PROMPTS = {
    "clarify": {
        "system": "You are an expert project planning consultant helping users clarify their project vision. Ask probing questions to help them think deeper about their project's purpose, users, and scope. Be encouraging but challenge vague statements.",
        "guidance": "Help me think deeper about this question. Ask follow-up questions to help me be more specific and comprehensive in my answer."
    },
    "organize": {
        "system": "You are an expert product manager helping users organize their project requirements. Focus on prioritization, feature definition, and user needs. Help them distinguish between must-haves and nice-to-haves.",
        "guidance": "Help me organize and prioritize my thoughts on this question. Challenge me to be more specific about priorities and trade-offs."
    },
    "refine": {
        "system": "You are an expert risk analyst and project consultant helping users identify and plan for potential challenges. Focus on realistic assessment of risks, constraints, and validation strategies.",
        "guidance": "Help me think critically about potential risks and challenges. Ask probing questions about what could go wrong and how to validate assumptions."
    },
    "equip": {
        "system": "You are an expert technical architect helping users create implementation plans. Focus on practical next steps, technical decisions, and actionable recommendations.",
        "guidance": "Help me create a practical implementation plan based on my project analysis. Focus on specific, actionable next steps."
    }
}


def get_phase_prompt(phase: str, question_text: str, current_answer: str = "") -> Dict[str, str]:
    """Get AI prompt for a specific phase and question"""
    
    phase_config = PHASE_PROMPTS.get(phase, PHASE_PROMPTS["clarify"])
    
    user_prompt = f"""
Question: {question_text}

Current answer: {current_answer if current_answer else "Not answered yet"}

{phase_config["guidance"]}

Please provide specific follow-up questions or suggestions to help me improve my answer. Keep your response concise and actionable.
"""
    
    return {
        "system": phase_config["system"],
        "user": user_prompt.strip()
    }
