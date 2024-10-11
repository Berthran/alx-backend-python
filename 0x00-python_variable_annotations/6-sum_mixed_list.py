#!/usr/bin/env python3
'''
Type-annotated function
'''


from typing import List


def sum_mixed_list(mxd_list: List[int | float]) -> float:
    '''
    returns sum of list elements as float
    '''
    return float(sum(input_list))
