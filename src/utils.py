"""Shared utility functions."""

import numpy as np


def flatten(nested_list):
    """Flatten a list of lists (skips NaN sublists)."""
    return [item for sublist in nested_list if sublist == sublist for item in sublist]


# Alias kept for backward compatibility
flatten2 = flatten


def gini(x):
    """Calculate Gini coefficient (numpy-based, O(n log n))."""
    v = np.asarray(x, dtype=float)
    if v.size == 0:
        return np.nan
    if np.all(v == 0):
        return 0.0
    v = np.sort(v)
    n = v.size
    cum = np.cumsum(v)
    return (n + 1 - 2 * np.sum(cum) / cum[-1]) / n
