# I have made this file as a tester to make individual aspecsts instead of cluddering main.py
# my initial thought was not to include, but shows development.

import txtadv
import datetime, random
from cat_picture.cat import pic



username = 'H'
tutorial = 'N'

user = txtadv.Player(username, tutorial, 0)

r1 = txtadv.Rooms('locked', 'key', 0)

# # tutorial
# # make a function that is in the main loop so can be called whenever

# def help():
#     print('All rooms have a locked door and a condition that must be solved to unlock it.')
#     prompt =  'nothing'
#     while prompt != 'Exit':
#         prompt =  input('Please enter: Clue, More or Exit. ')
#         if prompt == 'Clue':
#             # Clue can later be created into class so mitigate repetition. Make if more than 1 rooms are made.
#             # Nest prints into if statemnts to relay relavent clue
#             print('Have you looked around?')
#             print('Try putting the mirror under the light')
#             print('Is that a key on the wall?')
                  
#         elif prompt == 'More':
#             print('Below is a list of prompts, followed by their functionality.')
#             # Was going to make a list of prompts and description, 
#             # then make a loop which going through the list and prints them out for line by line output.
#             # But feels redundant as will only need a print command here.
#             print('FaceN : will make the user face North')
#             print('FaceE : will make the user face East')
#             print('FaceS : will make the user face South')
#             print('FaceW : will make the user face West')
#             print('pickupX : will allow you to pick up object X.')
#             print('useX : will allow you to use object X, if possible')
#             print('Giveup : will end game')
#             # insert cat pic
            

#         elif prompt == 'Exit':
#             return prompt == 'Exit'
        
#         else:
#             print('Invalid prompt. Please try again')
#             prompt =  input('Please enter: Clue, More or Exit. ')
    
# help()

# room and player are both confined to NESW configuration
# a class called Position will create a repeatable orientation for both
# start with the room, seperate. then incorporate the class and then the player
# soon after started didnt feel smooth so stop and theorised.
# room doesnt need a postion, the objects inside and the players will
# instead now creating the Position class first then the rooms objecsts and the player at none




# a position has been made for the rooms inv. (will use positions as a boolean, 0/1.)
# make a open loop that allows a player to face a direction on input
# make 2 print out. 1, is the initial. 2, is after input. should looke like below
# 1. {'north': 0, 'south': 0, 'east': 0, 'west': 0}
# 2. {'north': 1, 'south': 0, 'east': 0, 'west': 0}
# and elif and else (later the elif will include all prompts)
# make the position return to 0 when entering a diffenet prompt

# r1.inv.position.east = 1

# print(f'{user.position.__dict__}')

# while user.levels_complete < 2:
#     RefreshInput = input()
#     if RefreshInput == 'FaceN':
#         user.position.north = 1
#         user.position.east = 0
#         user.position.south = 0
#         user.position.west = 0
#     elif RefreshInput == 'FaceE':
#         user.position.north = 0
#         user.position.east = 1
#         user.position.south = 0
#         user.position.west = 0
#     elif RefreshInput == 'FaceS':
#         user.position.north = 0
#         user.position.east = 0
#         user.position.south = 1
#         user.position.west = 0
#     elif RefreshInput == 'FaceW':
#         user.position.north = 0
#         user.position.east = 0
#         user.position.south = 0
#         user.position.west = 1
#     user.levels_complete += 1

# print(f'{user.position.__dict__}')


# Above was initial solution but to much repetition, will brainstorm nicer method
# maybe put all prompts inside a single library 
# testing by making it call a function that says prints 'Hi'
# didnt work well, made a elif and it call the function. seems to work better will test on main.py with the help

# def hi():
#     print('Hi')

# r1.inv.position.east = 1

# print(f'{user.position.__dict__}')

