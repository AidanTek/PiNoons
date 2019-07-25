# mathfunction.py

def multiplyab(a, b):
    result = a*b
    return result

op_a = input("Input number to multiply: ")
op_b = input("Input number to multiply by: ")

check = multiplyab(int(op_a), int(op_b))

print()

print('The result is {}'.format(check))