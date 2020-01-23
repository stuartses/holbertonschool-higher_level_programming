#!/usr/bin/python3

"""14. Pascal's Triangle
Prints Pascal Triangle
Corresponds to Task 14.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def pascal_triangle(n):
    """Prints Pascal Triangle of size n

    Args:
        n: size of triangle
    """

    pascal = []

    if n <= 0:
        return pascal

    pascal.append([])
    pascal[0].append(1)

    for x in range(1, n):
        pascal.append([])

        for y in range(x + 1):
            if y - 1 < 0:
                sum1 = 0
            else:
                sum1 = pascal[x - 1][y - 1]

            if y > len(pascal[x - 1]) - 1:
                sum2 = 0
            else:
                sum2 = pascal[x - 1][y]

            pascal[x].append(sum1 + sum2)

    return pascal
