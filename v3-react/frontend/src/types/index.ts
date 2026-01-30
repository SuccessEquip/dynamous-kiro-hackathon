export interface Question {
  id: string;
  text: string;
  placeholder?: string;
  required?: boolean;
}

export interface Phase {
  id: string;
  title: string;
  description: string;
  questions: Question[];
}

export interface SessionData {
  id: string;
  title: string;
  currentPhase: string;
  answers: Record<string, string>;
  createdAt: string;
  updatedAt: string;
}

export interface OutputFormat {
  markdown: string;
  json: string;
  aiPrompt: string;
}
