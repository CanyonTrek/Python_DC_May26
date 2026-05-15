#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    Test Case for all the Basic Calc Functions
"""
import unittest
from calc.app import basic
# from basic import add, mul, div

class TestBasic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3, 2, 1), 10.1, "Should be 10.1")
        return None

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3, 2), 24.1, "Should be 24.1")
        return None

    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.334, "Should be 1.334")
        return None


if __name__ == "__main__":
    unittest.main()