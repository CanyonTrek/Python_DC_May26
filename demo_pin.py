#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will simulate an ATM PIN machine.
# Maximum of three attempts only!
""" 
    DocString
"""

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter your PIN: ")
    if pin == master_pin:
        print("Valid PIN")
    else:
        print("Invalid PIN")
        attempts += 1


print("Done.")
