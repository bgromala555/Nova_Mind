"""Planning agent that decides which specialised agent should handle a task."""

from typing import Dict

from agents.agent_base import Agent


class Smith(Agent):
    """Planner agent responsible for task routing."""

    def __init__(self) -> None:
        super().__init__(name="Smith", role="Planner")

    def act(self, input_data: str, context: Dict) -> Dict:
        """Return routing decision based on simple keyword checks."""
        lower = input_data.lower()
        if any(word in lower for word in ["calculate", "sum", "math"]):
            route = "Math"
        elif any(word in lower for word in ["code", "python", "function"]):
            route = "Code"
        elif any(word in lower for word in ["test", "verify"]):
            route = "Tester"
        else:
            route = "Vera"
        return {"route_to": route, "task": input_data}
