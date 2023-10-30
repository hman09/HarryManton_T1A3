import txtadv
import datetime, random
from cat_picture.cat import pic

# let user be able to set name
# make class for user, room and inventory
# game will need to be in loop with the final stage closing the loop and ending the game
# add end of game message outside of above mentioned loop
# make r1 loop
# making the tutorial before the room will help me define the room
# added progress to Room, now making clue a function that will call the relevant clue based on room progess
# Make item poisiton Random with random mod
# need to cap the progress counter to the max clue index

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

def tut():
    while user.first_try == 'Y':
        print('Blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah')
        user.first_try = 'N'

def room():
    while r1.lock == 'locked':
        input()
        r1.lock = 'unlocked'


def help():
    print('All rooms have a locked door and a that must be solved to unlock it.')
    prompt =  'nothing'
    while prompt != 'Exit':
        prompt =  input('Please enter: Clue, More or Exit. ')
        if prompt == 'Clue':
            print(Clues[r1.progress])
                  
        elif prompt == 'More':
            print('Below is a list of prompts, followed by their functionality.')
            # Was going to make a list of prompts and description, 
            # then make a loop which going through the list and prints them out for line by line output.
            # But feels redundant as will only need a print command here.
            print('FaceN : will make the user face North')
            print('FaceE : will make the user face East')
            print('FaceS : will make the user face South')
            print('FaceW : will make the user face West')
            print('Pickup : will allow you to pick up object X.')
            print('Use(item)on(enviroment) : will allow you to use object X, if possible')
            print('Giveup : will end game')
            print('Insperation : will show you who your getting back to')
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

r1 = txtadv.Rooms('Locked Door', 'Light', 0)
r1.inv.items = ['Mirror Peice']
r1.inv.position = {"north": 0, "east": 0, "south": 0, "west": 0}
positions = ["north", "east", "south", "west"]
random.shuffle(positions)
r1.inv.position[positions[0]] = 1
input('You wake up in darkness. There is 1 thing on your mind Escpae!')
input('The Room is almost completely black, there is however a small column of light.')



while user.levels_complete < 1:

    fresh_input = input()

    if fresh_input in user_direction:
        user.position = user_direction[fresh_input]
        if user.position == r1.inv.position:
            print('You Found a Mirror Peice on the ground.')

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





