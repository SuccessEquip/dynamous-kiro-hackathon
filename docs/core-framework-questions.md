# CORE Framework Questions

**Version**: 1.0.0  
**Last Updated**: 2026-01-29  
**Schema**: `shared/schema/methodology.json`

> **Purpose**: Complete question framework for the CORE methodology with AI guidance patterns and output templates.

---

## Framework Structure

The CORE Framework follows a **4-phase, 15-question + 4-action** structure:
- **Clarify** (5 questions): Define project purpose and scope
- **Organize** (5 questions): Structure requirements and priorities  
- **Refine** (5 questions): Analyze risks and constraints
- **Equip** (4 actions): Generate implementation documentation

---

## Phase 1: Clarify (C-01 to C-05)

### C-01: Project Purpose
**Question**: "What problem does this project solve, and for whom?"
**Guidance**: Think about the core pain point your project addresses. Be specific about your target users and their current struggles.
**AI Prompt**: "Help me clarify the core problem this project solves. Ask probing questions about the target users, their current pain points, and why existing solutions aren't adequate."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 500 }

### C-02: Success Vision
**Question**: "What does success look like for this project in 6 months?"
**Guidance**: Describe concrete, measurable outcomes. What will be different in the world when your project succeeds?
**AI Prompt**: "Help me define specific, measurable success criteria for this project. Challenge vague statements and push for concrete metrics and outcomes."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 400 }

### C-03: Core Value Proposition
**Question**: "What unique value does your solution provide that alternatives don't?"
**Guidance**: Focus on your competitive advantage. What makes your approach special or different?
**AI Prompt**: "Help me identify and articulate the unique value proposition. Ask about competitors and what makes this solution distinctly better."
**Input Type**: textarea
**Validation**: { "min_length": 30, "max_length": 300 }

### C-04: User Journey
**Question**: "Describe the ideal user experience from problem to solution."
**Guidance**: Walk through the complete user journey. How do users discover, try, and succeed with your solution?
**AI Prompt**: "Help me map out the complete user journey. Ask detailed questions about each touchpoint and potential friction points."
**Input Type**: textarea
**Validation**: { "min_length": 100, "max_length": 600 }

### C-05: Scope Boundaries
**Question**: "What is explicitly NOT included in this project's scope?"
**Guidance**: Clear boundaries prevent scope creep. What related problems will you NOT solve?
**AI Prompt**: "Help me define clear scope boundaries. Challenge me to be specific about what's excluded and why those boundaries make sense."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 400 }

---

## Phase 2: Organize (O-01 to O-05)

### O-01: Core Features
**Question**: "What are the 3-5 essential features that deliver your core value?"
**Guidance**: Focus on must-have features that directly support your value proposition. Avoid nice-to-haves.
**AI Prompt**: "Help me identify and prioritize the essential features. Challenge me to justify why each feature is truly necessary for the core value proposition."
**Input Type**: textarea
**Validation**: { "min_length": 100, "max_length": 500 }

### O-02: User Types
**Question**: "Who are your different user types and what does each need?"
**Guidance**: Different users may need different features or experiences. Be specific about user segments.
**AI Prompt**: "Help me identify distinct user types and their specific needs. Ask about how their requirements might differ and conflict."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 400 }

### O-03: MVP Definition
**Question**: "What's the smallest version that delivers real value to users?"
**Guidance**: Your MVP should solve the core problem for at least one user type. What can you cut while keeping the value?
**AI Prompt**: "Help me define a focused MVP. Challenge me to cut features that don't directly contribute to solving the core problem."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 400 }

### O-04: Success Metrics
**Question**: "How will you measure if users are getting value from your solution?"
**Guidance**: Define specific, measurable metrics that indicate user success and project impact.
**AI Prompt**: "Help me define actionable success metrics. Ask about leading vs lagging indicators and how I'll actually measure these."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 300 }

### O-05: Priority Framework
**Question**: "How will you decide what to build first, second, and third?"
**Guidance**: Establish clear criteria for prioritizing features and improvements based on impact and effort.
**AI Prompt**: "Help me create a framework for prioritizing features. Ask about impact vs effort, user feedback integration, and decision criteria."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 300 }

---

## Phase 3: Refine (R-01 to R-05)

### R-01: Technical Risks
**Question**: "What technical challenges or unknowns could derail this project?"
**Guidance**: Identify technical risks early. What don't you know how to build yet? What could go wrong?
**AI Prompt**: "Help me identify technical risks and unknowns. Ask probing questions about my technical assumptions and potential failure points."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 400 }

### R-02: Resource Constraints
**Question**: "What are your realistic constraints for time, budget, and team?"
**Guidance**: Be honest about your actual resources. What are the hard limits you're working within?
**AI Prompt**: "Help me realistically assess my resource constraints. Challenge optimistic assumptions about time, budget, and team capacity."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 300 }

