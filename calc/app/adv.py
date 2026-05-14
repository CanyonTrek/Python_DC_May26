#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines several calculator functions
# including, power, modulus and sqrt
"""
    Module for a Calc App with power, mod, and sqrt functions
"""
import sys

def power(x, z):
    """ Return Power of x to z as a float """
    return float(x**z)

def mod(x, z):
    """ Return REMAINDER after x divided by z as a float """
    return float(x%z)

def sqrt(x):
    """ Return Square Root of x as a float """
    return float(x**0.5)

def main():
    print("---------- ADV Calc Examples ----------")
    print(f"8 ** 7 = {power(8, 7)}")
    print(f"80 % 70 = {mod(80, 70)}")
    print(f"\N{square root}27= {sqrt(27)}")
    print("---------------------------------------")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module
    main()
    sys.exit(0)