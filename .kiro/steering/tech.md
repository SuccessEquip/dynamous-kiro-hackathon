# Technical Architecture

## Technology Stack
**Multi-Implementation Progressive Architecture:**
- **v1 (HTML/CSS/JS)**: Single-file web app with LocalStorage persistence
- **v2 (Python TUI)**: Python 3.14 + Textual + Rich + aiohttp for AI integration
- **v3 (React/Supabase)**: React 19 + Tailwind + shadcn/ui frontend, Supabase backend
- **AI Integration**: OpenRouter API for enhanced planning assistance (v2/v3)
- **Storage**: LocalStorage (v1), JSON files (v2), Supabase + optional JSON export (v3)

## Architecture Overview
**Progressive Complexity Design:**
- **Shared Core**: Same 4-phase, 15-question methodology across all versions
- **v1**: Single-page application with in-memory state management
- **v2**: Screen-based TUI with COREFramework + AIHandler classes, async AI calls
- **v3**: React SPA frontend + Supabase backend with optional Docker deployment
- **Data Flow**: User input → Phase processing → Multi-format output (Markdown/JSON/AI prompts)

## Development Environment
**Version-Specific Requirements:**
- **v1**: Modern web browser, text editor, local web server for testing
- **v2**: Python 3.14, pip, terminal with Unicode support
- **v3**: Node.js 18+, npm/yarn, Supabase CLI, Docker (optional)
- **Shared**: Git, code editor with syntax highlighting, browser dev tools

## Code Standards
**Cross-Version Standards:**
- **Accessibility**: WCAG AA compliance, keyboard navigation, ARIA labels
- **Security**: No API keys in source, input validation, CORS configuration
- **Documentation**: Inline comments, README per version, API documentation
- **Naming**: Descriptive variables, consistent casing (camelCase JS, snake_case Python)
- **Error Handling**: Graceful degradation, user-friendly error messages

## Testing Strategy
**Comprehensive Testing Approach:**
- **Unit Tests**: Core methodology logic, data validation, output generation
- **Integration Tests**: AI API calls, storage operations, cross-component workflows
- **Accessibility Tests**: Screen reader compatibility, keyboard navigation
- **Browser Tests**: Cross-browser compatibility (latest 2 versions)
- **User Acceptance**: End-to-end workflow testing with target user personas

## Deployment Process
**Version-Specific Deployment:**
- **v1**: Static file hosting (GitHub Pages, Netlify, Vercel)
- **v2**: pip package distribution, direct Python execution
- **v3**: Frontend (Vercel/Netlify) + Supabase backend, optional Docker Compose
- **CI/CD**: Automated testing, security scanning, multi-environment deployment
- **Monitoring**: Error tracking, usage analytics, performance monitoring

## Performance Requirements
**Scalability & Speed:**
- **Response Time**: <2s for phase transitions, <5s for AI-assisted responses
- **Compatibility**: Windows/macOS/Linux (v2), modern browsers (v1/v3)
- **Offline Support**: Full functionality without AI features
- **Session Management**: Efficient state persistence and restoration
- **Resource Usage**: Minimal memory footprint, optimized bundle sizes

## Security Considerations
**Multi-Layer Security:**
- **API Security**: Environment variables for keys, rate limiting, input sanitization
- **Data Protection**: Local-first approach, optional cloud sync, no PII storage
- **CORS Policy**: Explicit origin allowlisting in production
- **Input Validation**: Client and server-side validation, XSS prevention
- **Authentication**: Supabase auth integration (v3), secure session management
