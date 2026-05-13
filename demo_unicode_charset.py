#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will display the entire Unicode
# charset
""" 
    DocString
"""

# Iterate through all the char positions in the unicode
# charset from 0 to 65535 using an ITERATOR for loop plus
# built-in range() function
for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
    except UnicodeEncodeError:
        print(" ")
    if pos % 16 == 0:
        print("")