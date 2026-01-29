# CORE Framework — Validation & Testing

**Status**: Draft  •  **Version**: 0.1  •  **Last updated**: 2026-01-28  
**Owner**: Project Lead  •  **Repo**: CORE-ProjectPlanningFramework

> **Purpose**: Define comprehensive testing strategy and acceptance criteria for validating the CORE Framework across all three implementations.

---

## 0) Validation Strategy Overview
- **Multi-Implementation Consistency**: Same methodology behavior across v1, v2, v3
- **Progressive Testing**: Unit → Integration → Cross-Implementation → User Acceptance
- **Accessibility First**: WCAG AA compliance verified at each stage
- **Performance Validation**: Response time and resource usage within budgets
- **Security Testing**: Input validation, API security, data protection

## 1) Test Categories & Coverage

### 1.1 Unit Tests (Per Implementation)
**Scope**: Individual functions and components in isolation
**Coverage Target**: 90%+ for core methodology logic
**Tools**: 
- v1: Jest or Vitest for JavaScript
- v2: pytest for Python
- v3: Jest + React Testing Library

### 1.2 Integration Tests (Per Implementation)
**Scope**: Component interactions, API integrations, storage operations
**Coverage Target**: All user workflows end-to-end
**Tools**: 
- v1: Playwright for browser automation
- v2: pytest with async testing
- v3: Cypress or Playwright

### 1.3 Cross-Implementation Tests
**Scope**: Methodology consistency, output compatibility
**Coverage Target**: 100% of shared functionality
**Tools**: Shared JSON test fixtures, custom validation scripts

### 1.4 Accessibility Tests
**Scope**: WCAG AA compliance, keyboard navigation, screen readers
**Coverage Target**: All user interfaces
**Tools**: axe-core, WAVE, manual testing with screen readers

### 1.5 Performance Tests
**Scope**: Response times, memory usage, bundle sizes
**Coverage Target**: All performance requirements
**Tools**: Lighthouse, WebPageTest, custom benchmarks

## 2) Requirement Validation Matrix

| Requirement ID | Test Type | Validation Method | Success Criteria | Test Location |
|---|---|---|---|---|
| R-F-001 | Unit + Integration | Automated test suite | All 4 phases present and navigable | `tests/methodology/phases.test.*` |
| R-F-002 | Unit + Integration | Question count validation | Exactly 15 questions across phases | `tests/methodology/questions.test.*` |
| R-F-003 | Unit | Output generation test | Valid Markdown produced | `tests/output/markdown.test.*` |
| R-F-004 | Unit | JSON schema validation | Valid JSON against schema | `tests/output/json.test.*` |
| R-F-005 | Unit | AI prompt generation | Structured prompt format | `tests/output/ai-prompt.test.*` |
| R-F-006 | Integration | Session persistence test | Save/restore functionality | `tests/session/persistence.test.*` |
| R-F-007 | Unit | Input validation test | Invalid inputs rejected | `tests/validation/input.test.*` |
| R-F-008 | Integration | Navigation test | Phase navigation works | `tests/navigation/phases.test.*` |
| R-N-SEC-001 | Unit + Integration | Security test suite | Input validation enforced | `tests/security/validation.test.*` |
| R-N-SEC-002 | Static Analysis | Code scanning | No secrets in source | CI/CD pipeline check |
| R-N-SEC-003 | Integration | API rate limiting test | Rate limits enforced | `tests/api/rate-limiting.test.*` |
| R-N-PERF-001 | Performance | Response time test | <2s phase transitions | `tests/performance/transitions.test.*` |
| R-N-PERF-002 | Performance | Output generation test | <5s output generation | `tests/performance/output.test.*` |
| R-N-PERF-003 | Performance | Session operation test | <1s save/restore | `tests/performance/session.test.*` |
| R-N-REL-001 | Integration | Offline functionality test | Works without internet | `tests/reliability/offline.test.*` |
| R-N-REL-002 | Integration | AI failure handling test | Graceful degradation | `tests/reliability/ai-failure.test.*` |
| R-N-REL-003 | Integration | Data persistence test | Survives restarts | `tests/reliability/persistence.test.*` |
| R-N-UX-001 | Accessibility | WCAG AA audit | Passes accessibility scan | `tests/accessibility/wcag.test.*` |
| R-N-UX-002 | Accessibility | Keyboard navigation test | Full keyboard access | `tests/accessibility/keyboard.test.*` |
| R-N-UX-003 | Integration | Progress indicator test | Shows completion status | `tests/ui/progress.test.*` |
| R-N-UX-004 | Integration | Error handling test | Clear error messages | `tests/ui/errors.test.*` |

## 3) Test Data & Fixtures

### 3.1 Shared Test Data
**Location**: `tests/fixtures/`
**Contents**:
- `methodology-schema.json`: Reference schema for validation
- `sample-sessions.json`: Complete and partial session examples
- `test-questions.json`: Question definitions with validation rules
- `expected-outputs/`: Reference outputs for each format

### 3.2 Cross-Implementation Test Cases
```json
{
  "testCase": "complete-session-flow",
  "description": "User completes all 4 phases with valid inputs",
  "input": {
    "clarify": {"answers": ["Project management tool", "Small teams", "Productivity"]},
    "organize": {"answers": ["Task tracking", "Team collaboration", "Reporting"]},
    "refine": {"answers": ["Web application", "React + Node.js", "6 months"]},
    "equip": {"answers": ["MVP features", "Technical documentation", "Deployment plan"]}
  },
  "expectedOutput": {
    "phases": 4,
    "questionsAnswered": 15,
    "outputFormats": ["markdown", "json", "ai-prompt"],
    "sessionComplete": true
  }
}
```

