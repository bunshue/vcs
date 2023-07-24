
"""A ScrolledText widget feels like a text widget but also has a
vertical scroll bar on its right.  (Later, options may be added to
add a horizontal bar as well, to make the bars disappear
automatically when not needed, to move them to the other side of the
window, etc.)

Configuration options are passed to the Text widget.
A Frame widget is inserted between the master and the text, to hold
the Scrollbar widget.
Most methods calls are inherited from the Text widget; Pack, Grid and
Place methods are redirected to the Frame widget however.
"""

import sys


print('字串處理專區------------------------------')  #30個



target = 'https://tw.appledaily.com/new/realtime/{}'

for page in range(1, 11):
    url = target.format(page)
    print(url)

'''
filename = 'C:/_git/vcs/_1.data/______test_files2/news_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.json';
with open(filename, "w", encoding = 'utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)
'''



query_string = 'abcdefghijklmn'
query_number = 12345678901234
replace_parameter = "無f替換變數"
replace_parameter += " WHERE {query_string}"
replace_parameter += " ORDER BY record_no DESC LIMIT {query_number}"
print(replace_parameter)


replace_parameter = "有f替換變數"
replace_parameter += f" WHERE {query_string}"
replace_parameter += f" ORDER BY record_no DESC LIMIT {query_number}"
print(replace_parameter)


table_columns = '(alpaca_name, training, duration, date)'
postgres_insert_query = f"""INSERT INTO alpaca_training {table_columns} VALUES (%s,%s,%s,%s)"""

print(postgres_insert_query)



print('------------------------------')  #30個




print('------------------------------')  #30個



print('------------------------------')  #30個



print('------------------------------')  #30個






print('列印專區------------------------------')  #30個


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'


err = sys.stderr.write
dbg = err
rep = sys.stdout.write

msg = 'cccccc'
usage = 'dddddddddddd'
err(str(msg) + '\n')
err(msg)
err('-i option or file-or-directory missing\n')
err(usage)
err('%s: cannot open: %r\n' % (filename, msg))


'''
word = word.strip()


        if os.path.isdir(arg):
            if recursedown(arg): bad = 1
        elif os.path.islink(arg):
            err(arg + ': will not process symbolic links\n')
            bad = 1
        else:
            if fix(arg): bad = 1

    dbg('recursedown(%r)\n' % (dirname,))
##  dbg('fix(%r)\n' % (filename,))


'''
print('------------------------------')  #30個



import sys
def errprint(*args):
    sep = ""
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = " "
    sys.stderr.write("\n")


msg = 'this is a lion-mouse'
errprint(msg)
print(msg)




print('------------------------------')  #30個



def output(string = '', end = '\n'):
    sys.stdout.write(string + end)


def output(*strings):
    for s in strings:
        sys.stdout.write(str(s) + "\n")


pos = 'abcd'
output("Lexical error at position %s" % pos)



print('------------------------------')  #30個




def fail(msg):
    out = sys.stderr.write
    out(msg + "\n\n")
    return 0

filename = 'ccccc'
fail("couldn't open " + filename)





print('------------------------------')  #30個




arg = 'abcdefg'
sys.stderr.write("Can't find %s\n" % arg)


print('------------------------------')  #30個




print('------------------------------')  #30個

import sys

usage = """Usage: %s [-cd] paths...
    -c: recognize Python source files trying to compile them
    -d: debug output""" % sys.argv[0]

print('msgsssssss', file = sys.stderr)
print(usage, file = sys.stderr)


print('------------------------------')  #30個

total = 7
for i in range(0, (total+1)):
    #print(i)	# 0 ~ 7
    print(u"download: " + str(100 * i / total ) + " %.")

#替代字串
TABLE_NAME = 'people'
SELECT = 'select * from %s order by age, name' % TABLE_NAME

print('select * from %s order by age, name' % TABLE_NAME)
print(SELECT)

key_id = 1234
SELECT = 'SELECT * FROM memos WHERE key=?', (str(key_id))
print(SELECT)






print('------------------------------')  #30個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/aaaaa.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/bbbbb.jpg'

print("Copied %s to %s" % (filename1, filename2))



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print(filename)

print('file: %s' % filename)
print('file: %r' % filename)







print('python語言區------------------------------')  #30個





print(__doc__)
print(globals())


print(__file__)
print(__file__.upper())
print(__file__.lower())
print(__name__)
print(__name__)
#print(__name__._version)
print(__doc__)
print(__doc__)  # the docstring of this module above

import sympy
VERSION = sympy.__version__
print(VERSION)

import selenium
print(selenium.__version__)





