#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create a user function
# for searching inside files using Regular Expressions
"""
    DocString
"""
import re
from re import search

# Example of a USER function with optional parameter passing
# and default values
def search_pattern(pattern=r"^([A-Z]).*\1$", file=r"f:\labs\words"):
    lines = 0
    fh_in = open(file, mode="rt")

    for line in fh_in:
        m = re.search(pattern, line)
        if m:
            lines += 1
            print(line, end="")
    fh_in.close()
    return lines

search_pattern()
num_lines = search_pattern(r"^.{19}$", r"f:\labs\words")
print(f"{num_lines} lines matched")