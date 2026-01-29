# {PROJECT_NAME} — Requirements (Template)

**Status**: Draft  •  **Version**: 0.1  •  **Last updated**: 2025-11-09  
**Owners**: {OWNER_NAMES}  •  **Repo**: {REPO_URL}

> **Purpose**: Specify clear, testable requirements that drive deterministic tasks and validations. Use atomic statements. Map every task and validation back to these IDs.

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
Short, precise definitions for domain terms to reduce ambiguity.

## 2) Functional Requirements
> Use imperative, testable language. Include rationale and explicit acceptance criteria.

| ID | Statement | Rationale | Priority | Related Components | Acceptance criteria (Given/When/Then) |
|---|---|---|---|---|---|
| R-F-001 | {The system SHALL ...} | {WHY} | MUST | C-01,C-03 | Given {context} When {action} Then {observable} |

## 3) Non-Functional Requirements
### 3.1 Security
- R-N-SEC-001: {All external inputs are validated against strict schemas; invalid inputs are rejected with 4xx and logged without sensitive data.} — **Verify**: unit+integration tests, fuzzing, SAST/DAST.
- R-N-SEC-002: {AuthZ is role/scope-based with least privilege; admin endpoints require MFA.} — **Verify**: policy tests, e2e.

### 3.2 Performance
- R-N-PERF-001: {P95 request latency < {ms} at {QPS} on {baseline hardware}.} — **Verify**: load test.

### 3.3 Reliability
- R-N-REL-001: {Idempotent retries for create/update operations with 30s timeout and backoff.} — **Verify**: chaos/integration tests.

### 3.4 Usability & Accessibility
- R-N-UX-001: {Meets WCAG 2.2 AA for interactive surfaces.} — **Verify**: a11y test suite + manual checklist.

## 4) Constraints & Assumptions
- Platform/runtime versions, supported browsers/OS, storage limits, legal/regulatory constraints.
- Assumptions that must be validated during implementation.

## 5) Dependencies
- External APIs/services and their SLAs. Include failure behavior and fallbacks.

## 6) Out of Scope
- Explicit anti-requirements to prevent scope creep.

## 7) Traceability
- **Requirement → Task(s)**: Filled in in `tasks.md`  
- **Requirement → Validation(s)**: Filled in in `validation.md`
- **Coverage checkpoint**: No requirement without at least one task and one validation.

## 8) Change Control
- Proposed change format, approvers, and impact analysis template.

> **LLM usage note**: Treat IDs as canonical. Do not invent new requirements; propose changes via a PR to this file with impact analysis.
