import random

value1 = "10"

def dice(value1):
    max = int(value1)
    r = random.randint(1, max)
    return str(r)

msg = dice(value1)
print(msg)