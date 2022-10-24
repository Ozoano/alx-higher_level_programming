#!/usr/bin/python3
"""contains function is_kimd_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Returns:
        True if object is an instance of or inherited from class
    else:
        False
    """
    return (isinstance(obj, a_class))
