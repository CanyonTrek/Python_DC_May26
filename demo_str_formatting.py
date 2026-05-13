#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO format strings
# in different ways using escape chars, str concatenation,
# tr methods, and f-strings!
""" 
    DocString
"""
# A dictionary of planetory info with distance
# to the sun in Giga metres.
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# Iterate through the planet keys and print out
# planet info..
# using escape chars and str concatenation (UGLY)
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm")

print("-" * 40)
# using str justification methods and str concatenation (OK)
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12, '.') + " Gm")

print("-" * 40)
# using str.format() method (GOOD)
for planet in planets.keys():
    print("{0:>12s}: {1:.>12.3f} Gm".format(planet, planets[planet]))

print("-" * 40)
# using f-strings from Python 3.5 onwards (GOOD)
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.>12.3f} Gm")