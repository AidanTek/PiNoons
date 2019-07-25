# 02 Using the command line and the REPL

Python scripts/programs do not need an editor or special program to run. Once Python is installed in your system, scripts can be executed by the command line. This repository is intended for people learning Python programming on the Raspberry Pi, and as such will not go into detail on command line operations on other systems - but please know that you can do the same on any computer. Linux, and Mac OS X have a utility app called Terminal that provide access to a command line prompt. Terminal commands on the Raspberry Pi will be covered in more detail in the PiBasics directory of this repository.

On the Pi, Terminal can be launched with the keyboard combination **ctrl + alt + t**

## Executing a script with the command line

Python scripts can be executed using the python3 command, you will need Terminal to be in the directory that the script is stored in, or you will need to provide the complete file path:

```console
python3 hello.py
```

or something like

```console
python3 /home/pi/myPython/hello.py
```

Try running one of the scripts from the previous topic this way.

## The REPL

Python includes a powerful tool called the REPL. This stands for (R)ead (E)valuate (P)rogram (L)oop. In a nutshell, it is a live programming environment for Python, which is great for testing out ideas - try it now in Terminal by typing:

```console
python3
```

You can now type in any of the commands you know so far and get instant feedback. Try the following:

```python
print("Hello")

name = input("Enter your name: ")

print(name)
```

You can reset the current REPL by pressing **ctrl + c**. This will clear any variables and cancel any active loop or operation.

To exit the REPL, press **ctrl + d**

There are two other useful features of the REPL, autocomplete and recall (there are probably more shortcuts as well!)

When you are typing something, you can press **tab** and the REPL will try to complete it; try typing *pri* and press **tab** - which should result in completing to *print(*

Autocomplete will also work with variables that you have created. Try typing *na* and autocompleting with **tab** to get *name*

The recall function allows you to scroll up and down previously entered commands, using the up and down arrow keys. Try this now.

## Summary

* A Python script can be run from a command line prompt with the command python3 <filename>
* Typing python3 with no filename in the command line will launch the REPL
* Pressing the tab key in the REPL will attempt to complete what you are typing
* Pressing the up or down keys in the REPL will recall the commands you have previously entered
* Pressing ctrl+c will reset the REPL
* Pressing ctrl+d will exit the REPL

That's it. The REPL is a useful tool for testing ideas in code - perhaps you want to see if you can combine two functions in some way, or if a function will output what you expect - or that a data type is compatible with something else, these are all good use cases for the REPL
