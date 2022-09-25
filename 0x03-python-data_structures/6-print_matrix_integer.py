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
            for val in row:
                print("{}".format(val), end=" ")
            print()
