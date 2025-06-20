"""Simple manager for sequencing tasks.

This component is intentionally small but can be extended to support more
complex workflows.
"""

from typing import List


class TaskGraphManager:
    """Maintain a list of tasks and process them sequentially."""

    def __init__(self, tasks: List[str]):
        self.tasks = tasks
        self.index = 0

    def next_task(self):
        if self.index >= len(self.tasks):
            return None
        task = self.tasks[self.index]
        self.index += 1
        return task
