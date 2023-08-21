'''

random 專區

'''
import os
import sys
import time
import math
import random

print('------------------------------------------------------------')	#60個


from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

class Ball:
    def __init__(self):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2 # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

ballList = [] # Create a list for balls

length = len(ballList)
print('length = ', length)

for i in range(6):
    ballList.append(Ball())

length = len(ballList)
print('length = ', length)

for i in range(length):
    print('第', i, '個 : ', ballList[i].color)

'''
for ball in ballList:
    print(ball.color)
'''

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

print('------------------------------------------------------------')	#60個




from random import randint, random, getrandbits

def getrandbytes(size):
    return getrandbits(8 * size).to_bytes(size, 'little')


ccc = b'111' + getrandbytes(100)

print(type(ccc))
print(ccc)

datacount = randint(16, 64) * 1024 + randint(1, 1024)

ddd = random() * randint(-1000, 1000)
print(ddd)





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




import random
print(dir(random))


import random
t = random.randint(1, 100)
print(t)

import random as R
t = R.randint(1, 100)
print(t)


import random
r1 = random.randint(1, 6)
r2 = random.randint(1, 6)
print(r1 + r2)
lst1 = list(range(11))
print(lst1)
r3 = random.choice(lst1)
print(r3)



for _ in range(1000):
    x = random.random() * math.exp(random.random()*200.0 - 100.0)


for _ in range(1000):
    e = random.randrange(300)
    n = random.randrange(-10**e, 10**e)



'''
def _random_getnode():
    """Get a random node ID, with eighth bit set as suggested by RFC 4122."""
    import random
    return random.randrange(0, 1<<48) | 0x010000000000


        return UUID(bytes=os.urandom(16), version=4)
    except:
        import random
        bytes = bytes_(random.randrange(256) for i in range(16))
        return UUID(bytes=bytes, version=4)


        import os
        if int(os.uname().release.split('.')[0]) >= 9:

        import random
        clock_seq = random.randrange(1<<14) # instead of stable storage

'''



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




