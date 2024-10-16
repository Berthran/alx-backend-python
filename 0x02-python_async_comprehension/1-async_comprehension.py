#!/usr/bin/env python3
'''
an async generator with no arguments
'''


import random
import asyncio
from typing import AsyncGenerator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Calls an async generator
    '''
    result = [i async for i in async_generator()]
    return (result)
