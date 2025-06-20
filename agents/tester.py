"""Testing agent used to verify outputs or run checks."""

from agents.agent_base import Agent


class TesterAgent(Agent):
    """Simple agent to simulate testing behaviour."""

    def __init__(self) -> None:
        super().__init__(name="TesterAgent", role="Testing")

    def act(self, input_data, context):
        return f"Tested: {input_data} -> success"
