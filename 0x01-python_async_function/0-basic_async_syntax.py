#!/usr/bin/env python3
'''
Create a simple asyncronous in Python
'''


import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    '''
    waits for a random delay between 0 and max_delay
    seconds and eventually returns it
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    print('wait_random delayed for {} secs'.format(delay))
    return (delay)
