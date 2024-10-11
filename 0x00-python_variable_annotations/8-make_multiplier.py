#!/usr/bin/env python3
'''
Type-annotated function
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    returns a function that multiplies a float by multiplier.
    '''
    def multiplier_by_n(n: float) -> float:
        '''
        multiplies multiplier by n
        '''
        return n * multiplier
    return multiplier_by_n
