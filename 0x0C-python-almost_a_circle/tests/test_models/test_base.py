#!/usr/bin/python3

"""Unnittest Base class
Tests cases for Class Base using unittest
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for class Base
    """

    def test_base_init(self):
        """Test assign id for base
        """

        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        a = Base()
        self.assertEqual(a.id, 3)
        b = Base(8)
        self.assertEqual(b.id, 8)
        c = Base(-9)
        self.assertEqual(c.id, -9)
        d = Base(None)
        self.assertEqual(d.id, 4)


if __name__ == '__main__':
    unittest.main()
