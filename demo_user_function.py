#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define, name, and call
# a user function with optional parameters and return value.
""" 
    DocString
"""
# Example of a user function with
# optional parameter passing
# Enforce named parameters *,
# And default parameters
# Annotations (not enforced)= embedded comment
def say_hello(greeting:str="ni", recipient:str="hao")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello("hello", "my friends") # Positional parameter passing
say_hello(greeting="ciao", recipient="amici") # Named parameter passing
say_hello("hola", recipient="amigos") # Mixed parameter (positional->named)
say_hello(recipient="dosto", greeting="namaste") # Mixed (different order)
say_hello("ni", ['elizabeth', 'christian', 'elean'])
say_hello()

print(f"Annotations for say_hello = {say_hello.__annotations__}")