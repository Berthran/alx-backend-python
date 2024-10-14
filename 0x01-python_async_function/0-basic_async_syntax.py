#!/usr/bin/env python3
'''
Create a simple asyncronous in Python
'''


import random
import asyncio
from typings import Awaitable


async def wait_random(max_delay: int=10) -> Awaitable[float]:
    '''
    waits for a random delay between 0 and max_delay
    seconds and eventually returns it
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
