#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import shelve

movies = { 'presanna': ['goodfellas', 'bronx take', 'godfather'],
           'devin': ['the raid', 'the prestige', 'catch me'],
           'bryan': ['power rangers', 'lone ranger', 'texas ranger'],
}

tv_series = { 'presanna': ['breaking bad', 'soprana'],
              'devin': ['band of brothers', 'euphoria'],
              'bryan': ['celtics city', 'lone ranger'],
}

books = { 'presanna': ['harry potter'],
          'devin': ['the way of kings'],
          'bryan': ['paradise found'],
}

with shelve.open(r"f:\labs\projects\Python_DC_May26\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"f:\labs\projects\Python_DC_May26\media") as db:
    print(f"Presanna's favourite films are {db['movies']['presanna']}")
    print(f"Devin's favourite tv_series is {db['tv_series']['devin'][0]}")
    print(f"Bryan's ultimate CELTIC book is {db['books']['bryan']}")