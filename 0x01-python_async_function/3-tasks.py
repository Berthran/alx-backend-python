#!/usr/bin/env python3
'''
create task without creating asyncio function
'''

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task that is scheduled
    to run the wait_random coroutine.

    :param max_delay: Maximum delay in seconds.
    :return: asyncio.Task
    """
    # Use asyncio.create_task to create and return the Task
    return asyncio.create_task(wait_random(max_delay))
