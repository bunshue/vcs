import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

print('---- 字串處理專區 --------------------------------------------------------')	#60個

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


print('------------------------------------------------------------')	#60個


print('字典的用法')
plats = {
    'Linux': 'platform_linux_distribution',
    'Mac': 'platform_mac_ver',
    'Windows': 'platform_win32_ver',
}

print(type(plats))
print(plats)

for name, func in plats.items():
    plat = '%s %r' % (name, func)
    print(plat)

print('------------------------------------------------------------')	#60個



print('---- 列印專區 --------------------------------------------------------')	#60個


'''
word = word.strip()

    dbg('recursedown(%r)\n' % (dirname,))
##  dbg('fix(%r)\n' % (filename,))


'''
print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

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






print('---- python語言區 --------------------------------------------------------')	#60個



print(globals())

print('__file__ : 此檔案長檔名')
print(__file__)
print(__file__.upper()) #長檔名轉大寫
print(__file__.lower()) #長檔名轉小寫

print('__name__ : 目前所在模組名')
print(__name__)
#print(__name__._version)

print('sympy模組的版本')
import sympy
VERSION = sympy.__version__
print(VERSION)

print('selenium模組的版本')
import selenium
print(selenium.__version__)

#import somemodule as sm	#幫模組取個別名

print (sys.argv)
#print (s.argv)


print('---- 語法專區 --------------------------------------------------------')	#60個


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







print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個
x = 2
y = 0.5

print("x**y = " + str(x ** y))

print('------------------------------------------------------------')	#60個
print('list 使用')
lst = [3, 2, 1, 5, 9, 0]
print(type(lst))
print(lst)
sorted(lst)
print(lst)

print('------------------------------------------------------------')	#60個


