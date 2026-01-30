# CORE Framework - Quick Start Guide

Get started with CORE Framework in 5 minutes! Choose your preferred implementation and start planning your project.

## Easiest Way: Use the Launcher

The fastest way to get started is using the cross-platform launcher:

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
- Show a menu to choose your version
- Check for required dependencies
- Create a virtual environment for Python (v2)
- Install missing packages automatically
- Launch the selected version

**That's it!** Skip to [Using CORE Framework](#using-core-framework) below.

---

## Manual Setup (Alternative)

If you prefer manual setup or want more control:

## What is CORE Framework?

CORE Framework guides you through a structured 4-phase methodology to transform vague ideas into actionable project plans:

1. **Clarify** - Define your project vision and goals
2. **Organize** - Structure features and requirements
3. **Refine** - Analyze risks and constraints
4. **Equip** - Generate implementation documentation

## Choose Your Version

### v1: HTML/CSS/JS (Simplest - No Installation)

**Best for**: Quick start, no dependencies, works offline

```bash
# Option 1: Open directly in browser
cd v1-html
open index.html  # macOS
# or double-click index.html in file explorer

# Option 2: Use a local server
python -m http.server 8000
# Visit http://localhost:8000
```

**Features**:
- Single HTML file
- LocalStorage persistence
- Works completely offline
- No build process needed

---

### v2: Python TUI (Terminal Interface)

**Best for**: Developers who love the command line

**Prerequisites**: Python 3.8+

```bash
cd v2-python

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m core_framework.main
```

**Features**:
- Rich terminal interface
- Keyboard navigation
- JSON file export
- AI assistance (optional - requires OpenRouter API key)

**Keyboard Shortcuts**:
- `Tab` / `Shift+Tab` - Navigate fields
- `Ctrl+N` - Next phase
- `Ctrl+P` - Previous phase
- `Ctrl+S` - Save session
- `Ctrl+Q` - Quit

---

### v3: React + Supabase (Full-Featured)

**Best for**: Production use, cloud sync, team collaboration

**Prerequisites**: Node.js 18+

```bash
cd v3-react/frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Visit `http://localhost:5173` in your browser.

**Features**:
- Modern React UI
- Cloud storage with Supabase (optional)
- Real-time sync across devices
- Dark/light theme
- Mobile responsive

**Optional: Enable Cloud Sync**

1. Create a Supabase account at [supabase.com](https://supabase.com)
2. Create a new project
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Add your Supabase credentials to `.env`:
   ```
   VITE_SUPABASE_URL=your-project-url
   VITE_SUPABASE_ANON_KEY=your-anon-key
   ```
5. Restart the dev server

---

## Using CORE Framework

### Step 1: Create a Session

Enter your project title (e.g., "Mobile Fitness App" or "E-commerce Platform")

### Step 2: Answer Questions

Work through 4 phases with 15 strategic questions:

**Phase 1: Clarify (5 questions)**
- What problem does your project solve?
- Who are your target users?
- What makes your solution unique?
- What does success look like?
- What's your project scope?

**Phase 2: Organize (5 questions)**
- What are the essential features?
- What user types will you have?
- What's your MVP?
- How will you measure success?
- How will you prioritize features?

**Phase 3: Refine (5 questions)**
- What are the technical risks?
- What resource constraints exist?
- What market/adoption risks?
- How will you validate assumptions?
- What would trigger a pivot?

**Phase 4: Equip (Output Generation)**
- Generate comprehensive documentation
- Export in multiple formats

### Step 3: Generate Documentation

Click "Generate Output" to create:

- **Markdown** - Human-readable project documentation
- **JSON** - Structured data for tools/APIs
- **AI Prompt** - Ready-to-use prompt for AI coding assistants

### Step 4: Save and Export

- **v1**: Automatically saved to browser LocalStorage
- **v2**: Export as JSON file
- **v3**: Saved to cloud (if configured) or LocalStorage

---

## Example Workflow

```
1. Start CORE Framework
2. Create session: "Task Management App"
3. Phase 1 - Clarify:
   - Problem: Teams struggle with task coordination
   - Users: Small teams (5-10 people)
   - Unique: Real-time collaboration + AI prioritization
   - Success: 1000 active teams in 6 months
   - Scope: Web app, mobile later

4. Phase 2 - Organize:
   - Features: Task creation, assignments, comments, notifications
   - User types: Admin, Member, Guest
   - MVP: Basic task CRUD + assignments
   - Metrics: Daily active users, tasks completed
   - Priority: Core features first, AI later

5. Phase 3 - Refine:
   - Tech risks: Real-time sync complexity
   - Resources: 2 developers, 3 months
   - Market risks: Competitive space
   - Validation: Beta with 10 teams
   - Pivot triggers: <20% retention after 1 month

6. Phase 4 - Equip:
   - Generate comprehensive PRD
   - Export AI prompt for implementation
   - Save session for future reference
```

---

## Tips for Best Results

### Be Specific
❌ "Make money"  
✅ "Generate $10k MRR from 100 paying customers"

### Think Through Constraints
- Budget limitations
- Time constraints
- Technical expertise
- Market competition

### Define Success Clearly
- Quantifiable metrics
- Realistic timelines
- Clear milestones

### Consider Risks Early
- Technical challenges
- Resource limitations
- Market fit concerns

---

## Troubleshooting

### v1 (HTML)
**Issue**: Changes not saving  
**Solution**: Check browser LocalStorage is enabled

**Issue**: Page not loading  
**Solution**: Use a local server instead of file:// protocol

### v2 (Python)
**Issue**: Import errors  
**Solution**: Ensure you're in the v2-python directory and dependencies are installed

**Issue**: Terminal display issues  
**Solution**: Use a modern terminal with Unicode support

### v3 (React)
**Issue**: npm install fails  
**Solution**: Ensure Node.js 18+ is installed: `node --version`

**Issue**: Supabase connection fails  
**Solution**: Check .env file has correct credentials, restart dev server

---

## Next Steps

### After Planning
1. **Share** your documentation with team/stakeholders
2. **Use AI prompt** with coding assistants (Claude, ChatGPT, etc.)
3. **Iterate** - Come back and refine as you learn
4. **Track progress** - Update your plan as you build

### Advanced Features

**v2 Python**: Add OpenRouter API key for AI-assisted planning
**v3 React**: Enable Supabase for cloud sync and collaboration

---

## Getting Help

- **Documentation**: See version-specific READMEs
- **Issues**: Check GitHub issues or create a new one
- **Examples**: See `examples/` folder for sample sessions

---

## Quick Reference

| Task | v1 (HTML) | v2 (Python) | v3 (React) |
|------|-----------|-------------|------------|
| **Start** | Open index.html | `python -m core_framework.main` | `npm run dev` |
| **Save** | Automatic | Ctrl+S | Automatic |
| **Export** | Copy from output | JSON file | Copy/Download |
| **Navigate** | Click | Keyboard | Click/Keyboard |
| **Offline** | ✅ Yes | ✅ Yes | ✅ Yes (without cloud) |

---

**Ready to start planning?** Pick your version and create your first session! 🚀
