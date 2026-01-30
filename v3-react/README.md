# CORE Framework v3 - React Implementation

A modern React-based implementation of the CORE Framework project planning methodology with Tailwind CSS and shadcn/ui components.

## Features

- **4-Phase Methodology**: Clarify → Organize → Refine → Equip
- **15 Strategic Questions**: Comprehensive project analysis
- **Session Management**: Save and resume planning sessions
- **Multi-Format Output**: Markdown, JSON, and AI prompts
- **Modern UI**: Built with React 19, Tailwind CSS, and shadcn/ui
- **Responsive Design**: Works on desktop and mobile
- **Dark/Light Theme**: Automatic theme switching
- **Local Storage**: Client-side session persistence

## Quick Start

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Usage

1. **Create Session**: Enter a project title and click "Create Session"
2. **Navigate Phases**: Use the phase buttons to move through Clarify → Organize → Refine → Equip
3. **Answer Questions**: Fill out the strategic questions in each phase
4. **Generate Output**: Click "Generate Output" to create documentation
5. **Export Results**: Copy Markdown, JSON, or AI prompt formats

## Architecture

### Component Structure
```
src/
├── components/
│   ├── ui/                 # shadcn/ui components
│   ├── COREFramework.tsx   # Main application component
│   └── theme-provider.tsx  # Theme management
├── data/
│   └── phases.ts          # Phase and question definitions
├── lib/
│   ├── storage.ts         # LocalStorage utilities
│   ├── output-generator.ts # Output formatting
│   └── utils.ts           # Utility functions
├── types/
│   └── index.ts           # TypeScript definitions
└── App.tsx                # Root component
```

### Key Features

- **Session Management**: Create, load, save, and delete planning sessions
- **Phase Navigation**: Move between the 4 phases of the methodology
- **Real-time Saving**: Answers are automatically saved as you type
- **Output Generation**: Generate comprehensive documentation in multiple formats
- **Responsive Design**: Optimized for desktop and mobile use

## Technology Stack

- **React 19**: Latest React with concurrent features
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **shadcn/ui**: High-quality component library
- **Vite**: Fast build tool and development server
- **Radix UI**: Accessible component primitives

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Project Structure

The application follows a clean architecture with:

- **Components**: Reusable UI components
- **Data**: Static configuration and content
- **Lib**: Business logic and utilities
- **Types**: TypeScript type definitions

## Deployment

### Static Hosting

Build the project and deploy the `dist` folder to any static hosting service:

```bash
npm run build
# Deploy dist/ folder to Vercel, Netlify, etc.
```

### Environment Variables

No environment variables required for basic functionality. All data is stored locally in the browser.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details
