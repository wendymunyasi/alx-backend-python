#!/usr/bin/env python3
"""Module for task 3
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that takes an integer max_delay and returns a asyncio.Task.

    Args:
        max_delay (int):  The maximum delay to wait for, in seconds.

    Returns:
        asyncio.Task: An asyncio.Task that asynchronously waits for
        a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