## 4) Acceptance Criteria

### 4.1 Functional Acceptance
- [ ] All 15 questions (5-5-5) plus 4 actions are presented correctly
- [ ] Users can navigate between phases and edit previous answers
- [ ] All three output formats generated: Markdown (title/timestamp/Q&A/Next Steps), JSON (framework/project/ai_conversations), AI prompt (intro/context/deliverables)
- [ ] Session state persists with id/name/description/answers/ai_conversations
- [ ] AI integration works with both OpenRouter and Ollama
- [ ] Phase-specific AI guidance probes for better answers and refines scope

### 4.2 Non-Functional Acceptance
- [ ] Phase transitions complete within 2 seconds
- [ ] Output generation completes within 5 seconds
- [ ] Session operations complete within 1 second
- [ ] Target completion times: Quick (10-15 min), Standard (15-30 min), Deep (45-60 min)
- [ ] All implementations pass WCAG AA accessibility audit
- [ ] Full keyboard navigation works without mouse
- [ ] v1 bundle size <100KB for zero-setup deployment

### 4.3 Success Metrics Acceptance
- [ ] >60% completion rate to EQUIP phase
- [ ] >12/15 questions answered per session
- [ ] >80% export usage rate (at least one format downloaded)
- [ ] AI chat engagement >5 interactions per session
- [ ] Average answer length >100 characters
- [ ] Session completion time 30-90 minutes
- [ ] Cross-implementation methodology consistency verified

## 5) Test Automation Strategy

### 5.1 Continuous Integration
**Pipeline**: GitHub Actions
**Triggers**: Pull requests, main branch pushes
**Stages**:
1. **Lint & Format**: Code quality checks
2. **Unit Tests**: Fast feedback on core logic
3. **Integration Tests**: Full workflow validation
4. **Security Scan**: Dependency and code security
5. **Performance Tests**: Regression detection
6. **Accessibility Tests**: WCAG compliance
7. **Cross-Implementation**: Consistency validation

### 5.2 Test Environment Matrix
| Implementation | Environment | Browser/Runtime | Test Scope |
|---|---|---|---|
| v1 HTML | Chrome, Firefox, Safari | Latest 2 versions | Full suite |
| v1 HTML | Mobile browsers | iOS Safari, Chrome Mobile | Responsive tests |
| v2 Python | Linux, macOS, Windows | Python 3.14+ | Full suite |
| v3 React | Chrome, Firefox, Safari | Latest 2 versions | Full suite |
| v3 React | Node.js | 18+, 20+ | Build and unit tests |

## 6) Manual Testing Checklist

### 6.1 User Experience Testing
- [ ] First-time user can complete methodology without guidance
- [ ] Error messages are clear and actionable
- [ ] Progress indicators accurately reflect completion
- [ ] Generated outputs are useful and well-formatted
- [ ] Session restoration works as expected

### 6.2 Accessibility Testing
- [ ] Screen reader announces all content correctly
- [ ] All interactive elements are keyboard accessible
- [ ] Focus indicators are visible and logical
- [ ] Color contrast meets WCAG AA standards
- [ ] Text can be zoomed to 200% without horizontal scrolling

### 6.3 Edge Case Testing
- [ ] Very long text inputs are handled gracefully
- [ ] Network interruptions during AI calls are handled
- [ ] Browser storage quota exceeded scenarios
- [ ] Rapid navigation between phases
- [ ] Multiple browser tabs with same session

## 7) Performance Benchmarks

### 7.1 Response Time Targets
- **Phase Navigation**: <2 seconds (P95)
- **Output Generation**: <5 seconds (P95)
- **Session Save/Restore**: <1 second (P95)
- **Initial Load**: <3 seconds (P95)

### 7.2 Resource Usage Targets
- **v1 Bundle Size**: <100KB total
- **v2 Memory Usage**: <50MB peak
- **v3 Initial Bundle**: <500KB
- **v3 Total Bundle**: <2MB

### 7.3 Benchmark Test Suite
**Location**: `tests/benchmarks/`
**Tools**: Custom timing harnesses, Lighthouse CI
**Frequency**: Every release, performance regression detection

## 8) Security Testing

### 8.1 Input Validation Testing
- [ ] XSS prevention in all user inputs
- [ ] SQL injection prevention (v3 database)
- [ ] File upload validation (if applicable)
- [ ] API parameter validation
- [ ] Schema validation enforcement

### 8.2 API Security Testing
- [ ] Rate limiting effectiveness
- [ ] API key protection
- [ ] CORS configuration validation
- [ ] Error message information disclosure
- [ ] Authentication bypass attempts

## 9) Test Reporting

### 9.1 Coverage Reports
- **Unit Test Coverage**: Per-implementation and combined
- **Integration Test Coverage**: User workflow coverage
- **Accessibility Coverage**: WCAG checkpoint compliance
- **Performance Coverage**: All performance requirements tested

### 9.2 Test Results Dashboard
- **Real-time Status**: Current test suite status
- **Historical Trends**: Performance and reliability over time
- **Cross-Implementation Matrix**: Consistency validation results
- **Accessibility Scorecard**: WCAG compliance tracking

## 10) Definition of Done (Testing)
- [ ] All requirements have corresponding automated tests
- [ ] Cross-implementation consistency validated
- [ ] Performance benchmarks meet targets
- [ ] Accessibility compliance verified
- [ ] Security testing completed with no high-severity issues
- [ ] Manual testing checklist completed
- [ ] Test automation integrated into CI/CD pipeline

> **LLM usage note**: Execute all relevant tests before marking any requirement as complete. Prioritize cross-implementation consistency and accessibility compliance in all testing activities.
