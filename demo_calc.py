#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script is an ultra realistic calculator app
# with add, multiply and divide functions
""" 
    Calc App with add, multiply and divide functionality
"""

def add(x, z):
    """ Return SUM of all parameters as a float """
    return float(x+z)

def mul(x, z):
    """ Return PRODUCT of all parameters as a float """
    return float(x*z)

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places """
    return round(x/z, 3)

print(f"4 + 3 = {add(4, 3)}")
print(f"4 * 3 = {mul(4, 3)}")
print(f"4 / 3 = {div(4, 3)}")

# Alternativel, we could use a lambda function in replace
# of the function definition and use it directly where its needed
print(f"4 + 3 = {(lambda x, z:float(x+z))(4, 3)}")