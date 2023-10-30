# # I have made this file as a tester to make individual aspecsts instead of cluddering main.py

# import txtadv
# import datetime

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


