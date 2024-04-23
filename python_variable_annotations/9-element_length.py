#!/usr/bin/env python3
"""
This module provides a function that returns the length
of each element in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Determine the length of each sequence in an iterable.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each
        containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
