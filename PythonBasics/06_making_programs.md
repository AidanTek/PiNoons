# Making Programs in Python

The previous topics have covered a range of key methods in Python programming. It may all seem a little bit abstract at the moment, an important part of learning is applying what you know, so beyond this point it is good to start working towards some ideas of your own and experimenting.

This topic aims to share some approaches to building functioning programs in Python3.

## Abstraction 

When you **import** a module or part of a module, you are actually just linking in another Python script. Typically we do this because we want to take a complex task and make it simpler. This could be a Twitter client for example - writing your own code to use the Twitter API might be a tedious task, and you might want to use it over and over again. A Twitter Client like [Tweepy](https://www.tweepy.org/) breaks down the complex process into a module that means the user only ever needs to write a couple of lines of code to interract with a Twitter account (Twitter bot anyone?) - this process is called *abstraction*

Abstraction is not limited to you having to write your own modules - any process that compresses complex tasks can be thought of as abstraction. A common process that you will definitely want to use is creating your own functions. This is possible with the **def** method. For example:

```python
# lotteryselector.py

'''
This program will help you pick your Lotto numbers, I take no
responsibility for what you do with them...
'''

import random

# A user defined function for generating a list of random numbers
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
                repeat = False  # exit while loop to record the number
        lottolist.append(ball)

    return lottolist

winning = lotterygen()

print("Your lucky numbers are:")
print(winning)
```

Read through the program and try to understand how the **def lotterygen()** segment works. **lotterygen()** is now a defined function that can be used anywhere subsequently in the program. To use it at any point, all that is needed is to call the function by typing lotterygen(). 

In this case, the function outputs a list of numbers - this is achieved using the **return** method. Note that a function does not need to return anything. lotterygen() is stored in the variable 'winning' - but we could have just printed the output directly with a command like print(lotterygen()).

A user defined function can also take an input of some kind. This might be useful for performing math operations:

```python
# mathfunction.py

def multiplyab(a, b):
    result = a*b
    return result

op_a = input("Input number to multiply: ")
op_b = input("Input number to multiply by: ")

check = multiplyab(int(op_a), int(op_b))

print()

print('The result is {}'.format(check))
```

Any input should be specified when the user function is defined.

## Flow

**Flow** or **Control Flow** can be used to describe how a program works over time. You have probably worked out by now that a Python script starts at the top of the file, and is then executed line by line until the end of the file is reached - if there is nothing else to do then the program will end. As shown in the previous topic, loops can break this flow - in some cases indefinitely. 

Let's look at a number guessing game that uses a loop to control the flow of the program. 

```python
# numberguess.py

from random import randint

n = randint(0, 10)

print("Can you guess the number?")

guess = 999 # An irrelevant number in this scope

while guess != n:
    guess = int(input("What is your guess? "))
    
    if guess != n:
        print("Wrong!")
        print()
    else:
        print("Correct! Goodbye!")
```


# For fun

```python
# Emoji Generator

from random import randint, choice
from time import sleep

emojis = [':)', ':(', '<3', ':P', ';)', ';P', '8)', ':S', 'XD', ':/']

# Print emojis forever
while True:
    text = ""
    
    for n in range(1, 50):
        text += choice(emojis)
        text += " "
    
    print(text)
    sleep(5)
    
```