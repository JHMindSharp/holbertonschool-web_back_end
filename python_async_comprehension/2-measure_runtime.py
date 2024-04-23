#!/usr/bin/env python3
"""
This module measures the total execution time of running four asynchronous
comprehensions in parallel.
"""

import asyncio
import time
import importlib

async_comprehension = importlib.import_module(
    "1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel and measure the
    total runtime.

    Returns:
        float: The total time taken to execute all four comprehensions.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
