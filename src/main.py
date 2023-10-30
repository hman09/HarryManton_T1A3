import txtadv
import datetime

# let user be able to set name
# make class for user, room and inventory
# game will need to be in loop with the final stage closing the loop and ending the game
# add end of game message outside of above mentioned loop
# make r1 loop
# making the tutorial before the room will help me define the room

def tut():
    while user.first_try == 'Y':
        print('Blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah')
        user.first_try = 'N'

def room():
    while r1.lock == 'locked':
        input()
        r1.lock = 'unlocked'

def help():
    print('All rooms have a locked door and a condition that must be solved to unlock it.')
    prompt =  'nothing'
    while prompt != 'Exit':
        prompt =  input('Please enter: Clue, More or Exit. ')
        if prompt == 'Clue':
            # Clue can later be created into class so mitigate repetition. Make if more than 1 rooms are made.
            # Nest prints into if statemnts to relay relavent clue
            print('Have you looked around?')
            print('Try putting the mirror under the light')
            print('Is that a key on the wall?')
                  
        elif prompt == 'More':
            print('Below is a list of prompts, followed by their functionality.')
            # Was going to make a list of prompts and description, 
            # then make a loop which going through the list and prints them out for line by line output.
            # But feels redundant as will only need a print command here.
            print('FaceN : will make the user face North')
            print('FaceE : will make the user face East')
            print('FaceS : will make the user face South')
            print('FaceW : will make the user face West')
            print('pickupX : will allow you to pick up object X.')
            print('useX : will allow you to use object X, if possible')
            print('Giveup : will end game')
            # insert cat pic
            # give user opt to repeat the tutorial
            user.first_try = input('Do you want the tutorial repeated? (Y/N) ')
            tut()
            

        elif prompt == 'Exit':
            return prompt == 'Exit'
        
        else:
            print('Invalid prompt. Please try again')
            prompt =  input('Please enter: Clue, More or Exit. ')



# Main
username = 'H'#input('What is your name? ')
tutorial = 'N'#input('Do you want the tutorial?(Y/N) ')

user = txtadv.Player(username, tutorial, 0)

r1 = txtadv.Rooms('locked', 'key')

r1.inv.position.east = 1

print(f'{user.position.__dict__}')

user_direction = {
    'FaceN': {"north": 1, "east": 0, "south": 0, "west": 0},
    'FaceE': {"north": 0, "east": 1, "south": 0, "west": 0},
    'FaceS': {"north": 0, "east": 0, "south": 1, "west": 0},
    'FaceW': {"north": 0, "east": 0, "south": 0, "west": 1},
}

while user.levels_complete < 2:
    
    fresh_input = input()

    if fresh_input in user_direction:
        user.position = user_direction[fresh_input]
        
    elif fresh_input == 'Help':
        help()

    user.levels_complete += 1

print(f'{user.position}')
    

#tut()
#room()
#help()

# while user.levels_complete == 0:
    





# put everything above here and uncomment at the end
# current_datetime = datetime.datetime.now()
# print(f'Congratulations {user.name} you finished the game!!', current_datetime)

