import txtadv
import datetime, random
from cat_picture.cat import pic
from colort import colorize, ForegroundColor as fc, BackgroundColor as bc

# let user be able to set name
# make class for user, room and inventory
# game will need to be in loop with the final stage closing the loop and ending the game
# add end of game message outside of above mentioned loop
# make r1 loop
# making the tutorial before the room will help me define the room
# added progress to Room, now making clue a function that will call the relevant clue based on room progess
# Make item poisiton Random with random mod
# need to cap the progress counter to the max clue index
# putting in styled text to differentiate between outputs
# will need to categorise the texts into different parts (User Prompt, Help, Narrator)
# Cleaning and reading for submissions



Clues = [
    'Have you looked around?',
    'Try putting the mirror under the light.',
    'What does that button do?',
    'Walk out.']

user_direction = {
    'FaceN': {"north": 1, "east": 0, "south": 0, "west": 0},
    'FaceE': {"north": 0, "east": 1, "south": 0, "west": 0},
    'FaceS': {"north": 0, "east": 0, "south": 1, "west": 0},
    'FaceW': {"north": 0, "east": 0, "south": 0, "west": 1},
}

def colour_text(text, color):
    input(colorize(text, color))

def tut():
    while user.first_try == 'Y':
        print('Welcome to the Escape Room!')
        colour_text('When you see text like with press enter to move on', narrator)
        print('when the terminal like below. enter one of your user commands. Try: Help')
        first_prompt = input()
        if first_prompt == 'Help':
            help()
            user.first_try = 'N'
        else:
            print('You need to enter Help correctly to continue.')
        

def room():
    while r1.lock == 'locked':
        colour_text('When you see text with the red background(like is) it will wait for your to press enter before continuing', narrator)
        r1.lock = 'unlocked'

def help():
    print('All rooms have a locked door and a puzzle that must be solved to unlock it.')
    prompt =  'nothing'
    while prompt != 'Exit':
        prompt =  input('Please enter: Clue, Commands or Exit, to return to the game. ')
        if prompt == 'Clue':
            print(Clues[r1.progress])
                  
        elif prompt == 'Commands':
            print('Below is a list of prompts, followed by their functionality.')
            print('FaceN : will make the user face North')
            print('FaceE : will make the user face East')
            print('FaceS : will make the user face South')
            print('FaceW : will make the user face West')
            print('Pickup : will allow you to pick up object X.')
            print('Use(item)on(enviroment) : will allow you to use object X, if possible')
            print('Giveup : will end game')
            print('Insperation : will show you who your getting back to')
            user.first_try = input('Do you want the tutorial repeated? (Y/N) ')
            tut()            

        elif prompt == 'Exit':
            return prompt == 'Exit'
        
        else:
            print('Invalid prompt. Please try again')
            prompt =  input('Please enter: Clue, More or Exit. ')

narrator = bc.RED
user_prompt = bc.LIGHT_BLUE
helper = bc.GREEN

# Main
username = input('What is your name? ')
tutorial = input('Do you want the tutorial?(Y/N) ')

user = txtadv.Player(username, tutorial, 0)

r1 = txtadv.Rooms('Locked Door', 'Light', 0)
r1.inv.items = ['Mirror Peice']
r1.inv.position = {"north": 0, "east": 0, "south": 0, "west": 0}
positions = ["north", "east", "south", "west"]
random.shuffle(positions)
r1.inv.position[positions[0]] = 1

tut()

colour_text('You wake up in darkness. There is 1 thing on your mind Escape!', narrator)
colour_text('The Room is almost completely black, there is however a small column of light.', narrator)


while user.levels_complete < 1:

    fresh_input = input()

    if fresh_input in user_direction:
        user.position = user_direction[fresh_input]
        if user.position == r1.inv.position:
            print('You Found a Mirror Peice on the ground.')
        elif user.position != r1.inv.position:
            print('There is nothing there.')

    elif fresh_input == 'Pickup' and user.position == r1.inv.position:
        user.inv = r1.inv
        r1.progress += 1
        print('Mirror Peice added to your inventory')

    elif fresh_input =='Use(Mirror Peice)on(Light)' and user.inv == r1.inv:
        r1.progress += 1
        print('Using the Mirror Peice, you have revealed a Button on the wall.')
        button = input('Do you press the button(Y/N)? ')
        if button == 'Y':
            print('The Door Unlocks and you can leave the room.')
            r1.lock = 'Unlocked Door'
            r1.progress = -1
        else:
            print('You have stepped back into darkness and cannot see.')

    elif fresh_input == 'Leave Room' and r1.lock == 'Unlocked Door':
        user.levels_complete += 1

    elif fresh_input == 'Help':
        help()

    elif fresh_input == 'Insperation':
        pic()

    elif fresh_input == 'Giveup':
        user.levels_complete == 1

    else:
        print('Invalid promtp. Please Try again.')


current_datetime = datetime.datetime.now()

if user.levels_complete == 1:
    print(f'Congratulations {user.name} you finished the game!!', current_datetime)

else:
    print(f'Better luck next time, {user.name}.', current_datetime)





