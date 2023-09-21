import os
import sys
import time
import random
import numpy as np

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


print('------------------------------------------------------------')	#60個


print('字元轉unicode')
string = '你'

print(ord(string))

#print(hex(ord(string)))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


target_url = 'https://www.nkust.edu.tw/p/403-1000-12-{}.php'

for page in range(1, 6):
    html = target_url.format(page)
    print(html)

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

import sys
bytes = sys.maxsize  # smallest total size so far
print(bytes)

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

'''
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
'''

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

foldername = 'C:/_git/vcs/_1.data/______test_files2'

normdir = os.path.normcase(foldername)
print(normdir)


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

#degrees(x) 將x由弧度轉角度
#radians(x) 將x由角度轉弧度



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

from datetime import date, timedelta

d0 = date(1993, 12, 15)
d1 = date(2020, 12, 15)

delta = timedelta(days=1)

print(d0 + delta)

delta = timedelta(days=10000)

print(d0 + delta)

print(d1-d0)

d0 = date(2021, 5, 24)
d1 = date(2023, 8, 21)

print(d1-d0)

print('------------------------------------------------------------')	#60個

import sys
import time
import random

_FMT = '[Non-text (%(type)s) part of message omitted, filename %(filename)s]'
print(_FMT)

_width = len(repr(sys.maxsize-1))
_fmt = '%%0%dd' % _width

print(_width)
print(_fmt)

token = random.randrange(sys.maxsize)
print(token)
boundary = ('=' * 15) + (_fmt % token) + '=='
print(boundary)

print('------------------------------------------------------------')	#60個

import time
import datetime

def _format_time(hh, mm, ss, us):
    # Skip trailing microseconds when us==0.
    result = "%02d:%02d:%02d" % (hh, mm, ss)
    if us:
        result += ".%06d" % us
    return result

year = 2023
month = 8
day = 11
sep = 'W'
hour = 12
minute = 34
second = 56
microsecond = 123456
s = _format_time(hour, minute, second, microsecond)
print(s)


s = ("%04d-%02d-%02d%c" % (year, month, day, sep) +
     _format_time(hour, minute, second,microsecond))
print(s)


hh = 12
mm = 34
ss = 56
s = "%d:%02d:%02d" % (hh, mm, ss)
print(s)


print('------------------------------------------------------------')	#60個


import platform
print(platform.win32_ver())
print(platform.platform())



print('------------------------------------------------------------')	#60個


msg = '''
翠蓋龍旗出建章,鶯啼百囀柳初黃,
昆池冰泮三山近,阿閣花深九陌香,
徑轉虹梁通紫極,庭含玉樹隱霓裳,
侍臣緩步隨鑾輅,岡上應看集鳳皇,
小苑平臨太液池,金舖約戶鎖蟠螭,
雲中帝座飛華蓋,城上鈞陳繞翠旗,
紫氣旋面雙鳳閣,青松還有萬年枝,
從來清蹕深嚴地,開盡碧桃人未知
'''

print(f"<鳳>出現的次數 : {msg.count('鳳')}")

msg = msg.replace('Linda','Lxx')
print(f"新的msg內容 : {msg}")



print('------------------------------------------------------------')	#60個

x = [[a, b, c] for a in range(1,20) for b in range(a,20) for c in range(b,20)
     if a ** 2 + b ** 2 == c **2]
print(x)


print('------------------------------------------------------------')	#60個


for x in range(0x2160, 0x216a):
  print(chr(x),end=' ')

print()
  
print('------------------------------------------------------------')	#60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)     # 執行zip
print(type(zipData))            # 列印zip資料類型
player = list(zipData)          # 將zip資料轉成串列
print(player)

print('------------------------------------------------------------')	#60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30']
zipData = zip(fields, info)   # 執行zip
print(type(zipData))          # 列印zip資料類型
player = list(zipData)        # 將zip資料轉成串列
print(player)                 # 列印串列

print('------------------------------------------------------------')	#60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)     # 執行zip
print(type(zipData))            # 列印zip資料類型
player = list(zipData)          # 將zip資料轉成串列
print(player)                   # 列印串列

f, i = zip(*player)             # 執行unzip
print("fields = ", f)
print("info   = ", i)


