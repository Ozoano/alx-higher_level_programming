#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    replace an element at a position without
    modifying the original list
    Args:
        my_list - the original list
        idx - index position
        element - the new value
    """
    copy = my_list[:]
    if idx < 0 or idx >= len(copy):
        return copy
    copy[idx] = element
    return copy
