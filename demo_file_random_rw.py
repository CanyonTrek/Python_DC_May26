#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close files
# for random read, write and append using .seek() and .tell()
""" 
    DocString
"""
SOF = 0
CUR = 1
EOF = 2

with open(r"f:\labs\projects\Python_DC_May26\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, SOF) # Seek forwards 90 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(135, SOF) # Seek forwards 135 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

with open(r"f:\labs\projects\Python_DC_May26\movies.txt", mode="rb") as fh_in:
    fh_in.seek(-90, EOF) # Seek back 90 bytes from EOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(-85, CUR) # Seek back 85 bytes from Current position
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")