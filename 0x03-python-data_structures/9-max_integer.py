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
    max_val = my_list[0]
    if my_list == []:
        return None
    for item in my_list:
        if item > max_val:
            max_val = item
    return max_val
