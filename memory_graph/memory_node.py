from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional
import numpy as np


def default_vector() -> np.ndarray:
    return np.zeros(384)


@dataclass
class MemoryNode:
    """Representation of a memory unit in the graph."""

    id: str
    content: str
    weight: float = 1.0
    decay_rate: float = 0.01
    vector: np.ndarray = field(default_factory=default_vector)
    topic: Optional[str] = None
    links: List[str] = field(default_factory=list)

    def decay(self, steps: int = 1) -> None:
        """Apply decay to the node's weight."""
        self.weight *= (1 - self.decay_rate) ** steps

    def reinforce(self, amount: float = 1.0) -> None:
        """Increase the node's weight when referenced."""
        self.weight += amount
