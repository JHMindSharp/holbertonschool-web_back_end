#!/usr/bin/env python3
"""
This module provides a function to create asyncio tasks.
"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task from the wait_random
    coroutine."""
    return asyncio.create_task(wait_random(max_delay))
