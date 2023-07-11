
#替代字串
TABLE_NAME = 'people'
SELECT = 'select * from %s order by age, name' % TABLE_NAME


print('select * from %s order by age, name' % TABLE_NAME)
print(SELECT)





key_id = 1234
SELECT = 'SELECT * FROM memos WHERE key=?', (str(key_id))
print(SELECT)



print('----------------------------------------------------------------------')	#70個

print('-' * 70)	#70個

from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

class Ball:
    def __init__(self):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2 # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

ballList = [] # Create a list for balls

length = len(ballList)
print('length = ', length)

for i in range(6):
    ballList.append(Ball())

length = len(ballList)
print('length = ', length)

for i in range(length):
    print('第', i, '個 : ', ballList[i].color)

'''
for ball in ballList:
    print(ball.color)
'''

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

import os
import sys
from stat import *

print('顯示目前 PATH')
print(sys.path)
print(sys.path[0])

pathlist = os.environ['PATH'].split(os.pathsep)
print(pathlist)

#filename = os.path.join(dir, prog)

def msg(str):
    sys.stderr.write(str + '\n')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

try:
    st = os.stat(filename)
except OSError:
    print('error')
if not S_ISREG(st[ST_MODE]):
    msg(filename + ': not a disk file')
else:
    mode = S_IMODE(st[ST_MODE])
    if mode & 0o111:
        if not ident:
            print(filename)
            ident = st[:3]
        else:
            if st[:3] == ident:
                s = 'same as: '
            else:
                s = 'also: '
            msg(s + filename)
    else:
        msg(filename + ': not executable')

longlist = '-l'
filename = 'test01_io.py'

sts = os.system('ls ' + longlist + ' ' + filename)

if sts:
    msg('"ls -l" exit status: ' + repr(sts))


sts = os.system('ls ' + filename)

if sts:
    msg('"ls -l" exit status: ' + repr(sts))

sts = os.system('dir')

if sts:
    msg('"ls -l" exit status: ' + repr(sts))
else:
    print(sts)


foldername = '__code'
names = os.listdir(foldername)
for name in names:
    print(name)

arg = 'abcdefg'
sys.stderr.write("Can't find %s\n" % arg)

stats = {}

def addstats(ext, key, n):
    d = stats.setdefault(ext, {})
    d[key] = d.get(key, 0) + n

def statdir(dir):
    try:
        names = os.listdir(dir)
    except OSError as err:
        sys.stderr.write("Can't list %s: %s\n" % (dir, err))
        return
    for name in sorted(names):
        if name.startswith(".#"):
            continue  # Skip CVS temp files
        if name.endswith("~"):
            continue  # Skip Emacs backup files
        full = os.path.join(dir, name)
        if os.path.islink(full):
            addstats("<lnk>", "links", 1)
        elif os.path.isdir(full):
            statdir(full)
        else:
            statfile(full)

def statfile(filename):
    head, ext = os.path.splitext(filename)
    head, base = os.path.split(filename)
    if ext == base:
        ext = ""  # E.g. .cvsignore is deemed not to have an extension
    ext = os.path.normcase(ext)
    if not ext:
        ext = "<none>"
    addstats(ext, "files", 1)
    try:
        with open(filename, "rb") as f:
            data = f.read()
    except IOError as err:
        sys.stderr.write("Can't open %s: %s\n" % (filename, err))
        addstats(ext, "unopenable", 1)
        return
    addstats(ext, "bytes", len(data))
    if b'\0' in data:
        addstats(ext, "binary", 1)
        return
    if not data:
        addstats(ext, "empty", 1)
    # addstats(ext, "chars", len(data))
    lines = str(data, "latin-1").splitlines()
    addstats(ext, "lines", len(lines))
    del lines
    words = data.split()
    addstats(ext, "words", len(words))

def report():
    exts = sorted(stats)
    # Get the column keys
    columns = {}
    for ext in exts:
        columns.update(stats[ext])
    cols = sorted(columns)
    colwidth = {}
    colwidth["ext"] = max([len(ext) for ext in exts])
    minwidth = 6
    stats["TOTAL"] = {}
    for col in cols:
        total = 0
        cw = max(minwidth, len(col))
        for ext in exts:
            value = stats[ext].get(col)
            if value is None:
                w = 0
            else:
                w = len("%d" % value)
                total += value
            cw = max(cw, w)
        cw = max(cw, len(str(total)))
        colwidth[col] = cw
        stats["TOTAL"][col] = total
    exts.append("TOTAL")
    for ext in exts:
        stats[ext]["ext"] = ext
    cols.insert(0, "ext")

    def printheader():
        for col in cols:
            print("%*s" % (colwidth[col], col), end=' ')
        print()

    printheader()
    for ext in exts:
        for col in cols:
            value = stats[ext].get(col, "")
            print("%*s" % (colwidth[col], value), end=' ')
        print()
    printheader()  # Another header at the bottom


"""Show file statistics by extension."""

#filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/'

if os.path.isdir(filename):
    print('目錄')
    statdir(filename)
elif os.path.isfile(filename):
    statfile(filename)
    print('檔案')
elif os.path.islink(filename):
    print('連結')
    linkto = os.readlink(filename)
    print(linkto)
else:
    print('不詳')    

print(type(stats))
print(stats)

report()

