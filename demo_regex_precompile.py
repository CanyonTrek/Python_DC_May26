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

reobj = re.compile(r"^([A-Z]).*\1$") # Pre-compile pattern ONLY ONCE!

for line in fh_in:
    # m = re.search(r"^([A-Z]).*\1$", line)
    m = reobj.search(line)
    if m:
        print(line, end="")