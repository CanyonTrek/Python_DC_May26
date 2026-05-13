#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO split and rejoin strings
# using the str.split() and str.join() methods.

""" 
    DocString
"""

# Sample line from /etc/passwd on Linux for the root user account.
line = "root:x:0:0:Super User:/root:/bin/ksh"

# I want to modify parts of the string. BUT str are immutable!
fields = line.split(":") # Return a LIST of objects. list are MUTABLE!
fields[4] = "The Administrator"
fields[6] = "/bin/bash"
line = ":".join(fields)
print("Modified line =", line)

