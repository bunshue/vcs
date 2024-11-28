# Homework 2-10
from time import sleep
import random

try:
    while 1:
        print(random.random())
        sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program!")
finally:
    print("See you!")
