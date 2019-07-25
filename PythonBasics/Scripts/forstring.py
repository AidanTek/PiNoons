# forstring.py

import time

x = "Vladimir"
y = "f0rg3tful"

z = []

for character in x:
    print(character)
    time.sleep(0.5)

for character in y:
    z.append(character)

print(z)