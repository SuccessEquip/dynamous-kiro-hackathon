"""Main CORE Framework TUI Application - Simplified and Working"""

import json
import uuid
from datetime import datetime
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer, Button, Static, Input, Label
from textual.screen import Screen
from textual.binding import Binding

from .models import (
    SessionData, SessionMetadata, Answer, Question, PhaseType, 
    ImplementationType, SessionStatus, QUESTIONS_BY_PHASE
)
from .output_generator import OutputGenerator


class QuestionScreen(Screen):
    """Screen for answering a single question"""
    
    BINDINGS = [
        Binding("ctrl+s", "save_and_next", "Save & Next"),
        Binding("escape", "back", "Back"),
    ]
    
    def __init__(self, question: Question, session_data: SessionData, phase_index: int, question_index: int, total_questions: int):
        super().__init__()
        self.question = question
        self.session_data = session_data
        self.phase_index = phase_index
        self.question_index = question_index
        self.total_questions = total_questions
        self.answer_text = self.get_existing_answer()
    
    def get_existing_answer(self) -> str:
        for answer in self.session_data.answers:
            if answer.question_id == self.question.id:
                return answer.response
        return ""
    
    def compose(self) -> ComposeResult:
        phases = ["Clarify", "Organize", "Refine", "Equip"]
        yield Header()
        
        with ScrollableContainer():
            yield Static(f"[bold cyan]Phase {self.phase_index + 1}/4: {phases[self.phase_index]}[/bold cyan]")
            yield Static(f"Question {self.question_index + 1}/{self.total_questions}")
            yield Static("")
            yield Static(f"[bold]{self.question.text}[/bold]")
            yield Static(f"[dim]{self.question.guidance}[/dim]")
            yield Static("")
            yield Static("[yellow]Type your answer below (Ctrl+S to save & continue):[/yellow]")
            yield Input(
                value=self.answer_text,
                placeholder="Enter your answer here...",
                id="answer-input"
            )
            yield Static("")
            yield Button("Save & Next →", id="next-btn", variant="primary")
            yield Button("← Back", id="back-btn", variant="default")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "next-btn":
            self.action_save_and_next()
        elif event.button.id == "back-btn":
            self.action_back()
    
    def action_save_and_next(self):
        input_widget = self.query_one("#answer-input", Input)
        answer_text = input_widget.value.strip()
        
        if len(answer_text) < 10:
            self.notify("Please provide a more detailed answer (at least 10 characters)", severity="warning")
            return
        
        # Save answer
        existing_answer = None
        for answer in self.session_data.answers:
            if answer.question_id == self.question.id:
                existing_answer = answer
                break
        
        if existing_answer:
            existing_answer.response = answer_text
            existing_answer.answered_at = datetime.now()
        else:
            new_answer = Answer(
                question_id=self.question.id,
                response=answer_text,
                answered_at=datetime.now(),
                confidence=4
            )
            self.session_data.answers.append(new_answer)
        
        self.session_data.session.updated_at = datetime.now()
        self.dismiss(True)
    
    def action_back(self):
        self.dismiss(False)


class PhaseMenuScreen(Screen):
    """Menu for selecting which phase to work on"""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("ctrl+s", "save", "Save"),
    ]
    
    def __init__(self, session_data: SessionData):
        super().__init__()
        self.session_data = session_data
        self.phases = [
            (PhaseType.CLARIFY, "Clarify", "Define your project vision and goals"),
            (PhaseType.ORGANIZE, "Organize", "Structure features and requirements"),
            (PhaseType.REFINE, "Refine", "Analyze risks and constraints"),
        ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        
        with ScrollableContainer():
            yield Static("[bold cyan]CORE Framework - Project Planning[/bold cyan]")
            yield Static(f"Session: {self.session_data.session.name}")
            yield Static("")
            yield Static("[bold]Select a phase to work on:[/bold]")
            yield Static("")
            
            for i, (phase_type, name, desc) in enumerate(self.phases):
                questions = QUESTIONS_BY_PHASE[phase_type]
                answered = sum(1 for q in questions if any(a.question_id == q.id for a in self.session_data.answers))
                total = len(questions)
                
                status = f"[green]✓[/green]" if answered == total else f"[yellow]{answered}/{total}[/yellow]"
                yield Button(f"{status} Phase {i+1}: {name} - {desc}", id=f"phase-{i}", variant="primary" if answered < total else "default")
            
            yield Static("")
            yield Button("Save Session", id="save-btn", variant="success")
            yield Button("Generate Output", id="output-btn", variant="primary")
            yield Button("Exit", id="exit-btn", variant="default")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id.startswith("phase-"):
            phase_index = int(event.button.id.split("-")[1])
            self.start_phase(phase_index)
        elif event.button.id == "save-btn":
            self.action_save()
        elif event.button.id == "output-btn":
            self.generate_output()
        elif event.button.id == "exit-btn":
            self.app.exit()
    
    def start_phase(self, phase_index: int):
        phase_type = self.phases[phase_index][0]
        questions = QUESTIONS_BY_PHASE[phase_type]
        
        # Start with first question
        self.show_question(phase_index, 0, questions)
    
    def show_question(self, phase_index: int, question_index: int, questions: list):
        if question_index >= len(questions):
            self.notify(f"Phase {phase_index + 1} complete!", severity="information")
            return
        
        question = questions[question_index]
        screen = QuestionScreen(question, self.session_data, phase_index, question_index, len(questions))
        
        def on_question_complete(should_continue):
            if should_continue:
                self.show_question(phase_index, question_index + 1, questions)
        
        self.app.push_screen(screen, on_question_complete)
    
    def action_save(self):
        try:
            filename = f"core_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(self.session_data.model_dump(), f, indent=2, default=str)
            self.notify(f"Saved to {filename}", severity="information")
        except Exception as e:
            self.notify(f"Error saving: {str(e)}", severity="error")
    
    def generate_output(self):
        try:
            generator = OutputGenerator(self.session_data)
            output = generator.generate_markdown()
            
            filename = f"core_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(filename, 'w') as f:
                f.write(output)
            
            self.notify(f"Output saved to {filename}", severity="information")
        except Exception as e:
            self.notify(f"Error generating output: {str(e)}", severity="error")
    
    def action_back(self):
        self.app.pop_screen()


class COREFrameworkApp(App):
    """Main CORE Framework TUI Application"""
    
    CSS = """
    Screen {
        align: center top;
    }
    
    ScrollableContainer {
        width: 100%;
        height: 100%;
        padding: 1 2;
    }
    
    Static {
        width: 100%;
        margin-bottom: 1;
    }
    
    Input {
        width: 100%;
        margin-bottom: 1;
    }
    
    Button {
        width: 100%;
        margin-bottom: 1;
    }
    """
    
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
    ]
    
    def __init__(self):
        super().__init__()
        self.session_data = self.create_new_session()
    
    def create_new_session(self) -> SessionData:
        session_id = str(uuid.uuid4())
        return SessionData(
            session=SessionMetadata(
                id=session_id,
                name="New Project",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                version="1.0.0",
                implementation=ImplementationType.V2_PYTHON,
                status=SessionStatus.DRAFT
            )
        )
    
    def on_mount(self):
        self.push_screen(PhaseMenuScreen(self.session_data))


def main():
    app = COREFrameworkApp()
    app.run()


if __name__ == "__main__":
    main()
