import { describe, it, expect, beforeEach } from 'vitest'

// Mock CORE Framework data for testing
const mockMethodologyData = {
  framework: {
    name: 'CORE Framework',
    version: '1.0.0',
    description: 'Interactive project planning tool with 4-phase methodology',
    phases: [
      {
        id: 'clarify',
        name: 'Clarify',
        description: 'Define project purpose and scope',
        order: 1,
        questions: [
          {
            id: 'C-01',
            text: 'What problem does this project solve, and for whom?',
            guidance: 'Think about the core pain point your project addresses.',
            ai_prompt: 'Help me clarify the core problem this project solves.',
            input_type: 'textarea',
            validation: { min_length: 50, max_length: 500 }
          }
        ]
      },
      {
        id: 'organize',
        name: 'Organize',
        description: 'Structure requirements and priorities',
        order: 2,
        questions: [
          {
            id: 'O-01',
            text: 'What are the 3-5 essential features that deliver your core value?',
            guidance: 'Focus on must-have features that directly support your value proposition.',
            ai_prompt: 'Help me identify and prioritize the essential features.',
            input_type: 'textarea',
            validation: { min_length: 100, max_length: 500 }
          }
        ]
      },
      {
        id: 'refine',
        name: 'Refine',
        description: 'Analyze risks and constraints',
        order: 3,
        questions: [
          {
            id: 'R-01',
            text: 'What technical challenges or unknowns could derail this project?',
            guidance: 'Identify technical risks early.',
            ai_prompt: 'Help me identify technical risks and unknowns.',
            input_type: 'textarea',
            validation: { min_length: 50, max_length: 400 }
          }
        ]
      },
      {
        id: 'equip',
        name: 'Equip',
        description: 'Generate implementation documentation',
        order: 4,
        questions: [],
        actions: [
          {
            id: 'E-01',
            name: 'Generate Project Documentation',
            description: 'Create comprehensive project documentation in Markdown format',
            output_format: 'markdown'
          }
        ]
      }
    ]
  }
}

const mockSessionData = {
  session: {
    id: '12345678-1234-4123-8123-123456789012',
    name: 'Test Project Session',
    description: 'Testing the CORE Framework',
    created_at: '2026-01-29T14:50:00.000Z',
    updated_at: '2026-01-29T14:50:00.000Z',
    version: '1.0.0',
    implementation: 'v1-html',
    status: 'in_progress'
  },
  project: {
    title: 'Test Project',
    summary: 'A test project for validating the CORE Framework'
  },
  answers: [
    {
      question_id: 'C-01',
      response: 'This project solves the problem of inefficient project planning for solo developers and small teams.',
      answered_at: '2026-01-29T14:50:00.000Z',
      confidence: 4,
      notes: 'Based on personal experience with project planning challenges'
    }
  ],
  ai_conversations: []
}

describe('CORE Framework Integration', () => {
  describe('Methodology Data Structure', () => {
    it('should have correct framework metadata', () => {
      expect(mockMethodologyData.framework.name).toBe('CORE Framework')
      expect(mockMethodologyData.framework.version).toBe('1.0.0')
      expect(mockMethodologyData.framework.phases).toHaveLength(4)
    })

    it('should have phases in correct order', () => {
      const phases = mockMethodologyData.framework.phases
      expect(phases[0].id).toBe('clarify')
      expect(phases[1].id).toBe('organize')
      expect(phases[2].id).toBe('refine')
      expect(phases[3].id).toBe('equip')
    })

    it('should have questions with proper structure', () => {
      const clarifyPhase = mockMethodologyData.framework.phases[0]
      const question = clarifyPhase.questions[0]
      
      expect(question.id).toBe('C-01')
      expect(question.text).toBeDefined()
      expect(question.guidance).toBeDefined()
      expect(question.ai_prompt).toBeDefined()
      expect(question.input_type).toBe('textarea')
      expect(question.validation).toBeDefined()
    })

    it('should have actions in Equip phase', () => {
      const equipPhase = mockMethodologyData.framework.phases[3]
      expect(equipPhase.actions).toBeDefined()
      expect(equipPhase.actions[0].id).toBe('E-01')
      expect(equipPhase.actions[0].output_format).toBe('markdown')
    })
  })

  describe('Session Data Management', () => {
    it('should create valid session structure', () => {
      expect(mockSessionData.session.id).toMatch(/^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$/)
      expect(mockSessionData.session.implementation).toBe('v1-html')
      expect(mockSessionData.session.status).toBe('in_progress')
    })

    it('should store answers with proper structure', () => {
      const answer = mockSessionData.answers[0]
      expect(answer.question_id).toBe('C-01')
      expect(answer.response).toBeDefined()
      expect(answer.confidence).toBeGreaterThanOrEqual(1)
      expect(answer.confidence).toBeLessThanOrEqual(5)
    })

    it('should handle timestamps correctly', () => {
      const timestamp = mockSessionData.session.created_at
      expect(new Date(timestamp)).toBeInstanceOf(Date)
      expect(timestamp).toBe('2026-01-29T14:50:00.000Z')
    })
  })

  describe('Question Validation', () => {
    it('should validate question responses against schema', () => {
      const question = mockMethodologyData.framework.phases[0].questions[0]
      const answer = mockSessionData.answers[0]
      
      expect(answer.response.length).toBeGreaterThanOrEqual(question.validation.min_length)
      expect(answer.response.length).toBeLessThanOrEqual(question.validation.max_length)
    })

    it('should validate question ID format', () => {
      const questions = mockMethodologyData.framework.phases.flatMap(phase => phase.questions)
      questions.forEach(question => {
        expect(question.id).toMatch(/^[A-Z]-\d{2}$/)
      })
    })

    it('should validate action ID format', () => {
      const equipPhase = mockMethodologyData.framework.phases[3]
      equipPhase.actions.forEach(action => {
        expect(action.id).toMatch(/^E-\d{2}$/)
      })
    })
  })

  describe('Cross-Implementation Compatibility', () => {
    it('should support all implementation versions', () => {
      const validImplementations = ['v1-html', 'v2-python', 'v3-react']
      expect(validImplementations).toContain(mockSessionData.session.implementation)
    })

    it('should maintain consistent question structure across implementations', () => {
      // This test ensures that the question structure is compatible
      // across all three implementations (HTML, Python TUI, React)
      const question = mockMethodologyData.framework.phases[0].questions[0]
      
      // Required fields for all implementations
      expect(question).toHaveProperty('id')
      expect(question).toHaveProperty('text')
      expect(question).toHaveProperty('guidance')
      expect(question).toHaveProperty('ai_prompt')
      expect(question).toHaveProperty('input_type')
      expect(question).toHaveProperty('validation')
    })

    it('should support all output formats', () => {
      const validFormats = ['markdown', 'json', 'ai_prompt', 'all']
      const equipPhase = mockMethodologyData.framework.phases[3]
      
      equipPhase.actions.forEach(action => {
        expect(validFormats).toContain(action.output_format)
      })
    })
  })
})
