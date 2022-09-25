#!/usr/bin/python3
def max_integer(my_list=[]):

    '''
    find the maximum value  of a list.
    Args:
        my_list - list to search
    Returns:
        None if the list is empty
        Maximum value
    '''
    max = my_list[0]
    if len(my_list) == 0:
        return None
    for item in my_list:
        if item > max:
            max = item
    return max
