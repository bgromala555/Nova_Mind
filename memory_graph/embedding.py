from __future__ import annotations

from typing import Iterable, List

import numpy as np


class Vectorizer:
    """Basic interface for generating semantic vectors."""

    def embed(self, texts: Iterable[str]) -> List[np.ndarray]:
        """Generate embeddings for a list of texts.

        This implementation is a placeholder. Replace with calls to your
        embedding model (e.g. OLAMMA or sentence-transformers).
        """
        # TODO: connect to real embedding model
        return [np.zeros(384) for _ in texts]