print('---- datatime time random math --------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

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


print('------------------------------------------------------------')	#60個

from urllib import parse

string = '豬頭三'

string_url = parse.quote(string)
print('原字串:\t' + string)
print('轉網址:\t' + string_url)


'''
cnstr = '中文 test'
print(cnstr, len(cnstr))
#utfstr = unicode(cnstr, 'utf-8')
'''

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個


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


print('------------------------------------------------------------')	#60個


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
print('------------------------------------------------------------')	#60個


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

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('字元轉unicode')
string = '你'

print(ord(string))

#print(hex(ord(string)))

print('十進位 轉 十六進位')

# Convert a decimal to a hex as a string 
def decimalToHex(decimalValue):
    hex = ""
 
    while decimalValue != 0:
        hexValue = decimalValue % 16 
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
    
    return hex
  
# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

decimalValue = 170
hexValue = decimalToHex(decimalValue)
print('decimal : %d\thex : %s' % (decimalValue, hexValue) )

decimalValue = 65535
hexValue = decimalToHex(decimalValue)
print('decimal : %d\thex : %s' % (decimalValue, hexValue) )

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('list之使用')

llll = ['aa', 'bb', 'cc', 'dd', 'ee']
pppp = llll[2:] #第二項(含)以後的
print(llll)
print(pppp)

table1 = [] #list
table2 = {} #dict
print(type(table1))
print(type(table2))

print('------------------------------------------------------------')	#60個

a_dict = {}
print(type(a_dict))

a_list = []
print(type(a_list))


target_url = 'https://www.nkust.edu.tw/p/403-1000-12-{}.php'

for page in range(1, 6):
    html = target_url.format(page)
    print(html)


data = list()
for page in range(1, 6):
    pdate = 'aaaa'
    title = 'bbbb'
    link = 'cccc'
    data.append((pdate, link, title))
print(type(data))
print(data)


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

contents = list()

for page in range(1, 6):
    content = dict()
    content['link'] = 'aaaaa'
    content['content'] = 'bbbbb'
    content['date'] = 'ccccc'
    content['title'] = 'ddddd'
    contents.append(content)
    
print(contents)

print('------------------------------------------------------------')	#60個

if sys.version_info.major < 3 or sys.version_info.minor < 3:
    sys.exit("Error: clinic.py requires Python 3.3 or greater.")


print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個



print('格式化字串')

print(12345)

print('八位數 前面補0')
print('{:08d}\n{:08d}\n{:08d}'.format(123, 1234, 12345))




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('字串的 title 用法')
s = 'this is a lion mouse'

print(s.title())



print('------------------------------------------------------------')	#60個


import itertools
import threading
import subprocess
from optparse import OptionParser, SUPPRESS_HELP

def bark(duration):

    _time = time.time
    _sleep = time.sleep
    
    # We give the parent some time to be ready.
    _sleep(1.0)

    start_time = _time()
    end_time = start_time + duration * 2.0
    i = 0
    while _time() < end_time:
        print('b', end = ' ')
        i += 1


bark(0.2)


print('------------------------------------------------------------')	#60個



import sys
import time
import platform
CALIBRATION_LOOPS = 10
calibration_loops = range(CALIBRATION_LOOPS)

print(type(calibration_loops))
print(calibration_loops)


MILLI_SECONDS = 1e3
MICRO_SECONDS = 1e6
PERCENT = 100
LINE = 79
MIN_TEST_RUNTIME = 1e-3


name = 'david'
min_time = 11.11
avg_time = 22.22
op_avg = 33.33
min_overhead = 44.44
total_min_time = 55.55
total_avg_time = 66.66
other_min_time = 77.77
warp = 88.88
min_diff = 99.99
other_avg_time = 12.34
avg_diff =  23.45
overhead_times = 34.56
overhead_times = 45.67
eff_time = 56.78
abs_time = 67.89
min_overhead = 78.90

print('%30s:  %5.0fms  %5.0fms  %6.2fus  %7.3fms' % \
      (name,
       min_time * MILLI_SECONDS,
       avg_time * MILLI_SECONDS,
       op_avg * MICRO_SECONDS,
       min_overhead *MILLI_SECONDS))
print('-' * LINE)
print('Totals:                        '
      ' %6.0fms %6.0fms' %
      (total_min_time * MILLI_SECONDS,
       total_avg_time * MILLI_SECONDS,
       ))
print()

print('%30s: %5.0fms %5.0fms %7s %5.0fms %5.0fms %7s' % \
      (name,
       min_time * MILLI_SECONDS,
       other_min_time * MILLI_SECONDS * warp / warp,
       min_diff,
       avg_time * MILLI_SECONDS,
       other_avg_time * MILLI_SECONDS * warp / warp,
       avg_diff))

'''
print('%30s:  %6.3fms  %6.3fms' % \
      (name,
       min(overhead_times) * MILLI_SECONDS,
       max(overhead_times) * MILLI_SECONDS))
'''

print('    %5.0fms    %5.0fms %7.3fms' % \
      (eff_time * MILLI_SECONDS,
       abs_time * MILLI_SECONDS,
       min_overhead * MILLI_SECONDS))

i = 123
print(' Round %-25i  effective   absolute  overhead' % (i+1))

print('%30s:' % name, end=' ')


print('Calib. prep time     = %.6fms' % (
    total_min_time * MILLI_SECONDS))


# Name of the benchmark
name = '%04i-%02i-%02i %02i:%02i:%02i' % \
       (time.localtime(time.time())[:6])

print(name)


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print('測試hasattr功能')
print('內建函數 (function) hasattr() ，判斷參數 (parameter) name 是否為 object 的屬性名稱')

class Demo:
    def __init__(self, i):
        self.i = i
        self.x = "xxx"
        self.y = "yyy"
        self.z = "zzz"
     
    def __str__(self):
        return str(self.i)
          
    def hello(self):
        print("hello " + self.__str__())
 
d = Demo(22)

print(hasattr(d, "t"))  #不是
print(hasattr(d, "u"))  #不是
print(hasattr(d, "v"))  #不是
print(hasattr(d, "w"))  #不是
print(hasattr(d, "x"))  #是
print(hasattr(d, "y"))  #是
print(hasattr(d, "z"))  #是


print('------------------------------------------------------------')	#60個


print('建一個測試list')

class User:
    user_id: int
    first_name: str
    last_name: str

USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(2_0)]

print(type(USERS))
print(USERS)


def show_price(price: float) -> str:
    return "$ {0:,.2f}".format(price)


print(show_price(1000))
#    '$ 1,000.00'

print(show_price(1_250.75))
#    '$ 1,250.75'



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

a = 28
b = 49
c = gcd(a, b)
print(c)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



from random import randint, random, getrandbits

def getrandbytes(size):
    return getrandbits(8 * size).to_bytes(size, 'little')


ccc = b'111' + getrandbytes(100)

print(type(ccc))
print(ccc)

datacount = randint(16, 64) * 1024 + randint(1, 1024)

ddd = random() * randint(-1000, 1000)
print(ddd)



    
    

print('------------------------------------------------------------')	#60個


