# Loops and Lists

This section covers two more fundamentals in programming, which can be found in virtually any language. Lists and loops.

## Lists

A list is a *data set*, a collection of variables that might look like this:

```python
mylist = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
```

In this case, we have a list of strings. The entry in the list has the index 0, then add 1 for each subsequent entry to the right. You can access an entry in a list like this:

```python
print(mylist[4])

mylist[2] = 'Cat'
```

Try it out:

```python
# basiclist.py

mylist = ['First', 'Second', 'Third', 'Fourth', 'Fifth']

print(mylist)

print(mylist[4])

mylist[2] = 'Cat'

print(mylist)
```

Something a bit quirky about Python is that it allows you to mix up data types in a list, it won't care if you mix up strings, floats and integers - just don't try to multiply a float with a string!

Python provides a number of methods to format and manipulate lists [which can be found here](https://docs.python.org/3/tutorial/datastructures.html).

Another useful thing to know is that you can create lists within lists - this is called 'nesting'. Try out this example:

```python
# lols.py

lols = [[1,2,3], [4,5,6], [7,8,9]]

print("Outer list:")
print(lols)

print()

print("Inner lists:")
print(lols[0])
print(lols[1])
print(lols[2])

print()

print("Inner list indexing:")
print(lols[0][0])
print(lols[0][1])
print(lols[0][2])
```

You get the idea!!

## Loops

Looping is a super useful method in programing - many programs run as a continuous loop of commands. To pluck one example out of the air, let's think of a system that can turn on a light when you clap your hands. The system has a sound sensor and of course a light. A continuous loop constantly checks the sound sensor (a sensor only gets a reading at as a snapshot in time) to detect a peak in volume - when a peak is detected, the light is turned on. This program would not function without the loop, it would have to be run over and over again otherwise. 

There are two types of loops that are useful to get to grips with, **for** loops and **while** loops. 

### for

In Python, a **for** loop is a way of iterating through a sequence of some kind - **for** loops can be found in a number of programming languages such as C, but the way they are used in Python is different. It is a flexible method which can do a whole manner of things, so we will just cover the basic use here. A **for** loop will iterate through the input that you give it, and can repeat a segment of code each time it loops. Try this example:

```python 
# repeats.py

import time
repeats = 10

for i in range(0, repeats):
    print('This is repetition no.:{}'.format(i))
    time.sleep(0.5)
```

The range() function creates a sequence of numbers, from the left value to the right - we used a variable for the right value which could be changed. The **for** method iterates through the range() until it reaches the end. The variable i will have the same value as the loop iteration - this is a bit hard to explain, but all should become clear soon - pay attention to the output, how does it change for each loop iteration?

Notice that the end of the **for** line has a **:** so we need an indent for the code section that we want to loop

Try changing the left and right values of range() to see how it affects the loop. Before we move on, why not look up range() in the Python documentation?

Python allows you to do some pretty odd things with **for** which often turn out to be useful in the right circumstances, for example, you can iterate over the characters in a string:

```python
# forstring.py

import time

x = "Vladimir"
y = "f0rg3tful"

z = []

for character in x:
    print(character)
    time.sleep(0.5)

print()

for character in y:
    z.append(character)

print(z)
```

The string **x** is printed out character by character, the string **y** is loaded character by character into a list using the .append() method. 

You can also use a for loop to iterate through a list:

```python
# forlist.py

animals = ['cat', 'dog', 'camel', 'whale', 'unicorn']

for index in animals:
    print(index)
```

As a quick challenge, can you break a string into a list using a for loop, and then use a for loop to combine it back into a string? Make sure you print each stage so you can see what is happening.

### while

A **while** loop will repeat continuously providing the input statement remains **True**. 'While this is true, keep on doing that'. It could be used to repeat something a set amount of times: 

```python
# whileless.py

from time import sleep

loops = 0

while loops < 10:
    print(loops)
    sleep(1)
    loops += 1

print("End of loops")
```

The variable 'loops' has 1 added to it for each loop. The statement given to **while** is **True** providing that 'loops' is less than 10.

It is not uncommon to see simple programs built around **while** loops that never end:

```python 
# forever.py

from time import sleep

print("This program loops forever")
print("press CTRL+C to break the loop")

while True:
    print("Looping again")
    sleep(1)
```

You can also use while loops to effectively pause a program while waiting for something to happen - maybe you need to wait for a button or key to be pressed to acknowledge the user has read something, or wants to proceed.

## Summary

* **Lists** are data sets that can contain mixtures of data types. You can even make lists of lists, and even 'nest' variables in lists
* **for** loops are used to iterate through a sequence of some kind, this is useful for locating an item in an index, or making a staged transition of somekind, like fading in a light instead of turning it on immediately.
* **while** loops will loop continuously until the argument input is no longer **True**