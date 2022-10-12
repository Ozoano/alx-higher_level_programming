#!/usr/bin/python3
""" square class """


class Square:
    """ square method """

    def __init__(self, size=0):
        """
        initialize a new square
        Args:
            size(int): size of the new square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ returns the current square area """
        return (self.__size * self.__size)
