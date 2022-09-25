#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    '''
    deletes item at a specific position
    Args:
        my_list - list to search
        idx - position tk access
    Returns:
        my_list - if idx is out of range
    '''
    index = len(my_list)
    if idx < 0 or idx >= index:
        return my_list

    val = my_list[idx]
    my_list.remove(val)
    return my_list
