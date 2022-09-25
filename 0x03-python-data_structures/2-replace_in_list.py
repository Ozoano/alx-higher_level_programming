#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    replace an element at a specific position
    Args:
        my_list - original list
        idx - the index to be replaced at
        element - the new value
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
