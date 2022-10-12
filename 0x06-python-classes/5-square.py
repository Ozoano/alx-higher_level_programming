#!/usr/bin/python3
"""defines a class square """


class Square:
    """initialize a method
    Args:
        size(int): size of the new square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ retrieve the current size of the square. """
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with the character #"""
        for i in range(0, self.__size):
            print("".join(["#" for j in range(self.__size)]))
        if self.__size == 0:
            print("")
