#!/usr/bin/env python3
'''
Type-annotated function
'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    returns a tuple of k and square of v
    '''
    return (k, v**2)
