import { useState } from 'react'
import { useAuth } from '../hooks/useAuth'
import { Button } from './ui/button'
import { Input } from './ui/input'

export function Auth() {
  const { signIn, signUp, signOut, user, loading } = useAuth()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [isSignUp, setIsSignUp] = useState(false)
  const [authLoading, setAuthLoading] = useState(false)
  const [error, setError] = useState('')

  if (loading) {
    return <div className="flex justify-center p-4">Loading...</div>
  }

  if (user) {
    return (
      <div className="flex items-center gap-4 p-4 border-b">
        <span className="text-sm text-muted-foreground">
          Signed in as {user.email}
        </span>
        <Button variant="outline" onClick={signOut}>
          Sign Out
        </Button>
      </div>
    )
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setAuthLoading(true)
    setError('')

    try {
      if (isSignUp) {
        await signUp(email, password)
      } else {
        await signIn(email, password)
      }
    } catch (err: any) {
      setError(err.message)
    } finally {
      setAuthLoading(false)
    }
  }

  return (
    <div className="max-w-md mx-auto p-6 border rounded-lg">
      <h2 className="text-2xl font-bold mb-4">
        {isSignUp ? 'Sign Up' : 'Sign In'}
      </h2>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <Input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        
        <div>
          <Input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        
        {error && (
          <div className="text-red-500 text-sm">{error}</div>
        )}
        
        <Button type="submit" className="w-full" disabled={authLoading}>
          {authLoading ? 'Loading...' : (isSignUp ? 'Sign Up' : 'Sign In')}
        </Button>
      </form>
      
      <div className="mt-4 text-center">
        <button
          type="button"
          className="text-sm text-blue-600 hover:underline"
          onClick={() => setIsSignUp(!isSignUp)}
        >
          {isSignUp ? 'Already have an account? Sign In' : "Don't have an account? Sign Up"}
        </button>
      </div>
    </div>
  )
}
