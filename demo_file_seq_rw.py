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
fh_out = open(r"f:\labs\projects\Python_DC_May26\movies.txt", mode="wt")

# Iterate through the dict keys and write Names+MovieList to file
for name in movies.keys():
    print(f"{name}: {movies[name]}", end="\n")
    fh_out.write(f"{name}: {movies[name]}\n")

# fh_out.flush()
fh_out.close() # Flush buffers and close file handle

print("-" * 50)

# Open file handle for READING in TEXT mode
fh_in = open(r"f:\labs\projects\Python_DC_May26\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str object.Be Careful of large files
# text = fh_in.read(30) # Read NEXT 30 chars into str object.
# text = fh_in.readline() # Read NEXT LINE into str object
# lines = fh_in.readlines() # Read ENTIRE file into a LIST object. Be Careful
# print(f"1st line = {lines[0]}")
# print(f"Last line = {lines[-1]}")

# Iterate through file handle (Iterable Object = next/iter)
# for line in open(r"f:\labs\projects\Python_DC_May26\movies.txt", mode="rt"):
for line in fh_in:
    print(line, end="")

fh_in.close()