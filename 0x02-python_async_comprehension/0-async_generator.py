#!/usr/bin/env python3
'''
an async generator with no arguments
'''


import random
import asyncio
from typing import AsyncGenerator


async def async_generator():
    '''
    Yields a random floating point number between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
