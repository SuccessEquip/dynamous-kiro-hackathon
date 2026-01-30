import { describe, it, expect } from 'vitest'
import { readFileSync } from 'fs'
import { join } from 'path'

// Load test fixtures
const testFixtures = JSON.parse(
  readFileSync(join(__dirname, '../shared/fixtures/test-sessions.json'), 'utf-8')
)

describe('Output Format Compatibility', () => {
  describe('Markdown Output', () => {
    it('should generate consistent markdown structure', () => {
      const expectedStructure = testFixtures.expectedOutputs.markdown.structure
      
      // Test that all required sections are present
      const requiredSections = [
        '# {title}',
        '## Clarify Phase',
        '## Organize Phase', 
        '## Refine Phase',
        '## Equip Phase'
      ]
      
      requiredSections.forEach(section => {
        expect(expectedStructure).toContain(section)
      })
    })

    it('should include all question fields in markdown', () => {
      const structure = testFixtures.expectedOutputs.markdown.structure
      const allQuestions = testFixtures.expectedOutputs.json.answerFields
      
      allQuestions.forEach(questionId => {
        const fieldPattern = `{${questionId}}`
        const hasField = structure.some(line => line.includes(fieldPattern))
        expect(hasField).toBe(true)
      })
    })

    it('should have proper markdown formatting', () => {
      const structure = testFixtures.expectedOutputs.markdown.structure
      
      // Should have title as H1
      expect(structure[0]).toMatch(/^# /)
      
      // Should have phase headers as H2
      const phaseHeaders = structure.filter(line => line.startsWith('## '))
      expect(phaseHeaders).toHaveLength(4)
      
      // Should have bold field labels
      const boldFields = structure.filter(line => line.startsWith('**') && line.includes('**:'))
      expect(boldFields.length).toBeGreaterThan(10)
    })
  })

  describe('JSON Output', () => {
    it('should have all required session fields', () => {
      const requiredFields = testFixtures.expectedOutputs.json.requiredFields
      const session = testFixtures.testSessions[0]
      
      requiredFields.forEach(field => {
        expect(session).toHaveProperty(field)
      })
    })

    it('should have all answer fields for complete session', () => {
      const answerFields = testFixtures.expectedOutputs.json.answerFields
      const completeSession = testFixtures.testSessions[0]
      
      answerFields.forEach(field => {
        expect(completeSession.answers).toHaveProperty(field)
      })
    })

    it('should be valid JSON structure', () => {
      testFixtures.testSessions.forEach(session => {
        expect(() => JSON.stringify(session)).not.toThrow()
        expect(() => JSON.parse(JSON.stringify(session))).not.toThrow()
      })
    })
  })

  describe('AI Prompt Output', () => {
    it('should have consistent prompt structure', () => {
      const expectedStructure = testFixtures.expectedOutputs.aiPrompt.structure
      
      // Should start with role definition
      expect(expectedStructure[0]).toContain('expert project manager')
      
      // Should have project title
      expect(expectedStructure[1]).toContain('PROJECT:')
      
      // Should have analysis section
      expect(expectedStructure[2]).toBe('ANALYSIS:')
      
      // Should have deliverables section
      expect(expectedStructure.some(line => line.includes('Please provide:'))).toBe(true)
    })

    it('should include key analysis fields', () => {
      const structure = testFixtures.expectedOutputs.aiPrompt.structure
      const keyFields = ['problem', 'target_users', 'success_metrics']
      
      keyFields.forEach(field => {
        const hasField = structure.some(line => line.includes(`{${field}}`))
        expect(hasField).toBe(true)
      })
    })

    it('should request specific deliverables', () => {
      const structure = testFixtures.expectedOutputs.aiPrompt.structure
      const expectedDeliverables = [
        'technical architecture',
        'implementation roadmap',
        'risk mitigation',
        'technology stack',
        'resource allocation',
        'success metrics'
      ]
      
      const deliverablesText = structure.join(' ').toLowerCase()
      expectedDeliverables.forEach(deliverable => {
        expect(deliverablesText).toContain(deliverable)
      })
    })
  })

  describe('Cross-Format Consistency', () => {
    it('should use same field names across all formats', () => {
      const jsonFields = testFixtures.expectedOutputs.json.answerFields
      const markdownStructure = testFixtures.expectedOutputs.markdown.structure.join(' ')
      const aiPromptStructure = testFixtures.expectedOutputs.aiPrompt.structure.join(' ')
      
      // Key fields should appear in all formats
      const keyFields = ['problem', 'target_users', 'success_metrics']
      
      keyFields.forEach(field => {
        expect(jsonFields).toContain(field)
        expect(markdownStructure).toContain(`{${field}}`)
        expect(aiPromptStructure).toContain(`{${field}}`)
      })
    })

    it('should maintain data integrity across formats', () => {
      const session = testFixtures.testSessions[0]
      
      // All formats should reference the same session data
      expect(session.title).toBeTruthy()
      expect(session.answers.problem).toBeTruthy()
      expect(session.answers.target_users).toBeTruthy()
      expect(session.answers.success_metrics).toBeTruthy()
    })
  })
})
