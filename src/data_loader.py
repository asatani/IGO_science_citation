"""Data loading / saving helpers."""
import pickle
from pathlib import Path

import pandas as pd


def load_pickle(path):
    """Load a pandas object from a pickle file."""
    path = Path(path)
    with open(path, "rb") as f:
        obj = pickle.load(f)
    return obj


def save_pickle(obj, path):
    """Save a pandas object to a pickle file and print confirmation."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(obj, f)
    print(f"Saved: {path.resolve()}")
