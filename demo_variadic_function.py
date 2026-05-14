#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create a user VARIADIC function
# that allows a VARIABLE number of parameters
"""
    This module describes a collection of search tools for
    searching in files, databases for text data using
    regular expressions
"""
import re
from re import search

# Example of a USER VARIADIC function with optional parameter passing
# UNPACK all remaining parameters in a TUPLE!
def search_pattern(pattern=r"^([A-Z]).*\1$", *files):
    """ Return num lines matched for a given regular expressions  """
    lines = 0
    for file in files:
        fh_in = open(file, mode="rt")

        for line in fh_in:
            m = re.search(pattern, line)
            if m:
                lines += 1
                print(line, end="")
        fh_in.close()
    return lines


num_lines = search_pattern(r"^.{19}$", r"f:\labs\words", r"f:\labs\words2", r"f:\labs\words3")
print(f"{num_lines} lines matched")