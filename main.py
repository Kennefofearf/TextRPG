# Text RPG

import cmd
import textwrap
import sys
import os
import time
import random

from Player import player


player1 = player()

screen_width = 100

# ### Title Screen ###

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('cls')
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

zone_name = '',
description = 'description',
look = 'look',
speak = 'speak',
interact = player_interact()
interactText = '',
north = 'north', 'up'
south = 'south', 'down'
east = 'east', 'right'
west = 'west', 'left'

zone_map = {
    'Village Rear': {
        zone_name: 'd2',
        description: '\nYou are at the rear of the village.'
                     '\nThe buildings are very weathered and some have holes in the roofs.'
                     '\nYou notice a man staring at you and he shakes his head once you notice him.\n',
        look: '\nA man is staring at you.'
              "\nHe looks like he's waiting for you to speak.",
        speak:
            '\nAnother one? At least you dropped in a safe place.'
            "\nHad too many 'visitors' enter straight through some poor sap's ceiling."
            "\nHurry up and leave. We can barely shelter ourselves anymore...",
        interact: interact_text(),
        interactText: '\nThe man pulls his hand away as you try to shake it.',
        north: 'c2',
        south: '',
        east: '',
        west: '',
    },
    'c2': {
        zone_name: 'Village Square (South)',
        description: '',
        look: '',
        speak: '',
        interact: '',
        interactText: '',
        north: '',
        south: 'Village Rear',
        east: '',
        west: 'c1',
    },
    'c1': {
        zone_name: 'Village Home 1',
        description: '',
        look: '',
        speak: '',
        interact: '',
        interactText: '',
        north: '',
        south: '',
        east: 'c2',
        west: '',
    },
    'b2': {
        zone_name: 'Village Square (North)',
        description: '',
        look: '',
        speak: '',
        interact: '',
        interactText: '',
        north: '',
        south: 'c2',
        east: 'b3',
        west: '',
    },
    'b3': {
        zone_name: 'Village Home 2',
        description: '',
        look: '',
        speak: '',
        interact: '',
        interactText: '',
        north: '',
        south: '',
        east: '',
        west: 'b2',
    },
    'a2': {
        zone_name: 'Village Entrance',
        description: '',
        look: '',
        speak: '',
        interact: '',
        interactText: '',
        north: '',
        south: 'b2',
        east: '',
        west: '',
    },
}

### Interactivity ###

def player_interact():
    zone_map[player1.location][interact]

def interact_text():
    print(zone_map[player1.location][interactText])

def print_location():
    print('\n' + '-- ' + player1.location.upper() + ' --\n')
    print('\n' + zone_map[player1.location][description] + '\n')

def prompt():
    print_location()
    print('Command?\n')
    action = input("(A) Speak " + "(W) Look\n" + "(S) Interact " + "(D) Move\n" + "Type -quit- to exit.\n")
    valid_actions = ['a', 'w', 's', 'd', 'quit']
    while action.lower() not in valid_actions:
        print("Invalid command.\n")
        print('Command?\n')
        action = input("(A) Speak " + "(W) Look\n" + "(S) Interact " + "(D) Move\n" + "Type -quit- to exit.\n")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() == "a":
        player_speak()
    elif action.lower() == "w":
        player_look()
    elif action.lower() == "s":
        player_interact()
    elif action.lower() == "d":
        player_move(action.lower())

def player_look():
    print(zone_map[player1.location][look] + '\n')
    time.sleep(3)

def player_speak():
    print(zone_map[player1.location][speak] + '\n')
    time.sleep(3)

def player_move(myAction):
    print("Which direction?")
    dest = input(
        "         " + "(W) North" + "        \n" + "(A) West " + "          " + "(D) East \n" + "         " + "(S) South\n")
    valid_move_actions = ['a', 'w', 's', 'd', ' ']
    if dest == 'a':
        destination = zone_map[player1.location][west]
        move_handler(destination)
    elif dest == 'w':
        destination = zone_map[player1.location][north]
        move_handler(destination)
    elif dest == 'd':
        destination = zone_map[player1.location][east]
        move_handler(destination)
    elif dest == 's':
        destination = zone_map[player1.location][south]
        move_handler(destination)

def move_handler(destination):
    print("\nArrived at:\n")
    player1.location = destination

def game_loop():
    while player1.win_game is False:
        if player1.lose_game is False:
            prompt()

def setup_game():
    os.system('cls')
# Naming the Player
    name_question = ("What is your name?\n")
    print(name_question)
    player_name = input()
    player1.name = player_name
# Player attribute questions
    attribute_question = ("Are you: _____?\n" + "(A) Strong\n" + "(W) Nimble\n" + "(D) Average")
    print(attribute_question)
    player_attributes = input()
    valid_attribute_inputs = ['a', 'w', 'd']
    if player_attributes.lower() not in valid_attribute_inputs:
        print("Invalid selection.")
        attribute_question = ("Are you: _____?\n" + "(A) Strong\n" + "(W) Nimble\n" + "(D) Average\n")
        player_attributes = input()
    if player_attributes.lower() in valid_attribute_inputs:
        if player_attributes.lower() == 'a':
            player1.str = 12
            player1.dex = 8
            player1.cha = 10
            player1.hp = 12
        elif player_attributes.lower() == 'w':
            player1.str = 8
            player1.dex = 12
            player1.cha = 10
            player1.hp = 8
        elif player_attributes.lower() == 'd':
            player1.str = 10
            player1.dex = 10
            player1.cha = 10
            player1.hp = 10

    print("Welcome, " + player_name + "!\n")
    print("Seek the fortress. It is your only chance...")
    game_loop()

title_screen()