from __future__ import annotations

import networkx as nx
from typing import Iterable, Optional

from .memory_node import MemoryNode


class MemoryGraph:
    """Graph-based storage for memory nodes."""

    def __init__(self) -> None:
        self.graph = nx.DiGraph()

    def add_memory(self, node: MemoryNode) -> None:
        self.graph.add_node(node.id, data=node)

    def connect(self, src_id: str, dst_id: str, **attrs) -> None:
        self.graph.add_edge(src_id, dst_id, **attrs)

    def get_node(self, node_id: str) -> Optional[MemoryNode]:
        data = self.graph.nodes.get(node_id, {}).get("data")
        return data

    def decay_all(self, steps: int = 1) -> None:
        for _, data in self.graph.nodes(data=True):
            node: MemoryNode = data["data"]
            node.decay(steps=steps)

    def remove_low_weight(self, threshold: float = 0.1) -> None:
        to_remove = [n for n, d in self.graph.nodes(data=True) if d["data"].weight < threshold]
        self.graph.remove_nodes_from(to_remove)
