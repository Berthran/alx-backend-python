#!/usr/bin/env python3
'''
Execute multiple coroutines at the same time
'''


import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int,  max_delay: int) -> List[float]:
    '''
    return the list of all the delays (float values).
    '''
    delays = []
    for i in range(n):
        # delay = await wait_random(max_delay)
        # delays.append(delay)
        delay = await asyncio.gather(*(wait_random(max_delay)
                                       for i in range(n)))
    # delays.sort()
    delay.sort()
    # return (delays)
    return (delay)
