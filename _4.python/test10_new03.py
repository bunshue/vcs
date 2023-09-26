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



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

import os
import sys

foldername = 'C:/_git/vcs/_1.data/______test_files5'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個


print('---- os --------------------------------------------------------')	#60個

import test
packagedir = os.path.dirname(test.__file__)

import email
packagedir = os.path.dirname(email.__file__)
print(packagedir)

print('------------------------------------------------------------')	#60個








print(sys.maxsize)
print(2 ** 32)

import stat

print(os.name)
print(os.sep)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

print(os.getpid())



import os

def getuser():
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
        print(name)
        user = os.environ.get(name)
        if user:
            print(user)
            return user

print('get user name')
ccc = getuser()
print(ccc)



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



import os
import sys
m = sys.modules.get('__main__')

print(m)



foldername = 'C:/_git/vcs/_1.data/______test_files5'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

name = os.path.basename(filename)

print(name)


globs = {}
globs = globs.copy()
print(globs)

print()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

if filename.endswith(".jpg"):
    # It is a module -- insert its dir into sys.path and try to
    # import it. If it is part of a package, that possibly
    # won't work because of package imports.
    dirname, filename = os.path.split(filename)
    print(filename[:-3])




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個








filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
print(filename)
filename = os.path.normcase(filename)
print(filename)




print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個



print('---- sys --------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個




