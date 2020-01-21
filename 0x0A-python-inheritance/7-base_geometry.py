#!/usr/bin/python3
"""7. Integer validator
With integer validator
Corresponds to Task 7.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


class BaseGeometry:
    def area(self):
        """Defines area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check value

        args:
            name: input name
            value: input value
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
