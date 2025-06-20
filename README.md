# Nova_Mind

This repository contains two experimental components:

1. **Intelligent Memory Graph** – a toy system that models a self-organising
   memory using `networkx`.
2. **vera-agentic-system** – a small collection of local agents that interact
   via a planner and share reflections via a persistent memory store.

## Memory Graph

- `memory_graph/` – core Python package
  - `memory_node.py` – dataclass describing a memory unit
  - `memory_graph.py` – simple graph wrapper using `networkx`
  - `embedding.py` – placeholder embedding interface
  - `decay_engine.py` – utility for applying decay cycles
- `example.py` – demonstration script

## Vera Agentic System

- `agents/` – Vera, Smith and domain-specific agents
- `memory/` – external memory management
- `task_graph/` – lightweight task routing utilities
- `training/` – helper scripts for generating training data
- `start.py` – entry point that wires everything together

### Usage

```bash
pip install -r requirements.txt
python start.py
```

Running `start.py` will ask for a task, route it through Smith and dispatch it to
the appropriate agent. Reflections are stored in `memory/long_term_memory.json`.
