# CORE Framework — Requirements

**Status**: Draft  •  **Version**: 0.1  •  **Last updated**: 2026-01-28  
**Owner**: Project Lead  •  **Repo**: CORE-ProjectPlanningFramework

> **Purpose**: Specify clear, testable requirements that drive deterministic tasks and validations for the CORE Framework project planning tool.

---

## 0) ID & Priority Scheme
- **ID format**:  
  - Functional: `R-F-{###}`  
  - Security: `R-N-SEC-{###}`  
  - Performance: `R-N-PERF-{###}`  
  - Reliability: `R-N-REL-{###}`  
  - Usability/Accessibility: `R-N-UX-{###}`  
- **Priority**: MUST / SHOULD / COULD / WON'T  
- **Verification method**: Test / Analysis / Demonstration / Inspection

## 1) Glossary
- **CORE Methodology**: 4-phase planning process (Clarify → Organize → Refine → Equip)
- **Clarify Phase**: Define problem and vision (5 questions)
- **Organize Phase**: Structure the solution (5 questions)  
- **Refine Phase**: Stress-test the plan (5 questions)
- **Equip Phase**: Generate actionable documentation (4 actions, not questions)
- **Session**: Complete or partial user interaction with the planning tool
- **AI Chat Guidance**: Phase-specific assistance for better answers and scope refinement
- **Multi-Format Export**: Markdown plan, JSON data, AI continuation prompt
- **Implementation Version**: v1 (HTML single-file), v2 (Python TUI + AI), v3 (React/Supabase full UX)

## 2) Functional Requirements

| ID | Statement | Rationale | Priority | Related Components | Acceptance criteria (Given/When/Then) |
|---|---|---|---|---|---|
| R-F-001 | The system SHALL guide users through exactly 4 phases: Clarify (problem/vision), Organize (solution structure), Refine (stress-test), Equip (documentation) | Structured methodology for idea-to-plan transformation | MUST | C-01,C-02 | Given user starts session When they complete all phases Then Clarify/Organize/Refine have 5 questions each, Equip has 4 actions |
| R-F-002 | The system SHALL present exactly 15 questions: 5 in Clarify, 5 in Organize, 5 in Refine, plus 4 actions in Equip | Proven question framework for comprehensive planning | MUST | C-01,C-02 | Given user in any phase When questions are displayed Then Clarify/Organize/Refine show 5 questions each, Equip shows 4 actions |
| R-F-003 | The system SHALL generate Markdown output with project title, timestamp, phase sections (Q&A format), and Next Steps | Implementation-ready project documentation | MUST | C-03 | Given completed session When user exports Markdown Then document contains title, timestamp, all Q&A, detailed Next Steps |
| R-F-004 | The system SHALL generate JSON export with framework metadata, session data, and AI conversations | Structured data for integration and analysis | MUST | C-03 | Given completed session When user exports JSON Then schema includes framework/version/timestamp/project arrays/ai_conversations |
| R-F-005 | The system SHALL generate AI continuation prompt with "Based on the following CORE Framework analysis..." intro, Project Context, and deliverables list | Enable seamless handoff to AI coding assistants | MUST | C-03 | Given completed session When user exports AI prompt Then prompt includes intro, context sections, specific deliverables (architecture/roadmap/risks/guidelines/metrics for v3) |
| R-F-006 | The system SHALL save session state with id, name, description, created_at, answers, and ai_conversations | Multi-session planning support | MUST | C-04 | Given partial session When user saves and returns Then all data including AI chat history is restored |
| R-F-007 | The system SHALL provide phase-specific AI chat guidance to probe for better answers, refine scope, surface extra questions, and synthesize recommendations | Enhanced planning quality through AI assistance | SHOULD | C-05 | Given user in any phase When AI chat is used Then guidance is contextual to current phase and improves answer quality |
| R-F-008 | The system SHALL support OpenRouter API with user-selectable models and Ollama integration for local LLMs | Flexible AI provider options | SHOULD | C-05 | Given AI integration When user configures provider Then both OpenRouter and Ollama work with model selection |
| R-F-009 | The system SHALL allow navigation between phases with answer editing capability | Iterative refinement of planning | SHOULD | C-02 | Given user in any phase When they navigate to previous phase Then previous answers are editable and changes persist |

