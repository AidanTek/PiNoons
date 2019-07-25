# friendmatch.py

from random import choice

names = ['Fred', 'Pete', 'Hannah', 'Mary', 'James', 'Rachael']

person1 = choice(names)

person2 = choice(names)

s = "Person 1 is called " + person1 + " and person 2 is called " + person2

print(s)

if person1 == 'Fred' and person2 == 'Fred':
    print("Both people are called Fred")
elif person1 == 'Fred' or person2 == 'Fred':
    print("Someone is named Fred")
else:
    print("Nobody is named Fred")