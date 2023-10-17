import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個
'''
import numpy as np

N = 10

a = np.arange(N)    #numpy.ndarray

print(type(a))
print(a)

b = range(1, 11)    #range
print(type(b))
print(b)

c = list(b)         #list
print(type(c))
print(c)

for d in reversed(c):
    print(d)

print('------------------------------------------------------------')	#60個

import numpy as np

a = np.array([2,3,4,5,6])
print(f'a = {a}')
b = np.ma.masked_where(a > 3, a)
print(f'b = {b}')

print('------------------------------------------------------------')	#60個

"""
y = x ^ 2
x = [x for x in range(31)]
y = [(y * y) for y in x]
"""

print('------------------------------------------------------------')	#60個

print('取得本程式名稱')
progname = os.path.basename(sys.argv[0])
print(progname)

print('------------------------------------------------------------')	#60個

n = list(range(100))
r = list(range(25))
n = list(range(10)) * 10



print('------------------------------------------------------------')	#60個


import os
import sys

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
head, ext = os.path.splitext(filename)
head, base = os.path.split(filename)



print('------------------------------------------------------------')	#60個

name = 'aaaamock'
message = '%s(%%s)' % name

print(message)

print('------------------------------------------------------------')	#60個

number = 123456
NUMBER_OF_DIGITS = 10
print(number)
numberList = list(str(number).zfill(NUMBER_OF_DIGITS))
print(numberList)
numberList = list(str(number))
print(numberList)


print('------------------------------------------------------------')	#60個

time.sleep(random.randint(20, 50) / 10.0)

print('------------------------------------------------------------')	#60個

"""
drawTime = time.time()
#等待使用者按鍵輸入
input()  # This function call doesn't return until Enter is pressed.
timeElapsed = time.time() - drawTime

timeElapsed = round(timeElapsed, 4)
print('You took', timeElapsed, 'seconds to draw.')
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


pigLatin = 'this is a lion-mouse'


try:
    pyperclip.copy(pigLatin)
    print('(Copied pig latin to clipboard.)')
except NameError:
    pass  # Do nothing if pyperclip wasn't installed.

print('------------------------------------------------------------')	#60個

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


spongecase = 'this is aaaaaaaaa'

try:
    pyperclip.copy(spongecase)
    print('(cOpIed SpOnGeCasE to ClIpbOaRd.)')
except:
    pass  # Do nothing if pyperclip wasn't installed.

print('------------------------------------------------------------')	#60個


import random

numberOfDice = 5
numberOfSides = 6

# Simulate the dice rolls:
rolls = []
for i in range(numberOfDice):
    rollResult = random.randint(1, numberOfSides)
    rolls.append(rollResult)

print(type(rolls))
print(rolls)

# Display the total:
print('Total:', sum(rolls))


# Display the individual rolls:
for i, roll in enumerate(rolls):
    rolls[i] = str(roll)
print(', '.join(rolls), end='')

'''

print('------------------------------------------------------------')	#60個

try:
    import a_python_module
except ImportError:
    print('匯入模組 a_python_module 失敗')
    print('請安裝模組')
    sys.exit()


print('------------------------------------------------------------')	#60個

import time, sys

print('Press Ctrl-C to stop.')

try:
    while True:  # Main program loop.
        print('wait', end = ' ')
        time.sleep(1)  # Add a pause.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.



print('------------------------------------------------------------')	#60個


""" 統計亂數
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper  # Flip the case.
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

