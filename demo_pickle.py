#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import pickle
import pprint
import gzip # Others such as tarfile, shutil, bz2
movies = { 'presanna': ['goodfellas', 'bronx take', 'godfather'],
           'devin': ['the raid', 'the prestige', 'catch me'],
           'bryan': ['power rangers', 'lone ranger', 'texas ranger'],
           'xavier': ['dark knight', 'casino', 'friday']
}

# with open(r"f:\labs\projects\Python_DC_May26\movies.p", mode="wb") as fh_out:
with gzip.open(r"f:\labs\projects\Python_DC_May26\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Protocol (0=ASCII, 1-5=BINARY)
    # pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL) # Currently 4
    pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL) # Currently 5


# with open(r"f:\labs\projects\Python_DC_May26\movies.p", mode="rb") as fh_in:
with gzip.open(r"f:\labs\projects\Python_DC_May26\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 50)
pprint.pprint(films)