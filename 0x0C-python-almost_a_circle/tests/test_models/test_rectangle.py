#!/usr/bin/python3

"""Unnittest Rectangle class
Tests cases for Class Rectangle using unittest
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases for class Rectangle
    """

    def test_rectangle_args(self):
        """Test init and change arguments in class
        """

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(10, 2, 0, 3)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 3)


        self.assertRaises(ValueError, Rectangle, -4, 5)
        self.assertRaises(ValueError, Rectangle, 4, -5)
        self.assertRaises(ValueError, Rectangle, 0, 5)
        self.assertRaises(ValueError, Rectangle, 4, 0)
        self.assertRaises(ValueError, Rectangle, 4, 5, -3, 2)
        self.assertRaises(ValueError, Rectangle, 4, 5, 3, -2)

if __name__ == '__main__':
    unittest.main()
