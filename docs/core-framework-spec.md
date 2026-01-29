# CORE Framework — Project Specification

**Status**: Draft  •  **Version**: 0.1  •  **Last updated**: 2026-01-28  
**Owner**: Project Lead  •  **Repo**: CORE-ProjectPlanningFramework

> **Purpose**: Main specification connecting design, requirements, and implementation for the CORE Framework multi-implementation project planning tool.

---

## Project Overview

### Purpose
Interactive project planning tool that transforms vague ideas into actionable project plans through a structured 4-phase, 15-question methodology with multi-format output and optional AI assistance.

### Scope
**In Scope:**
- 4-phase methodology (Clarify → Organize → Refine → Equip)
- 15 strategic questions framework
- Multi-implementation approach (v1: HTML/JS, v2: Python TUI, v3: React/Supabase)
- Multi-format output (Markdown, JSON, AI prompts)
- Session persistence and restoration
- Optional AI integration (OpenRouter API)
- Accessibility compliance (WCAG AA)
- Cross-platform compatibility

**Out of Scope:**
- Real-time collaboration features
- Advanced project management (Gantt charts, resource allocation)
- Integration with external project management tools
- Multi-language internationalization (English only for v1)

### Success Criteria
- 80%+ completion rate through all 4 phases
- Generated plans contain actionable, specific requirements
- Users report increased project clarity and confidence
- All implementations maintain methodology consistency
- Accessibility compliance verified across all versions

## Context & Background

### Problem Statement
Individuals and small teams struggle to transform vague project ideas into structured, actionable plans. Current tools are either too complex (enterprise PM tools) or too simple (note-taking apps), leaving a gap for systematic yet accessible project planning.

### Stakeholders
- **Solo Entrepreneurs**: Need quick idea validation and structured planning
- **Developers**: Want systematic technical planning and requirements gathering
- **Small Product Teams**: Require PRD-like documents and shared project clarity
- **Non-technical Founders**: Need to communicate clear requirements to development teams

### Assumptions
- Users prefer progressive complexity (simple → advanced options)
- Local-first approach with optional cloud sync is preferred
- AI assistance enhances but doesn't replace human decision-making
- Cross-platform compatibility is essential for adoption

### Constraints
- Hackathon timeline (limited development time)
- No budget for premium APIs or services
- Must work offline for core functionality
- Single developer implementation

## High-Level Approach

### Solution Overview
Progressive complexity architecture with three implementations sharing the same core methodology, allowing users to choose their preferred interface while maintaining consistent output quality.

### Key Components
1. **Core Methodology Engine**: 4-phase, 15-question framework logic
2. **Multi-Format Output Generator**: Markdown, JSON, and AI prompt generation
3. **Session Management**: Save/restore functionality across implementations
4. **AI Integration Layer**: Optional OpenRouter API integration (v2/v3)
5. **User Interface Layers**: HTML/JS, Python TUI, React SPA

### Technology Stack
- **v1**: HTML5, CSS3, JavaScript ES6+, LocalStorage
- **v2**: Python 3.14, Textual, Rich, aiohttp, JSON files
- **v3**: React 19, TypeScript, Tailwind CSS, shadcn/ui, Supabase
- **Shared**: OpenRouter API, JSON schema validation

## Timeline & Milestones

### Project Phases
1. **Phase 1 - Foundation** (Days 1-3)
   - Core methodology implementation
   - v1 HTML single-file implementation
   - Basic output generation

2. **Phase 2 - Enhancement** (Days 4-7)
   - v2 Python TUI implementation
   - AI integration layer
   - Advanced output formats

3. **Phase 3 - Scale** (Days 8-12)
   - v3 React/Supabase implementation
   - Cross-implementation testing
   - Documentation and deployment

### Key Milestones
- **Day 3**: v1 functional with complete methodology
- **Day 7**: v2 functional with AI integration
- **Day 12**: v3 functional with cloud persistence
- **Day 15**: All implementations tested and documented

## Risk Assessment

### Technical Risks
- **Multi-implementation complexity**: High - Mitigation: Shared JSON schema and test cases
- **AI API reliability**: Medium - Mitigation: Graceful degradation, offline functionality
- **Accessibility compliance**: Medium - Mitigation: Built-in from start, automated testing

### Business Risks
- **User adoption**: Medium - Mitigation: Progressive complexity, clear value proposition
- **Scope creep**: High - Mitigation: Strict scope definition, MVP focus

## Related Documents

- **Design Document**: `core-framework-design.md` - Technical architecture and implementation details
- **Requirements Document**: `core-framework-requirements.md` - Detailed functional and non-functional requirements
- **Tasks Document**: `core-framework-tasks.md` - Implementation breakdown and workflow guidance
- **Validation Document**: `core-framework-validation.md` - Testing strategy and acceptance criteria

## Approval & Sign-off

### Review Process
- [ ] Technical architecture review
- [ ] Requirements completeness review
- [ ] Implementation feasibility review
- [ ] Final specification approval

### Change Management
Changes to this specification require:
1. Impact analysis on all three implementations
2. Update to related documents
3. Validation of continued feasibility within timeline

---

**Document Status**: Draft  
**Last Updated**: 2026-01-28  
**Version**: 0.1  
**Owner**: Project Lead
