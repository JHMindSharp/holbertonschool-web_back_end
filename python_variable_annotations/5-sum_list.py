#!/usr/bin/env python3
"""
This module provides a function to sum a list
of floating-point numbers.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum all the floats in a list.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all the floats in the list.
    """
    return sum(input_list)
