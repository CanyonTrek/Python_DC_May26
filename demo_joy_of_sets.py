#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, and grow, and
# shrink a set - AND combine sets using SET operators.
# Remember VENN diagrams!
""" 
    DocString
"""
marvel_fans = {'donald', 'sarah', 'patricio', 'bryan', 'elizabeth', 'christian'}
dc_fans = set() # Create an EMPTY set

# Grow a set..
dc_fans.add('donald')
dc_fans.add('grace')
dc_fans.add('isla')

# Shrink a set..
# dc_fans.pop() # Remove RANDOM value from SET

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")

comic_fans = dc_fans.copy() # Copy set
comic_fans.clear() # Empty set

# COMBINE set using SET OPERATORS (VENN diagrams)
print(f"Fans of Marvel OR DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of BOTH Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of EITHER Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 60)
print(f"Fans of Marvel OR DC = {marvel_fans | dc_fans}")
print(f"Fans of BOTH Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of EITHER Marvel OR DC = {marvel_fans ^ dc_fans}")














