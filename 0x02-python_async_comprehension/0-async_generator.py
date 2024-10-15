#!/usr/bin/env python3
'''
an async generator with no arguments
'''


import random
import time
import asyncio
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Yields a random floating point number between 0 and 10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