## 3) Non-Functional Requirements

### 3.1 Security
- R-N-SEC-001: All user inputs SHALL be validated against defined schemas; invalid inputs are rejected and logged without sensitive data. — **Verify**: unit+integration tests, input fuzzing.
- R-N-SEC-002: No API keys or secrets SHALL be stored in source code; environment variables only. — **Verify**: code review, SAST scanning.
- R-N-SEC-003: AI API calls SHALL include rate limiting and error handling to prevent abuse. — **Verify**: integration tests, load testing.

### 3.2 Performance
- R-N-PERF-001: Phase transitions SHALL complete within 2 seconds on standard hardware. — **Verify**: performance testing.
- R-N-PERF-002: Output generation SHALL complete within 5 seconds for complete sessions. — **Verify**: benchmark testing.
- R-N-PERF-003: Session save/restore operations SHALL complete within 1 second. — **Verify**: performance testing.
- R-N-PERF-004: Target completion times: Quick (10-15 min), Standard (15-30 min), Deep (45-60 min). — **Verify**: user journey testing.
- R-N-PERF-005: v1 bundle size SHALL be <100KB total for zero-setup deployment. — **Verify**: bundle analysis.

### 3.3 Reliability
- R-N-REL-001: The system SHALL function completely offline for core methodology (no AI features). — **Verify**: offline testing.
- R-N-REL-002: AI integration failures SHALL degrade gracefully without breaking core functionality. — **Verify**: fault injection testing.
- R-N-REL-003: Session data SHALL be preserved across browser/application restarts. — **Verify**: persistence testing.

### 3.4 Usability & Accessibility
- R-N-UX-001: All implementations SHALL meet WCAG 2.2 AA standards for accessibility. — **Verify**: automated a11y testing + manual checklist.
- R-N-UX-002: The system SHALL support full keyboard navigation without mouse. — **Verify**: keyboard-only testing.
- R-N-UX-003: Progress indicators SHALL show completion status across all phases. — **Verify**: UI testing.
- R-N-UX-004: The system SHALL provide clear error messages and recovery guidance. — **Verify**: error scenario testing.

## 4) Constraints & Assumptions
- **Platform Constraints**: v1 requires modern browser, v2 requires Python 3.14+, v3 requires Node.js 18+
- **Storage Constraints**: LocalStorage (v1), local files (v2), Supabase limits (v3)
- **API Constraints**: OpenRouter API rate limits and costs
- **Timeline Constraint**: Must be completed within hackathon timeframe
- **Assumptions**: Users have basic technical literacy, stable internet for AI features

## 5) Dependencies
- **OpenRouter API**: AI assistance features, rate limits apply, fallback to offline mode
- **Ollama**: Local LLM integration for privacy-conscious users, requires local installation
- **Supabase**: v3 backend services, 99.9% uptime SLA, fallback to local JSON export
- **Browser APIs**: LocalStorage, modern JavaScript features (ES6+)
- **Python Libraries**: Textual, Rich, aiohttp for v2 implementation
- **React Ecosystem**: React 19, TypeScript, Tailwind CSS, shadcn/ui for v3

## 6) Out of Scope
- Real-time collaboration between multiple users
- Integration with external project management tools (Jira, Asana, etc.)
- Advanced analytics or reporting features
- Multi-language support (English only)
- Mobile-specific optimizations (responsive web only)
- Enterprise authentication/authorization

## 7) Traceability
- **Requirement → Task(s)**: To be filled in `core-framework-tasks.md`  
- **Requirement → Validation(s)**: To be filled in `core-framework-validation.md`
- **Coverage checkpoint**: No requirement without at least one task and one validation

## 8) Change Control
- **Proposed changes**: Submit via GitHub issue with impact analysis
- **Approval required**: Technical feasibility and timeline impact assessment
- **Impact analysis**: Effect on all three implementations and timeline

> **LLM usage note**: Treat requirement IDs as canonical. Do not invent new requirements; propose changes via documented process with impact analysis.
