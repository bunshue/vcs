import os
import os, sys, stat, getopt

'''
import pydoc
if __name__ == '__main__':
    pydoc.cli()
'''

def mtime(f):
    st = os.fstat(f.fileno())
    return st[stat.ST_MTIME]


filename1 = 'D:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'D:/_git/vcs/_1.data/______test_files1/picture2.jpg'

try:
    sf = open(filename1, 'rb')
except IOError:
    sf = None
try:
    mf = open(filename2, 'r')
except IOError:
    mf = None


sft = mtime(sf)
mft = mtime(mf)
if mft > sft:
    # Master is newer -- copy master to slave
    sf.close()
    mf.close()
    print('1111111')
else:
    print('22222')

print('比較兩檔是否相同')

BUFSIZE = 16*1024

def identical(sf, mf):
    while 1:
        sd = sf.read(BUFSIZE)
        md = mf.read(BUFSIZE)
        if sd != md: return 0
        if not sd: break
    return 1

filename1 = 'D:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename2 = 'D:/_git/vcs/_1.data/______test_files1/poetry2.txt'

try:
    sf = open(filename1, 'r')
except IOError:
    sf = None
try:
    mf = open(filename1, 'r')
except IOError:
    mf = None


if sf and mf:
    if identical(sf, mf):
        print('兩檔相同')
    else:
        print('兩檔不同')
        


