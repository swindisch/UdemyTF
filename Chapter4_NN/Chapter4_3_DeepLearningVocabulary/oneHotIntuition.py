from typing import Tuple

import numpy as np


def get_dataset() -> Tuple[np.ndarray, np.ndarray]:
    """OR dataset."""
    x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    y = np.array([[0], [1], [1], [1]])
    return x, y


def to_one_hot(y: np.ndarray, num_classes: int) -> np.ndarray:
    y_one_hot = np.zeros(shape=(len(y), num_classes))  # 4x2
    for i, y_i in enumerate(y):
        y_oh = np.zeros(shape=num_classes)
        y_oh[y_i] = 1
        y_one_hot[i] = y_oh
    return y_one_hot


if __name__ == "__main__":
    pass
