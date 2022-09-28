#!/usr/bin/python3
def simple_delete(a_dict, key=""):
    if a_dict is None:
        return None
    a_dict.pop(key)
    return a_dict
