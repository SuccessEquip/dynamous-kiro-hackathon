"""Main CORE Framework TUI Application"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Button, Static, TextArea, RadioSet, RadioButton
from textual.screen import Screen
from textual.binding import Binding
from rich.text import Text
from rich.panel import Panel

from .models import (
    SessionData, SessionMetadata, Answer, Question, PhaseType, 
    ImplementationType, SessionStatus, QUESTIONS_BY_PHASE, QUESTIONS_BY_ID
)
from .output_generator import OutputGenerator


class ProgressWidget(Static):
    """Progress indicator showing current phase"""
    
    def __init__(self, current_phase: int = 0):
        super().__init__()
        self.current_phase = current_phase
        self.phases = ["Clarify", "Organize", "Refine", "Equip"]
    
    def compose(self) -> ComposeResult:
        yield Static(self.render_progress())
    
    def render_progress(self) -> Text:
        text = Text()
        for i, phase in enumerate(self.phases):
            if i == self.current_phase:
                text.append(f"● {phase}", style="bold blue")
            elif i < self.current_phase:
                text.append(f"✓ {phase}", style="green")
            else:
                text.append(f"○ {phase}", style="dim")
            
            if i < len(self.phases) - 1:
                text.append(" → ")
        
        return text
    
    def update_phase(self, phase: int):
        self.current_phase = phase
        self.update(self.render_progress())


class QuestionWidget(Container):
    """Widget for displaying and answering a single question"""
    
    def __init__(self, question: Question, answer: str = ""):
        super().__init__()
        self.question = question
        self.answer_text = answer
    
    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static(f"[bold]{self.question.text}[/bold]", classes="question-text")
            yield Static(f"[dim]{self.question.guidance}[/dim]", classes="guidance")
            yield TextArea(
                self.answer_text,
                id=f"answer-{self.question.id}",
                classes="answer-input"
            )
    
    def get_answer(self) -> str:
        textarea = self.query_one(f"#answer-{self.question.id}", TextArea)
        return textarea.text
    
    def validate_answer(self) -> tuple[bool, str]:
        answer = self.get_answer().strip()
        if len(answer) < self.question.min_length:
            return False, f"Please provide at least {self.question.min_length} characters."
        if len(answer) > self.question.max_length:
            return False, f"Please keep your response under {self.question.max_length} characters."
        return True, ""


class PhaseScreen(Screen):
    """Base screen for each phase"""
    
    BINDINGS = [
        Binding("ctrl+p", "previous_phase", "Previous"),
        Binding("ctrl+n", "next_phase", "Next"),
        Binding("ctrl+s", "save_session", "Save"),
        Binding("escape", "app.pop_screen", "Back"),
    ]
    
    def __init__(self, phase: PhaseType, session_data: SessionData):
        super().__init__()
        self.phase = phase
        self.session_data = session_data
        self.questions = QUESTIONS_BY_PHASE[phase]
        self.question_widgets = []
    
    def compose(self) -> ComposeResult:
        phase_names = {
            PhaseType.CLARIFY: "Clarify",
            PhaseType.ORGANIZE: "Organize", 
            PhaseType.REFINE: "Refine",
            PhaseType.EQUIP: "Equip"
        }
        
        yield Header()
        
        with Container():
            yield Static(f"[bold blue]Phase: {phase_names[self.phase]}[/bold blue]", classes="phase-title")
            
            # Create question widgets
            for question in self.questions:
                existing_answer = self.get_existing_answer(question.id)
                widget = QuestionWidget(question, existing_answer)
                self.question_widgets.append(widget)
                yield widget
            
            # Navigation buttons
            with Horizontal(classes="navigation"):
                yield Button("Previous", id="prev-btn", variant="default")
                yield Button("Next", id="next-btn", variant="primary")
        
        yield Footer()
    
    def get_existing_answer(self, question_id: str) -> str:
        """Get existing answer for a question"""
        for answer in self.session_data.answers:
            if answer.question_id == question_id:
                return answer.response
        return ""
    
    def save_answers(self):
        """Save current answers to session data"""
        for widget in self.question_widgets:
            answer_text = widget.get_answer().strip()
            if answer_text:
                # Update or create answer
                existing_answer = None
                for answer in self.session_data.answers:
                    if answer.question_id == widget.question.id:
                        existing_answer = answer
                        break
                
                if existing_answer:
                    existing_answer.response = answer_text
                    existing_answer.answered_at = datetime.now()
                else:
                    new_answer = Answer(
                        question_id=widget.question.id,
                        response=answer_text,
                        answered_at=datetime.now(),
                        confidence=4
                    )
                    self.session_data.answers.append(new_answer)
        
        self.session_data.session.updated_at = datetime.now()
    
    def validate_phase(self) -> tuple[bool, list[str]]:
        """Validate all answers in this phase"""
        errors = []
        for widget in self.question_widgets:
            is_valid, error = widget.validate_answer()
            if not is_valid:
                errors.append(f"{widget.question.id}: {error}")
        return len(errors) == 0, errors
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "prev-btn":
            self.action_previous_phase()
        elif event.button.id == "next-btn":
            self.action_next_phase()
    
    def action_previous_phase(self):
        self.save_answers()
        self.app.pop_screen()
    
    def action_next_phase(self):
        is_valid, errors = self.validate_phase()
        if is_valid:
            self.save_answers()
            self.app.pop_screen()
        else:
            # Show validation errors
            error_text = "\n".join(errors)
            self.notify(f"Please fix the following errors:\n{error_text}", severity="error")
    
    def action_save_session(self):
        self.save_answers()
        self.app.save_session()
        self.notify("Session saved!", severity="information")


class EquipScreen(Screen):
    """Special screen for the Equip phase with output generation"""
    
    BINDINGS = [
        Binding("ctrl+p", "previous_phase", "Previous"),
        Binding("ctrl+g", "generate_output", "Generate"),
        Binding("ctrl+s", "save_session", "Save"),
        Binding("escape", "app.pop_screen", "Back"),
    ]
    
    def __init__(self, session_data: SessionData):
        super().__init__()
        self.session_data = session_data
        self.output_generator = OutputGenerator(session_data)
    
    def compose(self) -> ComposeResult:
        yield Header()
        
        with Container():
            yield Static("[bold blue]Phase: Equip[/bold blue]", classes="phase-title")
            yield Static("Generate implementation documentation", classes="phase-description")
            
            with Vertical():
                yield Static("[bold]Choose Output Format:[/bold]")
                with RadioSet(id="output-format"):
                    yield RadioButton("Project Documentation (Markdown)", value="markdown")
                    yield RadioButton("Structured Data Export (JSON)", value="json") 
                    yield RadioButton("AI Implementation Prompt", value="ai_prompt")
                    yield RadioButton("Complete Documentation Package", value="all")
            
            with Horizontal(classes="navigation"):
                yield Button("Previous", id="prev-btn", variant="default")
                yield Button("Generate", id="generate-btn", variant="primary")
            
            yield TextArea("", id="output-display", read_only=True, classes="output-area")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "prev-btn":
            self.action_previous_phase()
        elif event.button.id == "generate-btn":
            self.action_generate_output()
    
    def action_previous_phase(self):
        self.app.pop_screen()
    
    def action_generate_output(self):
        radio_set = self.query_one("#output-format", RadioSet)
        selected_format = radio_set.pressed_button.value if radio_set.pressed_button else "markdown"
        
        try:
            if selected_format == "markdown":
                output = self.output_generator.generate_markdown()
            elif selected_format == "json":
                output = self.output_generator.generate_json()
            elif selected_format == "ai_prompt":
                output = self.output_generator.generate_ai_prompt()
            else:  # all
                output = self.output_generator.generate_all_formats()
            
            output_area = self.query_one("#output-display", TextArea)
            output_area.text = output
            
            # Save to file
            filename = self.save_output_to_file(output, selected_format)
            self.notify(f"Output generated and saved to {filename}", severity="information")
            
        except Exception as e:
            self.notify(f"Error generating output: {str(e)}", severity="error")
    
    def save_output_to_file(self, content: str, format_type: str) -> str:
        """Save output to file and return filename"""
        session_name = self.session_data.session.name.replace(" ", "_").lower()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        extensions = {
            "markdown": "md",
            "json": "json", 
            "ai_prompt": "txt",
            "all": "txt"
        }
        
        filename = f"core_framework_{session_name}_{timestamp}.{extensions.get(format_type, 'txt')}"
        filepath = Path(filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filename
    
    def action_save_session(self):
        self.app.save_session()
        self.notify("Session saved!", severity="information")


class COREFrameworkApp(App):
    """Main CORE Framework TUI Application"""
    
    CSS = """
    .phase-title {
        text-align: center;
        margin: 1;
    }
    
    .phase-description {
        text-align: center;
        margin-bottom: 1;
    }
    
    .question-text {
        margin-bottom: 1;
    }
    
    .guidance {
        margin-bottom: 1;
    }
    
    .answer-input {
        height: 6;
        margin-bottom: 2;
    }
    
    .navigation {
        height: 3;
        align: center middle;
    }
    
    .output-area {
        height: 20;
        margin-top: 1;
    }
    """
    
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
        Binding("ctrl+s", "save_session", "Save"),
        Binding("ctrl+l", "load_session", "Load"),
    ]
    
    def __init__(self):
        super().__init__()
        self.session_data = self.create_new_session()
        self.current_phase = 0
        self.phases = [PhaseType.CLARIFY, PhaseType.ORGANIZE, PhaseType.REFINE, PhaseType.EQUIP]
    
    def create_new_session(self) -> SessionData:
        """Create a new session with default data"""
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
    
    def compose(self) -> ComposeResult:
        yield Header()
        
        with Container():
            yield ProgressWidget(self.current_phase)
            yield Static("[bold]CORE Framework - Interactive Project Planning[/bold]", classes="phase-title")
            yield Static("Transform vague ideas into actionable project plans", classes="phase-description")
            
            with Horizontal(classes="navigation"):
                yield Button("Start Clarify", id="start-btn", variant="primary")
                yield Button("Load Session", id="load-btn", variant="default")
                yield Button("Quit", id="quit-btn", variant="default")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start-btn":
            self.start_phase(0)
        elif event.button.id == "load-btn":
            self.action_load_session()
        elif event.button.id == "quit-btn":
            self.exit()
    
    def start_phase(self, phase_index: int):
        """Start a specific phase"""
        self.current_phase = phase_index
        
        if phase_index < 3:  # Clarify, Organize, Refine
            phase_type = self.phases[phase_index]
            screen = PhaseScreen(phase_type, self.session_data)
        else:  # Equip
            screen = EquipScreen(self.session_data)
        
        self.push_screen(screen, callback=self.on_phase_complete)
    
    def on_phase_complete(self, result=None):
        """Called when a phase screen is popped"""
        if self.current_phase < 3:
            self.current_phase += 1
            # Update progress widget
            progress = self.query_one(ProgressWidget)
            progress.update_phase(self.current_phase)
            
            # Auto-advance to next phase
            if self.current_phase < 4:
                self.start_phase(self.current_phase)
        else:
            # All phases complete
            self.notify("All phases completed! Session saved.", severity="information")
            self.save_session()
    
    def save_session(self):
        """Save session to JSON file"""
        try:
            filename = f"core_framework_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.session_data.model_dump(), f, indent=2, default=str)
            self.notify(f"Session saved to {filename}", severity="information")
        except Exception as e:
            self.notify(f"Error saving session: {str(e)}", severity="error")
    
    def action_load_session(self):
        """Load session from JSON file (simplified - would need file picker in real implementation)"""
        self.notify("Load session functionality would open a file picker", severity="information")
    
    def action_save_session(self):
        self.save_session()


def main():
    """Main entry point"""
    app = COREFrameworkApp()
    app.run()


if __name__ == "__main__":
    main()
