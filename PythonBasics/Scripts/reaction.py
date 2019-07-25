# reaction.py

from time import monotonic, sleep

prompt = '''This game tests your reaction speed
type your name as fast as you can when the timer runs out
remember to press RETURN/ENTER'''

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

