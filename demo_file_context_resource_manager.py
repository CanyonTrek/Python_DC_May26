#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close, a TEXT File
# for Reading, Writing or Appending.
"""
    DocString
"""
movies = { 'presanna': ['goodfellas', 'bronx take', 'godfather'],
           'devin': ['the raid', 'the prestige', 'catch me'],
           'bryan': ['power rangers', 'lone ranger', 'texas ranger'],
           'xavier': ['dark knight', 'casino', 'friday']
}

# Open file handle for WRITING in TEXT mode
with open(r"f:\labs\projects\Python_DC_May26\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name}: {movies[name]}", end="\n")
        fh_out.write(f"{name}: {movies[name]}\n")

print("-" * 50)

with open(r"f:\labs\projects\Python_DC_May26\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")
    # End of Block, filehandle is auto closed
