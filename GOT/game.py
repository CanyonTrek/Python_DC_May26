#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    GOT - Game of Tanks
"""
import sys
from app import tank

def main():
    # Instantiate/create 3 new Tank objects
    jesse_tank = tank.Tank('American', 'Sherman')
    tyler_tank = tank.Tank('German', 'Tiger')
    xav_tank = tank.Tank('British', 'Churchill')

    # And the game begins..
    jesse_tank.accel(63)
    tyler_tank.accel(34)

    xav_tank.rotate_left(289)
    xav_tank.accel(29)
    xav_tank.shoot()

    # And success..
    jesse_tank.take_damage(58)
    tyler_tank.take_damage(24)

    # And now for some game visuals - well some print statements
    print(f"Health of Jesse's tank is {jesse_tank._health}") # POOR CODE

    # Example of operator overloading
    print(f"Health of Jesse's and Tyler's Tank = {jesse_tank + tyler_tank}")

    # Jesse has received a health boost
    # jesse_tank._health = 100  # POOR CODE
    # print(f"NEW health of Jesse's tank is {jesse_tank._health}") # POOR CODE
    jesse_tank.set_health(101) # SETTER method
    print(f"NEW health of Jesse's tank is {jesse_tank.get_health()}") # GETTER method
    jesse_tank.tank_health = 102 # special property
    print(f"NEW health of Jesse's tank is {jesse_tank.tank_health}") # special property


    return None

if __name__ == "__main__":
    main()
    sys.exit(0)