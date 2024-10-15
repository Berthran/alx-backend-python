#!/usr/bin/env python3
'''
change wait_n to task_n
'''

import random
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes task_wait_random n times concurrently and return
    a sorted list of delays.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)  # Sort and return the list of delays
