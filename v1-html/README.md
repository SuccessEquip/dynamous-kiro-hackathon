# CORE Framework v1 - HTML/CSS/JS

Single-file web implementation with no dependencies or build process.

## Quick Start

### Using the Launcher (Easiest)

From the project root:
```bash
# Windows
launch.bat  # or launch.ps1

# macOS/Linux
./launch.sh
```

Select option 1 for HTML/CSS/JS. The launcher will open the file in your browser.

### Manual Setup

Simply open `index.html` in any modern web browser:

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html

# Or use a local server
python -m http.server 8000
# Visit http://localhost:8000
```

## Features

- **Zero Dependencies**: No installation required
- **Offline First**: Works completely offline
- **LocalStorage**: Automatic session persistence
- **Single File**: Everything in one HTML file
- **4-Phase Methodology**: Complete CORE Framework workflow
- **Multi-Format Output**: Markdown, JSON, and AI prompts

## How It Works

This version includes everything in a single HTML file:
- HTML structure
- CSS styling (embedded)
- JavaScript logic (embedded)
- Complete CORE methodology

Sessions are automatically saved to browser LocalStorage and restored when you return.

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

## Advantages

- **No Setup**: Just open and use
- **Portable**: Copy the file anywhere
- **Fast**: No build process or server needed
- **Private**: All data stays in your browser

## Limitations

- Data stored only in browser LocalStorage
- No cloud sync
- No collaboration features
- Limited to single device

For cloud sync and collaboration, see v3 (React + Supabase).
