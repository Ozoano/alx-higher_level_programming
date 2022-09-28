#!/usr/bin/python3
def multiply_by_2(a_dict):
    if a_dict is None:
        return None
    for k in a_dict:
        a_dict[k] * 2
    return a_dict
