#!/usr/bin/python3
"""defines a class rectangle"""


class Rectangle:
    """represents a rectangle"""

    @property
    def width(self):
        """retries/get the private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.height = height
        self.width = width

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle parameter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
            return string