# user_commands = {
#     'FaceN': {"north": 1, "east": 0, "south": 0, "west": 0},
#     'FaceE': {"north": 0, "east": 1, "south": 0, "west": 0},
#     'FaceS': {"north": 0, "east": 0, "south": 1, "west": 0},
#     'FaceW': {"north": 0, "east": 0, "south": 0, "west": 1}
#     }

# while user.levels_complete < 1:
    
#     fresh_input = input()
#     if fresh_input in user_commands:
#         user.position = user_commands[fresh_input]
#         print(f'{user.position}')

#     elif fresh_input == 'hi':
#         hi()

#     user.levels_complete += 1

# will proceed as above as it works will with the help. will change lib name to precify direction.

# make it so if the user has the same position as the rooms item the user can pickup the thing
# need to make the inv 
# print 'can pickup' if users position is same as items
# was running into problem and couldnt get print out below. found that r1.position.east = 1 was rearranging the dict and so wants equal.


# r1.inv.items = ['Mirror Peice']
# r1.inv.position = {"north": 0, "east": 1, "south": 0, "west": 0}
# # r1.inv.position.east = 1

# user_commands = {
#     'FaceN': {"north": 1, "east": 0, "south": 0, "west": 0},
#     'FaceE': {"north": 0, "east": 1, "south": 0, "west": 0},
#     'FaceS': {"north": 0, "east": 0, "south": 1, "west": 0},
#     'FaceW': {"north": 0, "east": 0, "south": 0, "west": 1}
#     }

# while user.levels_complete < 3:
    
#     fresh_input = input()

#     if fresh_input in user_commands:
#         user.position = user_commands[fresh_input]
#         print(f'{user.position}')

#     elif fresh_input == 'pickup' and user.position == r1.inv.position:
#         print('can pick up')

    

#     user.levels_complete += 1

# print(f'{r1.inv.items}, {r1.inv.position.__dict__}')

# will continue below and keep above to show errors/ resolutions

# make user inv = room inv if condition is true

# r1.inv.items = ['Mirror Peice']
# r1.inv.position = {"north": 0, "east": 1, "south": 0, "west": 0}

# user_commands = {
#     'FaceN': {"north": 1, "east": 0, "south": 0, "west": 0},
#     'FaceE': {"north": 0, "east": 1, "south": 0, "west": 0},
#     'FaceS': {"north": 0, "east": 0, "south": 1, "west": 0},
#     'FaceW': {"north": 0, "east": 0, "south": 0, "west": 1}
#     }

# while user.levels_complete < 3:
    
#     fresh_input = input()

#     if fresh_input in user_commands:
#         user.position = user_commands[fresh_input]
#         print(f'{user.position}')

#     elif fresh_input == 'pickup' and user.position == r1.inv.position:
#         user.inv = r1.inv

        

#     user.levels_complete += 1

# print(f'{user.inv.items}')

# Make it so the 1 is random everytime the program runs



# r1.inv.position = {"north": 0, "east": 0, "south": 0, "west": 0}

# positions = ["north", "east", "south", "west"]
# random.shuffle(positions)

# r1.inv.position[positions[0]] = 1

# print(f'{r1.inv.position}')

# test with the cat package

# cat = input()

# if cat != 0:
#     pic()

#colort for coloring text
# print hello green and gooodbye with a blue background


from colort import colorize, ForegroundColor as fc, Style, BackgroundColor as bc

# colored_text = colorize('Hello', fc.GREEN)
# colored_background = colorize('Goodbye', bc.BLUE)

# input(colored_text)
# print(colored_background)

# make the below repeatable

# input((colorize('You wake up in darkness. There is 1 thing on your mind Escape!', bc.RED)))
# input((colorize('The Room is almost completely black, there is however a small column of light.', bc.RED)))

# # there is the input then inside the mod and within that 2 variables

# def test(text, color):
#     print(colorize(text, color))

# narrator = bc.RED

# test('1', narrator)

# test  colors

colored_text = colorize('Hello', fc.LIGHT_BLUE)
print(colored_text)

