#!/usr/bin/python3
def multiply_by_2(a_dict):
    if a_dict is None:
        return None
    return (map(lambda k: a_dict[k] * 2, a_dict))
