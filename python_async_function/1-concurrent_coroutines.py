#!/usr/bin/env python3
"""
This module provides a function to concurrently execute multiple coroutines.
"""

import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times with the specified max_delay
    and returns sorted delays."""
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await f for f in asyncio.as_completed(delays)]
