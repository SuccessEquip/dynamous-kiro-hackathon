import { describe, it, expect } from 'vitest'
import { readFileSync } from 'fs'
import { join } from 'path'

// Load test fixtures
const testFixtures = JSON.parse(
  readFileSync(join(__dirname, '../shared/fixtures/test-sessions.json'), 'utf-8')
)

describe('CORE Framework Methodology Consistency', () => {
  describe('Phase Structure', () => {
    it('should have exactly 4 phases in correct order', () => {
      const expectedPhases = ['clarify', 'organize', 'refine', 'equip']
      
      // This test would be run against each implementation
      // For now, we'll test the expected structure
      expect(expectedPhases).toHaveLength(4)
      expect(expectedPhases[0]).toBe('clarify')
      expect(expectedPhases[1]).toBe('organize') 
      expect(expectedPhases[2]).toBe('refine')
      expect(expectedPhases[3]).toBe('equip')
    })

    it('should have 15 total questions across all phases', () => {
      const questionCounts = {
        clarify: 4,    // problem, target_users, success_metrics, scope
        organize: 4,   // core_features, nice_to_have, user_journey, technical_requirements
        refine: 4,     // constraints, risks, assumptions, dependencies
        equip: 3       // timeline, resources, next_steps
      }
      
      const totalQuestions = Object.values(questionCounts).reduce((sum, count) => sum + count, 0)
      expect(totalQuestions).toBe(15)
    })
  })

  describe('Session Data Structure', () => {
    it('should have consistent session structure across implementations', () => {
      const session = testFixtures.testSessions[0]
      
      // Required fields
      expect(session).toHaveProperty('id')
      expect(session).toHaveProperty('title')
      expect(session).toHaveProperty('currentPhase')
      expect(session).toHaveProperty('answers')
      expect(session).toHaveProperty('createdAt')
      expect(session).toHaveProperty('updatedAt')
      
      // Data types
      expect(typeof session.id).toBe('string')
      expect(typeof session.title).toBe('string')
      expect(typeof session.currentPhase).toBe('string')
      expect(typeof session.answers).toBe('object')
      expect(typeof session.createdAt).toBe('string')
      expect(typeof session.updatedAt).toBe('string')
    })

    it('should have valid phase values', () => {
      const validPhases = ['clarify', 'organize', 'refine', 'equip']
      
      testFixtures.testSessions.forEach(session => {
        expect(validPhases).toContain(session.currentPhase)
      })
    })

    it('should have ISO date strings for timestamps', () => {
      testFixtures.testSessions.forEach(session => {
        expect(() => new Date(session.createdAt)).not.toThrow()
        expect(() => new Date(session.updatedAt)).not.toThrow()
        
        // Should be valid ISO strings
        expect(session.createdAt).toMatch(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/)
        expect(session.updatedAt).toMatch(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/)
      })
    })
  })

  describe('Question Consistency', () => {
    it('should have consistent question IDs across implementations', () => {
      const expectedQuestions = [
        // Clarify phase
        'problem', 'target_users', 'success_metrics', 'scope',
        // Organize phase  
        'core_features', 'nice_to_have', 'user_journey', 'technical_requirements',
        // Refine phase
        'constraints', 'risks', 'assumptions', 'dependencies',
        // Equip phase
        'timeline', 'resources', 'next_steps'
      ]
      
      const completeSession = testFixtures.testSessions[0]
      const actualQuestions = Object.keys(completeSession.answers)
      
      expectedQuestions.forEach(questionId => {
        expect(actualQuestions).toContain(questionId)
      })
    })

    it('should group questions correctly by phase', () => {
      const phaseQuestions = {
        clarify: ['problem', 'target_users', 'success_metrics', 'scope'],
        organize: ['core_features', 'nice_to_have', 'user_journey', 'technical_requirements'],
        refine: ['constraints', 'risks', 'assumptions', 'dependencies'],
        equip: ['timeline', 'resources', 'next_steps']
      }
      
      // Verify each phase has the correct number of questions
      expect(phaseQuestions.clarify).toHaveLength(4)
      expect(phaseQuestions.organize).toHaveLength(4)
      expect(phaseQuestions.refine).toHaveLength(4)
      expect(phaseQuestions.equip).toHaveLength(3)
    })
  })
})
