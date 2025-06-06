from __future__ import annotations

from .memory_graph import MemoryGraph


class DecayEngine:
    """Simple decay cycle runner."""

    def __init__(self, graph: MemoryGraph, steps: int = 1) -> None:
        self.graph = graph
        self.steps = steps

    def run(self) -> None:
        self.graph.decay_all(steps=self.steps)
        self.graph.remove_low_weight()
