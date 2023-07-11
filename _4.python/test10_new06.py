import sys
import os
from stat import *

join = os.path.join

error = 'mkreal error'

BUFSIZE = 32*1024

def test_file(name):
    st = os.stat(name) # Get the mode
    mode = S_IMODE(st[ST_MODE])
    print(st)
    print(mode)

    files = os.listdir(name)
    
    for filename in files:
        print(filename)

sys.stdout = sys.stderr
progname = os.path.basename(sys.argv[0])

print(progname)

#name = 'cccc.dat'
name = 'dddd.pdf'
name = 'C:/_git/vcs/_4.python/__code/__tmp_code/scripts1/'

test_file(name)