### R-03: Market Risks
**Question**: "What could prevent users from adopting or paying for this solution?"
**Guidance**: Consider adoption barriers, competition, and market timing. What might make users say no?
**AI Prompt**: "Help me identify market and adoption risks. Ask about user behavior, competitive threats, and market timing concerns."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 400 }

### R-04: Validation Plan
**Question**: "How will you test your assumptions before building everything?"
**Guidance**: Plan specific experiments to validate your riskiest assumptions with real users.
**AI Prompt**: "Help me design experiments to validate key assumptions. Ask about the riskiest assumptions and how to test them cheaply and quickly."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 400 }

### R-05: Pivot Triggers
**Question**: "What evidence would convince you to significantly change direction?"
**Guidance**: Define clear criteria that would indicate your current approach isn't working.
**AI Prompt**: "Help me define pivot triggers and decision points. Ask about what evidence would indicate the need for major changes."
**Input Type**: textarea
**Validation**: { "min_length": 50, "max_length": 300 }

---

## Phase 4: Equip (E-01 to E-04)

### E-01: Generate Project Documentation
**Name**: "Create Comprehensive Project Documentation"
**Description**: "Generate detailed project documentation in Markdown format including all phases, answers, and next steps."
**Output Format**: "markdown"

### E-02: Export Structured Data
**Name**: "Export Session Data as JSON"
**Description**: "Export complete session data including metadata, answers, and AI conversations in structured JSON format."
**Output Format**: "json"

### E-03: Create AI Implementation Prompt
**Name**: "Generate AI-Assisted Implementation Prompt"
**Description**: "Create a comprehensive prompt for AI-assisted development including project context and specific deliverables."
**Output Format**: "ai_prompt"

### E-04: Generate All Formats
**Name**: "Export Complete Documentation Package"
**Description**: "Generate all output formats (Markdown, JSON, AI prompt) for comprehensive project handoff."
**Output Format**: "all"

---

## AI Guidance Patterns

### Phase-Specific AI Behavior

**Clarify Phase**: 
- Probe for specificity and concrete details
- Challenge vague statements
- Ask "why" and "for whom" questions
- Help identify core problems vs symptoms

**Organize Phase**:
- Push for prioritization and trade-offs
- Challenge feature bloat
- Ask about user needs and workflows
- Help define measurable success criteria

**Refine Phase**:
- Surface hidden assumptions and risks
- Challenge optimistic estimates
- Ask about failure modes and contingencies
- Help plan validation experiments

**Equip Phase**:
- Focus on actionable next steps
- Help structure implementation plans
- Ask about resource allocation and timelines
- Ensure deliverables are specific and measurable

---

## Output Templates

### Markdown Template
```markdown
# {project_title} - CORE Framework Analysis

**Generated**: {timestamp}
**Session**: {session_name}
**Framework Version**: {version}

## Executive Summary
{project_summary}

## Phase 1: Clarify
{clarify_questions_and_answers}

## Phase 2: Organize  
{organize_questions_and_answers}

## Phase 3: Refine
{refine_questions_and_answers}

## Next Steps
{implementation_recommendations}

## AI Conversations
{ai_conversation_summaries}
```

### AI Prompt Template
```
Based on the following CORE Framework analysis, provide detailed implementation guidance for this project:

## Project Context
{project_summary_and_key_insights}

## Requirements Analysis
{organized_requirements_from_all_phases}

## Please provide:
{version_specific_deliverables}

## Additional Context
{ai_conversation_insights}
```

### Version-Specific AI Deliverables

**v1 (HTML/JS)**:
- Single-file HTML structure and component breakdown
- CSS framework recommendations and responsive design approach
- JavaScript architecture for state management and persistence
- Accessibility implementation checklist
- Performance optimization strategies

**v2 (Python TUI)**:
- Python package structure and dependency management
- Textual framework implementation approach
- AI integration architecture (OpenRouter + Ollama)
- CLI workflow and user experience design
- Testing strategy for TUI applications

**v3 (React/Supabase)**:
- React component architecture and state management
- Supabase integration and database schema design
- Authentication and authorization implementation
- Deployment strategy and CI/CD pipeline
- Performance monitoring and optimization plan

---

## Validation Rules

### Question Validation
- All questions must have minimum character requirements
- Guidance text should be actionable and specific
- AI prompts should encourage depth and specificity
- Input types should match the expected response format

### Schema Compliance
- Question IDs follow pattern: `{Phase}-{Number}` (C-01, O-01, R-01)
- Action IDs follow pattern: `E-{Number}` (E-01, E-02, E-03, E-04)
- All required fields must be present in schema
- Validation rules must be enforceable across all implementations

### Cross-Implementation Consistency
- Same questions and guidance across all versions
- Consistent output formats and templates
- Compatible session data structures
- Unified AI guidance patterns

---

*This question framework serves as the foundation for all CORE Framework implementations and ensures consistent methodology across HTML, Python TUI, and React versions.*
