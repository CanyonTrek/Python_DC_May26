#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO COPY and optionally
# FILTER collections using loops, if statements, user functions
# lambda functions, filter() function and comprehensions..
""" 
    DocString
"""
students = ['sarah', 'christian', 'jesse', 'tyler', 'devin',
            'elean', 'patricio', 'grace', 'isla', 'tyler']

# Copy Source collection and optionally filter using..
# 1. Iterator Loop + collection, if condition (filtering), expression
wee_names = []
for name in students: # 1.Iterator loop + source collection
    if len(name) <= 5: # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"1.Short names = {wee_names}")

def filter_names(name):
    """ Return True if parameter is <= 5 chars in length """
    if len(name) <= 5:
        return True
    else:
        return False

# 2. Iterator Loop + collection, user function (filtering), expression
wee_names = []
for name in students: # 1.Iterator loop + source collection
    if filter_names(name): # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"2.Short names = {wee_names}")

# 3. Built-in filter() function, user function (filtering)
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4. Built-in filter() function, lambda function (filtering)
wee_names = list(filter(lambda name: len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5. LIST COMPREHENSION: expr, iterator loop + source, optional condition
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1 LIST COMPREHENSION: expr, iterator loop + source, optional condition
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1.Short names = {wee_names}")

# 5.2 DICT COMPREHENSION: expr, iterator loop + source, optional condition
# FREE EXTRA FILTERING - duplicate keys have been filtered out!
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2.Short names = {wee_names}")

# 5.3 DICT COMPREHENSION: expr, iterator loop + source, optional condition
# FREE EXTRA FILTERING - duplicate VALUES have been filtered out!
wee_names = { name.upper() for name in students if len(name) <= 5 }
print(f"5.3.Short names = {wee_names}")


