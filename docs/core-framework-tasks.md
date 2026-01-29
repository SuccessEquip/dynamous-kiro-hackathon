# CORE Framework — Tasks

**Status**: Draft  •  **Version**: 0.1  •  **Last updated**: 2026-01-28  
**Owner**: Project Lead  •  **Repo**: CORE-ProjectPlanningFramework

> **Purpose**: Provide ordered, atomic task list for implementing the CORE Framework project planning tool across three implementations.

---

## 0) Workflow Conventions
- **Branching**: `feat/{implementation}-{feature}` / `fix/{implementation}-{issue}` per task group  
- **Commits**: Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `test:`). Reference requirement IDs  
- **Implementation Order**: v1 (HTML) → v2 (Python) → v3 (React) for methodology validation  
- **Testing**: Each implementation includes unit tests for core logic, integration tests for full workflow  
- **Documentation**: Update README and implementation-specific docs with each major feature

## 1) Environment Detection
- **v1**: Modern browser with ES6+ support, local web server for development
- **v2**: Python 3.14+, pip, terminal with Unicode support
- **v3**: Node.js 18+, npm/yarn, modern browser for testing

## 2) Task Records

### Foundation Tasks

```
T-001: Define Core Methodology Schema and Question Framework ✅ COMPLETE
Maps to: R-F-001, R-F-002
Component(s): C-01
Description: Create JSON schema and question framework defining 5-5-5+4 structure (Clarify/Organize/Refine questions + Equip actions)
Files/Paths: shared/schema/methodology.json, shared/schema/session.json, docs/core-framework-questions.md
Definition of Done:
  - ✅ JSON schema validates 15 questions (5-5-5) + 4 actions structure
  - ✅ All questions defined with AI guidance prompts
  - ✅ Session schema includes id/name/description/answers/ai_conversations
  - ✅ Export schema for Markdown/JSON/AI prompt formats
Evidence to Produce:
  - ✅ Tests: schema validation tests, question framework tests (25 tests passing)
  - ✅ Artifacts: JSON schema files, complete question framework document
Risk Level: High (foundation for all implementations)
Rollback Plan: Revert to basic question list without formal schema
Implementation Notes:
  - ✅ Must support all three implementation approaches
  - ✅ Include AI guidance patterns for each phase
  - ✅ Define output templates for all three formats
  - ✅ Automated testing infrastructure established
  - ✅ CI/CD pipeline configured for quality assurance
Completed: 2026-01-29 by automated workflow system
```

```
T-002: Implement v1 HTML Core Structure
Maps to: R-F-001, R-F-002, R-N-UX-001, R-N-UX-002
Component(s): C-01, C-02
Description: Create single-file HTML implementation with 4-phase navigation and question presentation
Files/Paths: v1-html/index.html
Definition of Done:
  - Single HTML file with embedded CSS and JavaScript
  - 4-phase navigation with progress indicators
  - All 15 questions distributed across phases
  - Full keyboard navigation support
  - WCAG AA compliance verified
Evidence to Produce:
  - Tests: Accessibility audit results, keyboard navigation test
  - Artifacts: Working HTML file, lighthouse accessibility score
Risk Level: Medium (sets UX pattern for other implementations)
Rollback Plan: Simplify to basic form without phase navigation
Implementation Notes:
  - Use semantic HTML for accessibility
  - CSS Grid/Flexbox for responsive layout
  - Vanilla JavaScript, no external dependencies
```

```
T-003: Implement v1 Session Persistence
Maps to: R-F-006, R-N-REL-003
Component(s): C-04
Description: Add LocalStorage-based session save/restore functionality to v1
Files/Paths: v1-html/index.html (session management section)
Definition of Done:
  - User progress saved automatically on input changes
  - Session restored on page reload
  - Multiple sessions supported with unique IDs
  - Data persists across browser restarts
Evidence to Produce:
  - Tests: LocalStorage persistence tests, session restoration tests
  - Artifacts: Session data examples, storage size analysis
Risk Level: Low (well-established browser API)
Rollback Plan: Remove persistence, warn users about data loss
Implementation Notes:
  - Handle LocalStorage quota exceeded gracefully
  - Include session metadata (timestamp, version)
  - Validate restored data against schema
```

