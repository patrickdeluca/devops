```python
from rich.console import Console
from rich.prompt import Prompt

class UserInterface:
    def __init__(self):
        self.console = Console()
        self.chat_history = []

    def display_message(self, sender, message):
        self.console.print(f"{sender}: {message}")
        self.chat_history.append((sender, message))

    def get_user_input(self):
        user_input = Prompt.ask("User")
        self.display_message("User", user_input)
        return user_input

    def display_chat_history(self):
        self.console.print("\nChat History:")
        for sender, message in self.chat_history:
            self.console.print(f"{sender}: {message}")

def design_interface():
    ui = UserInterface()
    return ui
```