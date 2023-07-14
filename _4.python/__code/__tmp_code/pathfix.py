import sys
import re
import os
from stat import *
import getopt

def recursedown(dirname):
    try:
        names = os.listdir(dirname)
    except OSError as msg:
        err('%s: cannot list directory: %r\n' % (dirname, msg))
        return 1
    names.sort()
    subdirs = []
    for name in names:
        if name in (os.curdir, os.pardir):
            continue
        fullname = os.path.join(dirname, name)
        if os.path.islink(fullname):
            pass
        elif os.path.isdir(fullname):
            subdirs.append(fullname)
        else:
            print('a')
    bad = 0
    for fullname in subdirs:
        if recursedown(fullname):
            bad = 1
    return bad

foldername = 'C:/_git/vcs/_1.data/______test_files1/_opencv'

recursedown(foldername)



    
