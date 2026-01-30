import { useState, useEffect } from 'react'
import { SessionData } from '../types'
import { PHASES } from '../data/phases'
import { loadSessions, saveSession, createNewSession, deleteSession } from '../lib/storage'
import { generateOutputs } from '../lib/output-generator'
import { Button } from './ui/button'
import { Input } from './ui/input'
import { Textarea } from './ui/textarea'
import { Badge } from './ui/badge'
import { Tabs, TabsContent, TabsList, TabsTrigger } from './ui/tabs'

export function COREFramework() {
  const [sessions, setSessions] = useState<SessionData[]>([])
  const [currentSession, setCurrentSession] = useState<SessionData | null>(null)
  const [newSessionTitle, setNewSessionTitle] = useState('')
  const [showOutput, setShowOutput] = useState(false)

  useEffect(() => {
    setSessions(loadSessions())
  }, [])

  const handleCreateSession = () => {
    if (!newSessionTitle.trim()) return
    
    const session = createNewSession(newSessionTitle.trim())
    saveSession(session)
    setSessions(loadSessions())
    setCurrentSession(session)
    setNewSessionTitle('')
    setShowOutput(false)
  }

  const handleLoadSession = (session: SessionData) => {
    setCurrentSession(session)
    setShowOutput(false)
  }

  const handleDeleteSession = (sessionId: string) => {
    deleteSession(sessionId)
    setSessions(loadSessions())
    if (currentSession?.id === sessionId) {
      setCurrentSession(null)
      setShowOutput(false)
    }
  }

  const handleAnswerChange = (questionId: string, value: string) => {
    if (!currentSession) return

    const updatedSession = {
      ...currentSession,
      answers: { ...currentSession.answers, [questionId]: value },
      updatedAt: new Date().toISOString()
    }

    setCurrentSession(updatedSession)
    saveSession(updatedSession)
    setSessions(loadSessions())
  }

  const handlePhaseChange = (phaseId: string) => {
    if (!currentSession) return

    const updatedSession = {
      ...currentSession,
      currentPhase: phaseId,
      updatedAt: new Date().toISOString()
    }

    setCurrentSession(updatedSession)
    saveSession(updatedSession)
  }

  const handleGenerateOutput = () => {
    setShowOutput(true)
  }

  const currentPhase = PHASES.find(p => p.id === currentSession?.currentPhase)
  const outputs = currentSession ? generateOutputs(currentSession) : null

  if (!currentSession) {
    return (
      <div className="container mx-auto p-6 max-w-4xl">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold mb-4">CORE Framework</h1>
          <p className="text-lg text-muted-foreground">
            Transform ideas into actionable project plans through structured methodology
          </p>
        </div>

        <div className="mb-8">
          <div className="flex gap-2 mb-4">
            <Input
              placeholder="Enter project title..."
              value={newSessionTitle}
              onChange={(e) => setNewSessionTitle(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleCreateSession()}
            />
            <Button onClick={handleCreateSession} disabled={!newSessionTitle.trim()}>
              Create Session
            </Button>
          </div>
        </div>

        {sessions.length > 0 && (
          <div>
            <h2 className="text-2xl font-semibold mb-4">Saved Sessions</h2>
            <div className="grid gap-4">
              {sessions.map((session) => (
                <div key={session.id} className="border rounded-lg p-4 flex justify-between items-center">
                  <div>
                    <h3 className="font-medium">{session.title}</h3>
                    <p className="text-sm text-muted-foreground">
                      Last updated: {new Date(session.updatedAt).toLocaleDateString()}
                    </p>
                    <Badge variant="outline" className="mt-1">
                      {PHASES.find(p => p.id === session.currentPhase)?.title}
                    </Badge>
                  </div>
                  <div className="flex gap-2">
                    <Button onClick={() => handleLoadSession(session)}>
                      Load
                    </Button>
                    <Button 
                      variant="destructive" 
                      onClick={() => handleDeleteSession(session.id)}
                    >
                      Delete
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    )
  }

  if (showOutput && outputs) {
    return (
      <div className="container mx-auto p-6 max-w-4xl">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold">{currentSession.title} - Output</h1>
          <Button onClick={() => setShowOutput(false)}>
            Back to Session
          </Button>
        </div>

        <Tabs defaultValue="markdown" className="w-full">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="markdown">Markdown</TabsTrigger>
            <TabsTrigger value="json">JSON</TabsTrigger>
            <TabsTrigger value="ai-prompt">AI Prompt</TabsTrigger>
          </TabsList>
          
          <TabsContent value="markdown" className="mt-4">
            <div className="border rounded-lg p-4">
              <pre className="whitespace-pre-wrap text-sm">{outputs.markdown}</pre>
            </div>
          </TabsContent>
          
          <TabsContent value="json" className="mt-4">
            <div className="border rounded-lg p-4">
              <pre className="whitespace-pre-wrap text-sm font-mono">{outputs.json}</pre>
            </div>
          </TabsContent>
          
          <TabsContent value="ai-prompt" className="mt-4">
            <div className="border rounded-lg p-4">
              <pre className="whitespace-pre-wrap text-sm">{outputs.aiPrompt}</pre>
            </div>
          </TabsContent>
        </Tabs>
      </div>
    )
  }

  return (
    <div className="container mx-auto p-6 max-w-4xl">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">{currentSession.title}</h1>
        <div className="flex gap-2">
          <Button onClick={handleGenerateOutput}>
            Generate Output
          </Button>
          <Button variant="outline" onClick={() => setCurrentSession(null)}>
            Back to Sessions
          </Button>
        </div>
      </div>

      <div className="mb-6">
        <div className="flex gap-2 mb-4">
          {PHASES.map((phase) => (
            <Button
              key={phase.id}
              variant={phase.id === currentSession.currentPhase ? "default" : "outline"}
              onClick={() => handlePhaseChange(phase.id)}
            >
              {phase.title}
            </Button>
          ))}
        </div>
      </div>

      {currentPhase && (
        <div>
          <div className="mb-6">
            <h2 className="text-2xl font-semibold mb-2">{currentPhase.title}</h2>
            <p className="text-muted-foreground">{currentPhase.description}</p>
          </div>

          <div className="space-y-6">
            {currentPhase.questions.map((question) => (
              <div key={question.id}>
                <label className="block text-sm font-medium mb-2">
                  {question.text}
                  {question.required && <span className="text-red-500 ml-1">*</span>}
                </label>
                <Textarea
                  placeholder={question.placeholder}
                  value={currentSession.answers[question.id] || ''}
                  onChange={(e) => handleAnswerChange(question.id, e.target.value)}
                  className="min-h-[100px]"
                />
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
