"""Tests for CORE Framework Python TUI"""

import pytest
import json
from datetime import datetime
from unittest.mock import patch, mock_open

from core_framework.models import (
    SessionData, SessionMetadata, Answer, Question, PhaseType,
    ImplementationType, SessionStatus, QUESTIONS_BY_ID, QUESTIONS_BY_PHASE
)
from core_framework.output_generator import OutputGenerator


class TestModels:
    """Test Pydantic models and data validation"""
    
    def test_session_metadata_creation(self):
        """Test creating session metadata"""
        session = SessionMetadata(
            id="12345678-1234-4123-8123-123456789012",
            name="Test Project",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            version="1.0.0",
            implementation=ImplementationType.V2_PYTHON
        )
        
        assert session.name == "Test Project"
        assert session.implementation == ImplementationType.V2_PYTHON
        assert session.status == SessionStatus.DRAFT  # default value
    
    def test_answer_validation(self):
        """Test answer model validation"""
        answer = Answer(
            question_id="C-01",
            response="This is a test response",
            answered_at=datetime.now(),
            confidence=4
        )
        
        assert answer.question_id == "C-01"
        assert answer.confidence == 4
        
        # Test invalid question ID pattern
        with pytest.raises(ValueError):
            Answer(
                question_id="INVALID",
                response="Test",
                answered_at=datetime.now()
            )
    
    def test_questions_structure(self):
        """Test question definitions and structure"""
        # Test that all expected questions exist
        expected_questions = [
            "C-01", "C-02", "C-03", "C-04", "C-05",
            "O-01", "O-02", "O-03", "O-04", "O-05", 
            "R-01", "R-02", "R-03", "R-04", "R-05"
        ]
        
        for question_id in expected_questions:
            assert question_id in QUESTIONS_BY_ID
            question = QUESTIONS_BY_ID[question_id]
            assert question.text
            assert question.guidance
            assert question.ai_prompt
            assert question.min_length > 0
            assert question.max_length > question.min_length
    
    def test_questions_by_phase(self):
        """Test questions are properly organized by phase"""
        assert len(QUESTIONS_BY_PHASE[PhaseType.CLARIFY]) == 5
        assert len(QUESTIONS_BY_PHASE[PhaseType.ORGANIZE]) == 5
        assert len(QUESTIONS_BY_PHASE[PhaseType.REFINE]) == 5
        
        # Test phase assignment
        for question in QUESTIONS_BY_PHASE[PhaseType.CLARIFY]:
            assert question.id.startswith("C-")
            assert question.phase == PhaseType.CLARIFY


class TestOutputGenerator:
    """Test output generation functionality"""
    
    @pytest.fixture
    def sample_session_data(self):
        """Create sample session data for testing"""
        session_data = SessionData(
            session=SessionMetadata(
                id="12345678-1234-4123-8123-123456789012",
                name="Test Project",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                version="1.0.0",
                implementation=ImplementationType.V2_PYTHON
            )
        )
        
        # Add some sample answers
        session_data.answers = [
            Answer(
                question_id="C-01",
                response="This project solves the problem of inefficient project planning for developers.",
                answered_at=datetime.now(),
                confidence=4
            ),
            Answer(
                question_id="C-02", 
                response="Success looks like developers completing projects 50% faster with better outcomes.",
                answered_at=datetime.now(),
                confidence=5
            ),
            Answer(
                question_id="O-01",
                response="Essential features include: 1) Interactive planning wizard, 2) Multi-format output, 3) Session persistence, 4) Progress tracking, 5) Validation system.",
                answered_at=datetime.now(),
                confidence=4
            )
        ]
        
        return session_data
    
    def test_markdown_generation(self, sample_session_data):
        """Test Markdown output generation"""
        generator = OutputGenerator(sample_session_data)
        markdown = generator.generate_markdown()
        
        assert "# Test Project - CORE Framework Analysis" in markdown
        assert "## Executive Summary" in markdown
        assert "This project solves the problem of inefficient project planning" in markdown
        assert "Success looks like developers completing projects 50% faster" in markdown
        assert "## Phase 1: Clarify" in markdown
        assert "## Phase 2: Organize" in markdown
        assert "## Next Steps" in markdown
        assert "*Generated by CORE Framework v1.0.0 - Python TUI Implementation*" in markdown
    
    def test_json_generation(self, sample_session_data):
        """Test JSON output generation"""
        generator = OutputGenerator(sample_session_data)
        json_output = generator.generate_json()
        
        # Parse JSON to verify it's valid
        data = json.loads(json_output)
        
        assert data["session"]["name"] == "Test Project"
        assert data["session"]["implementation"] == "v2-python"
        assert len(data["answers"]) == 3
        assert data["answers"][0]["question_id"] == "C-01"
    
    def test_ai_prompt_generation(self, sample_session_data):
        """Test AI prompt generation"""
        generator = OutputGenerator(sample_session_data)
        ai_prompt = generator.generate_ai_prompt()
        
        assert "Based on the following CORE Framework analysis" in ai_prompt
        assert "## Project Context" in ai_prompt
        assert "**Project**: Test Project" in ai_prompt
        assert "**Core Problem**: This project solves the problem of inefficient project planning" in ai_prompt
        assert "## Requirements Analysis" in ai_prompt
        assert "### 1. Technical Architecture" in ai_prompt
        assert "### 2. Implementation Plan" in ai_prompt
        assert "### 3. Development Guidelines" in ai_prompt
        assert "### 4. Success Metrics & Validation" in ai_prompt
    
    def test_all_formats_generation(self, sample_session_data):
        """Test combined format generation"""
        generator = OutputGenerator(sample_session_data)
        all_formats = generator.generate_all_formats()
        
        assert "CORE Framework - Complete Documentation Package" in all_formats
        assert "FILE: markdown.txt" in all_formats
        assert "FILE: json.txt" in all_formats
        assert "FILE: ai_prompt.txt" in all_formats
        assert "Generated:" in all_formats
    
    def test_get_answer_method(self, sample_session_data):
        """Test getting specific answers"""
        generator = OutputGenerator(sample_session_data)
        
        answer = generator.get_answer("C-01")
        assert answer == "This project solves the problem of inefficient project planning for developers."
        
        # Test non-existent answer
        empty_answer = generator.get_answer("R-05")
        assert empty_answer == ""


