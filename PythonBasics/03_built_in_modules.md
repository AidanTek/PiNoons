# Built-in modules: Time and Random

Beyond functions like print() and input(), Python has a range of built-in *modules* which provide extra functionality and advanced features. A module is in effect a script in itself which will contain a number of functions. The level of complexity under the hood can vary as a module might do anything from providing some simple shortcuts in writing a program, to offering novel features that for example might make use of system parameters, create files like spreadsheets or text documents, or use peripherals like the Raspberry Pi GPIO.

It is also possible to extend Pythons syntax with external modules that others have made, in fact it is not too difficult to write your own, but that is not dealt with here.

In this topic we are going to look at two useful built-in modules, **time** and **random**.

## Time
### sleep()

The **time** module gives your script access to the system clock, allowing you to make use of a variety of time dependant operations in your code. For example, maybe you want to create a pause in a program, one way to do this is with sleep(). Try creating a new script in Thonny or your editor of choice, save the file as something like waiting.py and enter the following code:

```python
# waiting.py

import time

print("This is a demonstration of sleep()")

time.sleep(2)

print("sleep() is part of the time module")

time.sleep(2)

print("sleep() takes an argument in its brackets")

time.sleep(2)

print("The argument is the time to wait in seconds")

time.sleep(0.5)

print("Use a float/fraction as an argument to wait less than a second")
```

Notice the first line of code in this program is using **import** to access the **time** module. time has a number of functions, sleep() is just one of them. sleep() instructs the program to pause for a set amount of time in seconds. The time to wait is set by entering a number as an argument in the round brackets.

Alternatively, you can import the specific function you want from a module like this:

```python
from time import sleep
```

which means instead of writing

```python
time.sleep(1)
```

you can write

```python
sleep(1)
```

And that is all there is to that!

### monotonic()

Turning the idea of sleep() on its head, maybe you want to know how much time has passed? monotonic() from the time module reports the time in seconds since the script began.

```python
# printmonotic.py

from time import monotonic, sleep

print(monotonic())

sleep(1)

print(monotonic())

sleep(1)

print(monotonic())
```

Here is a simple reaction timer script that demonstrates the use of monotonic - save it as reaction.py:

```python
# reaction.py

from time import monotonic, sleep

prompt = '''This game tests your reaction speed
type your name as fast as you can when the timer runs out
remember to press ENTER/RETURN'''

print(prompt)

sleep(1)

print("READY...")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")

reaction = monotonic()

name = input("TYPE: ")

result = monotonic() - reaction

print('You typed {} in {} seconds.'.format(name, result))
```

Try running the program, test it works a second time by delaying how long you take to enter something at the point of prompt.

The action is all taking place in the last couple of lines. The variable 'reaction' is a *float* data type, a decimal point number - it stores the current timer output of monotonic(). Once the user has entered something, the variable 'result' is created and quickly processes the reaction time by subtracting the stored result in 'reaction' from the updated output of monotonic() - remember monotonic() is forever increasing. The result is then printed out.

In a real world situation, this could be used to record the lap time of an athlete completing a circuit.

As it is another new thing, notice the variable at the top of this script called 'prompt'. This variable is storing a string data type - using three speech marks ''' allows you to enter a section of text where any formatting such as writing on a new line is maintained.

### asctime()

There are a whole range of functions derived from the systems clock in the time module. The system clock is usually synced to the web - on the Raspberry Pi, it is necessary to have an internet connection in order for the correct time to be available. One of the more nicely formatted time functions is asctime(), which returns the current date and time as a string:

```python
# datetime.py

import time

t = time.asctime()

print('The date and time according to the system is: ' + t)
```

Take a look at the [official documentation on the time module](https://docs.python.org/3/library/time.html) for more functions

## Random

**random** is a great module for escaping inertia in a program - particularly useful in generative applications that might be useful in games, simulations or creative programs.

There are lots of exotic [functions in the random module](https://docs.python.org/3/library/random.html), let's look at some of the simpler ones

### random()

Outputs a random float data type between 0.0 and 1.0:

```python
# random3.py

from random import random

rand1 = str(random())
rand2 = str(random())
rand3 = str(random())

print("Random number 1 = " + rand1)
print("Random number 2 = " + rand2)
print("Random number 3 = " + rand3)
```

Notice that there are quite a few decimal places!

### randint()

Outputs an integer from somewhere within a set range of numbers:

```python
# randint766.py

import random

print("Here are a bunch of random numbers between 7 and 666:")
print(random.randint(7, 666))
print(random.randint(7, 666))
print(random.randint(7, 666))
```

### choice()

To jump ahead a little, choice() returns an option from a list - lists will be explored in a later topic, but for now, try the program below to get a taste:

```python
# listchoice.py

from random import choice

names = ['Vlad', 'Pete', 'Nancy', 'Spud', 'Seren', 'Oliver']
colours = ['Red', 'Green', 'Blue', 'Yellow', 'Pink', 'Orange']

print("Your best friends name is " + choice(names))
print("Their favourite colour is " + choice(colours))
```

## Summary

* Python comes with a number of built-in modules that expand the syntax
* The time module grants access to a number of functions based on the operating system clock
* The random module grants access to a variety of ways to generate pseudo-random numbers and choices

There are plenty more built-in modules that expand the Python language. **math** is an essential module for making advanced number processing more palatable.  **os** and **sys** allow direct manipulation of files in the operating system, perhaps even from a USB drive. Want to work with html, json, csv or even email? Guess what, there are modules to do just that!

[Take a look at the list of built-in modules here](https://docs.python.org/3/py-modindex.html)

Be sure to familiarise yourself with the [Python Documentation](https://docs.python.org/3/index.html), all the information you need is there.
