"""Tests for AI integration functionality"""

import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime

from core_framework.ai_handler import AIHandler, RateLimiter
from core_framework.config import AIConfig, AIProvider, OpenRouterModel, OllamaModel, get_phase_prompt


class TestRateLimiter:
    """Test rate limiting functionality"""
    
    def test_rate_limiter_allows_requests_within_limit(self):
        """Test that rate limiter allows requests within the limit"""
        limiter = RateLimiter(max_requests=5, window_seconds=60)
        
        # Should allow first 5 requests
        for i in range(5):
            assert limiter.can_make_request()
            limiter.record_request()
        
        # Should deny 6th request
        assert not limiter.can_make_request()
    
    def test_rate_limiter_resets_after_window(self):
        """Test that rate limiter resets after time window"""
        limiter = RateLimiter(max_requests=2, window_seconds=1)
        
        # Use up the limit
        assert limiter.can_make_request()
        limiter.record_request()
        assert limiter.can_make_request()
        limiter.record_request()
        assert not limiter.can_make_request()
        
        # Wait for window to pass (simulate by clearing old requests)
        limiter.requests = []
        assert limiter.can_make_request()


class TestAIConfig:
    """Test AI configuration management"""
    
    def test_default_config_creation(self):
        """Test creating default AI configuration"""
        config = AIConfig()
        
        assert config.provider == AIProvider.DISABLED
        assert config.fallback_provider == AIProvider.DISABLED
        assert config.max_requests_per_minute == 20
        assert config.max_retries == 3
        assert config.enable_cache == True
    
    @patch.dict('os.environ', {'OPENROUTER_API_KEY': 'test-key'})
    @patch('core_framework.config.check_ollama_availability', return_value=True)
    def test_config_loading_with_env_vars(self):
        """Test loading configuration from environment variables"""
        from core_framework.config import load_config
        
        config = load_config()
        
        assert config.provider == AIProvider.OPENROUTER
        assert config.fallback_provider == AIProvider.OLLAMA
        assert config.openrouter_api_key == 'test-key'
    
    def test_phase_prompt_generation(self):
        """Test phase-specific prompt generation"""
        prompt = get_phase_prompt("clarify", "What is your project about?", "Building an app")
        
        assert "system" in prompt
        assert "user" in prompt
        assert "What is your project about?" in prompt["user"]
        assert "Building an app" in prompt["user"]
        assert "project planning consultant" in prompt["system"]


