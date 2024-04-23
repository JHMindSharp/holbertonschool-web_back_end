#!/usr/bin/env python3
"""
This module alters the wait_n function to use asyncio tasks.
"""

import asyncio
from random import uniform
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio task from the wait_random coroutine."""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times with the specified max_delay
    and gathers results."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    async def main():
        n = 5
        max_delay = 6
        results = await task_wait_n(n, max_delay)
        print(results)

    asyncio.run(main())
