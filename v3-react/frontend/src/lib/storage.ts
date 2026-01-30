import { SessionData } from '../types'

const STORAGE_KEY = 'core-framework-sessions'

export const saveSessions = (sessions: SessionData[]): void => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(sessions))
}

export const loadSessions = (): SessionData[] => {
  const stored = localStorage.getItem(STORAGE_KEY)
  return stored ? JSON.parse(stored) : []
}

export const saveSession = (session: SessionData): void => {
  const sessions = loadSessions()
  const existingIndex = sessions.findIndex(s => s.id === session.id)
  
  if (existingIndex >= 0) {
    sessions[existingIndex] = session
  } else {
    sessions.push(session)
  }
  
  saveSessions(sessions)
}

export const deleteSession = (sessionId: string): void => {
  const sessions = loadSessions().filter(s => s.id !== sessionId)
  saveSessions(sessions)
}

export const createNewSession = (title: string): SessionData => ({
  id: crypto.randomUUID(),
  title,
  currentPhase: 'clarify',
  answers: {},
  createdAt: new Date().toISOString(),
  updatedAt: new Date().toISOString()
})
