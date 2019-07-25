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
