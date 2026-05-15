#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines several calculator functions
# including, add, multiply and divide
""" 
    Module for a Calc App with add, mul, and div functions
"""
import sys

def add(*args):
    """ Return SUM of all parameters as a float
    >>> add(4, 3, 2, 1)
    10.0
    >>> add(10, 20)
    30.0
    """
    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul(*args):
    """ Return PRODUCT of all parameters as a float
    >>> mul(4, 3, 2)
    24.0
    """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places
    >>> div(4, 3)
    1.333
    """
    return round(x/z, 3)

def main():
    print("---------- Basic Calc Examples ----------")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    print("-----------------------------------------")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module
    import doctest
    doctest.testmod() # Automates the Docstring Usage Examples
    main()
    sys.exit(0)