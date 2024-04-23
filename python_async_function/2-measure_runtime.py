#!/usr/bin/env python3
"""
This module measures the total execution time for wait_n coroutine.
"""

import asyncio
import time
from typing import Callable, List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Placeholder for wait_n function from previous task."""
    pass


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n and returns
    average time per call."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n


if __name__ == "__main__":
    print(measure_time(5, 9))
