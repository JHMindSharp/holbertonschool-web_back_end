#!/usr/bin/env python3
"""File helper function."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end index for the given page and page_size.

    Args:
        page: An integer representing the page number.
        page_size: An integer representing the size of each page.

    Returns:
        A tuple of two integers representing the start and end indices.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
