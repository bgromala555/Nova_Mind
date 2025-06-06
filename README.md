# Nova_Mind

This repository contains a prototype implementation of an **Intelligent Memory Graph System**. The goal is to model a self-organising memory similar to a mind that recalls, forgets, and links ideas over time.

## Structure

- `memory_graph/` – core Python package
  - `memory_node.py` – dataclass describing a memory unit
  - `memory_graph.py` – simple graph wrapper using `networkx`
  - `embedding.py` – placeholder embedding interface
  - `decay_engine.py` – utility for applying decay cycles
- `example.py` – demonstration script

## Quick Start

```bash
pip install -r requirements.txt
python example.py
```

The example shows how to create memory nodes, link them and run a decay cycle. Real semantic embeddings and additional behaviors can be built on top of this foundation.
