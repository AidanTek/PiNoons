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
    
    