print('------------------------------------------------------------')	#60個


import random
random.seed(5)  #固定亂數種子
for i in range(5):
    print(random.random())
    


print('------------------------------------------------------------')	#60個

import random                       # 導入模組random

for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))

print('------------------------------------------------------------')	#60個

import random                   # 導入模組random

for i in range(10):
    print(random.choice([1,2,3,4,5,6]), end=",")

print('------------------------------------------------------------')	#60個

import random                 # 導入模組random

porker = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
for i in range(3):
    random.shuffle(porker)    # 將次序打亂重新排列
    print(porker)

print('------------------------------------------------------------')	#60個

import random                               # 導入模組random

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print(f"\n特別號:{specialNum}")             # 列印特別號

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("年 ", xtime.tm_year)         # 物件設定方式顯示
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print('------------------------------------------------------------')	#60個

''' fail in kilo
import time

x = 1000000
pi = 0
time.process_time()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print(f"當 {i=:7d} 時 PI={pi:8.7f}, 所花時間={e_time}")



x = 1000000
pi = 0
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i % 100000 == 0:      # 隔100000執行一次
        print(f"當 {i = :7d} 時 PI = {pi:20.19f}")

'''

print('------------------------------------------------------------')	#60個

import sys

print("目前Python版本是: ", sys.version)
print("目前Python版本是: ", sys.version_info)

import sys
print(sys.version_info)
print("---")
print(sys.platform)
print("---")
print(sys.argv)
print("---")
print(sys.path)

version_rows = [("platform", platform.platform()), ("Python", sys.version)]
print(version_rows)

if sys.version_info.major < 3 or sys.version_info.minor < 3:
    sys.exit("Error: clinic.py requires Python 3.3 or greater.")

print('------------------------------------------------------------')	#60個

import keyword
print(keyword.kwlist)

import keyword

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")

print('------------------------------------------------------------')	#60個

import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)

print('------------------------------------------------------------')	#60個

import string

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串
    
abc = string.printable[:-5]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串
encry_dict = dict(zip(subText, abc))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)

print('------------------------------------------------------------')	#60個

print(f"全域變數 : {globals()}")

print('------------------------------------------------------------')	#60個

import os

print('顯示資料夾內的特定格式的檔案')

def is_image(filename):
    f = filename.lower()
    return f.endswith('.png') or f.endswith('.jpg') or \
           f.endswith('.jpeg') or f.endswith('.bmp') or \
           f.endswith('.gif') or '.jpg' in f or f.endswith('.svg')


def find_similar_images(foldername):
    image_filenames = []
    image_filenames += [os.path.join(foldername, path) for path in os.listdir(foldername) if is_image(path)]
    for img in sorted(image_filenames):
        print(img)

foldername = 'C:/_git/vcs/_1.data/______test_files2'
find_similar_images(foldername)

print('------------------------------------------------------------')	#60個

import builtins
print(dir(builtins))

import time
print(time.time())

import time
print(time.localtime())

