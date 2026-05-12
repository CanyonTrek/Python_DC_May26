#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO repeat a BLOCK of
# commands a specific number of repetitions using a COUNTER LOOP
""" 
    DocString
"""

count = 0 # 1.Initialise counter
while count < 10: # 2.Test condition
    print(count)
    count += 1 # 3.Increment counter

# Alternatively, we could use a FOR loop plus the
# built-in range(start, stop, step) function
for num in range(0, 10, 1):
    print(num)

# built-in range(start, stop, step=1) function
for num in range(0, 10):
    print(num)

# built-in range(start=0, stop, step=1) function
for num in range(10):
    print(num)