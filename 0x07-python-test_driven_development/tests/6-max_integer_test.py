#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        """Check if input for different

        Args: self object
        """
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([0, 1, -2, -3]), 1)
        self.assertEqual(max_integer([0.15, 0.28, 0.01, 0.21]), 0.28)
        self.assertEqual(max_integer([[0, 1, 2, 3],[4, 5, 6, 7]]), [4, 5, 6, 7])
        self.assertEqual(max_integer([[4, 0, 2, 3],[2, 3, 0, 4]]), [4, 0, 2, 3])
        self.assertEqual(max_integer("abecd"), 'e')
        self.assertEqual(max_integer("abc" "def"), 'f')
        self.assertEqual(max_integer(" "), ' ')
        self.assertEqual(max_integer("R"), 'R')
        self.assertEqual(max_integer((0, 1, 2, 3)), 3)

if __name__ == '__main__':
    unittest.main()