import time
year, month, day, hour, minute, second, _, _, _ = time.localtime()
print("{}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second))

import time
print(time.asctime())

import time
print(time.strftime("%Y-%m-%d %H:%M:%S %a"))

import datetime
#當前的日期及時間
print(datetime.datetime.now())

import datetime

today = datetime.datetime.today()
birthday = datetime.datetime(2018,10,27, 17, 0, 0)
print(today - birthday)

from datetime import datetime
now = datetime.now()
print("今天是{}".format(datetime.strftime(now, "%Y-%m-%d")))
date = input("請輸入一個日期（yyyy-mm-dd):")
target = datetime.strptime(date, "%Y-%m-%d")
diff = now-target
print("到今天共經過了{}天。".format(diff.days))

print('------------------------------------------------------------')	#60個

import calendar
print(calendar.month(2018,10))
print(calendar.calendar(2019))

print('------------------------------------------------------------')	#60個

import os
items = os.listdir()
print(os.path.exists('myprime.py'))
for item in items:
    print(os.path.abspath(item))


print('------------------------------------------------------------')	#60個

''' no file
import os
fullpath = os.path.abspath('myprime.py')
print(fullpath)
print("os.path.basename:", os.path.basename(fullpath))
print("os.path.dirname:", os.path.dirname(fullpath))
print("os.path.getatime:", os.path.getatime(fullpath))
print("os.path.getmtime:", os.path.getmtime(fullpath))
print("os.path.getctime:", os.path.getctime(fullpath))
print("os.path.getsize:", os.path.getsize(fullpath))
print("os.path.isabs:", os.path.isabs(fullpath))
print("os.path.isfile:", os.path.isfile(fullpath))
print("os.path.isdir:", os.path.isdir(fullpath))
print("os.path.split:", os.path.split(fullpath))
print("os.path.splitdrive:", os.path.splitdrive(fullpath))
print("os.path.splitext:", os.path.splitext(fullpath))

'''


print('------------------------------------------------------------')	#60個

'''

python的日期當中分成
1. date(日期)
2. time(時間)
3. datetime(混合date跟time)
4. timedelta(計算歷時期間的型態)
5. timezone(處理時區資訊的型態)

'''

import datetime

#輸出當前的日期及時間

print(datetime.datetime.now())

print(datetime.datetime.today())

#而如果只想要輸出現在的日期的話則用
print(datetime.date.today())


#而如果要輸出此時準確的時間的話則

import time
print(time.localtime())

#而我們也可以一一拆解

tonow = datetime.datetime.now()
print(tonow.year)
print(tonow.month)
print(tonow.day)

#而我們也可以算今天是今年的第幾天

dts = '20201007'
dt = datetime.datetime.strptime(dts,"%Y%m%d")
another_dts = dts[:4]+"0101"
another_dt = datetime.datetime.strptime(another_dts,"%Y%m%d")
print(int((dt-another_dt).days)+1)


'''
由上可得知datetime.datetime.strptime()這個是將所輸入的dts轉換成日期的格式則格式為後面的年月日，再來取出輸入的西元年加上"0101"後一樣轉換成日期的格式最後將輸入日期減掉設定日期後+1輸出成今天為今年的第幾天
'''

loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours=3) 
new_dt = loc_dt + time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)


'''
由上可得知我們也可以調整時差，將我們現在的時間加上3小時的時差並將其輸出出來，一開始我們將抓出本地的時間並且將變數time_del宣告為時差差三個小時，最後將其相加就變成有時差三個小時最後將其指定格式後輸出，而以此類推我們也可以將時差晚三個小時
'''


loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours=3) 
new_dt = loc_dt - time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)

print('------------------------------------------------------------')	#60個

import codecs
import contextlib
import io
import locale
import sys
import unittest
import warnings
import encodings


all_unicode_encodings = [
    "ascii",
    "big5",
    "big5hkscs",
    "charmap",
    "cp037",
    "cp1006",
    "cp1026",
    "cp1125",
    "cp1140",
    "cp1250",
    "cp1251",
    "cp1252",
    "cp1253",
    "cp1254",
    "cp1255",
    "cp1256",
    "cp1257",
    "cp1258",
    "cp424",
    "cp437",
    "cp500",
    "cp720",
    "cp737",
    "cp775",
    "cp850",
    "cp852",
    "cp855",
    "cp856",
    "cp857",
    "cp858",
    "cp860",
    "cp861",
    "cp862",
    "cp863",
    "cp864",
    "cp865",
    "cp866",
    "cp869",
    "cp874",
    "cp875",
    "cp932",
    "cp949",
    "cp950",
    "euc_jis_2004",
    "euc_jisx0213",
    "euc_jp",
    "euc_kr",
    "gb18030",
    "gb2312",
    "gbk",
    "hp_roman8",
    "hz",
    "idna",
    "iso2022_jp",
    "iso2022_jp_1",
    "iso2022_jp_2",
    "iso2022_jp_2004",
    "iso2022_jp_3",
    "iso2022_jp_ext",
    "iso2022_kr",
    "iso8859_1",
    "iso8859_10",
    "iso8859_11",
    "iso8859_13",
    "iso8859_14",
    "iso8859_15",
    "iso8859_16",
    "iso8859_2",
    "iso8859_3",
    "iso8859_4",
    "iso8859_5",
    "iso8859_6",
    "iso8859_7",
    "iso8859_8",
    "iso8859_9",
    "johab",
    "koi8_r",
    "koi8_u",
    "latin_1",
    "mac_cyrillic",
    "mac_greek",
    "mac_iceland",
    "mac_latin2",
    "mac_roman",
    "mac_turkish",
    "palmos",
    "ptcp154",
    "punycode",
    "raw_unicode_escape",
    "shift_jis",
    "shift_jis_2004",
    "shift_jisx0213",
    "tis_620",
    "unicode_escape",
    "utf_16",
    "utf_16_be",
    "utf_16_le",
    "utf_7",
    "utf_8",
]

