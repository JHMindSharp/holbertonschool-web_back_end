#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that waits for a random delay.
"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay
    up to max_delay seconds."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    asyncio.run(wait_random())
