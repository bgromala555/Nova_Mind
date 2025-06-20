"""Agent that handles code generation or analysis tasks."""

from agents.agent_base import Agent


class CodeAgent(Agent):
    """Stub for coding-related tasks."""

    def __init__(self) -> None:
        super().__init__(name="CodeAgent", role="Coding")

    def act(self, input_data, context):
        # Placeholder behaviour
        return f"Generated code in response to: {input_data}"
