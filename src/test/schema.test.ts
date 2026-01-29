import { describe, it, expect } from 'vitest'
import methodologySchema from '../../shared/schema/methodology.json'
import sessionSchema from '../../shared/schema/session.json'

describe('Schema Validation', () => {
  describe('Methodology Schema', () => {
    it('should have valid JSON schema structure', () => {
      expect(methodologySchema).toBeDefined()
      expect(methodologySchema.$schema).toBe('http://json-schema.org/draft-07/schema#')
      expect(methodologySchema.title).toBe('CORE Framework Methodology Schema')
    })

    it('should define framework structure with 4 phases', () => {
      const frameworkProps = methodologySchema.properties.framework.properties
      expect(frameworkProps.phases.items.properties.id.pattern).toBe('^(clarify|organize|refine|equip)$')
      expect(frameworkProps.phases.minItems).toBe(4)
      expect(frameworkProps.phases.maxItems).toBe(4)
    })

    it('should define question ID pattern', () => {
      const questionProps = methodologySchema.properties.framework.properties.phases.items.properties.questions.items.properties
      expect(questionProps.id.pattern).toBe('^[A-Z]-\\d{2}$')
      expect(questionProps.input_type.enum).toContain('textarea')
      expect(questionProps.input_type.enum).toContain('text')
    })

    it('should define action ID pattern for Equip phase', () => {
      const actionProps = methodologySchema.properties.framework.properties.phases.items.properties.actions.items.properties
      expect(actionProps.id.pattern).toBe('^E-\\d{2}$')
      expect(actionProps.output_format.enum).toContain('markdown')
      expect(actionProps.output_format.enum).toContain('json')
      expect(actionProps.output_format.enum).toContain('ai_prompt')
    })

    it('should define output formats', () => {
      const outputFormats = methodologySchema.properties.output_formats.properties
      expect(outputFormats.markdown).toBeDefined()
      expect(outputFormats.json).toBeDefined()
      expect(outputFormats.ai_prompt).toBeDefined()
    })
  })

  describe('Session Schema', () => {
    it('should have valid JSON schema structure', () => {
      expect(sessionSchema).toBeDefined()
      expect(sessionSchema.$schema).toBe('http://json-schema.org/draft-07/schema#')
      expect(sessionSchema.title).toBe('CORE Framework Session Schema')
    })

    it('should define session metadata structure', () => {
      const sessionProps = sessionSchema.properties.session.properties
      expect(sessionProps.id.pattern).toBe('^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$')
      expect(sessionProps.implementation.enum).toContain('v1-html')
      expect(sessionProps.implementation.enum).toContain('v2-python')
      expect(sessionProps.implementation.enum).toContain('v3-react')
    })

    it('should define answers array structure', () => {
      const answersProps = sessionSchema.properties.answers.items.properties
      expect(answersProps.question_id.pattern).toBe('^[A-Z]-\\d{2}$')
      expect(answersProps.confidence.minimum).toBe(1)
      expect(answersProps.confidence.maximum).toBe(5)
    })

    it('should define AI conversations structure', () => {
      const aiProps = sessionSchema.properties.ai_conversations.items.properties
      expect(aiProps.phase.pattern).toBe('^(clarify|organize|refine|equip)$')
      expect(aiProps.messages.items.properties.role.enum).toContain('user')
      expect(aiProps.messages.items.properties.role.enum).toContain('assistant')
    })
  })

  describe('Cross-Schema Consistency', () => {
    it('should have consistent phase identifiers', () => {
      const methodologyPhases = '^(clarify|organize|refine|equip)$'
      const sessionPhases = '^(clarify|organize|refine|equip)$'
      expect(methodologyPhases).toBe(sessionPhases)
    })

    it('should have consistent question ID patterns', () => {
      const methodologyPattern = '^[A-Z]-\\d{2}$'
      const sessionPattern = '^[A-Z]-\\d{2}$'
      expect(methodologyPattern).toBe(sessionPattern)
    })

    it('should have consistent implementation versions', () => {
      const sessionImplementations = sessionSchema.properties.session.properties.implementation.enum
      expect(sessionImplementations).toEqual(['v1-html', 'v2-python', 'v3-react'])
    })
  })
})