import sys
#import somemodule as sm	#幫模組取個別名

print (sys.argv)
#print (s.argv)


print('檔頭的註解')
print(__doc__)





print('語法專區------------------------------')  #30個




print('for-test')
for i in range(4, -1, -1):
    print(i)

for i in range(0, 6):
    print(i)




#產生連續的整數
for num in range(10):
    print(num)

for num in range(2, 7):
    print(num)





 

print('全圖640X480, 每160X160裁一塊出來')
W = 640
H = 480
w = 160
h = 160

'''
for(y = 0; y < H; y += h)
  for(x = 0; x < W; x += w)
'''
for y in range(0, H, h):
    for x in range(0, W, w):
        box = x, y, min(W, x + w), min(H, y + h)
        print(box)
        #tile = ImageTk.PhotoImage(image.crop(box))
        #canvas.create_image(x, y, image = tile, anchor = NW)
        #print(x, y)
        #print(box)







print('------------------------------')  #30個

print('字串處理')

items = "03/11/2006".split("/")
print(items)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

name = filename.split('/')
print(len(name))
print(name)
print(type(name))

ccc = name.reverse()
print(ccc)

print('------------------------------')  #30個
x = 2
y = 0.5

print("x**y = " + str(x ** y))

print('------------------------------')  #30個
print('list 使用')
lst = [3, 2, 1, 5, 9, 0]
print(type(lst))
print(lst)
sorted(lst)
print(lst)

print('------------------------------')  #30個





print('datatime time random math------------------------------')  #30個

import datetime
seconds = datetime.datetime(2004, 10, 26, 10, 33, 33, tzinfo = datetime.timezone(datetime.timedelta(0))).timestamp()
print(seconds)


import time
print('存檔紀念')

fp = open('Build.txt', 'w')
fp.write("# BUILD INFO\n")
fp.write("# Date: %s\n" % time.ctime())
#fp.write("# By: %s\n" % pwd.getpwuid(os.getuid()).pw_gecos)
fp.close()




print('------------------------------')  #30個





import random
s = ''
for i in range(0, 10):
    s += random.choice('<>=^')
    s += random.choice('+- ')
    s += str(random.randrange(1, 100))
    s += str(random.randrange(100))
    s += random.choice(('', 'E', 'e', 'G', 'g', 'F', 'f', '%'))

print(s)

print('------------------------------')  #30個

import time

randseed = int(time.time())
random.seed(randseed)

print('------------------------------')  #30個

import sys, os, time, difflib, argparse
from datetime import datetime, timezone

path = 'C:/_git/vcs/_4.python'
t1 = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
print(t1)

t2 = t1.astimezone().isoformat()
print(t2)

print('------------------------------')  #30個

i = 30
import math
math.sin(math.pi * i / 2)


print('------------------------------')  #30個



print('os.system------------------------------')  #30個


print('製作cmd指令')

cmd = 'dir'
if os.system(cmd) != 0:
    raise RuntimeError(cmd)


print('------------------------------')  #30個

def msg(str):
    sys.stderr.write(str + '\n')

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


print('------------------------------')  #30個


os.system('cmd')



print('------------------------------')  #30個



print('處理網址資料')

url = "https://www.nkust.edu.tw/p/403-1000-12-{}.php?Lang=zh-tw"
for pg in range(1, 11):
    print(url.format(pg))


url = "https://tw.stock.yahoo.com/news_list/url/d/e/N{}.html?q=&pg={}"
for cate in [1, 4]:
    for pg in range(1, 6):
        print(url.format(cate, pg))



def hexToDecimal(hex):
    decimalValue = 0
    for i in range(len(hex)):
        ch = hex[i]
        if 'A' <= ch <= 'F' or '0' <= ch <= '9':
            decimalValue = decimalValue * 16 + \
                hexCharToDecimal(ch)
        else:
            return None

    return decimalValue

def hexCharToDecimal(ch):
    if 'A' <= ch <= 'F':
        return 10 + ord(ch) - ord('A')
    else:
        return ord(ch) - ord('0')

hex = 'aa'
decimal = hexToDecimal(hex.upper())

if decimal == None:
    print("Incorrect hex number")
else:
    print("The decimal value for hex number", hex, "is", decimal) 


print('------------------------------')  #30個

from urllib import parse

string = '豬頭三'

string_url = parse.quote(string)
print('原字串:\t' + string)
print('轉網址:\t' + string_url)