print(type(all_unicode_encodings))
    
for encoding in all_unicode_encodings:
    name = codecs.lookup(encoding).name
    print(name)

for encoding in all_unicode_encodings:
    reader = codecs.getreader(encoding)
    print(reader)

for encoding in all_unicode_encodings:
    decoder = codecs.getdecoder(encoding)

for encoding in all_unicode_encodings:
    encoder = codecs.getencoder(encoding)


ALL_CJKENCODINGS = [
# _codecs_cn
    'gb2312', 'gbk', 'gb18030', 'hz',
# _codecs_hk
    'big5hkscs',
# _codecs_jp
    'cp932', 'shift_jis', 'euc_jp', 'euc_jisx0213', 'shift_jisx0213',
    'euc_jis_2004', 'shift_jis_2004',
# _codecs_kr
    'cp949', 'euc_kr', 'johab',
# _codecs_tw
    'big5', 'cp950',
# _codecs_iso2022
    'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004',
    'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr',
]



for enc in ALL_CJKENCODINGS:
    code = '# coding: {}\n'.format(enc)
    print(code)


print('------------------------------------------------------------')	#60個


ticks = time.time() #至今的tick數
print(ticks)

localtime = time.localtime(ticks)   #傳回時間元組
print(type(localtime))
print(localtime)

print('年 :', localtime[0])
print('月 :', localtime[1])
print('日 :', localtime[2])
print('時 :', localtime[3])
print('分 :', localtime[4])
print('秒 :', localtime[5])

#asctime() #傳回時間元組的日期時間字串
formattime = time.asctime(time.localtime(ticks))
print(formattime)



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個















#以下為OK可以搬出的


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


def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)

printArea() # Default arguments width = 1 and height = 2
printArea(4, 2.5) # Positional arguments width = 4 and height = 2.5
printArea(height = 5, width = 3) # Keyword arguments width 
printArea(width = 1.2) # Default height = 2
printArea(height = 6.2) # Default widht = 1



print('------------------------------------------------------------')	#60個



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



import collections

import nt
_ntuple_diskusage = collections.namedtuple('usage', 'total used free')

def disk_usage(path):
    total, free = nt._getdiskusage(path)
    used = total - free
    return _ntuple_diskusage(total, used, free)

foldername = 'C:/_git/vcs/_1.data/______test_files1'
du = disk_usage(foldername)
print(du)
print('容量 :', du.total, '個位元組\t', du.total//1024//1024//1024, 'GB')
print('已使用空間 :', du.used, '個位元組\t', du.used//1024//1024//1024, 'GB')
print('可用空間 :', du.free, '個位元組\t', du.free//1024//1024//1024, 'GB')

foldername = 'D:/tmp_romeo'
du = disk_usage(foldername)
print(du)
print('容量 :', du.total, '個位元組\t', du.total//1024//1024//1024, 'GB')
print('已使用空間 :', du.used, '個位元組\t', du.used//1024//1024//1024, 'GB')
print('可用空間 :', du.free, '個位元組\t', du.free//1024//1024//1024, 'GB')

print('------------------------------------------------------------')	#60個

def test():
    for x in 'abcde':
        for y in '12345':
            print(y, x, end = ' ')

test()

print('------------------------------------------------------------')	#60個



# 定義lambda函數
square = lambda x: x ** 2

# 輸出平方值
print(square(10))

print('------------------------------------------------------------')	#60個

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

a, b = 24, 36
print("最大公約數是 : ", gcd(a, b))

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

