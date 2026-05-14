#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This is a simple calculator app
""" 
    Calc App with Basic and Adv Functions
"""
import sys
from app import basic
from app import adv

def main():
    menu = """
        Menu Options
        ------------
        1.Display Basic Calc examples
        2.Display Adv Calc examples
    """

    while True:
        print(menu)
        option = input("Enter option (1-2,q=quit): ")

        match option:
            case "1":
                print(f"9 + 8 + 7 = {basic.add(9, 8, 7)}")
                print(f"9 * 8 * 7 = {basic.mul(9, 8, 7)}")
                print(f"9 / 8 = {basic.div(9, 8)}")
            case "2":
                print(f"9 + 8 + 7 = {adv.power(9, 8)}")
                print(f"9 * 8  = {adv.mod(9, 8)}")
                print(f"\N{square root}9 = {adv.sqrt(9)}")
            case "q":
                print("Quitting app..")
                break
            case _:
                print("Invalid option")

    print("Done")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module
    main()
    sys.exit(0)
