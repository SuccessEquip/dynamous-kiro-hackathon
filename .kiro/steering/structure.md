# Project Structure

## Directory Layout
**Multi-Version Project Structure:**
```
CORE-ProjectPlanningFramework/
├── v1-html/                    # Single-file web implementation
│   ├── index.html             # Complete standalone app
│   ├── README.md              # v1-specific documentation
│   └── demo/                  # Example sessions and screenshots
├── v2-python/                 # Python TUI implementation
│   ├── core_framework/        # Main package
│   │   ├── __init__.py
│   │   ├── core.py           # COREFramework class
│   │   ├── ai_handler.py     # AIHandler class
│   │   ├── screens/          # TUI screen components
│   │   └── utils/            # Helper functions
│   ├── tests/                # Unit and integration tests
│   ├── requirements.txt      # Python dependencies
│   ├── setup.py             # Package configuration
│   └── README.md            # v2-specific documentation
├── v3-react/                 # React + Supabase implementation
│   ├── frontend/             # React SPA
│   │   ├── src/
│   │   │   ├── components/   # React components
│   │   │   ├── hooks/        # Custom React hooks
│   │   │   ├── lib/          # Utilities and API clients
│   │   │   └── styles/       # Tailwind + shadcn styles
│   │   ├── public/           # Static assets
│   │   └── package.json      # Frontend dependencies
│   ├── supabase/             # Backend configuration
│   │   ├── migrations/       # Database schema
│   │   └── functions/        # Edge functions
│   ├── docker-compose.yml    # Optional containerization
│   └── README.md            # v3-specific documentation
├── shared/                   # Common resources
│   ├── methodology/          # CORE Framework documentation
│   ├── examples/            # Sample sessions and outputs
│   └── assets/              # Shared images and resources
├── docs/                    # Project documentation
│   ├── api/                 # API documentation (v3)
│   ├── user-guide/          # User documentation
│   └── development/         # Development guides
├── .kiro/                   # Kiro CLI configuration
│   ├── steering/            # Project context documents
│   ├── prompts/             # Custom development prompts
│   └── agents/              # Custom AI agents
└── README.md               # Main project documentation
```

## File Naming Conventions
**Cross-Version Standards:**
- **Components**: PascalCase (React), snake_case (Python), kebab-case (HTML)
- **Files**: snake_case for Python, kebab-case for config, camelCase for JS/TS
- **Directories**: kebab-case for public, snake_case for internal
- **Constants**: UPPER_SNAKE_CASE across all versions
- **Classes**: PascalCase (COREFramework, AIHandler, SessionManager)

## Module Organization
**Version-Specific Patterns:**
- **v1**: Single-file with clear section comments and modular functions
- **v2**: Class-based architecture with separate concerns (UI, logic, AI, storage)
- **v3**: Component-based React with custom hooks and service layers
- **Shared**: Common methodology logic abstracted for reuse

## Configuration Files
**Environment and Build Configuration:**
- **v1**: No build process, configuration via HTML meta tags
- **v2**: `requirements.txt`, `setup.py`, `config.json` for settings
- **v3**: `package.json`, `tailwind.config.js`, `supabase/config.toml`
- **Shared**: `.gitignore`, `LICENSE`, `CONTRIBUTING.md`

## Documentation Structure
**Comprehensive Documentation Strategy:**
- **README.md**: Main project overview and quick start
- **Version READMEs**: Implementation-specific setup and usage
- **docs/user-guide/**: End-user documentation with screenshots
- **docs/api/**: API documentation for v3 backend
- **docs/development/**: Contributing guidelines and architecture decisions
- **shared/methodology/**: CORE Framework methodology documentation

## Asset Organization
**Shared and Version-Specific Assets:**
- **shared/assets/**: Common images, icons, and branding
- **v1**: Inline CSS and minimal assets
- **v2**: Terminal-based, no visual assets needed
- **v3**: `frontend/public/` for static assets, `src/assets/` for bundled resources

## Build Artifacts
**Version-Specific Build Outputs:**
- **v1**: No build process, direct file serving
- **v2**: Python package distribution via `setup.py`
- **v3**: React build output in `frontend/dist/`, Docker images
- **Documentation**: Generated API docs, user guides

## Environment-Specific Files
**Multi-Environment Configuration:**
- **Development**: Local config files, development databases
- **Testing**: Test-specific configurations and mock data
- **Production**: Environment variables, production builds
- **Docker**: Container-specific environment files and health checks
