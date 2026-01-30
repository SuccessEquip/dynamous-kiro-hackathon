import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL || 'https://your-project-id.supabase.co'
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY || 'your-anon-key'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

export interface SupabaseSession {
  id: string
  user_id: string
  title: string
  current_phase: string
  answers: Record<string, string>
  created_at: string
  updated_at: string
}

export const sessionService = {
  async getSessions(): Promise<SupabaseSession[]> {
    const { data, error } = await supabase
      .from('sessions')
      .select('*')
      .order('updated_at', { ascending: false })
    
    if (error) throw error
    return data || []
  },

  async getSession(id: string): Promise<SupabaseSession | null> {
    const { data, error } = await supabase
      .from('sessions')
      .select('*')
      .eq('id', id)
      .single()
    
    if (error) throw error
    return data
  },

  async createSession(session: Omit<SupabaseSession, 'id' | 'user_id' | 'created_at' | 'updated_at'>): Promise<SupabaseSession> {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) throw new Error('User not authenticated')

    const { data, error } = await supabase
      .from('sessions')
      .insert({
        ...session,
        user_id: user.id
      })
      .select()
      .single()
    
    if (error) throw error
    return data
  },

  async updateSession(id: string, updates: Partial<Pick<SupabaseSession, 'title' | 'current_phase' | 'answers'>>): Promise<SupabaseSession> {
    const { data, error } = await supabase
      .from('sessions')
      .update(updates)
      .eq('id', id)
      .select()
      .single()
    
    if (error) throw error
    return data
  },

  async deleteSession(id: string): Promise<void> {
    const { error } = await supabase
      .from('sessions')
      .delete()
      .eq('id', id)
    
    if (error) throw error
  },

  subscribeToSessions(callback: (sessions: SupabaseSession[]) => void) {
    return supabase
      .channel('sessions')
      .on('postgres_changes', 
        { event: '*', schema: 'public', table: 'sessions' },
        () => {
          this.getSessions().then(callback).catch(console.error)
        }
      )
      .subscribe()
  }
}
