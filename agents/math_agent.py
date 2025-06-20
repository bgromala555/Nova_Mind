"""Simple agent capable of performing basic arithmetic."""

from agents.agent_base import Agent


class MathAgent(Agent):
    """Performs mathematical calculations."""

    def __init__(self) -> None:
        super().__init__(name="MathAgent", role="Mathematics")

    def act(self, input_data, context):
        try:
            result = eval(input_data)
            return f"Result: {result}"
        except Exception as exc:
            return f"Math error: {exc}"
