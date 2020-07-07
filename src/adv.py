from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# declare items

items = {
    'sword': Item('Sword', 'description: Silver, One-Handed'),
    'shield': Item('shield', 'description: Knight Symbol'),
    'potion': Item('potion', 'description: Health Boost'),
    'chest': Item('chest', 'description: Gold Treasure')
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#add room items
room['foyer'].room_items.append(items['sword'])
room['overlook'].room_items.append(items['shield'])
room['narrow'].room_items.append(items['potion'])
room['treasure'].room_items.append(items['chest'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Jeremy', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f'\nWelcome to the Adventure Game!! :D\n')

while True:
    print(f'\nCurrent Room: {player.current_room.name}\n')
    print(textwrap.TextWrapper().fill(text=player.current_room.description))
    print(f'\n{player.current_room.current_items()}')

    action = input('\nSelect the Direction You Would Like to Explore (n - North, s - South, e - East, w - West)\n\nCommands (get or take item name - Pickup, drop item name - Drop, i - Inventory, q - Quit)\n').split(" ")

    #take and drop commands
    if len(action) == 2:
        if action[0] == 'get' or action[0] == 'take':
            found = False
            for i in range(len(player.current_room.room_items)):
                item = player.current_room.room_items[i]
                if action[1] == item.name:
                    player.items.append(player.current_room.room_items.pop(i))
                    item.on_take()
                    found = True
                    break
            if not found:
                print(f'\n{action[1]} not found in {player.current_room.name}.')
        elif action[0] == 'drop':
            found = False
            for i in range(len(player.items)):
                item = player.items[i]
                if action[1] == item.name:
                    player.current_room.room_items.append(player.items.pop(i))
                    item.on_drop()
                    found = True
                    break
            if not found:
                print(f'\n{action[1]} not found in inventory.')

    #Travel directions
    elif action[0] == 'n':
        if player.current_room.n_to == None:
            print(f'\nYou cannot go that way!\n')
        else: 
            player.current_room = player.current_room.n_to
    elif action[0] == 's':
        if player.current_room.s_to == None:
            print(f'\nYou cannot go that way!\n')
        else:
            player.current_room = player.current_room.s_to
    elif action[0] == 'e':
        if player.current_room.e_to == None:
            print(f'\nYou cannot go that way!\n')
        else:
            player.current_room = player.current_room.e_to
    elif action[0] == 'w':
        if player.current_room.w_to == None:
            print(f'\nYou cannot go that way!\n')
        else:
            player.current_room = player.current_room.w_to
    elif action[0] == 'i' or action[0] == 'inventory':
        print(player.current_inventory())
    elif action[0] == 'q':
        print('\nThanks for Playing!\n')
        exit()
    else: 
        print('\nInvalid Direction!')  
        
        ## ka - chow
