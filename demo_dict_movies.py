#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import pprint

# Example of a multi-dimensional dictionary of lists
movies = { 'presanna': ['goodfellas', 'bronx take', 'godfather'],
           'devin': ['the raid', 'the prestige', 'catch me'],
           'bryan': ['power rangers', 'lone ranger', 'texas ranger'],
}

# Grow a dict by assigning new key+values
movies['xavier'] = ['dark knight', 'casino', 'friday']
movies['donald'] = ['braveheart', 'brave', 'trainspoting']

# Shrink a dict..
movies.pop('presanna') # Remove Key + Values
movies.popitem() # Remove LAST INSERTED key + value

# Accessing Dict Keys and Values..
pprint.pprint(movies)
print("-" * 60)
print(f"Bryan's favourite movies are {movies['bryan']}") # Prefer this!
print(f"Devin's ultimate movie is {movies.get('bryan')}")
print(f"Devin's ultimate movie is {movies['devin'][0]}")

# Accessing keys and values
# using an ITERATOR for loop and the .keys() method
for name in movies.keys():
    print(f"{name} likes the movies {movies[name]}")

# using an ITERATOR for loop and the .values() method
for films in movies.values():
    print(f"Recommended films: {films}")

# Iterate through keys+values using dict.items() method
for (name, films) in movies.items():
    print(f"{name} LOVES the films {films}")

films = movies.copy() # Copy dict
films.clear() # Empty the dict