import txtadv
import datetime

# let user be able to set name
# make class for user, room and inventory
# game will need to be in loop with the final stage closing the loop and ending the game
# add end of game message outside of above mentioned loop
# make r1 loop

def tut():
    while user.first_try == 'Y':
        print('Blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah')
        user.first_try = 'N'

def room():
    while r1.lock == 'locked':
        input()
        r1.lock = 'unlocked'



# Main
username = 'H'#input('What is your name? ')
tutorial = 'N'#input('Do you want the tutorial?(Y/N) ')

user = txtadv.Player(username, tutorial, 0)

r1 = txtadv.Rooms('locked', 'key')
    

tut()
room()
print(r1.lock)

# while user.levels_complete == 0:
    





# put everything above here and uncomment at the end
# current_datetime = datetime.datetime.now()
# print(f'Congratulations {user.name} you finished the game!!', current_datetime)

