#!/usr/bin/python3
"""
Contains the is_kind_of_class function
"""


def is_same_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (type(obj) == a_class)
