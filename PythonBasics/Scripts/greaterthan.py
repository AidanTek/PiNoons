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