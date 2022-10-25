#!/usr/bin/python
"""defines class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a Rectangle"""
    def __init__(self, size):
        """instanciation of a Rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returnns the area of a square"""
        return (self.__size) ** 2
