#!/usr/bin/python3
""" defines a square """


class Square:
    """ a class method
    Attributes:
        __size(int): Private instance
    """
    def __init__(self, size):
        """
        initializes a square
        Args:
        size(int): an Instance
        Return: None
        """

        self.__size = size
