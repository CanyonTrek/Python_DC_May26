#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create a user function
# for searching inside files using Regular Expressions
"""
    DocString
"""
import sys
import re
from re import search

# Example of a USER function with optional parameter passing
# and default values
def search_pattern(pattern=r"^([A-Z]).*\1$", file=r"f:\labs\words"):
    lines = 0
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"Error: {err.args[0]}, Msg: {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"Error: {err.args[0]}, Msg: {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(2)
    except Exception as err:
        print(f"Other error occurred: {err.args}", file=sys.stderr)
        sys.exit(3)
    else:
        # Executes when try block SUCCEEDS
        for line in fh_in:
            m = re.search(pattern, line)
            if m:
                lines += 1
                print(line, end="")
        fh_in.close()
    finally:
        print(f"And now for something completely different..")

    return lines

def main():
    search_pattern()
    num_lines = search_pattern(r"^.{19}$", r"f:\labs\words")
    print(f"{num_lines} lines matched")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)