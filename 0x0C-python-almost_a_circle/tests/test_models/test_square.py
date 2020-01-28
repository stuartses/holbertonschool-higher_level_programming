#!/usr/bin/python3

"""Unnittest Square class
Tests cases for Class Square using unittest
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for class Square
    """

    def test_square_args(self):
        """Test init and change arguments in class
        """

        r1 = Square(10)
        self.assertEqual(r1.size, 10)

        r2 = Square(10, 0, 3)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 3)

        self.assertRaises(ValueError, Square, -4)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, 3, -1, 0)
        self.assertRaises(ValueError, Square, 3, 0, -1)

        self.assertRaises(TypeError, Square, 1.2)
        self.assertRaises(TypeError, Square, 2, 3.3, 9)
        self.assertRaises(TypeError, Square, float('inf'))
        self.assertRaises(TypeError, Square, float('nan'))
        self.assertRaises(TypeError, Square, 3, float('inf'), 3)
        self.assertRaises(TypeError, Square, 3, 2, float('nan'))

        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, 2, None, 0)
        self.assertRaises(TypeError, Square, 1, 9, None)

        self.assertRaises(TypeError, Square, "abc")
        self.assertRaises(TypeError, Square, 1, "abc", 0)
        self.assertRaises(TypeError, Square, 2, 1, "abc")

    def test_display(self):
        a = Square(1, 2, 3)
        self.assertRaises(TypeError, a.display, 1)

if __name__ == '__main__':
    unittest.main()
