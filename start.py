"""Entry point for the vera-agentic-system.

This script wires together the planner (:class:`agents.smith.Smith`) with the
:class:`task_graph.task_router.TaskRouter` to handle user tasks.
"""

from agents import smith
from task_graph.task_router import TaskRouter


def main() -> None:
    router = TaskRouter()
    planner = smith.Smith()

    task = input("Enter a task: ")
    decision = planner.act(task, context={})
    print(f"Smith routed task to: {decision['route_to']}")

    output = router.dispatch(decision)
    print("Agent output:", output)


if __name__ == "__main__":
    main()
