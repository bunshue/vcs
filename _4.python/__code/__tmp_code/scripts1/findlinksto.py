#! /usr/bin/env python3

# findlinksto
#
# find symbolic links to a path matching a regular expression

import os
import sys
import re
import getopt

def visit(prog, dirname, names):
    print('a')
    if os.path.islink(dirname):
        print('link')
        names[:] = []
        return
    if os.path.ismount(dirname):
        print('descend into', dirname)
    for name in names:
        name = os.path.join(dirname, name)
        print(name)
        try:
            linkto = os.readlink(name)
            if prog.search(linkto) is not None:
                print(name, '->', linkto)
        except OSError:
            pass

pattern = 'pic'
foldername = 'C:/_git/vcs/_1.data/______test_files1/'

prog = re.compile(pattern)
for dirname in foldername:
    os.walk(dirname, visit, prog)