import sys
bytes = sys.maxsize  # smallest total size so far
print(bytes)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


for name in ('__repr__', '__str__', '__format__', '__reduce_ex__'):
    print(name)


for x in (15, 25, 35, 45, 55):
    print(x)



'''    
_b85alphabet = (b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                b"abcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")


_b85chars = [bytes((i,)) for i in _b85alphabet]
print(_b85chars)
print()

_b85chars2 = [(a + b) for a in _b85chars for b in _b85chars]

print(_b85chars2)

'''

print('------------------------------------------------------------')	#60個








from itertools import islice as _islice, count as _count

# Helper to generate new thread names
_counter = _count().__next__
_counter() # Consume 0 so first non-main thread has id 1.
def _newname(template="Thread-%d"):
    return template % _counter()

print(_newname())
print(_newname())
print(_newname())
print(_newname())
print(_newname())
print(_newname())

print('------------------------------------------------------------')	#60個



print('字串轉拜列')
string = 'lion'
data = repr(string).encode('utf-8') + b'\0'
print(type(data))
print(data)

        
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


import importlib
import platform
import sys
from types import ModuleType
from typing import Optional, Tuple, List, cast



def print_table(version_rows: List[Tuple[str, str]]) -> None:
    row_format = "{:12} | {}"
    print(row_format.format("module", "version"))
    print(row_format.format("------", "-------"))
    for module, version in version_rows:
        # Some version strings have multiple lines and need to be squashed
        print(row_format.format(module, version.replace("\n", " ")))


def extract_version(module: ModuleType) -> Optional[str]:
    if module.__name__ == "gdcm":
        return cast(Optional[str], getattr(module, "GDCM_VERSION", None))

    return cast(Optional[str], getattr(module, "__version__", None))




version_rows = [("platform", platform.platform()), ("Python", sys.version)]
print(version_rows)

modules = (
    "os", "sys", "cv2", "numpy", "PIL", "pylibjpeg",
    "openjpeg", "libjpeg",
)

for module in modules:
    try:
        m = importlib.import_module(module)
    except ImportError:
        version = "_module not found_"
    else:
        version = extract_version(m) or "**cannot determine version**"

    version_rows.append((module, version))

print('print_table')
print_table(version_rows)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

_size_factors = {
    "kb": 1000, "mb": 1000 * 1000, "gb": 1000 * 1000 * 1000,
    "kib": 1024, "mib": 1024 * 1024, "gib": 1024 * 1024 * 1024,
}

for aaa in _size_factors:
    print(aaa, _size_factors[aaa])


print('------------------------------------------------------------')	#60個


_deprecations = {
    "JPEGBaseline": "JPEGBaseline8Bit",
    "JPEGExtended": "JPEGExtended12Bit",
    "JPEGLossless": "JPEGLosslessSV1",
    "JPEGLSLossy": "JPEGLSNearLossless",
    "JPEG2000MultiComponentLossless": "JPEG2000MCLossless",
    "JPEG2000MultiComponent": "JPEG2000MC",
}

for name in _deprecations:
    print(name)

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


import os
from os.path import abspath

def _basename(path):
    # A basename() variant which first strips the trailing slash, if present.
    # Thus we always get the last component of the path, even for directories.
    sep = os.path.sep + (os.path.altsep or '')
    return os.path.basename(path.rstrip(sep))



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
base_name = _basename(filename)
print(base_name)



src = abspath(base_name)
print(src)


zip_filename = base_name + ".zip"

print(zip_filename)


print('------------------------------------------------------------')	#60個

foldername = 'C:/_git/vcs/_1.data/______test_files5'

normdir = os.path.normcase(foldername)
print(normdir)


print('------------------------------------------------------------')	#60個

import collections

import nt
_ntuple_diskusage = collections.namedtuple('usage', 'total used free')

def disk_usage(path):
    total, free = nt._getdiskusage(path)
    used = total - free
    return _ntuple_diskusage(total, used, free)


foldername = 'C:/_git/vcs/_1.data/______test_files5'
ret = disk_usage(foldername)
print(ret)

print('------------------------------------------------------------')	#60個

import re

ispythonprog = re.compile('^[a-zA-Z0-9_]+\.py$')
def ispython(name):
    return bool(ispythonprog.match(name))


short_filename = 'picture1.jpg'
status = ispython(short_filename)
print(status)

short_filename = 'test10_new02.py'
status = ispython(short_filename)
print(status)






