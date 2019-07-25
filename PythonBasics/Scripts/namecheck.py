# namecheck.py

name = input("Type in your name: ")
namecheck = input("Type it in again: ")

if not name == namecheck:
    print("You made a mistake")
else:
    print("Ok, your name is " + name)