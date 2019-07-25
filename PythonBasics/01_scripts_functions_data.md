# 01 Scripts, functions and data

This topic covers the basics of creating a Python program, and introduces some fundamental concepts. The title doesn't sound too sexy, but bear with us!

A text file that contains Python commands can be called a *script*, it will have a .py extension like hello.py to indicate that it is a Python file. A script can be created in virtually any text editor, but some editors will provide some extra fancy features like *autocomplete* (essentially predictive text for code) and *syntax highlighting* where key components that make a program function are colour coded, both making the experience of writing code more accessible and streamlined.

It is suggested that you start with an editor like Thonny, Mu or IDLE

You might want to put a folder/directory in an easy to access location on your hard drive to save your work.

## Say hello and print your name

In Thonny or your editor of choice, create a new file (use the new icon or choose from the menus) and try typing the following:

```python
# hello.py

print("Hello")

name = "Vladimir"

print("My name is " + name)
```

When you have typed the program out, save the program as hello.py and press the run button in the editor to see the result in the *Shell*. You have probably already figured out what this program will do, maybe you even went crazy and put your own name in - it is simple of course but there is plenty to unpack here!

The first line starts with a # - this is a comment, it is just for the programmer or someone else to interpret the code, and is ignored by the program itself.

On the next line there is a command called print(). This is a *function*. A function is like a tiny software machine that produces some kind of output, sometimes requiring an input of some kind. A function will be a keyword followed by rounded brackets:

```python
print("Hello")
```

The print() function will print the input in the brackets as an output to the *shell*. In the brackets we have a data type called a *string*. Without getting into lots of detail, strings in Python are very flexible data types, they are made up of any combination of letters and numbers. You can tell a string as it will have double or single speech marks like "Hello" or 'Vladimir'. Moving on to the last two lines:

```python
name = "Vladimir"

print("My name is " + name)
```

At the second line of the program, a *variable* object is created. A variable in Python is a container for some kind of data type. This is very flexible and fast to implement and a variable can be manipulated and replaced at any point - it will become easier to understand as we work with variables some more. 'name' is the identity attributed to this variable, it is user defined, meaning that it could called be something else - the identity will be used to summon the contents elsewhere in the program.

The final line uses the print() function again, but something slightly more interesting is going on in the brackets. The two strings "My name is " and 'name' are being combined, where 'name' is recalling the contents of the variable. This is called *concatenating* strings - linking things together in a series. Shall we move on?

## input() and numbers

Let's make a program that involves some user interaction! Create a new file in your editor and save it as question.py. Type out the following program:

```python
# question.py

print("What is your first name?")
print("Type it in and press return/enter")

fname = input()

print("What is your surname?")

sname = input()

print("And how old are you?")

age = input()

print("So, your name is " + fname + sname + "and you are " + age + "years young")
```

Try running the program - if it runs without errors then you should see some prompt in the shell asking you to type in some data. When the script is complete you will see that the final output is not very optimised. Spend a little time now to see if you can improve the output from this line.

This script makes use of a function called input() - this is used for some simple interaction with a program where the user is expected to enter something by keyboard. It expects entry to be completed with an enter/return press.

## Data type conversion and simple processing

Let's do one more thing with this program, to highlight some of the flexibility that can be found in the Python language - let's get the program to convert a string, and do some simple processing to produce a new result:

Look at this line:

```python
age = input()
```

The 'age' variable will be stored as a string data type, because that is always the output of the input() function. What if we want to use the input as a number? We need to convert it in some way. Add these lines of code to the end of the program:

```python
years = 100 - int(age)

print("In " + str(years) + " years you will be 100 years old!")
```

Run the code again and see how the program plays out. The variable 'years' is going to be stored as an *integer* data type, a whole number with no decimal point. This is because it has been created by some operation with whole numbers, notice the new function int() which is being used here; int() can convert some data types to an integer for an operation like we are seeing here, so the previously entered 'age' string data type variable is converted to an integer. It is worth noting that if you entered something that is not a number into the 'age' variable - an error would be produced here. Try it.

The final line has another print() output. Notice that another new function is being used *within* the print(). The str() function is another data type conversion. Concatenating expects data types to be the same, so the integer 'years' must be converted to be a string for this line to work.

## Summary

* A python program can be created as a script
* A function is a process within a script that produces some kind of output
* The print() function can be used to print almost anything to your shell prompt
* Variables store data, there are a number of data types available
* A string is a data type that can be made up of any combination of letters and numbers
* An integer is a whole number data type
* Strings can be combined in a sequence, this is called concatenation
* Data types can be converted with functions like int() and str()

That is the end of this topic - but just to finish off, here is an honourable mention to another way to manipulate strings, the *.format* operation; an alternative way to write the print() commands in this program is to not use concatenation, but to insert variables into the strings, have a look below:

```python
print('So, your name is {} {} and you are {} years young'.format(fname, sname, age))

print('In {} years you will be 100 years old!'.format(years))
```

Neat!

There are of course, many ways to achieve the same thing, and many shortcuts. How about this one?:

```python
age = int(input())
```

A complete list of the built-in functions that can be used in Python can be [found here](https://docs.python.org/3/library/functions.html)
