#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO MATCH and SUBSTITUTE
# using the re.sub() and re.subn() functions
""" 
    DocString
"""
import re
line = "root:x:0:0:The Super User:/root:/bin/ksh"

line = re.sub(r"[sS]uper [uU]ser", r"Administrator", line) # Returns a modified string
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns a TUPLE (line, num changes)

print(f"Modified line = {line} with {num} changes")