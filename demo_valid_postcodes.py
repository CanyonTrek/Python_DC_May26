#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import re
# Open file handle for READING in TEXT mode
fh_in = open(r"f:\labs\postcodes.txt", mode="rt")

valid = 0
invalid = 0

# Iterate through the file handle using an ITERATOR for loop.
for postcode in fh_in:
    if postcode.isspace(): continue

    # Ques 1 Solution
    postcode = postcode.upper()
    postcode = re.sub(r"\s+", r"", postcode)
    postcode = re.sub(r"(\d[A-Z]{2})$", r" \1", postcode)

    # Ques 2 Solution
    m = re.search(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z]{2}$", postcode)
    if m:
        valid += 1
        print(postcode)
    else:
        invalid += 1

print(f"Valid postcodes = {valid}")
print(f"Invalid postcodes = {invalid}")