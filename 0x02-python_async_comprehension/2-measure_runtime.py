#!/usr/bin/env python3
"""Module for task 2
"""


import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """_This is a coroutine that measures the total runtime of executing
    async_comprehension four times in parallel using asyncio.gather.

    Returns:
        float:  The total runtime in seconds as float.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
