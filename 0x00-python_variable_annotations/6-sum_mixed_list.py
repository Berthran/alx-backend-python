#!/usr/bin/env python3
'''
Type-annotated function
'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    returns sum of list elements as float
    '''
    return float(sum(mxd_lst))
