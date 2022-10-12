#!/usr/bin/python3
""" defijes a square class """


class Square:
    " initialize a class "

    def __init__(self, size=0):
        """size (int): size of the new class """
        self.size = size

    @property
    def size(self):
        """initialze a setter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ initialize setter """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square are  """
        return (self.__size * self.__size)
