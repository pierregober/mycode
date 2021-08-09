#!/usr/bin/python3

import random
import sys
import os
# Replace RPG starter project with this code when new instructions are live


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
  look
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'severed hand',
        'item_status': "There's a um... severed hand with a note... Bring a helping hand!",
        'desc': "You see a hand in the room. Also the kitchen (to the south) is dimmly lit. You saw something move... you shouldn't go unless you are prepared"
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'east': 'Dark Room',
        'item': 'glock 17',
        'item_status': 'Theres a Glock 17 w/ extended Magazine full with rounds... hopefully there arent any ghosts here',
        'north': 'Pantry',
        'desc': 'A oodly very clean dining room. You are feeling safe. This is the center of the house',
    },
    'Garden': {
        'north': 'Dining Room',
        'desc': 'A garden with only glowing mushrooms and a fierce looking goat. The goa tis going you a stare down',
    },
    'Pantry': {
        'south': 'Dining Room',
        'desc': 'Empty shevles and some broken glass. Brightly lit room',
    },
    'Dark Room': {
        'west': 'Dining Room',
        'obj': 'finger_printer',
        'desc': 'you see something shimmer in the corner... theres a fingerprint scanner'
    },
    'Tunnel': {
        'north': 'Tunnel Enterance',
        'desc': 'You are in a dark tunnel. The only way you can go is north.'
    },
    'Tunnel Enterance': {
        'desc': "birds are chirping"
    }
}

# start the player in the Hall
currentRoom = 'Hall'

os.system('clear')  # start game with a fresh screen
showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        print(move)
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

      # if they type 'look' in any room
    if move[0] == 'look':
        if 'desc' in rooms[currentRoom]:
            print(rooms[currentRoom]['desc'])  # print the look description
        else:
            print('You can\'t see anything.')

    if move[0] == 'use':
        if 'obj' in rooms[currentRoom] and 'severed hand' in inventory:
            print("You used the index finger of the severed hand to the finger scanner")
            print("You fall through a trap door!")
            currentRoom = 'Tunnel'
            print(
                "You are stuck in a tunnel. but you see a light. You are only able to head north")

    # Define how a player can win This is the last senario. is escaping through the tunnel
    if currentRoom == 'Tunnel Enterance':
        print('You escaped the house with your life... YOU WIN!')
        break

    # If a player enters a room with a monster 2 out the 3 winning senarios are here
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'glock 17' in inventory:
            print('You shot and killed the monster with Glock17. You find a door leading to your escape. You Win! \n***There are multiple senarios. Would you like to give it another try? \nFind a way to escape without killing something this time. That monster probably had a family. :( ')
        elif random.randint(0, 100) > 95:
            print('You killed the monster with you bare hands....and you jump out the window before another monster found the body. \n*** You passed the game with a 5 percent chance of killing the monster from the start (PURE LUCK) but there are other endings... do you dare to try again?? \nFind a way to escape without killing something this time. That monster probably had a family. :( ')
        else:
            print('A monster has got you... GAME OVER!')
        break
