#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    prints a matrix of integers.
    Args:
    matrix - list matrix
    Return:
        matrix integers
    """
    for row in matrix:
        print(" ".join("{:d}".format(j) for j in row))
