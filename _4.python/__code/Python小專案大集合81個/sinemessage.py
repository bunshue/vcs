"""Sine Message, by Al Sweigart al@inventwithpython.com
Create a sine-wavy message.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import math, shutil, sys, time

WIDTH, HEIGHT = shutil.get_terminal_size()
print('視窗大小 W =', WIDTH, 'H =', HEIGHT)

WIDTH -= 1

print('Sine Message')
print('(Press Ctrl-C to quit.)')
print()
print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')

while True:
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')

step = 0.0  # The "step" determines how far into the sine wave we are.
# Sine goes from -1.0 to 1.0, so we need to change it by a multiplier:
multiplier = (WIDTH - len(message)) / 2

try:
    while True:  # Main program loop.
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.25  # (!) Try changing this to 0.1 or 0.5.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
