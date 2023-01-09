#!/usr/bin/env python3
"""Module for task 0
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay between 0 and
    max_delay (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int, optional): The max delay in seconds. Defaults to 10.

    Returns:
        float: The delay in seconds.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
