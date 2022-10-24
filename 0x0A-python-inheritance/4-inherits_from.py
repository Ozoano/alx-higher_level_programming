#!/usr/bin/python3
"""contains inherits_from function"""


def inherits_from(obj, a_class):
    """
    Returns:
        True if object is an instance of a class that inherited from class
    Else:
        False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
