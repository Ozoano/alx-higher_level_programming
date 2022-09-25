#!/usr/bin/python3
def add_tuple(a=(), b=()):
    """
    adds 2 tuples
    Args:
        tuple_a - first tuple with element
        tuple_b - second tuple with element
    Return:
        a tuple with 2 integars
    """
    while len(a) < 2:
        a = (*a, 0)
    while len(b) < 2:
        b = (*b, 0)
    return a[0] + b[0], a[1] + b[1]
