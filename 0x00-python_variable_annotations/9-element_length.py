#!/usr/bin/env python3
'''
Type-annotated function
'''


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    returns a tuple of k and square of v
    '''
    return [(i, len(i)) for i in lst]
