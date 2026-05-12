#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO ITERATE through a
# collection (str/tuple/list/dict/set) using an ITERATOR for loop.
""" 
    DocString
"""
import sys
#              0               1               2               3
heroes = ['virat kohli', 'kevin the cat', 'wayne rooney', 'marie curie',
          'larry ellison', 'federer', 'guido van rossum']

# ITERATE through the sequence (e.g. a list) one element
# at a time using an ITERATOR for loop.
for name in heroes:
    print(name, end="\n")
print("Heroes =", heroes)

# ITERATE through list and modify the elements
idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes =", heroes)

# ITERATE through list and modify the elements using an
# ITERATOR for loop plus built-in enumerate() function
for (idx, name) in enumerate(heroes, start=0):
    print(name.title(), end="\n")
    heroes[idx] = name.title()
print("Heroes =", heroes)

try:
    sys.exit(0) # Explicit EXIT with error code (0=success, 1-255=error code)
    # sys.exit("goodbye") # Explicit EXIT with error msg (STDERR) + error code=1
except SystemExit:
    print("Quitting..")
    sys.exit(66)
