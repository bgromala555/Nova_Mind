"""Reflection agent responsible for summarising lessons and storing insights."""

from agents.agent_base import Agent
from memory.memory_manager import MemoryManager


class Vera(Agent):
    """Reflective agent that records outcomes for future improvement."""

    def __init__(self) -> None:
        super().__init__(name="Vera", role="Reflection")
        self.memory = MemoryManager()

    def act(self, input_data, context):
        """Generate a reflection and store it in long-term memory."""
        reflection = f"Reflected on: {input_data} with context: {context}"
        self.memory.store_reflection(reflection)
        return reflection
