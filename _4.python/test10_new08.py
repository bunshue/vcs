import os

filename = __file__
print(filename)

path_split = filename.split(os.sep)
print(path_split)

print(os.sep)
print(os.altsep)

bn = os.path.basename(filename)
print(bn)

import test
packagedir = os.path.dirname(test.__file__)


import email
packagedir = os.path.dirname(email.__file__)
print(packagedir)

fpath = 'aaaaaaaaaaa'
correctfile = os.path.join(os.getcwd(), fpath)
correctfile = os.path.normpath(correctfile)

ccc = os.path.join(os.getcwd(), 'ziptest2dir')
print(ccc)

'''
import time
print(time.strptime(date, '%Y-%m-%d'))
print(time.strptime(time_, '%H:%M:%S'))
'''


print('------------------------------')  #30個

print('------------------------------')  #30個


print('------------------------------')  #30個


print('------------------------------')  #30個


