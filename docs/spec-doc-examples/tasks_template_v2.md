# {PROJECT_NAME} — Tasks (Template)

**Status**: Draft  •  **Version**: 0.1  •  **Last updated**: 2025-11-09  
**Owners**: {OWNER_NAMES}  •  **Repo**: {REPO_URL}

> **Purpose**: Provide an ordered, atomic task list that an LLM or human can execute deterministically. Every task maps to one or more requirement IDs and yields objective evidence.

---

## 0) Workflow Conventions
- **Branching**: `feat/{short-slug}` / `fix/{short-slug}` per task group.  
- **Commits**: Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `test:`). Small, focused diffs.  
- **PRs**: One logical change per PR; include checklists and links to requirements and validations.  
- **Coding standards**: Lint/format/type-check must pass locally and on CI before requesting review.  
- **Security baseline**: No plaintext secrets; input validation at boundaries; dependency updates pinned and audited.

## 1) Environment Detection (auto by assistant)
Detect the ecosystem and choose the correct toolchain:
- Node.js: `npm ci && npm run lint && npm test`
- Python: `pip install -r requirements.txt && ruff . && pytest -q`
- Go: `go vet ./... && go test ./...`
- Java: `mvn -q -DskipTests=false test`
> If multiple ecosystems exist, operate only within the target subproject path: `{SUBDIR}`.

## 2) Task Records
> Use this schema for each atomic task. Keep tasks <= half-day of work and independently verifiable.

```
T-{###}: {TITLE}
Maps to: R-{IDs comma-separated}
Component(s): C-{IDs}
Description: {WHAT to change/build and WHY in one paragraph}
Files/Paths: {relative paths or globs}
Definition of Done:
  - {observable outcome 1}
  - {observable outcome 2}
Evidence to Produce:
  - Tests: {paths or new test names}
  - Logs/Artifacts: {coverage report path, screenshots, build artifact}
Risk Level: Low/Med/High (with brief reason)
Rollback Plan: {how to revert safely}
Implementation Notes:
  - {edge cases, invariants, error handling}
Commands (template):
  - {build/test/lint commands}
```

### Example skeleton entries
- T-001: Bootstrap CI to enforce lint, type-check, test, and security audit.  
  Maps to: R-N-SEC-001, R-N-REL-001  
  DoD: CI fails on medium+ vulnerabilities or failing tests; artifacts uploaded.

- T-002: Implement endpoint `GET /v1/items` with pagination and input validation.  
  Maps to: R-F-001, R-N-SEC-001, R-N-PERF-001  
  Evidence: Unit tests for validation, integration test for pagination, load test script stub.

## 3) Iteration Loop (Assistant-Operable)
1. **Plan**: Choose the smallest next task that increases validated value.
2. **Change**: Apply minimal patch; prefer editing existing code over rewrites.
3. **Build & Test**: Run format/lint/tests and security audit.
4. **Evaluate**: Compare outcomes to DoD/Evidence; if unmet, iterate; else commit.
5. **Commit**: Conventional message referencing IDs (e.g., `feat: add paginated GET /v1/items (R-F-001, R-N-SEC-001)`).
6. **Open PR**: Use PR template below; link to requirement IDs and validations.

## 4) PR Template (Paste into PR body)
```
## Summary
{what/why}

## Linked Requirements
- R-...

## Validation Evidence
- Tests: {links to files and CI run}
- Coverage: {% summary}
- Security: {SAST/DAST results summary}
- Performance: {baseline comparisons}

## Risk & Rollback
{impact, migration plan, fallback}

## Checklist
- [ ] Lint/format/type-check pass
- [ ] Unit/Integration/E2E pass
- [ ] No new high severity vulns
- [ ] Docs/CHANGELOG updated
```

> **LLM usage note**: Never skip tests or linters. If a gate fails, stop and fix before proceeding. Prefer additive tests before code changes when feasible (red → green).
