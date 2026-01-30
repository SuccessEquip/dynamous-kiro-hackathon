import { Phase } from '../types'

export const PHASES: Phase[] = [
  {
    id: 'clarify',
    title: 'Clarify',
    description: 'Define the core purpose and scope of your project',
    questions: [
      {
        id: 'problem',
        text: 'What specific problem does this project solve?',
        placeholder: 'Describe the pain point or opportunity...',
        required: true
      },
      {
        id: 'target_users',
        text: 'Who are your target users?',
        placeholder: 'Define your primary audience...',
        required: true
      },
      {
        id: 'success_metrics',
        text: 'How will you measure success?',
        placeholder: 'Define key metrics and goals...',
        required: true
      },
      {
        id: 'scope',
        text: 'What is the project scope?',
        placeholder: 'Define boundaries and limitations...',
        required: true
      }
    ]
  },
  {
    id: 'organize',
    title: 'Organize',
    description: 'Structure your requirements and priorities',
    questions: [
      {
        id: 'core_features',
        text: 'What are the core features (MVP)?',
        placeholder: 'List essential functionality...',
        required: true
      },
      {
        id: 'nice_to_have',
        text: 'What are nice-to-have features?',
        placeholder: 'List additional features for later...'
      },
      {
        id: 'user_journey',
        text: 'Describe the main user journey',
        placeholder: 'Walk through the primary user flow...',
        required: true
      },
      {
        id: 'technical_requirements',
        text: 'What are the technical requirements?',
        placeholder: 'Platform, performance, integration needs...'
      }
    ]
  },
  {
    id: 'refine',
    title: 'Refine',
    description: 'Analyze risks and constraints',
    questions: [
      {
        id: 'constraints',
        text: 'What are your main constraints?',
        placeholder: 'Time, budget, technical limitations...',
        required: true
      },
      {
        id: 'risks',
        text: 'What are the biggest risks?',
        placeholder: 'Technical, market, resource risks...',
        required: true
      },
      {
        id: 'assumptions',
        text: 'What assumptions are you making?',
        placeholder: 'List key assumptions to validate...'
      },
      {
        id: 'dependencies',
        text: 'What external dependencies exist?',
        placeholder: 'Third-party services, team members, resources...'
      }
    ]
  },
  {
    id: 'equip',
    title: 'Equip',
    description: 'Generate implementation roadmap',
    questions: [
      {
        id: 'timeline',
        text: 'What is your target timeline?',
        placeholder: 'Milestones and deadlines...',
        required: true
      },
      {
        id: 'resources',
        text: 'What resources do you need?',
        placeholder: 'Team, tools, budget requirements...',
        required: true
      },
      {
        id: 'next_steps',
        text: 'What are the immediate next steps?',
        placeholder: 'First 3-5 actions to take...',
        required: true
      }
    ]
  }
]
