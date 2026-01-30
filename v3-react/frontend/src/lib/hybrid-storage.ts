import { SessionData } from '../types'
import { supabase, sessionService, SupabaseSession } from './supabase'

// Hybrid storage that uses Supabase when authenticated, localStorage as fallback
export class HybridStorage {
  private static async isAuthenticated(): Promise<boolean> {
    const { data: { user } } = await supabase.auth.getUser()
    return !!user
  }

  private static convertToSessionData(supabaseSession: SupabaseSession): SessionData {
    return {
      id: supabaseSession.id,
      title: supabaseSession.title,
      currentPhase: supabaseSession.current_phase,
      answers: supabaseSession.answers,
      createdAt: supabaseSession.created_at,
      updatedAt: supabaseSession.updated_at
    }
  }

  private static convertFromSessionData(sessionData: SessionData): Omit<SupabaseSession, 'id' | 'user_id' | 'created_at' | 'updated_at'> {
    return {
      title: sessionData.title,
      current_phase: sessionData.currentPhase,
      answers: sessionData.answers
    }
  }

  static async loadSessions(): Promise<SessionData[]> {
    try {
      if (await this.isAuthenticated()) {
        const supabaseSessions = await sessionService.getSessions()
        return supabaseSessions.map(this.convertToSessionData)
      }
    } catch (error) {
      console.warn('Failed to load from Supabase, falling back to localStorage:', error)
    }

    // Fallback to localStorage
    const stored = localStorage.getItem('core-framework-sessions')
    return stored ? JSON.parse(stored) : []
  }

  static async saveSession(session: SessionData): Promise<void> {
    try {
      if (await this.isAuthenticated()) {
        if (session.id && session.id.length > 10) { // Existing Supabase session
          await sessionService.updateSession(session.id, {
            title: session.title,
            current_phase: session.currentPhase,
            answers: session.answers
          })
        } else {
          // Create new session
          const newSession = await sessionService.createSession(
            this.convertFromSessionData(session)
          )
          // Update the session ID to match Supabase
          session.id = newSession.id
        }
        return
      }
    } catch (error) {
      console.warn('Failed to save to Supabase, falling back to localStorage:', error)
    }

    // Fallback to localStorage
    const sessions = await this.loadSessions()
    const existingIndex = sessions.findIndex(s => s.id === session.id)
    
    if (existingIndex >= 0) {
      sessions[existingIndex] = session
    } else {
      sessions.push(session)
    }
    
    localStorage.setItem('core-framework-sessions', JSON.stringify(sessions))
  }

  static async deleteSession(sessionId: string): Promise<void> {
    try {
      if (await this.isAuthenticated()) {
        await sessionService.deleteSession(sessionId)
        return
      }
    } catch (error) {
      console.warn('Failed to delete from Supabase, falling back to localStorage:', error)
    }

    // Fallback to localStorage
    const sessions = await this.loadSessions()
    const filteredSessions = sessions.filter(s => s.id !== sessionId)
    localStorage.setItem('core-framework-sessions', JSON.stringify(filteredSessions))
  }

  static async createNewSession(title: string): Promise<SessionData> {
    const session: SessionData = {
      id: crypto.randomUUID(),
      title,
      currentPhase: 'clarify',
      answers: {},
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    }

    await this.saveSession(session)
    return session
  }

  static async exportToJSON(sessions: SessionData[]): Promise<string> {
    return JSON.stringify(sessions, null, 2)
  }

  static subscribeToChanges(callback: (sessions: SessionData[]) => void) {
    // Only subscribe if authenticated
    return supabase.auth.getUser().then(({ data: { user } }) => {
      if (user) {
        return sessionService.subscribeToSessions((supabaseSessions) => {
          const sessions = supabaseSessions.map(this.convertToSessionData)
          callback(sessions)
        })
      }
      return undefined
    })
  }
}
