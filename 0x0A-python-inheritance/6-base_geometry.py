#!/usr/bin/python3
"""6. Improve Geometry
Raise a Error when method area is used
Corresponds to Task 6.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


class BaseGeometry:
    """Class BaseGeometry
    Defines Geometry"""

    def area(self):
        """Defines area"""

        raise Exception("area() is not implemented")
