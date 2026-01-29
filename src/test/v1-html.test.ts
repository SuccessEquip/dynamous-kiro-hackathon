import { describe, it, expect, beforeEach } from 'vitest'
import { JSDOM } from 'jsdom'
import fs from 'fs'
import path from 'path'

describe('v1 HTML Implementation', () => {
  let dom
  let document
  let window

  beforeEach(() => {
    const htmlPath = path.join(__dirname, '../../v1-html/index.html')
    const htmlContent = fs.readFileSync(htmlPath, 'utf-8')
    
    dom = new JSDOM(htmlContent, {
      runScripts: 'dangerously',
      resources: 'usable'
    })
    
    document = dom.window.document
    window = dom.window
    
    // Wait for DOM to be ready
    return new Promise(resolve => {
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', resolve)
      } else {
        resolve()
      }
    })
  })

  describe('HTML Structure', () => {
    it('should have proper document structure', () => {
      expect(document.doctype.name).toBe('html')
      expect(document.documentElement.lang).toBe('en')
      expect(document.title).toBe('CORE Framework - Interactive Project Planning')
    })

    it('should have all required semantic elements', () => {
      expect(document.querySelector('header[role="banner"]')).toBeTruthy()
      expect(document.querySelector('main[role="main"]')).toBeTruthy()
      expect(document.querySelector('footer[role="contentinfo"]')).toBeTruthy()
    })

    it('should have progress navigation with 4 phases', () => {
      const progressSteps = document.querySelectorAll('.progress-steps .step')
      expect(progressSteps).toHaveLength(4)
      
      const phases = ['clarify', 'organize', 'refine', 'equip']
      progressSteps.forEach((step, index) => {
        expect(step.dataset.phase).toBe(phases[index])
      })
    })

    it('should have all 4 phase sections', () => {
      const phaseSections = document.querySelectorAll('.phase-section')
      expect(phaseSections).toHaveLength(4)
      
      const phaseIds = ['phase-clarify', 'phase-organize', 'phase-refine', 'phase-equip']
      phaseSections.forEach((section, index) => {
        expect(section.id).toBe(phaseIds[index])
      })
    })

    it('should have all 15 questions with proper IDs', () => {
      const expectedQuestions = [
        'c-01', 'c-02', 'c-03', 'c-04', 'c-05',
        'o-01', 'o-02', 'o-03', 'o-04', 'o-05',
        'r-01', 'r-02', 'r-03', 'r-04', 'r-05'
      ]
      
      expectedQuestions.forEach(questionId => {
        const element = document.getElementById(questionId)
        expect(element).toBeTruthy()
        expect(element.tagName.toLowerCase()).toBe('textarea')
      })
    })
  })

  describe('Accessibility Features', () => {
    it('should have proper ARIA labels and roles', () => {
      const progressNav = document.querySelector('.progress-nav')
      expect(progressNav.getAttribute('aria-label')).toBe('Progress')
      
      const sessionControls = document.querySelector('.session-controls')
      expect(sessionControls.getAttribute('aria-label')).toBe('Session Management')
    })

    it('should have proper form labels', () => {
      const sessionNameInput = document.getElementById('session-name')
      const sessionNameLabel = document.querySelector('label[for="session-name"]')
      
      expect(sessionNameInput).toBeTruthy()
      expect(sessionNameLabel).toBeTruthy()
      expect(sessionNameLabel.textContent.trim()).toBe('Session Name:')
    })

    it('should have validation messages with role="alert"', () => {
      const errorElements = document.querySelectorAll('.validation-message')
      errorElements.forEach(element => {
        expect(element.getAttribute('role')).toBe('alert')
      })
    })

    it('should have proper heading hierarchy', () => {
      const h1 = document.querySelector('h1')
      const h2s = document.querySelectorAll('h2')
      
      expect(h1).toBeTruthy()
      expect(h1.textContent).toBe('CORE Framework')
      expect(h2s.length).toBeGreaterThan(0)
    })
  })

  describe('Form Validation', () => {
    it('should have required attributes on question textareas', () => {
      const questionTextareas = document.querySelectorAll('textarea[id^="c-"], textarea[id^="o-"], textarea[id^="r-"]')
      
      questionTextareas.forEach(textarea => {
        expect(textarea.hasAttribute('required')).toBe(true)
        expect(textarea.hasAttribute('minlength')).toBe(true)
        expect(textarea.hasAttribute('maxlength')).toBe(true)
      })
    })

    it('should have proper validation constraints', () => {
      const c01 = document.getElementById('c-01')
      expect(c01.getAttribute('minlength')).toBe('50')
      expect(c01.getAttribute('maxlength')).toBe('500')
      
      const o01 = document.getElementById('o-01')
      expect(o01.getAttribute('minlength')).toBe('100')
      expect(o01.getAttribute('maxlength')).toBe('500')
    })
  })

  describe('Navigation Controls', () => {
    it('should have navigation buttons', () => {
      const prevButton = document.getElementById('prev-phase')
      const nextButton = document.getElementById('next-phase')
      
      expect(prevButton).toBeTruthy()
      expect(nextButton).toBeTruthy()
      expect(prevButton.textContent.trim()).toBe('Previous')
      expect(nextButton.textContent.trim()).toBe('Next')
    })

    it('should have session management buttons', () => {
      const saveButton = document.getElementById('save-session')
      const loadButton = document.getElementById('load-session')
      
      expect(saveButton).toBeTruthy()
      expect(loadButton).toBeTruthy()
      expect(saveButton.textContent.trim()).toBe('Save Session')
      expect(loadButton.textContent.trim()).toBe('Load Session')
    })
  })

  describe('Output Generation', () => {
    it('should have output format selection in Equip phase', () => {
      const outputRadios = document.querySelectorAll('input[name="output-action"]')
      expect(outputRadios).toHaveLength(4)
      
      const expectedValues = ['markdown', 'json', 'ai_prompt', 'all']
      outputRadios.forEach((radio, index) => {
        expect(radio.value).toBe(expectedValues[index])
      })
    })

    it('should have generate output button', () => {
      const generateButton = document.getElementById('generate-output')
      expect(generateButton).toBeTruthy()
      expect(generateButton.textContent.trim()).toBe('Generate Documentation')
    })

    it('should have output display area', () => {
      const outputDisplay = document.getElementById('output-display')
      expect(outputDisplay).toBeTruthy()
      expect(outputDisplay.tagName.toLowerCase()).toBe('textarea')
      expect(outputDisplay.hasAttribute('readonly')).toBe(true)
    })
  })

  describe('Responsive Design', () => {
    it('should have viewport meta tag', () => {
      const viewportMeta = document.querySelector('meta[name="viewport"]')
      expect(viewportMeta).toBeTruthy()
      expect(viewportMeta.getAttribute('content')).toBe('width=device-width, initial-scale=1.0')
    })

    it('should have responsive CSS classes', () => {
      const styles = document.querySelector('style').textContent
      expect(styles).toContain('@media (max-width: 768px)')
      expect(styles).toContain('@media (prefers-contrast: high)')
      expect(styles).toContain('@media (prefers-reduced-motion: reduce)')
    })
  })

  describe('JavaScript Functionality', () => {
    it('should initialize CORE Framework class', () => {
      expect(window.coreFramework).toBeTruthy()
      expect(typeof window.coreFramework).toBe('object')
    })

    it('should have proper phase management', () => {
      const framework = window.coreFramework
      expect(framework.phases).toEqual(['clarify', 'organize', 'refine', 'equip'])
      expect(framework.currentPhase).toBe(0)
    })

    it('should have question schema matching methodology', () => {
      const framework = window.coreFramework
      const questions = framework.questions
      
      // Check that all expected questions are present
      const expectedQuestions = [
        'c-01', 'c-02', 'c-03', 'c-04', 'c-05',
        'o-01', 'o-02', 'o-03', 'o-04', 'o-05',
        'r-01', 'r-02', 'r-03', 'r-04', 'r-05'
      ]
      
      expectedQuestions.forEach(questionId => {
        expect(questions[questionId]).toBeTruthy()
        expect(questions[questionId]).toHaveProperty('phase')
        expect(questions[questionId]).toHaveProperty('minLength')
        expect(questions[questionId]).toHaveProperty('maxLength')
      })
    })

    it('should have session data structure', () => {
      const framework = window.coreFramework
      const sessionData = framework.sessionData
      
      expect(sessionData).toHaveProperty('session')
      expect(sessionData).toHaveProperty('project')
      expect(sessionData).toHaveProperty('answers')
      expect(sessionData).toHaveProperty('ai_conversations')
      expect(sessionData).toHaveProperty('exports')
      
      expect(sessionData.session.implementation).toBe('v1-html')
      expect(sessionData.session.version).toBe('1.0.0')
    })
  })
})
