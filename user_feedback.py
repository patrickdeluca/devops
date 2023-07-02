```python
from rich.prompt import Prompt
from rich.console import Console

console = Console()

class UserFeedback:
    def __init__(self):
        self.feedback_data = []

    def capture_feedback(self):
        console.print("We value your feedback to improve our service.")
        feedback = Prompt.ask("Please provide your feedback")
        self.feedback_data.append(feedback)
        console.print("Thank you for your feedback!")

    def get_feedback_data(self):
        return self.feedback_data

if __name__ == "__main__":
    feedback = UserFeedback()
    feedback.capture_feedback()
```