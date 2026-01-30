"""Data models for CORE Framework using Pydantic"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum


class PhaseType(str, Enum):
    CLARIFY = "clarify"
    ORGANIZE = "organize"
    REFINE = "refine"
    EQUIP = "equip"


class ImplementationType(str, Enum):
    V1_HTML = "v1-html"
    V2_PYTHON = "v2-python"
    V3_REACT = "v3-react"


class SessionStatus(str, Enum):
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class Answer(BaseModel):
    question_id: str = Field(..., pattern=r"^[A-Z]-\d{2}$")
    response: str
    answered_at: datetime
    confidence: Optional[int] = Field(None, ge=1, le=5)
    notes: Optional[str] = None


class AIMessage(BaseModel):
    role: str = Field(..., pattern=r"^(user|assistant|system)$")
    content: str
    timestamp: datetime
    model: Optional[str] = None


class AIConversation(BaseModel):
    id: str
    phase: PhaseType
    question_id: Optional[str] = Field(None, pattern=r"^[A-Z]-\d{2}$")
    messages: List[AIMessage]
    created_at: datetime
    updated_at: datetime


class SessionMetadata(BaseModel):
    id: str = Field(..., pattern=r"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$")
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    created_at: datetime
    updated_at: datetime
    version: str = Field(..., pattern=r"^\d+\.\d+\.\d+$")
    implementation: ImplementationType
    status: SessionStatus = SessionStatus.DRAFT


class ProjectData(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    summary: Optional[str] = Field(None, max_length=1000)


class ExportInfo(BaseModel):
    format: str
    timestamp: datetime
    file_size: Optional[int] = None
    checksum: Optional[str] = None


class SessionData(BaseModel):
    session: SessionMetadata
    project: ProjectData = ProjectData()
    answers: List[Answer] = []
    ai_conversations: List[AIConversation] = []
    exports: Dict[str, Any] = {}


class Question(BaseModel):
    id: str = Field(..., pattern=r"^[A-Z]-\d{2}$")
    text: str
    guidance: str
    ai_prompt: str
    input_type: str = "textarea"
    min_length: int = 50
    max_length: int = 500
    phase: PhaseType


# Question definitions matching T-001 schema
QUESTIONS = [
    # Clarify Phase
    Question(
        id="C-01",
        text="What problem does this project solve, and for whom?",
        guidance="Think about the core pain point your project addresses. Be specific about your target users and their current struggles.",
        ai_prompt="Help me clarify the core problem this project solves. Ask probing questions about the target users, their current pain points, and why existing solutions aren't adequate.",
        min_length=50,
        max_length=500,
        phase=PhaseType.CLARIFY
    ),
    Question(
        id="C-02",
        text="What does success look like for this project in 6 months?",
        guidance="Describe concrete, measurable outcomes. What will be different in the world when your project succeeds?",
        ai_prompt="Help me define specific, measurable success criteria for this project. Challenge vague statements and push for concrete metrics and outcomes.",
        min_length=50,
        max_length=400,
        phase=PhaseType.CLARIFY
    ),
    Question(
        id="C-03",
        text="What unique value does your solution provide that alternatives don't?",
        guidance="Focus on your competitive advantage. What makes your approach special or different?",
        ai_prompt="Help me identify and articulate the unique value proposition. Ask about competitors and what makes this solution distinctly better.",
        min_length=30,
        max_length=300,
        phase=PhaseType.CLARIFY
    ),
    Question(
        id="C-04",
        text="Describe the ideal user experience from problem to solution.",
        guidance="Walk through the complete user journey. How do users discover, try, and succeed with your solution?",
        ai_prompt="Help me map out the complete user journey. Ask detailed questions about each touchpoint and potential friction points.",
        min_length=100,
        max_length=600,
        phase=PhaseType.CLARIFY
    ),
    Question(
        id="C-05",
        text="What is explicitly NOT included in this project's scope?",
        guidance="Clear boundaries prevent scope creep. What related problems will you NOT solve?",
        ai_prompt="Help me define clear scope boundaries. Challenge me to be specific about what's excluded and why those boundaries make sense.",
        min_length=50,
        max_length=400,
        phase=PhaseType.CLARIFY
    ),
    # Organize Phase
    Question(
        id="O-01",
        text="What are the 3-5 essential features that deliver your core value?",
        guidance="Focus on must-have features that directly support your value proposition. Avoid nice-to-haves.",
        ai_prompt="Help me identify and prioritize the essential features. Challenge me to justify why each feature is truly necessary for the core value proposition.",
        min_length=100,
        max_length=500,
        phase=PhaseType.ORGANIZE
    ),
    Question(
        id="O-02",
        text="Who are your different user types and what does each need?",
        guidance="Different users may need different features or experiences. Be specific about user segments.",
        ai_prompt="Help me identify distinct user types and their specific needs. Ask about how their requirements might differ and conflict.",
        min_length=50,
        max_length=400,
        phase=PhaseType.ORGANIZE
    ),
    Question(
        id="O-03",
        text="What's the smallest version that delivers real value to users?",
        guidance="Your MVP should solve the core problem for at least one user type. What can you cut while keeping the value?",
        ai_prompt="Help me define a focused MVP. Challenge me to cut features that don't directly contribute to solving the core problem.",
        min_length=50,
        max_length=400,
        phase=PhaseType.ORGANIZE
    ),
    Question(
        id="O-04",
        text="How will you measure if users are getting value from your solution?",
        guidance="Define specific, measurable metrics that indicate user success and project impact.",
        ai_prompt="Help me define actionable success metrics. Ask about leading vs lagging indicators and how I'll actually measure these.",
        min_length=50,
        max_length=300,
        phase=PhaseType.ORGANIZE
    ),
    Question(
        id="O-05",
        text="How will you decide what to build first, second, and third?",
        guidance="Establish clear criteria for prioritizing features and improvements based on impact and effort.",
        ai_prompt="Help me create a framework for prioritizing features. Ask about impact vs effort, user feedback integration, and decision criteria.",
        min_length=50,
        max_length=300,
        phase=PhaseType.ORGANIZE
    ),
    # Refine Phase
    Question(
        id="R-01",
        text="What technical challenges or unknowns could derail this project?",
        guidance="Identify technical risks early. What don't you know how to build yet? What could go wrong?",
        ai_prompt="Help me identify technical risks and unknowns. Ask probing questions about my technical assumptions and potential failure points.",
        min_length=50,
        max_length=400,
        phase=PhaseType.REFINE
    ),
    Question(
        id="R-02",
        text="What are your realistic constraints for time, budget, and team?",
        guidance="Be honest about your actual resources. What are the hard limits you're working within?",
        ai_prompt="Help me realistically assess my resource constraints. Challenge optimistic assumptions about time, budget, and team capacity.",
        min_length=50,
        max_length=300,
        phase=PhaseType.REFINE
    ),
    Question(
        id="R-03",
        text="What could prevent users from adopting or paying for this solution?",
        guidance="Consider adoption barriers, competition, and market timing. What might make users say no?",
        ai_prompt="Help me identify market and adoption risks. Ask about user behavior, competitive threats, and market timing concerns.",
        min_length=50,
        max_length=400,
        phase=PhaseType.REFINE
    ),
    Question(
        id="R-04",
        text="How will you test your assumptions before building everything?",
        guidance="Plan specific experiments to validate your riskiest assumptions with real users.",
        ai_prompt="Help me design experiments to validate key assumptions. Ask about the riskiest assumptions and how to test them cheaply and quickly.",
        min_length=50,
        max_length=400,
        phase=PhaseType.REFINE
    ),
    Question(
        id="R-05",
        text="What evidence would convince you to significantly change direction?",
        guidance="Define clear criteria that would indicate your current approach isn't working.",
        ai_prompt="Help me define pivot triggers and decision points. Ask about what evidence would indicate the need for major changes.",
        min_length=50,
        max_length=300,
        phase=PhaseType.REFINE
    ),
]

# Create lookup dictionaries
QUESTIONS_BY_ID = {q.id: q for q in QUESTIONS}
QUESTIONS_BY_PHASE = {
    PhaseType.CLARIFY: [q for q in QUESTIONS if q.phase == PhaseType.CLARIFY],
    PhaseType.ORGANIZE: [q for q in QUESTIONS if q.phase == PhaseType.ORGANIZE],
    PhaseType.REFINE: [q for q in QUESTIONS if q.phase == PhaseType.REFINE],
}
