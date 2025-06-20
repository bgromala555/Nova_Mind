"""Utility for turning stored reflections into training samples."""

from memory.memory_manager import MemoryManager


def generate_dataset(output_path: str = "training/dataset.jsonl") -> None:
    """Export reflections to a JSONL file for later fine-tuning."""
    memory = MemoryManager()
    reflections = memory.get_reflections()
    with open(output_path, "w") as f:
        for text in reflections:
            f.write('{"text": ' + f'"{text}"' + '}\n')
    print(f"Wrote {len(reflections)} samples to {output_path}")


if __name__ == "__main__":
    generate_dataset()
