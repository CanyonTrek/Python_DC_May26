#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO Match TEXT data
# using str testing and Regex pattern matching
"""
    DocString
"""
import re
# Open file handle for READING in TEXT mode
fh_in = open(r"f:\labs\words", mode="rt")

for line in fh_in:
    m = re.search(r"^(.)(.).\2\1$", line) # Match 5 char palindromes

    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}, "
              f"Groupings = {m.groups()}, Group 1 = {m.group(1)}")