class TestAIHandler:
    """Test AI handler functionality"""
    
    @pytest.fixture
    def mock_config(self):
        """Create mock AI configuration"""
        return AIConfig(
            provider=AIProvider.OPENROUTER,
            openrouter_api_key="test-key",
            openrouter_model=OpenRouterModel.CLAUDE_HAIKU,
            max_requests_per_minute=10,
            enable_cache=True
        )
    
    @pytest.fixture
    def ai_handler(self, mock_config):
        """Create AI handler with mock configuration"""
        return AIHandler(mock_config)
    
    def test_ai_handler_initialization(self, ai_handler):
        """Test AI handler initialization"""
        assert ai_handler.config.provider == AIProvider.OPENROUTER
        assert ai_handler.rate_limiter.max_requests == 10
        assert ai_handler.cache == {}
    
    def test_cache_key_generation(self, ai_handler):
        """Test cache key generation"""
        key1 = ai_handler._get_cache_key("test prompt", "model1")
        key2 = ai_handler._get_cache_key("test prompt", "model2")
        key3 = ai_handler._get_cache_key("different prompt", "model1")
        
        assert key1 != key2  # Different models
        assert key1 != key3  # Different prompts
        assert key1 == ai_handler._get_cache_key("test prompt", "model1")  # Same inputs
    
    def test_cache_operations(self, ai_handler):
        """Test cache storage and retrieval"""
        cache_key = "test-key"
        response = "test response"
        
        # Initially no cached response
        assert ai_handler._get_cached_response(cache_key) is None
        
        # Cache response
        ai_handler._cache_response(cache_key, response)
        
        # Should retrieve cached response
        assert ai_handler._get_cached_response(cache_key) == response
    
    def test_provider_status(self, ai_handler):
        """Test provider status reporting"""
        status = ai_handler.get_provider_status()
        
        assert "primary_provider" in status
        assert "fallback_provider" in status
        assert "openrouter_configured" in status
        assert "rate_limit_remaining" in status
        assert "cache_enabled" in status
        assert "cached_responses" in status
        
        assert status["primary_provider"] == "openrouter"
        assert status["openrouter_configured"] == True
        assert status["cache_enabled"] == True
    
    @pytest.mark.asyncio
    async def test_disabled_ai_handler(self):
        """Test AI handler when disabled"""
        config = AIConfig(provider=AIProvider.DISABLED)
        handler = AIHandler(config)
        
        success, response, conversation = await handler.get_ai_guidance(
            "clarify", "Test question", "Test answer"
        )
        
        assert not success
        assert "not configured" in response
        assert conversation is None
    
    @pytest.mark.asyncio
    async def test_rate_limit_exceeded(self, ai_handler):
        """Test behavior when rate limit is exceeded"""
        # Exhaust rate limit
        for _ in range(ai_handler.config.max_requests_per_minute):
            ai_handler.rate_limiter.record_request()
        
        success, response, conversation = await ai_handler.get_ai_guidance(
            "clarify", "Test question", "Test answer"
        )
        
        assert not success
        assert "Rate limit exceeded" in response
        assert conversation is None
    
    @pytest.mark.asyncio
    @patch('aiohttp.ClientSession.post')
    async def test_openrouter_api_call_success(self, mock_post, ai_handler):
        """Test successful OpenRouter API call"""
        # Mock successful API response
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "AI guidance response"}}]
        }
        mock_post.return_value.__aenter__.return_value = mock_response
        
        async with ai_handler:
            success, response = await ai_handler._call_openrouter({
                "system": "Test system prompt",
                "user": "Test user prompt"
            })
        
        assert success
        assert response == "AI guidance response"
    
    @pytest.mark.asyncio
    @patch('aiohttp.ClientSession.post')
    async def test_openrouter_api_call_failure(self, mock_post, ai_handler):
        """Test failed OpenRouter API call"""
        # Mock failed API response
        mock_response = AsyncMock()
        mock_response.status = 401
        mock_response.text.return_value = "Unauthorized"
        mock_post.return_value.__aenter__.return_value = mock_response
        
        async with ai_handler:
            success, response = await ai_handler._call_openrouter({
                "system": "Test system prompt",
                "user": "Test user prompt"
            })
        
        assert not success
        assert "OpenRouter API error (401)" in response
    
    @pytest.mark.asyncio
    @patch('aiohttp.ClientSession.post')
    async def test_ollama_api_call_success(self, mock_post):
        """Test successful Ollama API call"""
        config = AIConfig(
            provider=AIProvider.OLLAMA,
            ollama_model=OllamaModel.LLAMA3
        )
        handler = AIHandler(config)
        
        # Mock successful API response
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = {"response": "Ollama guidance response"}
        mock_post.return_value.__aenter__.return_value = mock_response
        
        async with handler:
            success, response = await handler._call_ollama({
                "system": "Test system prompt",
                "user": "Test user prompt"
            })
        
        assert success
        assert response == "Ollama guidance response"
    
    @pytest.mark.asyncio
    @patch('aiohttp.ClientSession.post')
    async def test_ollama_connection_error(self, mock_post):
        """Test Ollama connection error"""
        config = AIConfig(provider=AIProvider.OLLAMA)
        handler = AIHandler(config)
        
        # Mock connection error
        from aiohttp import ClientConnectorError
        mock_post.side_effect = ClientConnectorError(None, OSError("Connection refused"))
        
        async with handler:
            success, response = await handler._call_ollama({
                "system": "Test system prompt", 
                "user": "Test user prompt"
            })
        
        assert not success
        assert "Cannot connect to Ollama" in response
    
    @pytest.mark.asyncio
    async def test_get_ai_guidance_with_cache(self, ai_handler):
        """Test AI guidance with caching"""
        # Pre-populate cache
        cache_key = ai_handler._get_cache_key("Test user prompt", str(ai_handler.config.provider))
        ai_handler._cache_response(cache_key, "Cached response")
        
        success, response, conversation = await ai_handler.get_ai_guidance(
            "clarify", "Test question", "Test answer"
        )
        
        assert success
        assert response == "Cached response"
        assert conversation is None  # No conversation created for cached responses
    
    @pytest.mark.asyncio
    @patch('aiohttp.ClientSession.post')
    async def test_fallback_provider(self, mock_post):
        """Test fallback to secondary provider"""
        config = AIConfig(
            provider=AIProvider.OPENROUTER,
            fallback_provider=AIProvider.OLLAMA,
            openrouter_api_key="test-key"
        )
        handler = AIHandler(config)
        
        # Mock OpenRouter failure, then Ollama success
        responses = [
            # OpenRouter failure
            AsyncMock(status=500, text=AsyncMock(return_value="Server error")),
            # Ollama success
            AsyncMock(status=200, json=AsyncMock(return_value={"response": "Fallback response"}))
        ]
        
        mock_post.return_value.__aenter__.side_effect = responses
        
        async with handler:
            success, response, conversation = await handler.get_ai_guidance(
                "clarify", "Test question", "Test answer"
            )
        
        assert success
        assert response == "Fallback response"
        assert conversation is not None
        assert conversation.messages[1].model == "ollama"  # Used fallback provider


class TestIntegration:
    """Integration tests for AI functionality"""
    
    @pytest.mark.asyncio
    async def test_complete_ai_workflow(self):
        """Test complete AI guidance workflow"""
        config = AIConfig(
            provider=AIProvider.DISABLED,  # Start disabled
            enable_cache=True
        )
        
        async with AIHandler(config) as handler:
            # Test disabled state
            success, response, conversation = await handler.get_ai_guidance(
                "clarify", "What is your project?", ""
            )
            
            assert not success
            assert "not configured" in response
            
            # Test status reporting
            status = handler.get_provider_status()
            assert status["primary_provider"] == "disabled"
            assert status["openrouter_configured"] == False
    
    def test_phase_prompt_consistency(self):
        """Test that phase prompts are consistent and complete"""
        from core_framework.config import PHASE_PROMPTS
        
        required_phases = ["clarify", "organize", "refine", "equip"]
        
        for phase in required_phases:
            assert phase in PHASE_PROMPTS
            assert "system" in PHASE_PROMPTS[phase]
            assert "guidance" in PHASE_PROMPTS[phase]
            assert len(PHASE_PROMPTS[phase]["system"]) > 50  # Substantial system prompt
            assert len(PHASE_PROMPTS[phase]["guidance"]) > 20  # Meaningful guidance


if __name__ == "__main__":
    pytest.main([__file__])
