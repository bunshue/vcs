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


filename1 = 'C:/_git/vcs/_1.data/______test_files1/human1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/human2.jpg'

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

filename1 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

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
        

err = sys.stderr.write
dbg = err
rep = sys.stdout.write

err('AAAAA')
dbg('BBBBB')
rep('CCCCC')

#err(str(msg) + '\n')

err('-i option or file-or-directory missing\n')

'''
import webbrowser
print('用預設的瀏覽器開啟網頁')
url = 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5'
print(url)
webbrowser.open(url)
'''
