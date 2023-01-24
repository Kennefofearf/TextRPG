# Text RPG

import cmd
import textwrap
import sys
import os
import time
import random

from Player import player

screen_width = 100

# ### Title Screen ###

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # placeholder
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()  # placeholder
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print("#########################")
    print("# RRRRR    PPPPP  GGGGG #")
    print("# R   R    P   P  G     #")
    print("# RRRRR    PPPPP  G GGG #")
    print("# R    R   P      G   G #")
    print("# R     R  P      GGGGG #")
    print("#########################")
    print("        - Play -         ")
    print("        - Help -         ")
    print("        - Quit -         ")
    title_screen_selections()

def help_menu():
    title_screen_selections()


    # Village MAP

#       1    2    3    4
#     ______________________
#  A  |    |  x  |    |    |
#     -----------------------
#  B  |    |  x  |  x  |    |
#     -----------------------
#  C  |  x  |  x  |    |    |
#     -----------------------
#  D  |    |  x  |    |    |
#     ----------------------

# Highlands MAP

#       1    2    3    4
#     ______________________
#  A  |    |    |    |    |
#     ----------------------
#  B  |    |    |    |    |
#     ----------------------
#  C  |    |    |    |    |
#     ----------------------
#  D  |    |    |    |    |
#     ----------------------

# ___ MAP

#       1    2    3    4
#     ______________________
#  A  |    |    |    |    |
#     ----------------------
#  B  |    |    |    |    |
#     ----------------------
#  C  |    |    |    |    |
#     ----------------------
#  D  |    |    |    |    |
#     ----------------------

zone_name = ''
description = 'description'
look = 'look'
north = 'north', 'up'
south = 'south', 'down'
east = 'east', 'right'
west = 'west', 'left'

zone_map = {
    'd2': {
        zone_name: 'Village Start',
        description: '',
        look: '',
        north: 'c2',
        south: '',
        east: '',
        west: '',
    },
    'c2': {
        zone_name: 'Village Square South',
        description: '',
        look: '',
        north: '',
        south: 'd2',
        east: '',
        west: 'c1',
    },
    'c1': {
        zone_name: 'Village Home 1',
        description: '',
        look: '',
        north: '',
        south: '',
        east: 'c2',
        west: '',
    },
    'b2': {
        zone_name: 'Village Square North',
        description: '',
        look: '',
        north: '',
        south: 'c2',
        east: 'b3',
        west: '',
    },
    'b3': {
        zone_name: 'Village Home 2',
        description: '',
        look: '',
        north: '',
        south: '',
        east: '',
        west: 'b2',
    },
    'a2': {
        zone_name: 'Village Entrance',
        description: '',
        look: '',
        north: '',
        south: 'b2',
        east: '',
        west: '',
    },
}

def start_game():
    return