#!/usr/bin/env python3
'''
Type-annotated function
'''


from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    '''
    returns an arbitrary type of Any or type T
    '''
    if key in dct:
        return (dct[key])
    else:
        return default
