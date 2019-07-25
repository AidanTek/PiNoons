# whileless.py

from time import sleep

loops = 0

while loops < 10:
    print(loops)
    sleep(1)
    loops += 1

print("End of loops")