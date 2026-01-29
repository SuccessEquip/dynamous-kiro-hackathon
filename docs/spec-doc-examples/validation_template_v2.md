# {PROJECT_NAME} — Validation (Template)

**Status**: Draft  •  **Version**: 0.1  •  **Last updated**: 2025-11-09  
**Owners**: {OWNER_NAMES}  •  **Repo**: {REPO_URL}

> **Purpose**: Define objective checks that prove the system meets its requirements. Every requirement has at least one validation. Favor automated checks; document minimal manual steps when unavoidable.

---

## 0) Quality Gates (fail the build if unmet)
- **Static**: Lint/format/type-check clean; no secrets committed; license allowlist respected.  
- **Security**: 0 high/critical vulnerabilities; dependency audit passes; input validation tests present.  
- **Tests**: Unit + integration pass; coverage ≥ {TARGET}% on changed lines and ≥ {GLOBAL}% overall.  
- **Performance**: P95 latency within budget on baseline hardware; no >{X}% regression vs. previous main.  
- **Compliance/Accessibility**: WCAG AA checks pass for UI; privacy checks for data handling.

## 1) Validation Matrix
> Map requirements to validations. Each validation links to concrete artifacts.

| Requirement ID | Validation ID | Type | Description | Artifacts/Commands | Result |
|---|---|---|---|---|---|
| R-F-001 | V-UT-001 | Unit | Validate {function} behavior | `pytest -k test_x`; report: `/artifacts/unit.xml` | Pass/Fail |
| R-N-SEC-001 | V-SEC-DAST-001 | DAST | Validate input rejection | `{scan command}`; report: `/artifacts/dast.json` | Pass/Fail |

## 2) Test Plan
- **Unit**: fast, isolated; strict input validation and edge cases.  
- **Integration**: real I/O with ephemeral deps; idempotency and error paths.  
- **E2E/Smoke**: representative user flows; run in CI on PRs and on main.  
- **Security**: SAST/DAST/secret scan; fuzz critical parsers.  
- **Performance**: Lightweight load test with baseline comparison.  
- **Accessibility** (if UI): automated axe checks + manual keyboard navigation checklist.

## 3) Commands (fill per ecosystem)
```
# Node
npm ci && npm run lint && npm test -- --ci --reporters=jest-junit
# Python
pip install -r requirements.txt && ruff . && pytest -q --junitxml=artifacts/unit.xml
# Go
go vet ./... && go test ./... -json > artifacts/go-test.json
# Web a11y
npx @axe-core/cli http://localhost:{port} --exit 1
# Performance (example)
k6 run perf/script.js
```

## 4) Manual Validation (minimal; only where automation is insufficient)
- Step-by-step script with preconditions and expected outputs. Include screenshots or logs if applicable.

## 5) Failure Triage & Reporting
- **On failure**: Capture logs, artifacts, inputs; open issue with reproducible case using template below.
```
### Bug Report
Requirement(s): R-...
Observed: ...
Expected: ...
Repro steps: ...
Artifacts: links
Impact: ...
```
- **Severity**: Critical / High / Medium / Low with SLA to fix.

## 6) Definition of Done (Validation)
- All mapped validations pass in CI; quality gates met.  
- Evidence artifacts attached to PR.  
- No open Critical/High defects.  
- Human reviewer signs off (name/date).

> **LLM usage note**: Use this file to decide completion. If any mapped validation is missing or failing, you are **not done**. Generate missing tests before altering code when feasible.
