import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

"""
#按 ctrl + c 離開程式

import random, shutil, sys, time

PAUSE = 0.1  # (!) Try changing this to 0.0 or 2.0.
STREAM_CHARS = ['0', '1']  # (!) Try changing this to other characters.

print('按 ctrl + c 離開程式')

try:
    while True:
        print(random.choice(STREAM_CHARS), end='')
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.

print("------------------------------------------------------------")  # 60個

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        # % 12 so we use a 12-hour clock, not 24:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'  # 12-hour clocks show 12:00, not 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        print(hours, minutes, seconds)

        print('按 ctrl + c 離開程式')

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""


print("------------------------------------------------------------")  # 60個

import itertools

print('test itertools')
local_y_range = range(10)
local_x_range = range(10)
coords = list(itertools.product(local_x_range, local_y_range))
random.shuffle(coords)
print(coords)


print("------------------------------------------------------------")  # 60個

print('test random.triangular')

for _ in range(10):
    print(random.triangular(1, 5))

print('test random.uniform')
for _ in range(10):
    print(random.uniform(0.2, 0.9))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
