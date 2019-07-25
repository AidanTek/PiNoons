# lotteryselector.py

'''
This program will help you pick your Lotto numbers, I take no
responsibility for what you do with them...
'''

import random

# A custom function for generating a list of random numbers
def lotterygen():
    lottolist = [] # An empty list
    ball = 0 # A variable to hold an integer

    for n in range(0,6):
        repeat = True # repeat until a unique number is picked:
        while repeat == True:
            ball = random.randint(0,59)
            if ball in lottolist:
                continue # loop again
            else:
                repeat = False  # exit loop and record the number
        lottolist.append(ball)

    return lottolist

winning = lotterygen()

print("Your lucky numbers are:")
print(winning)