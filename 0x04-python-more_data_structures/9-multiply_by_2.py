#!/usr/bin/python3
def multiply_by_2(a_dict):
    mult = {}
    if a_dict is None:
        return None
    for v in a_dict:
        mult.append(v * 2)
    return a_dict
