#!/usr/bin/env python3
'''
Add timer to wait n
'''

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns
    the average time per task.

    :param n: Number of times to run the wait_random function.
    :param max_delay: Maximum delay for each task.
    :return: Average time per task (float).
    """
    # Start the timer
    start_time = time.perf_counter()

    # Run the wait_n function using asyncio.run to execute it
    asyncio.run(wait_n(n, max_delay))

    # Stop the timer and calculate the elapsed time
    total_time = time.perf_counter() - start_time

    # Return the average time (total_time / n)
    return total_time / n
