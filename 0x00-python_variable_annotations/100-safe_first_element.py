#!/usr/bin/env python3
'''
Type-annotated function
'''


from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    returns an arbitrary type of Any or type None
    '''
    if lst:
        return lst[0]
    else:
        return None
