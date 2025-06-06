"""Demonstration script for the memory graph system."""

from memory_graph import MemoryGraph, MemoryNode, DecayEngine, Vectorizer


def main() -> None:
    vect = Vectorizer()
    graph = MemoryGraph()

    texts = [
        "A + B = C",
        "How to plan daily?",
        "How do you estimate time?",
    ]
    embeddings = vect.embed(texts)

    for idx, text in enumerate(texts):
        node = MemoryNode(id=str(idx), content=text, vector=embeddings[idx])
        graph.add_memory(node)

    # Connect related nodes
    graph.connect("1", "2", relation="similar")

    # Run a decay cycle
    decay = DecayEngine(graph)
    decay.run()

    for node_id in graph.graph.nodes:
        node = graph.get_node(node_id)
        print(node_id, node.content, node.weight)


if __name__ == "__main__":
    main()
