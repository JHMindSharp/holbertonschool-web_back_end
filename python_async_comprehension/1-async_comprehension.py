#!/usr/bin/env python3
"""
This module demonstrates the use of asynchronous comprehensions to collect
values from an asynchronous generator.
"""

import asyncio
from typing import List
import importlib

async_generator = importlib.import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Uses an async comprehension to collect 10 random numbers
    from async_generator."""
    return [i async for i in async_generator()]
