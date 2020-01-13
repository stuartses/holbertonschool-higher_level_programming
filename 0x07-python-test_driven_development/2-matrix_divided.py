#!/usr/bin/python3

"""1. Divide a matrix
This module divides all elements of a matrix in a number
Corresponds to Task 1.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix in a number
    Args:
        matrix (list): List of list. Each element inside Matrix must to be \
        integer or float
        div (int): Divisor must to be integer or float
    Returns:
        list: new matrix
    """

    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    is_matrix = all(isinstance(ele, list) for ele in matrix)

    if is_matrix is False:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    for i in range(len(matrix)):
        new_row = []
        if i < len(matrix) - 1 and len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

        for value in matrix[i]:
            if type(value) != int and type(value) != float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

            new_value = round(float(value) / float(div), 2)
            new_row.append(new_value)

        new_matrix.append(new_row)

    return new_matrix
