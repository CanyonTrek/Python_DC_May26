#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines a class of Tank
""" 
    Tank class for a computer game
"""
from GOT.app import vehicle # BEST solution for importing within app
# and also importing from game.py in parent package

class Tank(vehicle.Vehicle):
    # 2 Components of class: Attribute/Data + Behaviour/Methods
    def __init__(self, country, model):
        # CONSTRUCTOR
        # vehicle.Vehicle.__init__(self, country, model)
        super().__init__(country, model)
        self._location = {'x':0, 'y':0, 'z':0}
        self._direction = 0
        self._shells = 20
        self._health = 100
        # No EXPLICIT return as called IMPLICITLY



    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    def __del__(self):
        # DESTRUCTOR
        print("Boom..Boom..Boom")
        return None

    # SPECIAL methods..
    # Example of OPERATOR overloading
    def __add__(self, other):
        return self._health + other._health

    # Example of a GETTER and a SETTER
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    # WRAP a ONE variable name interface to the getter/setter methods
    # tank_health = property(get_health, set_health)

    # Alternatively, we could DECORATE our methods with another FUNCTION
    # DECORATOR is ADDING FUNCTIONALITY from another function to your method
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, new_health):
        self._health = new_health
        return None


