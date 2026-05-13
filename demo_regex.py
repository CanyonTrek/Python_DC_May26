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

# Iterate through file handle one line at a time
for line in fh_in:
    # Example of str testing
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search(r"banana", line) # Match "banana" anywhere on line
    # m = re.search(r"^the", line)  # Match lines starting with 'the'
    # m = re.search(r"ing$", line)  # Match lines ending with 'ing'
    # m = re.search(r"^.ing$", line)  # Match 4 char lines ending in 'ing'
    # m = re.search(r"^[adpr]ing$", line)  # Match 4 char lines ending in 'ing'
    # m = re.search(r"^...................$", line)  # Match lines exactly 19 chars
    # m = re.search(r"^.{19}$", line)  # Match lines exactly 19 chars
    # m = re.search(r"^[A-Z]", line)  # Match lines starting with a CAPITAL
    # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match lines with 3 consecutive vowels
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines at least 5 consecutive vowels
    # m = re.search(r"\.", line)  # Match lines starting with a DOT
    # m = re.search(r"[.]", line)  # Match lines starting with a DOT
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines start/end with a CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # Match 6 chat lines start/end with a CAPITAL
    # m = re.search(r"^(.)(.).\2\1$", line)  # Match 5 char palindromes
    # m = re.search(r"^([A-Z]).*\1$", line)  # Match lines start/end with SAME CAPITAL
    # m = re.search(r"diacritic|pneumono|rangers|petroleum", line) # Match lines
    # m = re.match(r"^([A-Z]).*\1$", line)  # Auto matches Lines STARTING WITH
    m = re.fullmatch(r"^([A-Z]).*\1$\n", line, flags=re.IGNORECASE|re.DOTALL)  # Match FULL LINE incl hidden newlines
    if m:
        print(line, end="")