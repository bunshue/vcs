import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

import copy, random, sys, time

WIDTH = 16
HEIGHT = 8

nextCells = {}  #字典
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = 'Y'
        else:
            nextCells[(x, y)] = 'N'

print(type(nextCells))
print(nextCells)

cells = copy.deepcopy(nextCells)

print('顯示內容')
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(cells[(x, y)], end = '')
    print()

print('Press Ctrl-C to quit.')

while True:
    try:
        time.sleep(1)
        print('A', end = ' ')
    except KeyboardInterrupt:
        print('你按了 ctrl + C, 離開')
        sys.exit()

