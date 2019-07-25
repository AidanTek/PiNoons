# Logic

Functional programs typically need to process some kind of input into some kind of output, and to achieve this will often need to make choices based on the input. Simple programs (and often complex ones) can be mapped out in a flow diagram illustrating the path of choices the process can take. Every programming language makes use of logical operations; if *this* is true then do *x*, else do *y*. Combining logic with topics covered in the previous sections arms you with much of what is needed to start making useful programs!

## if, elif and else

**if** is the fundamental logic operation in computing. Most program functions can be described with the statement 'if this is true then do something', even if the implementation is not so apparent. For example:

* if the button is pressed, turn on the light

You might want some more complexity in such an operation such as:

* **if** the button is pressed
  * **if** the light is on
    * *turn the light on*
  * **else**
    * *turn the light off*

This already looks quite like a program, and is also quite readable. **if** can be combined with **elif** (else if) and **else** to allow for a number of possible outcomes in an operation. The hierarchy of these commands is:

* **if** (this statement is true)
  * execute and exit sequence
* **elif** (otherwise this statement is true)
  * execute and exit sequence
* **elif** (...)
  * execute and exit sequence
* **else** (if none of the above is true)
  * execute and exit

You do not need to use **elif** and/or **else** in every case. Let's try it out...

Type the following code into Thonny, or your editor of choice, save it as something like greaterthan.py

```python
# greaterthan.py

import random

x = random.randint(0, 100)
y = random.randint(0, 100)

print('The value of x is {}'.format(x))
print('The value of y is {}'.format(y))

if x > y:
    print('x is greater than y')
else:
    print('y is greater than x')
```

The script generates two random numbers, and checks which value is greater than the other.

```python
if x > y:
```

**if** instructs the script to perform a logical test. The **>** symbol means 'greater than'.

Notice that the print() functions that follow **if** and **else** are indented to the right by one **tab** press. This is important and mandatory in the Python syntax, it indicates the *control flow* of the program. Whenever a **:** colon is present in the code, the next line will be indented to the right. A uniform use of indentation must be used throughout your program otherwise it will fail to run and you will get an error prompt.

In this case we did a mathematical test, some other math operations are:

* **<** less than
* **==** equal to
* **>=** greater than or equal to
* **<=** less than or equal to
* **!=** not equal to (or alternatively you can write **not** in front of any test to check if 'not' true)

Tests can also be performed on strings, this example shows the use of **not**, in other words, if the statement is 'not' true:

```python
# namecheck.py

name = input("Type in your name: ")
namecheck = input("Type it in again: ")

if not name == namecheck:
    print("You made a mistake")
else:
    print("Ok, your name is " + name)
```

You could use a sequence of logic to make a decision from a set of possible commands:

```python
# udir.py

move = input("Type 'up', 'down', 'left', or 'right': ")

if move == 'up':
    print("You typed up")
elif move == 'down':
    print("You typed down")
elif move == 'left':
    print("You typed left")
elif move == 'right':
    print("You typed right")
else:
    print("Input not recognised")
```

## and, or

Further extensions to make decisions include **and** and **or**. These can be used to check things like

* **if** x **and** y are both true
* **if** either x **or** y are true

Here is an example that makes use of a couple of the things covered so far:

```python
# namematch.py

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
```

It is a fairly silly example - but hopefully you can deploy this practically soon! Notice that a complete argument is required in both cases of **and** and **or** - writing something like *if person1 and person2 == 'Fred'* will not work.

## Summary

* **if**, **elif** and **else** are logic operations that allow your software to make choices based on some kind of input
* Logic can be used to test if a set argument is **true**, numbers and strings can be tested
* **and** / **or** can be used to test multiple statements simultaneously
* **not** will reverse the logic in an argument

These examples scratch the surface when it comes to testing arguments. In Python, you can do things like import a text file and search for a passage of text using **if**, and perhaps output it as a string, or add in a new string to the file at a specific point. You could look for an anomaly in a table of data. You can of course test readings from sensors and turn hardware devices on or off in reaction.

Now is a good time to experiment with some of the things you have learned:

* Try expanding the reaction game by generating some random numbers, giving the user a time limit to complete entry, and checking the correct thing was entered?

* Try to create a guessing game with a random list of names or numbers - can the user guess the random selection?
