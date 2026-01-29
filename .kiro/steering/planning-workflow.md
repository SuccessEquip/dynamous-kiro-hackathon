# Planning & Workflow Standards

## Planning & Iteration Workflow

### When to Use Plan Mode

| Use Plan Mode | Skip Plan Mode |
|---------------|----------------|
| New features | Single-line fixes |
| Multi-file changes | Typo corrections |
| Database migrations | Simple renames |
| Architectural decisions | Adding debug statements |
| Bug fixes requiring investigation | Obvious one-liner bugs |

### Plan Mode Process

1. **Explore** - Understand existing patterns, identify all affected files
2. **Clarify** - Ask questions to resolve ambiguities before coding
3. **Document** - Write plan file with:
   - Problem statement / root cause
   - Solution approach with rationale
   - Implementation steps with file paths
   - Migration safety analysis (if applicable)
   - Verification steps
   - Commit strategy
4. **Approve** - Exit plan mode only after plan is solid

### Execution Process

1. Create **todo list** to track progress visibly
2. Mark tasks `in_progress` before starting, `completed` immediately after
3. Run **build and tests** after changes
4. Commit atomically as logical units complete

### Investigation Process

When issues arise:
- Use git history (`git log`, `git show`, `git diff`) to find root cause
- Identify what changed and when
- Update plan if scope changes

## Atomic Commits & Rollback

### Commit Philosophy

Each commit must be:
- **Single-purpose** - One logical change
- **Self-contained** - Doesn't break the build alone
- **Descriptive** - Clear message explaining what and why

### Conventional Commits Format

```
type(scope): short description

- What changed
- Why it changed
- References to issues or prior commits

Co-Authored-By: Kiro <assistant>
```

### Commit Types

| Type | Use |
|------|-----|
| `feat` | New functionality |
| `fix` | Bug fixes |
| `refactor` | Code changes without behavior change |
| `docs` | Documentation only |
| `test` | Adding/updating tests |
| `chore` | Maintenance, dependencies |
| `perf` | Performance improvements |

### Commit Sequencing

For multi-part features:
```
1. feat(ui): add shared component
2. feat(db): add migration
3. feat(api): add backend logic
4. feat(feature): wire up frontend
5. test(feature): add tests
```

## Git Workflow

### Branch Model

```
main ────────────────── Production (auto-deploys)
  │
  └── staging ────────── Pre-production (auto-deploys)
        │
        └── dev ──────── Active development
```

### Branch Rules

| Branch | Purpose | Stability |
|--------|---------|-----------|
| `main` | Production-ready | Must always work |
| `staging` | Pre-production testing | Should work |
| `dev` | Active development | May be unstable |

### Workflow Commands

```bash
# Start work
git checkout dev && git pull origin dev

# Commit
git add -A && git commit -m "type(scope): description"

# Promote to staging
git push origin dev
git checkout staging && git merge dev && git push origin staging

# Promote to production
git checkout main && git merge staging && git push origin main

# Rollback
git revert <commit-hash>
```

### Branch Protection (Recommended)

| Branch | Rules |
|--------|-------|
| `main` | Require PR, reviews, CI pass |
| `staging` | Require CI pass |
| `dev` | No restrictions |

## Deployment Pipeline

### Environment Mapping

| Branch | Environment |
|--------|-------------|
| `dev` | Local |
| `staging` | Staging server |
| `main` | Production |

### Deployment Checklist

- [ ] Tests pass
- [ ] Build succeeds
- [ ] Staging tested manually
- [ ] Database migrations deployed (if any)
- [ ] Backend/functions deployed (if any)
- [ ] Environment variables configured
- [ ] Rollback plan identified

**Order matters**: Deploy migrations BEFORE code that depends on them.

## Quick Reference

### Investigation Commands
```bash
git log --oneline -20
git show <commit>
git diff <branch1>..<branch2>
git bisect start && git bisect bad && git bisect good <hash>
```

### Deployment Commands
```bash
# Check project steering documents for specific commands
git push origin staging  # Auto-deploys to staging
git push origin main     # Auto-deploys to production
```
