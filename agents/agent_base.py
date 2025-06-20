from abc import ABC, abstractmethod

class Agent(ABC):
    """Abstract base class for all agents.

    Parameters
    ----------
    name : str
        Display name of the agent.
    role : str
        Short description of the agent's role within the system.
    """

    def __init__(self, name: str, role: str) -> None:
        self.name = name
        self.role = role

    @abstractmethod
    def act(self, input_data, context):
        """Perform the agent's primary action."""

    def receive(self, message: str) -> None:
        """Receive a message from another agent."""
        print(f"{self.name} received: {message}")
