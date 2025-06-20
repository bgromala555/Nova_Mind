"""Memory management for agents.

This module provides short-term memory (in-memory list) and long-term
memory persisted to disk as JSON. Used primarily by :mod:`agents.vera` but
accessible to any agent that requires persistent state.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List


class MemoryManager:
    """Handles read/write operations for agent memory."""

    def __init__(self, long_term_path: str = "memory/long_term_memory.json") -> None:
        self.path = Path(long_term_path)
        self.short_term: List[str] = []
        self._load_memory()

    def _load_memory(self) -> None:
        if self.path.exists():
            self.long_term = json.loads(self.path.read_text())
        else:
            self.long_term = {}

    def store_reflection(self, text: str) -> None:
        """Persist a reflection to long-term memory and cache in short-term."""
        self.short_term.append(text)
        self.long_term.setdefault("reflections", []).append(text)
        self.path.write_text(json.dumps(self.long_term, indent=2))

    def get_reflections(self) -> List[str]:
        return self.long_term.get("reflections", [])
