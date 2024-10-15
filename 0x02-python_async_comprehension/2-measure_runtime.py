#!/usr/bin/env python3
'''
an async generator with no arguments
'''


import time
import random
import asyncio
from typing import AsyncGenerator, List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Returns the time it takes to run async_comprehension 4 times
    '''
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop_time = time.perf_counter()
    return (stop_time - start_time)