class TestSessionData:
    """Test session data management"""
    
    def test_session_data_creation(self):
        """Test creating complete session data"""
        session_data = SessionData(
            session=SessionMetadata(
                id="12345678-1234-4123-8123-123456789012",
                name="Integration Test",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                version="1.0.0",
                implementation=ImplementationType.V2_PYTHON
            )
        )
        
        assert session_data.session.name == "Integration Test"
        assert len(session_data.answers) == 0
        assert len(session_data.ai_conversations) == 0
        assert session_data.project.title is None
    
    def test_session_data_serialization(self):
        """Test session data can be serialized to JSON"""
        session_data = SessionData(
            session=SessionMetadata(
                id="12345678-1234-4123-8123-123456789012",
                name="Serialization Test",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                version="1.0.0",
                implementation=ImplementationType.V2_PYTHON
            )
        )
        
        # Add an answer
        session_data.answers.append(
            Answer(
                question_id="C-01",
                response="Test response",
                answered_at=datetime.now()
            )
        )
        
        # Serialize to dict
        data_dict = session_data.model_dump()
        assert data_dict["session"]["name"] == "Serialization Test"
        assert len(data_dict["answers"]) == 1
        
        # Serialize to JSON
        json_str = json.dumps(data_dict, default=str)
        assert "Serialization Test" in json_str


class TestQuestionValidation:
    """Test question validation logic"""
    
    def test_question_length_validation(self):
        """Test question response length validation"""
        question = QUESTIONS_BY_ID["C-01"]
        
        # Test minimum length
        assert question.min_length == 50
        assert question.max_length == 500
        
        # Test validation logic (would be in widget)
        short_response = "Too short"
        long_response = "x" * 600
        valid_response = "This is a valid response that meets the minimum length requirement for the question and provides meaningful content."
        
        assert len(short_response) < question.min_length
        assert len(long_response) > question.max_length
        assert question.min_length <= len(valid_response) <= question.max_length
    
    def test_all_questions_have_required_fields(self):
        """Test that all questions have required fields"""
        for question_id, question in QUESTIONS_BY_ID.items():
            assert question.id == question_id
            assert len(question.text) > 0
            assert len(question.guidance) > 0
            assert len(question.ai_prompt) > 0
            assert question.min_length > 0
            assert question.max_length > question.min_length
            assert question.phase in [PhaseType.CLARIFY, PhaseType.ORGANIZE, PhaseType.REFINE]


class TestIntegration:
    """Integration tests for the complete system"""
    
    def test_complete_workflow_simulation(self):
        """Test a complete workflow from start to finish"""
        # Create new session
        session_data = SessionData(
            session=SessionMetadata(
                id="12345678-1234-4123-8123-123456789012",
                name="Workflow Test",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                version="1.0.0",
                implementation=ImplementationType.V2_PYTHON
            )
        )
        
        # Simulate answering questions from each phase
        test_answers = [
            ("C-01", "This project helps developers plan projects more effectively using a structured methodology."),
            ("C-02", "Success means 80% of users complete their project planning in under 2 hours with actionable outcomes."),
            ("O-01", "Core features: 1) Guided questionnaire, 2) Progress tracking, 3) Multi-format output, 4) Session management, 5) Validation system."),
            ("R-01", "Technical risks include terminal compatibility issues, dependency management, and user experience consistency across platforms."),
        ]
        
        for question_id, response in test_answers:
            answer = Answer(
                question_id=question_id,
                response=response,
                answered_at=datetime.now(),
                confidence=4
            )
            session_data.answers.append(answer)
        
        # Test output generation
        generator = OutputGenerator(session_data)
        
        # Test all output formats
        markdown = generator.generate_markdown()
        json_output = generator.generate_json()
        ai_prompt = generator.generate_ai_prompt()
        
        assert "Workflow Test" in markdown
        assert "developers plan projects more effectively" in markdown
        
        json_data = json.loads(json_output)
        assert len(json_data["answers"]) == 4
        
        assert "Technical risks include terminal compatibility" in ai_prompt
        
        # Test session data integrity
        assert len(session_data.answers) == 4
        assert session_data.session.implementation == ImplementationType.V2_PYTHON


if __name__ == "__main__":
    pytest.main([__file__])
