"""AI Handler for OpenRouter and Ollama integration"""

import asyncio
import json
import time
from typing import Optional, Dict, Any, List, Tuple
from datetime import datetime, timedelta
import aiohttp
from dataclasses import dataclass

from .config import AIConfig, AIProvider, load_config, get_phase_prompt
from .models import AIConversation, AIMessage


@dataclass
class RateLimiter:
    """Simple rate limiter for API calls"""
    max_requests: int
    window_seconds: int = 60
    requests: List[float] = None
    
    def __post_init__(self):
        if self.requests is None:
            self.requests = []
    
    def can_make_request(self) -> bool:
        """Check if we can make a request within rate limits"""
        now = time.time()
        # Remove requests older than window
        self.requests = [req_time for req_time in self.requests if now - req_time < self.window_seconds]
        return len(self.requests) < self.max_requests
    
    def record_request(self):
        """Record a new request"""
        self.requests.append(time.time())


class AIHandler:
    """Handles AI integration for both OpenRouter and Ollama"""
    
    def __init__(self, config: Optional[AIConfig] = None):
        self.config = config or load_config()
        self.rate_limiter = RateLimiter(self.config.max_requests_per_minute)
        self.session: Optional[aiohttp.ClientSession] = None
        self.cache: Dict[str, Tuple[str, datetime]] = {}
    
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.config.timeout)
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    def _get_cache_key(self, prompt: str, model: str) -> str:
        """Generate cache key for prompt and model"""
        return f"{model}:{hash(prompt)}"
    
    def _get_cached_response(self, cache_key: str) -> Optional[str]:
        """Get cached response if still valid"""
        if not self.config.enable_cache:
            return None
        
        if cache_key in self.cache:
            response, timestamp = self.cache[cache_key]
            if datetime.now() - timestamp < timedelta(seconds=self.config.cache_ttl):
                return response
            else:
                del self.cache[cache_key]
        
        return None
    
    def _cache_response(self, cache_key: str, response: str):
        """Cache a response"""
        if self.config.enable_cache:
            self.cache[cache_key] = (response, datetime.now())
    
    async def get_ai_guidance(
        self, 
        phase: str, 
        question_text: str, 
        current_answer: str = "",
        conversation_id: Optional[str] = None
    ) -> Tuple[bool, str, Optional[AIConversation]]:
        """
        Get AI guidance for a specific question
        
        Returns:
            (success, response_text, conversation)
        """
        
        if self.config.provider == AIProvider.DISABLED:
            return False, "AI assistance is not configured. Set OPENROUTER_API_KEY or ensure Ollama is running.", None
        
        # Check rate limits
        if not self.rate_limiter.can_make_request():
            return False, "Rate limit exceeded. Please wait before making another request.", None
        
        # Generate prompt
        prompt_data = get_phase_prompt(phase, question_text, current_answer)
        
        # Check cache
        cache_key = self._get_cache_key(prompt_data["user"], str(self.config.provider))
        cached_response = self._get_cached_response(cache_key)
        if cached_response:
            return True, cached_response, None
        
        # Try primary provider
        success, response = await self._make_ai_request(prompt_data)
        
        # Try fallback provider if primary fails
        if not success and self.config.fallback_provider != AIProvider.DISABLED:
            original_provider = self.config.provider
            self.config.provider = self.config.fallback_provider
            success, response = await self._make_ai_request(prompt_data)
            self.config.provider = original_provider
        
        if success:
            self.rate_limiter.record_request()
            self._cache_response(cache_key, response)
            
            # Create conversation record
            conversation = AIConversation(
                id=conversation_id or f"ai_{int(time.time())}",
                phase=phase,
                messages=[
                    AIMessage(
                        role="user",
                        content=prompt_data["user"],
                        timestamp=datetime.now()
                    ),
                    AIMessage(
                        role="assistant", 
                        content=response,
                        timestamp=datetime.now(),
                        model=str(self.config.provider)
                    )
                ],
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            return True, response, conversation
        
        return False, response, None
    
    async def _make_ai_request(self, prompt_data: Dict[str, str]) -> Tuple[bool, str]:
        """Make AI request to configured provider"""
        
        for attempt in range(self.config.max_retries):
            try:
                if self.config.provider == AIProvider.OPENROUTER:
                    return await self._call_openrouter(prompt_data)
                elif self.config.provider == AIProvider.OLLAMA:
                    return await self._call_ollama(prompt_data)
                else:
                    return False, "No AI provider configured"
                    
            except Exception as e:
                if attempt == self.config.max_retries - 1:
                    return False, f"AI request failed after {self.config.max_retries} attempts: {str(e)}"
                
                # Exponential backoff
                await asyncio.sleep(self.config.retry_delay * (2 ** attempt))
        
        return False, "Maximum retries exceeded"
    
    async def _call_openrouter(self, prompt_data: Dict[str, str]) -> Tuple[bool, str]:
        """Call OpenRouter API"""
        
        if not self.config.openrouter_api_key:
            return False, "OpenRouter API key not configured"
        
        headers = {
            "Authorization": f"Bearer {self.config.openrouter_api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/core-framework/core-framework",
            "X-Title": "CORE Framework"
        }
        
        payload = {
            "model": self.config.openrouter_model.value,
            "messages": [
                {"role": "system", "content": prompt_data["system"]},
                {"role": "user", "content": prompt_data["user"]}
            ],
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature
        }
        
        url = f"{self.config.openrouter_base_url}/chat/completions"
        
        async with self.session.post(url, headers=headers, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                content = data["choices"][0]["message"]["content"]
                return True, content.strip()
            else:
                error_text = await response.text()
                return False, f"OpenRouter API error ({response.status}): {error_text}"
    
    async def _call_ollama(self, prompt_data: Dict[str, str]) -> Tuple[bool, str]:
        """Call Ollama local API"""
        
        # Combine system and user prompts for Ollama
        combined_prompt = f"{prompt_data['system']}\n\nUser: {prompt_data['user']}\n\nAssistant:"
        
        payload = {
            "model": self.config.ollama_model.value,
            "prompt": combined_prompt,
            "stream": False,
            "options": {
                "temperature": self.config.temperature,
                "num_predict": self.config.max_tokens
            }
        }
        
        url = f"{self.config.ollama_base_url}/api/generate"
        
        try:
            async with self.session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return True, data["response"].strip()
                else:
                    error_text = await response.text()
                    return False, f"Ollama API error ({response.status}): {error_text}"
        except aiohttp.ClientConnectorError:
            return False, "Cannot connect to Ollama. Make sure Ollama is running on localhost:11434"
    
    async def list_available_models(self) -> Tuple[bool, List[str]]:
        """List available models for the current provider"""
        
        if self.config.provider == AIProvider.OPENROUTER:
            # For OpenRouter, return predefined models
            from .config import OpenRouterModel
            return True, [model.value for model in OpenRouterModel]
        
        elif self.config.provider == AIProvider.OLLAMA:
            try:
                url = f"{self.config.ollama_base_url}/api/tags"
                async with self.session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        models = [model["name"] for model in data.get("models", [])]
                        return True, models
                    else:
                        return False, []
            except:
                return False, []
        
        return False, []
    
    def get_provider_status(self) -> Dict[str, Any]:
        """Get status information about AI providers"""
        
        return {
            "primary_provider": self.config.provider.value,
            "fallback_provider": self.config.fallback_provider.value,
            "openrouter_configured": bool(self.config.openrouter_api_key),
            "ollama_available": self.config.provider == AIProvider.OLLAMA or self.config.fallback_provider == AIProvider.OLLAMA,
            "rate_limit_remaining": self.config.max_requests_per_minute - len(self.rate_limiter.requests),
            "cache_enabled": self.config.enable_cache,
            "cached_responses": len(self.cache)
        }