### Output Generation Tasks

```
T-004: Implement Multi-Format Output Generation
Maps to: R-F-003, R-F-004, R-F-005
Component(s): C-03
Description: Create output generators for Markdown (title/timestamp/Q&A/Next Steps), JSON export (framework/project/ai_conversations), and AI prompt (intro/context/deliverables)
Files/Paths: v1-html/index.html (output generation section), shared/templates/
Definition of Done:
  - Markdown output: project title, timestamp, phase sections with Q&A, detailed Next Steps
  - JSON export: framework metadata, project arrays (clarify/organize/refine), ai_conversations
  - AI prompt: "Based on the following CORE Framework analysis..." intro, Project Context, deliverables (v2: architecture/plan/challenges/tools/timeline, v3: architecture/roadmap/risks/guidelines/metrics)
  - Download functionality for all formats
Evidence to Produce:
  - Tests: Output format validation tests, template rendering tests
  - Artifacts: Sample outputs for each format, format specifications
Risk Level: Medium (complex template logic)
Rollback Plan: Provide basic text output only
Implementation Notes:
  - Use template literals for Markdown generation
  - Validate JSON output against schema
  - Include metadata in all output formats
  - AI prompt varies by implementation version
```

### Python TUI Implementation Tasks

```
T-005: Bootstrap v2 Python TUI Structure
Maps to: R-F-001, R-F-002, R-N-UX-001
Component(s): C-01, C-02
Description: Create Python TUI application using Textual framework with same methodology
Files/Paths: v2-python/core_framework/, v2-python/requirements.txt, v2-python/setup.py
Definition of Done:
  - Textual-based TUI with 4-phase navigation
  - Rich formatting for enhanced readability
  - Same question flow as v1 implementation
  - Keyboard navigation and accessibility features
Evidence to Produce:
  - Tests: TUI interaction tests, methodology consistency tests
  - Artifacts: Package structure, installation instructions
Risk Level: Medium (new framework, terminal compatibility)
Rollback Plan: Simplify to basic CLI prompts
Implementation Notes:
  - Use Textual widgets for consistent UI
  - Handle terminal resize gracefully
  - Support both light and dark terminal themes
```

```
T-006: Add AI Integration to v2 (OpenRouter + Ollama)
Maps to: R-F-007, R-F-008, R-N-SEC-003, R-N-REL-002
Component(s): C-05
Description: Integrate both OpenRouter API and Ollama for AI-assisted planning with phase-specific chat guidance
Files/Paths: v2-python/core_framework/ai_handler.py, v2-python/core_framework/config.py
Definition of Done:
  - Async API calls to OpenRouter with user-selectable models
  - Ollama integration for local LLM support
  - Phase-specific AI guidance (probe for better answers, refine scope, surface extra questions)
  - Rate limiting, retry logic, and graceful degradation
  - Environment variable configuration for API keys
  - AI conversation history storage in session data
Evidence to Produce:
  - Tests: API integration tests, error handling tests, offline mode tests, Ollama integration tests
  - Artifacts: API usage examples, configuration documentation, AI guidance examples
Risk Level: High (dual external API dependencies)
Rollback Plan: Disable AI features, provide manual guidance prompts
Implementation Notes:
  - Use aiohttp for async HTTP requests
  - Implement exponential backoff for retries
  - Cache responses to reduce API calls
  - Support both cloud (OpenRouter) and local (Ollama) models
  - Phase-specific prompt templates for AI guidance
```

### React Implementation Tasks

