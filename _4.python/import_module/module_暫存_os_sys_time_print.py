import sys


print('---- os ------------------------------------------------------------------')	#70個

import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(base_dir)

import os
user = os.getlogin()
print(user)

font_file = os.path.join(os.path.dirname(__file__), "OpenFlame.ttf")
print(font_file)

import os

print(os.listdir())
print(os.listdir('/'))

import sys, os

def lll(dirname):
    for name in os.listdir(dirname):
        print(name)
        if name not in (os.curdir, os.pardir):
            print(name)
            full = os.path.join(dirname, name)
            if os.path.islink(full):    #尋找link
                print('link')
                print(name, '->', os.readlink(full))
            else:
                print('f')
        else:
            print('x')

foldername = 'C:/_git/vcs/_1.data/______test_files1/_opencv'

#lll(foldername)


print('---- sys ------------------------------------------------------------------')	#70個


print('---- time ------------------------------------------------------------------')	#70個


print('---- print ------------------------------------------------------------------')	#70個

import sys
import os

join = os.path.join

error = 'mkreal error'

BUFSIZE = 32*1024

sys.stdout = sys.stderr
progname = os.path.basename(sys.argv[0])

print(progname)



print('---- 新進暫存 ------------------------------------------------------------------')	#70個




