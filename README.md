# CORE Framework - Interactive Project Planning Tools

🚀 **Transform vague ideas into actionable project plans** through a structured 4-phase, 15-question methodology with multiple implementation options.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Kiro CLI](https://img.shields.io/badge/Built%20with-Kiro%20CLI-blue)](https://kiro.dev)

> **📖 New to Kiro?** Check out [kiro-guide.md](kiro-guide.md) to understand how this project leverages Kiro CLI for development.

## About the Hackathon

The **Kiro Hackathon** is a coding competition where developers build real-world applications using the Kiro CLI. Show off your AI-powered development skills and compete for **$17,000 in prizes**.

- **📅 Dates**: January 5-23, 2026
- **💰 Prize Pool**: $17,000 across 10 winners
- **🎯 Theme**: Open - build anything that solves a real problem
- **🔗 More Info**: [dynamous.ai/kiro-hackathon](https://dynamous.ai/kiro-hackathon)

## What is CORE Framework?

CORE Framework is an interactive project planning tool that guides you through a structured methodology to transform vague ideas into comprehensive, actionable project plans. Whether you're a solo entrepreneur, developer, or small team, CORE helps you:

- **Clarify** your project vision and goals
- **Organize** features and requirements systematically  
- **Refine** risks, constraints, and success metrics
- **Equip** yourself with implementation-ready documentation

### Three Implementation Options

Choose the version that fits your workflow:

| Version | Technology | Best For | Status |
|---------|-----------|----------|--------|
| **v1** | HTML/CSS/JS | Quick prototyping, static hosting | ✅ Complete |
| **v2** | Python TUI | CLI enthusiasts, terminal workflows | ✅ Complete |
| **v3** | React + Supabase | Production apps, cloud sync | ✅ Complete |

All versions share the same proven 4-phase, 15-question methodology and generate identical output formats (Markdown, JSON, AI prompts).

## What's Included

This template provides everything you need to get started:

- **📋 Steering Documents**: Pre-configured project templates (product.md, tech.md, structure.md)
- **⚡ Custom Prompts**: 11 powerful development workflow prompts
- **📖 Examples**: Sample README and DEVLOG showing best practices
- **🏆 Hackathon Tools**: Specialized code review prompt for submission evaluation

## Quick Start

**New here?** Check out [QUICKSTART.md](QUICKSTART.md) for a detailed getting-started guide!

### Easy Launch (Recommended)

Use the cross-platform launcher to automatically check dependencies and start any version:

**Windows:**
```cmd
# Command Prompt
launch.bat

# PowerShell
.\launch.ps1
```

**macOS/Linux:**
```bash
./launch.sh
```

The launcher will:
- Check for required dependencies (Python, Node.js)
- Create a virtual environment for Python (v2)
- Install missing packages automatically
- Open the appropriate interface for each version

### Manual Setup

### Prerequisites
- **Kiro CLI**: Install from [kiro.dev](https://kiro.dev) (for contributors only)
- **Node.js 18+**: For v3 React implementation
- **Python 3.8+**: For v2 Python TUI
- **Modern Browser**: For v1 HTML version

### 1. Clone This Repository
```bash
git clone https://github.com/SuccessEquip/dynamous-kiro-hackathon.git
cd dynamous-kiro-hackathon
```

### 2. Choose Your Implementation

#### v1: HTML/CSS/JS (Simplest - No Installation)
```bash
cd v1-html
open index.html  # or double-click in file explorer
```

#### v2: Python TUI (Terminal Interface)
```bash
cd v2-python
pip install -r requirements.txt
python -m core_framework.main
```

#### v3: React + Supabase (Full-Featured)
```bash
cd v3-react/frontend
npm install
npm run dev
# Visit http://localhost:5173
```

See [QUICKSTART.md](QUICKSTART.md) for detailed instructions and [version-specific READMEs](v1-html/README.md) for advanced configuration.

### 3. Start Planning
1. Create a new session with your project title
2. Answer questions through the 4 phases (Clarify → Organize → Refine → Equip)
3. Generate comprehensive documentation
4. Export in your preferred format (Markdown, JSON, AI prompt)

---

## For Contributors

This project was built for the Kiro Hackathon. If you're contributing to development:

### Initial Setup (One-Time)
1. **Complete setup**: Run `@quickstart` to configure your project

### Core Development Cycle (Every Feature/Session)

### Phase 1: Setup & Planning
1. **Load context**: Use `@prime` to understand your codebase
2. **Plan features**: Use `@plan-feature` for comprehensive planning

### Phase 2: Build & Iterate
1. **Implement**: Use `@execute` to build features systematically
2. **Review**: Use `@code-review` to maintain code quality
3. **Document**: Update your DEVLOG.md as you work
4. **Optimize**: Customize your `.kiro/` configuration for your workflow

### Phase 3: Submission Preparation
1. **Final review**: Run `@code-review-hackathon` for submission evaluation
2. **Polish documentation**: Ensure README.md and DEVLOG.md are complete
3. **Verify requirements**: Check all submission criteria are met

## Submission Requirements

Your submission will be judged on these criteria (100 points total):

### Application Quality (40 points)
- **Functionality & Completeness** (15 pts): Does it work as intended?
- **Real-World Value** (15 pts): Does it solve a genuine problem?
- **Code Quality** (10 pts): Is the code well-structured and maintainable?

### Kiro CLI Usage (20 points)
- **Effective Use of Features** (10 pts): How well did you leverage Kiro CLI?
- **Custom Commands Quality** (7 pts): Quality of your custom prompts
- **Workflow Innovation** (3 pts): Creative use of Kiro CLI features

### Documentation (20 points)
- **Completeness** (9 pts): All required documentation present
- **Clarity** (7 pts): Easy to understand and follow
- **Process Transparency** (4 pts): Clear development process documentation

### Innovation (15 points)
- **Uniqueness** (8 pts): Original approach or solution
- **Creative Problem-Solving** (7 pts): Novel technical solutions

### Presentation (5 points)
- **Demo Video** (3 pts): Clear demonstration of your project
- **README** (2 pts): Professional project overview

## Required Documentation

Ensure these files are complete and high-quality:

### README.md
- Clear project description and value proposition
- Prerequisites and setup instructions
- Architecture overview and key components
- Usage examples and troubleshooting

*There's a lot of freedom for how you can structure this. Just make sure that it's easy for someone viewing this to know exactly what your project is about and how to run it themselves. This is the main criteria that explains the project clearly and how to test it in a local environment.*

### DEVLOG.md
- Development timeline with key milestones
- Technical decisions and rationale
- Challenges faced and solutions implemented
- Time tracking and Kiro CLI usage statistics

*There's a lot of freedom in how you structure this too. It's up to you how you want to document your timeline, milestones, decisions made, challenges you encounter, and all those kinds of things. Feel free to use Kiro to help you maintain your devlog as you're working on the project. Hint: create a Kiro prompt to help you update your log based on what's happening.*

### .kiro/ Directory
- **Steering documents**: Customized for your project
- **Custom prompts**: Workflow-specific commands
- **Configuration**: Optimized for your development process

*This template provides a good starting point with prompts, and the wizard helps you set up your initial steering documents. However, it's encouraged for you to continue to customize things and refine it as you're working on your project.*

## Available Prompts

This template includes 11 powerful development prompts:

### Core Development
- **`@prime`** - Load comprehensive project context
- **`@plan-feature`** - Create detailed implementation plans
- **`@execute`** - Execute plans with systematic task management
- **`@quickstart`** - Interactive project setup wizard

### Quality Assurance
- **`@code-review`** - Technical code review for quality and bugs
- **`@code-review-hackathon`** - Hackathon submission evaluation
- **`@code-review-fix`** - Fix issues found in code reviews
- **`@system-review`** - Analyze implementation vs plan

### Documentation & Planning
- **`@create-prd`** - Generate Product Requirements Documents
- **`@execution-report`** - Generate implementation reports
- **`@rca`** - Root cause analysis for issues
- **`@implement-fix`** - Implement fixes based on analysis

## Examples

Check the `examples/` folder for:
- **README.md**: Professional project documentation example
- **DEVLOG.md**: Comprehensive development log example

These examples show the level of detail and professionalism expected for hackathon submissions.

## Tips for Success

### Maximize Your Score
1. **Use Kiro CLI extensively** - It's 20% of your score
2. **Document everything** - Process documentation is 20% of your score
3. **Build something useful** - Real-world value is heavily weighted
4. **Optimize your workflow** - Custom prompts and steering documents matter

### Development Best Practices
- **Start with `@quickstart`** to set up your foundation properly
- **Use `@prime`** at the start of every new conversation to quickly catch the coding assistant up to speed on what has been built in the project already
- **Update your DEVLOG.md** continuously, not just at the end
- **Customize your `.kiro/` configuration** as you learn your workflow
- **Run `@code-review-hackathon`** periodically to compare your project against the judging rubric and before submitting

## Getting Help

- **Kiro CLI Documentation**: [kiro.dev/docs/cli](https://kiro.dev/docs/cli)
- **Hackathon Community**: Join the Dynamous community for support
- **Built-in Help**: Use `/help` in Kiro CLI for command assistance

---

**Ready to build something amazing?** Run `@quickstart` and let's get started! 🚀