'''
#傑卡德相似係數 Jaccard Similarity Coefficient

from numpy import *
import scipy.spatial.distance as dist

mat1 = [1,1,0,1,0,1,0,0,1]
mat2 = [0,1,1,0,0,0,1,1,1]
mat3 = [1,1,0,1,0,1,0,0,1]  #the same as mat1
mat4 = [0,0,1,0,1,0,1,1,0]  #invert of mat1

matV = mat([mat1,mat4])

print('dist.jaccard : ')
print(dist.pdist(matV, 'jaccard'))

'''

'''
cnstr = '中文 test'
print(cnstr, len(cnstr))
#utfstr = unicode(cnstr, 'utf-8')
'''
'''
import win32api, win32con
rc = win32api.MessageBox(0, 'kkkkk', "Installation Error", win32con.MB_ABORTRETRYIGNORE)
if rc == win32con.IDABORT:
    print('1111')
elif rc == win32con.IDIGNORE:
    print('2222')
else:
    print('3333')
'''

print('------------------------------')  #30個

print('兩點距離')
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print('兩點距離 : ', distance) 


print('if and or')
year = 2024
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(year, "is a leap year?", isLeapYear)

print('if and or')
number = 126

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by 2 and 3")

if number % 2 == 0 or number % 3 == 0:
    print(number, "is divisible by 2 or 3")

if (number % 2 == 0 or number % 3 == 0) and \
       not (number % 2 == 0 and number % 3 == 0):
    print(number, "divisible by 2 or 3, but not both")


print('if and or')
lottery = 35
guess = 35

# Get digits from lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

# Get digits from guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 
        or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")


#test strip
#filename = input("Enter a filename: ").strip()

print('測試 strip()')
input_string = 'ABCDEFG       '
print('無strip <<<' + input_string + '>>>')
input_string = input_string.strip()
print('有strip <<<' + input_string + '>>>')

def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)

printArea() # Default arguments width = 1 and height = 2
printArea(4, 2.5) # Positional arguments width = 4 and height = 2.5
printArea(height = 5, width = 3) # Keyword arguments width 
printArea(width = 1.2) # Default height = 2
printArea(height = 6.2) # Default widht = 1

print('------------------------------')  #30個


a = 5
b = "Hello"
c = 0.15
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

a = "Why not to learn "
b = "Python?"

print(len(a))
print(a[2])
print(a[4 : 7])
print(a.replace("learn", "teach"))
print(a.split(" "))
print(a + b)


string = '測試字串是不是有被包含'
ss = '要'
if ss in string:
    print('有被包含')
else:
    print('沒有被包含')

ss = '包含'
if ss in string:
    print('有被包含')
else:
    print('沒有被包含')



#檢查有無包含中文
def is_contains_chinese():
  print('is_contains_chinese')
  global search_word
  for _char in search_word:
    if '\u4e00' <= _char <= '\u9fa5':
      print('True')
      return True
  print('False')
  return False
  

search_word = 'oat'
is_contains_chinese()
search_word = '英國'
is_contains_chinese()


print('------------------------------')  #30個


'''
print('一種寫入檔案的方法')
filename = 'tmp.txt'

fp = open(filename,'w')
print('[OPTIONS]', file=fp)
print('Auto Index=Yes', file=fp)
print('Binary TOC=No', file=fp)
print('Binary Index=Yes', file=fp)
print('Compatibility=1.1', file=fp)
print('Error log file=ErrorLog.log', file=fp)
print('Display compile progress=Yes', file=fp)
print('Full-text search=Yes', file=fp)
print('Default window=main', file=fp)
print('', file=fp)  #寫一個空白列
print('[WINDOWS]', file=fp)
print('main=,"' + '","'
+ '","","",,,,,0x23520,222,0x1046,[10,10,780,560],'
'0xB0000,,,,,,0', file=fp)
print('', file=fp)
print('[FILES]', file=fp)
print('', file=fp)
fp.close()
'''
print('------------------------------')  #30個


import os
import sys

print(sys.maxsize)
print(2 ** 32)

import os
import stat

print(os.name)
print(os.sep)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

foldername = os.path.dirname(filename)
print(filename)
print(foldername)

if os.path.exists(filename):
    print('True')
else:
    print('False')

if os.path.isdir(filename):
    print('True')
else:
    print('False')

print('------------------------------')  #30個

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

print('------------------------------')  #30個

import os
import sys
from stat import *

print('顯示目前 PATH')
print(sys.path)
print(sys.path[0])

pathlist = os.environ['PATH'].split(os.pathsep)
print(pathlist)

#filename = os.path.join(dir, prog)
print('------------------------------')  #30個


print('------------------------------')  #30個




print('------------------------------')  #30個




print('------------------------------')  #30個