print('------------------------------------------------------------')	#60個



import os
import sys
import time

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('尋找python程式碼的所在地')

module_name = 'pytube'
code_place = os.path.dirname(__import__(module_name).__file__)
print(code_place)


print('取得相對路徑')
foldername = 'C:/_git/vcs/_1.data/______test_files1/'
fn = os.path.relpath(foldername, code_place)

print(fn)

print('------------------------------------------------------------')	#60個

def test():
    for x in 'abcde':
        for y in '12345':
            print(y, x, end = ' ')

test()
print('------------------------------------------------------------')	#60個


ENDMARKER = 0
NAME = 1
NUMBER = 2
STRING = 3
NEWLINE = 4
INDENT = 5
DEDENT = 6
LPAR = 7
RPAR = 8
LSQB = 9
RSQB = 10
PERCENT = 24
LBRACE = 25
RBRACE = 26
EQEQUAL = 27
N_TOKENS = 54
NT_OFFSET = 256

tok_name = {value: name
            for name, value in globals().items()
            if isinstance(value, int) and not name.startswith('_')}

print(type(tok_name))
print(tok_name)


print('------------------------------------------------------------')	#60個


import os
print(os.name)
print(os.name)
print(os.name)

if os.name == 'nt':
    print('kkk')
    import nt
    if sys.getwindowsversion()[:2] >= (6, 0):
        print('aaa')
    else:
        print('bbb')



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

rad = np.arctan2(3, 4)  # 求角度（radian）
th = np.degrees(rad)    # 轉成度數

import math
rad = math.atan2(3, 2)  # 計算角度（radian）
th = math.degrees(rad)  # 轉成度數
th

import math
10 * math.cos(math.radians(60)) 



# 計算角度
rad = math.acos(3/5)
deg = math.degrees(rad)
print(deg)

print('------------------------------------------------------------')	#60個


### 列表3-8　繪製半徑300的圓（y >= 0）

import matplotlib.pyplot as plt
import numpy as np

# 圓的方程式
r = 300  # 半徑
x = np.arange(-r, r+1)    # x: -300～300
y = np.sqrt(r**2 - x**2)  # y

# 繪圖
plt.plot(x, y)
plt.axis('equal') 
plt.grid(color='0.8')
plt.show()


print('------------------------------------------------------------')	#60個




dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
days, hours = divmod(total_hours, 24)   # 商和餘數
print("總供需要天數")
print(days)
print("小時數")
print(hours)


print('------------------------------------------------------------')	#60個

x1 = 97
x2 = chr(x1)      
print(x2)             # 輸出數值97的字元
x3 = ord(x2)
print(x3)             # 輸出字元x3的Unicode碼值
x4 = '魁'
print(ord(x4))        # 輸出字元'魁'的Unicode碼值

print('------------------------------------------------------------')	#60個

print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

x = 100
print("x=/%-6d/" % x)
y = 10.5
print("y=/%-6.2f/" % y)
s = "Deep"
print("s=/%-6s/" % s)

x = 100
print("x=/%6d/" % x)
y = 10.5
print("y=/%6.2f/" % y)
s = "Deep"
print("s=/%6s/" % s)
print("以下是保留格數空間不足的實例")
print("x=/%2d/" % x)
print("y=/%3.2f/" % y)
print("s=/%2s/" % s)


title = "南極旅遊講座"
print("/{0:*^20s}/".format(title))


print('------------------------------------------------------------')	#60個


import math

r = 6371                        # 地球半徑
x1, y1 = 22.2838, 114.1731      # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168      # 台北車站經緯度

d = 6371*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                   math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                   math.cos(math.radians(y1-y2)))

print("distance = ", d)


print('------------------------------------------------------------')	#60個

#貸款試算
loan = 10000 #貸款金額
year = 1 #年限
rate = 10 #年利率%
month_rate = rate / (12*100)             # 改成百分比以及月利率

# 計算每月還款金額
molecules = loan * month_rate
denominator = 1 - (1 / (1 + month_rate) ** (year * 12))
monthly_pay = molecules / denominator    # 每月還款金額
total_pay = monthly_pay * year * 12      # 總共還款金額

print("每月還款金額 %d" % int(monthly_pay))
print("總共還款金額 %d" % int(total_pay))



print('------------------------------------------------------------')	#60個

numberStr = input("請輸入數值公式 : ")
number = eval(numberStr)
print("計算結果 : %5.2f" % number)






print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個



