```
T-007: Bootstrap v3 React Application
Maps to: R-F-001, R-F-002, R-N-UX-001, R-N-PERF-001
Component(s): C-01, C-02
Description: Create React SPA with TypeScript, Tailwind CSS, and shadcn/ui components
Files/Paths: v3-react/frontend/src/, v3-react/frontend/package.json
Definition of Done:
  - React 19 application with TypeScript
  - Tailwind CSS + shadcn/ui component library
  - Same 4-phase methodology as other implementations
  - Responsive design for mobile and desktop
  - Performance budget met (<500KB initial bundle)
Evidence to Produce:
  - Tests: Component tests, integration tests, performance tests
  - Artifacts: Bundle size analysis, lighthouse performance score
Risk Level: Medium (complex modern stack)
Rollback Plan: Simplify to basic React without advanced features
Implementation Notes:
  - Use React hooks for state management
  - Implement code splitting for performance
  - Follow React 19 best practices
```

```
T-008: Integrate Supabase Backend
Maps to: R-F-006, R-N-REL-003, R-N-SEC-001
Component(s): C-04
Description: Add Supabase integration for authentication and data persistence
Files/Paths: v3-react/supabase/, v3-react/frontend/src/lib/supabase.ts
Definition of Done:
  - Supabase project configured with authentication
  - Database schema for session storage
  - Real-time sync for session updates
  - Optional local JSON export functionality
Evidence to Produce:
  - Tests: Database integration tests, auth flow tests, sync tests
  - Artifacts: Database schema, API documentation
Risk Level: Medium (cloud service dependency)
Rollback Plan: Fall back to LocalStorage like v1
Implementation Notes:
  - Use Supabase Auth for user management
  - Implement row-level security policies
  - Handle offline scenarios gracefully
```

### Testing and Validation Tasks

```
T-009: Implement Cross-Implementation Test Suite
Maps to: All requirements
Component(s): All components
Description: Create shared test suite validating methodology consistency across implementations
Files/Paths: tests/shared/, tests/integration/
Definition of Done:
  - Shared test data for all implementations
  - Methodology consistency validation
  - Output format compatibility tests
  - Performance benchmarks for all versions
Evidence to Produce:
  - Tests: Cross-implementation test results, performance benchmarks
  - Artifacts: Test reports, compatibility matrix
Risk Level: High (validates entire project)
Rollback Plan: Test implementations individually
Implementation Notes:
  - Use JSON test fixtures for consistency
  - Automate testing in CI/CD pipeline
  - Include accessibility testing for all implementations
```

```
T-010: Documentation and Deployment
Maps to: R-N-UX-004, deployment requirements
Component(s): All components
Description: Complete documentation and deployment setup for all implementations
Files/Paths: README.md, docs/, deployment configs
Definition of Done:
  - Comprehensive README with setup instructions
  - Implementation-specific documentation
  - Deployment automation for all versions
  - User guide with examples and screenshots
Evidence to Produce:
  - Tests: Documentation accuracy tests, deployment verification
  - Artifacts: Live deployments, user guide, API documentation
Risk Level: Low (documentation and deployment)
Rollback Plan: Manual deployment with basic documentation
Implementation Notes:
  - Use GitHub Actions for CI/CD
  - Deploy v1 to static hosting, v2 as pip package, v3 to Vercel
  - Include troubleshooting guides
```

## 3) Implementation Priority Order
1. **T-001**: Foundation schema (blocks all other work)
2. **T-002, T-003, T-004**: Complete v1 implementation (validates methodology)
3. **T-005, T-006**: v2 Python TUI with AI integration
4. **T-007, T-008**: v3 React/Supabase implementation
5. **T-009**: Cross-implementation testing
6. **T-010**: Documentation and deployment

## 4) PR Template
```
## Summary
{Implementation and feature description}

## Linked Requirements
- R-F-XXX: {requirement description}
- R-N-XXX: {non-functional requirement}

## Validation Evidence
- Tests: {test files and CI results}
- Accessibility: {a11y audit results}
- Performance: {benchmark results}
- Cross-implementation: {consistency verification}

## Risk & Rollback
- Risk Level: {Low/Medium/High}
- Rollback Plan: {specific steps to revert}

## Checklist
- [ ] Methodology consistency maintained
- [ ] Accessibility requirements met
- [ ] Performance budgets respected
- [ ] Tests pass for affected implementation
- [ ] Documentation updated
```

> **LLM usage note**: Execute tasks in priority order. Validate methodology consistency across implementations. Never skip accessibility or performance requirements.
