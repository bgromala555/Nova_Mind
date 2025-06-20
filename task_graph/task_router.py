"""Lightweight task router used by :class:`agents.smith.Smith`."""

from typing import Dict

from agents.code_agent import CodeAgent
from agents.math_agent import MathAgent
from agents.tester import TesterAgent
from agents.vera import Vera


class TaskRouter:
    """Instantiate and dispatch tasks to domain-specific agents."""

    def __init__(self) -> None:
        self.agents = {
            "Code": CodeAgent(),
            "Math": MathAgent(),
            "Tester": TesterAgent(),
            "Vera": Vera(),
        }

    def dispatch(self, decision: Dict) -> str:
        agent_name = decision.get("route_to")
        agent = self.agents.get(agent_name)
        if not agent:
            return f"Unknown agent: {agent_name}"
        return agent.act(decision["task"], context={})
