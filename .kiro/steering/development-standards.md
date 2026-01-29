# Development Standards & Workflow

## Critical Rules

**NEVER ASSUME OR GUESS** - Ask for clarification when uncertain
**NEVER COMMIT SECRETS** - Respect .gitignore, use environment variables
**NO EMOJIS** - Unless explicitly instructed by user
**EVIDENCE-BASED CHANGES** - All plans, fixes, or changes require explicit evidence that they are:
1. The best options for the situation
2. Aligned with best practices (KISS, YAGNI, DRY, SRP, etc.)
3. Consistent with project principles and philosophy
4. Include structured commit plans and rollback steps

## Core Design Principles

### KISS (Keep It Super Simple)
- Choose straightforward solutions over complex ones
- Simple, elegant solutions are easier to understand, maintain, and debug
- Prioritize clarity and maintainability

### YAGNI (You Aren't Gonna Need It)
- Avoid building functionality on speculation
- Implement features only when needed, not when anticipated
- Focus on current requirements

### DRY (Don't Repeat Yourself)
- Avoid code duplication
- Extract common functionality into reusable components
- Extract shared patterns into reusable code

### Single Responsibility Principle (SRP)
- Functions and classes should do one thing well
- Each component should have only one reason to change
- Maintain clear separation of concerns

### Dependency Inversion
- Depend on abstractions, not concretions
- Use interfaces and dependency injection
- Enable flexible, testable architecture

### Open/Closed Principle
- Open for extension, closed for modification
- Design systems for extensibility without changing existing code
- Use composition and configuration over modification

## Code Structure Heuristics

**Primary Objective**: Generate logical and maintainable code prioritizing clarity, cohesion, and SRP.

### Size Guidelines (Heuristics, not hard rules)
- **Functions**: ~50 lines max, single responsibility
- **Methods**: ~50 lines max within classes  
- **Classes**: ~300-400 lines max, single reason to change
- **Files**: ~500 lines max, single logical component

### Modularity Standards
- **High internal cohesion**: Related functionality grouped together
- **Low coupling**: Minimal dependencies between modules
- **Clear interfaces**: Well-defined boundaries between components
- **Feature-based organization**: Group code by business functionality

### Responsibility Guidelines
- **Functions**: One clear, testable responsibility
- **Classes**: Follow SRP - one reason to change
- **Files**: Single focused logical component
- **Modules**: Cohesive feature or domain area

## Quality Standards

### Comments & Documentation
- Explain **why**, not **what**
- Document public APIs using standard formats (JSDoc, docstrings, etc.)
- Add `# Reason:` comments for complex logic
- Keep documentation current with code changes

### Error Handling
- Catch specific exceptions, not generic ones
- Log errors with sufficient context for debugging
- User-facing messages: meaningful but no sensitive details
- Implement graceful degradation where possible

### Security Requirements
- **Input validation**: type, length, format, range checks
- **Output encoding**: escape based on context (HTML, SQL, etc.)
- **Authentication**: use established libraries, never roll your own
- **CORS**: explicit allowed origins configuration
- **Rate limiting**: implement for public APIs
- **Secrets management**: environment variables only, never in code

### Dependency Management
- Pin exact versions in production environments
- Regular security audits and updates
- Prefer actively maintained packages (commits in last 6 months)
- Use standard package managers for the ecosystem

### Performance Standards
- Profile before optimizing - measure, don't guess
- Implement appropriate caching strategies (memory, disk, CDN)
- Use async/await for I/O operations
- Database optimization: indexes, avoid N+1 queries, batch operations

## Testing Standards

### Test Location Strategy
Tests live **next to source files**, not in separate `tests/` directory:
```
src/
├── component.ext
├── component.test.ext
```
Follow ecosystem conventions when they strongly differ.

### Test Pattern (AAA)
```
// Arrange - Set up test data and conditions
// Act - Perform the action being tested
// Assert - Verify the expected outcome
```

### Testing Guidelines
- Write tests alongside implementation, not after
- Use descriptive names that explain the scenario
- Avoid mocks unless absolutely necessary
- Update tests when logic changes
- Aim for meaningful coverage, not just high percentages

## Operational Preferences

### Development Workflow
- Run lint and typecheck when available
- Use parallel operations when possible
- Prefer batch tool operations over sequential when practical
- Use incremental edits/diffs instead of rewriting entire files
- Assess available tools before responding

### File Maintenance Standards
- **README.md**: Update for configuration changes, new features, anything affecting user/developer experience
- **Steering Documents**: Add new dependencies, document important types and patterns, record key decisions
- **Documentation**: Keep current with code changes, include examples

### Investigation Process
When issues arise:
- Use git history (`git log`, `git show`, `git diff`) to find root cause
- Identify what changed and when
- Update plans if scope changes
- Document findings for future reference

## Code Review Standards

### Review Checklist
- [ ] Follows design principles (KISS, YAGNI, DRY, SRP)
- [ ] Meets code structure heuristics
- [ ] Includes appropriate error handling
- [ ] Has security considerations addressed
- [ ] Includes tests where appropriate
- [ ] Documentation is updated
- [ ] No secrets or sensitive data exposed

### Review Process
- Focus on architecture and design decisions
- Verify adherence to project standards
- Check for potential security issues
- Ensure maintainability and readability
- Validate test coverage and quality
