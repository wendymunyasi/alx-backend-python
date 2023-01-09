#!/usr/bin/env python3
"""Module for task 2
"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function that measures the total execution time for wait_n.

    Args:
        n (int): The number of times to wait.
        max_delay (int):  The maximum delay to wait for, in seconds.

    Returns:
        float:  The average time taken to execute `wait_n` for
        each iteration, in seconds.total_time/n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return (total_time) / n
