# 01. Basic Input and Output

It is recommended that you have at least completed the 'Scripts, functions and data', 'Built in Modules' and 'Logic' topics of the Python Basics section before starting here.

The Raspberry Pi has a set of 'header pins' on one side - these are a bunch of tiny pins that can carry electronic signals. Some of these pins are used for sharing the Pi's power supply, it is necessary in every case to at least connect **ground** between circuits, and sometimes you will want 5V or 3V3 to power something as well. The rest of the pins work as inputs and outputs, meaning a seperate device can send or receive signals or data from the Pi. Some of the pins are capable of quite sophisticated transmissions for particular communication protocols - but we won't deal with those here.

## Breadboard

A 'breadboard' is a simple bit of hardware makes prototyping electronics possible without having to solder. To make a 'circuit' you need some closed path of components between positive and negative volts. Breadboard makes this easy by giving you access to a good number of linked connection points, arranged into rows and columns. A typical breadboard has 4 rows which do not connect with each other, but are a strip of metal that runs along the length of the board. The columns are typically arranged in groups of 5, a groove in the middle of the breadboard seperates the top set of columns with the bottom - they do not join across this groove. To make use of the board, you can use wires or components to jump across on column to another, or from a row to a column etc. See the diagram below:

[breadboard image]   

## Input

The most basic input device we can use to interface with the Raspberry Pi is a button or switch. An electronic switch is a very simple device as in essence it is made up by two bits of conductive material that either do or do not touch together. Two parts are needed to implement a switch input - a switch of some kind (of course!) and a resistor.

When we want to read from an input like this, we need to attach it to a free GPIO pin, and write some software that is instructed to pay attention to the state of that pin. The state of the pin can only ever be ON or OFF, or 1 or 0. In electronics terms this is HIGH or LOW voltage measured on the pin, we are talking about a 'logic level' voltage in this case which is defined by the Pi's logic operating voltage - 3.3V. 3.3V is logic HIGH and 0V is logic LOW. 

The name of the game is to use the switch to change a pin from one logic level to another. Try building the circuit below:

[circuit image]

The resistor is a 10k ohm, or something close to that value like 12k will also do us fine. When the button is not pressed, the pin is 'pulled' HIGH by the resistor link to 3.3V. When the button is pressed the pin drops to LOW, because there is effectively a short circuit straight to ground. 

Here is a simple program to get some input from the button:

```cpp
# simplebutton.py

from gpiozero import button
from time import sleep

buttonpin = Button(17) # Button is on pin 17
val = 0 # This variable will hold the button state

# loop forever, press ctrl-c to quit
while True:
	val = buttonpin.value

	print(val)
	sleep(0.1)
```

If everything worked out, then you should see a stream of 0's in the shell. When you press the button, this changes to a value of 1. This program works but it has very limited application as we are just capturing the button state momentarily. Let's go one step further for now and implement a **transition**.

A transition is a clever little mechanism that is designed to detect when something changes from one state to another, as opposed to reacting to a state at a point in time. The difference here is that with the first example, you could use the button to turn a light on, but it would turn off as soon as the button is released as the light would just follow the 'val' variable. With a transition you could get a light to switch on with one press of a button, and then switch off again when pressed a second time. To achieve this we need two variables instead of one. The first variable (val) stores the current state of the button, the second variable is used to check if 'val' has changed from 0 to 1 or from 1 to 0 - this change is the *transition*.

Try the program below which has some additional lines of code:

```cpp
# statechangedetect.py

from gpiozero import button

buttonpin = Button(17)
val = 0
lastval = 0

while True:
	val = buttonpin.value

	if not val == lastval: # if val is not the same as lastval
		lastval = val # then make them the same and...
		print('Button State Changed to {}'.format(val)
```

Notice in this program we did not need the time module - it was used simply to stop the shell from being overloaded with thousands of print() commands. Now print() is only used when the button is pressed or released. Take a moment to look over the program to see how this works.

## Output

Possibly the easiest way to test an output on the Raspberry Pi is to use an LED (Light Emitting Diode) - something we can blink! An LED has a positive and negative side (called the anode and cathode respectively), the positive side has a longer leg and the negative side is shorter. When the positive side connected to a higher voltage than the negative side, current flows across the LED and it lights up. One thing to mention here is that an LED can't control how much current flows across it, and too much current will burn it out - it may even pop in a puff of smoke. To prevent this, we use a resistor in series.

The GPIO pins in output mode can be set to switch between HIGH and LOW states. Just like with our input logic, a HIGH state is 3.3V and a LOW state is 0V or ground. We can connect the positive leg of an LED to a pin and change the pin state to control the LED. Try building the circuit below:

[LED Circuit image]

A good starting resistance to use is 470Ω, if the LED is too dull, try a lower resistor value.

Try entering the code below:

```cpp
# simpleLED.py

from gpiozero import LED
from time import sleep

ledpin = LED(10) # make an LED object

while True:
	ledpin.toggle() # change the state of the LED pin
	sleep(1)

```
