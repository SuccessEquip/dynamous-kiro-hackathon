# CORE Framework - Python TUI Implementation

Interactive Project Planning Tool with 4-phase methodology using Python and Textual framework.

## ⚠️ Known Issues

The v2 Python TUI implementation is currently experiencing UI rendering issues:
- Text input fields may be cut off or not fully visible
- Some input fields may not respond to keyboard input
- On-screen instructions are minimal
- AI assistance configuration is not yet exposed in the UI

**Recommended Alternative**: Use **v1 (HTML)** or **v3 (React)** for the best experience.

We're working on fixing these issues. In the meantime, v1 and v3 provide full functionality with better UX.

## Quick Start

### Using the Launcher (Easiest)

From the project root:
```bash
# Windows
launch.bat  # or launch.ps1

# macOS/Linux
./launch.sh
```

Select option 2 for Python TUI. The launcher will automatically check and install dependencies.

### Manual Setup

## Features

- **4-Phase Methodology**: Clarify → Organize → Refine → Equip
- **15 Strategic Questions**: Comprehensive project analysis framework
- **Rich TUI Interface**: Built with Textual framework for enhanced terminal experience
- **Multi-Format Output**: Generate Markdown, JSON, and AI prompts
- **Session Persistence**: Save and resume planning sessions as JSON files
- **Keyboard Navigation**: Full keyboard support with accessibility features
- **Cross-Platform**: Works on Windows, macOS, and Linux terminals

## Installation

### Prerequisites

- Python 3.8 or higher
- Terminal with Unicode support

### Install from Source

```bash
# Clone the repository
git clone <repository-url>
cd v2-python

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Install Dependencies Only

```bash
pip install textual rich pydantic click
```

## Usage

### Command Line Interface

```bash
# Start the TUI application
core-framework

# Or run directly with Python
python -m core_framework.main
```

### TUI Navigation

- **Arrow Keys**: Navigate between elements
- **Tab/Shift+Tab**: Move between input fields
- **Enter**: Activate buttons or confirm selections
- **Ctrl+P**: Previous phase
- **Ctrl+N**: Next phase
- **Ctrl+S**: Save session
- **Ctrl+G**: Generate output (in Equip phase)
- **Ctrl+Q**: Quit application
- **Escape**: Go back/cancel

### Workflow

1. **Start Application**: Launch the TUI interface
2. **Clarify Phase**: Answer 5 questions about project purpose and scope
3. **Organize Phase**: Structure requirements and priorities (5 questions)
4. **Refine Phase**: Analyze risks and constraints (5 questions)
5. **Equip Phase**: Generate implementation documentation
6. **Save Session**: Export session data and generated outputs

## Output Formats

### Markdown Documentation
- Project title and metadata
- Executive summary
- Phase-by-phase analysis
- Next steps and recommendations

### JSON Export
- Complete session data
- Structured answers and metadata
- Timestamps and version information

### AI Implementation Prompt
- Project context and requirements
- Specific deliverables for AI assistance
- Technical architecture guidance
- Implementation recommendations

## Development

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=core_framework
```

### Project Structure

```
v2-python/
├── core_framework/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # Main TUI application
│   ├── models.py            # Pydantic data models
│   └── output_generator.py  # Multi-format output generation
├── tests/
│   └── test_core_framework.py  # Comprehensive test suite
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── setup.py                # Package configuration
└── README.md               # This file
```

### Architecture

- **Models**: Pydantic models for data validation and serialization
- **TUI Components**: Textual widgets for interactive interface
- **Output Generation**: Multi-format documentation generation
- **Session Management**: JSON-based persistence and restoration

## Methodology

The CORE Framework follows a structured 4-phase approach:

### Phase 1: Clarify (5 Questions)
- Define project purpose and target users
- Establish success criteria and vision
- Identify unique value proposition
- Map user journey and experience
- Set clear scope boundaries

### Phase 2: Organize (5 Questions)
- Identify essential features
- Define user types and needs
- Establish MVP requirements
- Define success metrics
- Create prioritization framework

### Phase 3: Refine (5 Questions)
- Identify technical risks and challenges
- Assess resource constraints
- Analyze market and adoption risks
- Plan assumption validation
- Define pivot triggers

### Phase 4: Equip (Output Generation)
- Generate comprehensive documentation
- Create AI implementation prompts
- Export structured data
- Provide actionable next steps

## Compatibility

- **Python**: 3.8+
- **Terminals**: Modern terminals with Unicode support
- **Platforms**: Windows, macOS, Linux
- **Dependencies**: Textual, Rich, Pydantic, Click

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## Support

For issues, questions, or contributions, please refer to the main CORE Framework repository.
