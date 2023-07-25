import time
import os
import sys
import itertools
import threading
import subprocess
from optparse import OptionParser, SUPPRESS_HELP
import platform

def bark(duration):

    _time = time.time
    _sleep = time.sleep
    
    # We give the parent some time to be ready.
    _sleep(1.0)

    start_time = _time()
    end_time = start_time + duration * 2.0
    i = 0
    while _time() < end_time:
        print('b')
        i += 1


bark(0.2)


import platform

print("== %s %s (%s) ==" % (
    platform.python_implementation(),
    platform.python_version(),
    platform.python_build()[0],
))

# Processor identification often has repeated spaces
cpu = ' '.join(platform.processor().split())
print("== %s %s on '%s' ==" % (
    platform.machine(),
    platform.system(),
    cpu,
))
print()



'''
import hashlib

string = 'lion-mouse'

result = hashlib.sha1(string).digest() 

print(result)
'''

