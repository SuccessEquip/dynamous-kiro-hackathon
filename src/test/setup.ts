// Global test setup and mocks
import { vi } from 'vitest'

// Mock localStorage for testing
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn(),
  length: 0,
  key: vi.fn()
}

Object.defineProperty(window, 'localStorage', {
  value: localStorageMock
})

// Mock fetch for API testing
global.fetch = vi.fn()

// Mock crypto.randomUUID for session ID generation
Object.defineProperty(global, 'crypto', {
  value: {
    randomUUID: vi.fn(() => '12345678-1234-4123-8123-123456789012')
  }
})

// Mock Date for consistent timestamps in tests
const mockDate = new Date('2026-01-29T14:50:00.000Z')
vi.setSystemTime(mockDate)

// Clean up after each test
afterEach(() => {
  vi.clearAllMocks()
  localStorageMock.clear()
})
