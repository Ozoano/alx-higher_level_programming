#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = matrix[:]
    newMatrix = [[val ** 2 for val in row] for row in matrix]
    return newMatrix
