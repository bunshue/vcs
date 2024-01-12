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

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#替代字串
TABLE_NAME = 'people'
SELECT = 'select * from %s order by age, name' % TABLE_NAME

print('select * from %s order by age, name' % TABLE_NAME)
print(SELECT)

key_id = 1234
SELECT = 'SELECT * FROM memos WHERE key=?', (str(key_id))
print(SELECT)

print('---- 語法專區 --------------------------------------------------------')	#60個

print('字串處理')

items = "03/11/2006".split("/")
print(items)

print('------------------------------------------------------------')	#60個

x = 2
y = 0.5

print("x ** y = " + str(x ** y))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


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

print('------------------------------------------------------------')	#60個

print('if and or')
year = 2024
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(year, "is a leap year?", isLeapYear)

print('------------------------------------------------------------')	#60個

print('if and or')
number = 126

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by 2 and 3")

if number % 2 == 0 or number % 3 == 0:
    print(number, "is divisible by 2 or 3")

if (number % 2 == 0 or number % 3 == 0) and \
       not (number % 2 == 0 and number % 3 == 0):
    print(number, "divisible by 2 or 3, but not both")

print('------------------------------------------------------------')	#60個

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

"""
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
"""

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

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

print('字串的 title 用法, 首字大寫')
s = 'this is a lion mouse'

print(s.title())

print('------------------------------------------------------------')	#60個

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
"""
print('%30s:  %6.3fms  %6.3fms' % \
      (name,
       min(overhead_times) * MILLI_SECONDS,
       max(overhead_times) * MILLI_SECONDS))
"""
print('    %5.0fms    %5.0fms %7.3fms' % \
      (eff_time * MILLI_SECONDS,
       abs_time * MILLI_SECONDS,
       min_overhead * MILLI_SECONDS))

i = 123
print(' Round %-25i  effective   absolute  overhead' % (i+1))

print('%30s:' % name, end = ' ')

print('Calib. prep time     = %.6fms' % (
    total_min_time * MILLI_SECONDS))

print('------------------------------------------------------------')	#60個

for name in ('__repr__', '__str__', '__format__', '__reduce_ex__'):
    print(name)

for x in (15, 25, 35, 45, 55):
    print(x)

print('------------------------------------------------------------')	#60個

import importlib
import platform
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


modules = (
    "os", "sys", "cv2", "numpy", "PIL", "pylibjpeg",
    "openjpeg", "libjpeg",
)
"""
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
"""

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

dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
days, hours = divmod(total_hours, 24)   # 商和餘數
print("總供需要天數")
print(days)
print("小時數")
print(hours)

print('------------------------------------------------------------')	#60個

print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

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

print('測試 eval()')

numberStr = '12.34*56.78'
print('數值公式 :', numberStr)

number = eval(numberStr)
print("計算結果 : %5.2f" % number)

print('------------------------------------------------------------')	#60個

msg = """
翠蓋龍旗出建章,鶯啼百囀柳初黃,
昆池冰泮三山近,阿閣花深九陌香,
徑轉虹梁通紫極,庭含玉樹隱霓裳,
侍臣緩步隨鑾輅,岡上應看集鳳皇,
小苑平臨太液池,金舖約戶鎖蟠螭,
雲中帝座飛華蓋,城上鈞陳繞翠旗,
紫氣旋面雙鳳閣,青松還有萬年枝,
從來清蹕深嚴地,開盡碧桃人未知
"""

print(f"<鳳>出現的次數 : {msg.count('鳳')}")

msg = msg.replace('Linda','Lxx')
print(f"新的msg內容 : {msg}")

print('------------------------------------------------------------')	#60個

x = [[a, b, c] for a in range(1, 20) for b in range(a, 20) for c in range(b, 20)
     if a ** 2 + b ** 2 == c **2]
print(x)

print('------------------------------------------------------------')	#60個

for x in range(0x2160, 0x216a):
  print(chr(x), end = ' ')

print()

print('------------------------------------------------------------')	#60個


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

items = os.listdir()
print(os.path.exists('myprime.py'))
for item in items:
    print(os.path.abspath(item))

print('------------------------------------------------------------')	#60個

""" no file
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

"""

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

#以下為OK可以搬出的

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

def test():
    for x in 'abcde':
        for y in '12345':
            print(y, x, end = ' ')

test()

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

print('------------------------------------------------------------')	#60個

print('2 進位整數運算')
x = 0b1101          # 這是2進位整數
print(x)            # 列出10進位的結果
y = 13              # 這是10進位整數
print(bin(y))       # 列出轉換成2進位的結果
print('8 進位整數運算')
x = 0o57            # 這是8進位整數
print(x)            # 列出10進位的結果
y = 47              # 這是10進位整數
print(oct(y))       # 列出轉換成8進位的結果
print('16 進位整數運算')
x = 0x5D            # 這是16進位整數
print(x)            # 列出10進位的結果
y = 93              # 這是10進位整數
print(hex(y))       # 列出轉換成16進位的結果

print('------------------------------------------------------------')	#60個

x1 = "22"
x2 = "33"
x3 = x1 + x2
print("type(x3) = ", type(x3))
print("x3 = ", x3)             # 列印字串相加
x4 = int(x1) + int(x2)
print("type(x4) = ", type(x4))
print("x4 = ", x4)             # 列印整數相加
x5 = '1100'
print("2進位  '1100' = ", int(x5,2))
print("8進位  '22'   = ", int(x1,8))
print("16進位 '22'   = ", int(x1,16))
print("16進位 '5A'   = ", int('5A',16))

print('------------------------------------------------------------')	#60個

str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出")
print(str2)

print('------------------------------------------------------------')	#60個

x1 = 97
x2 = chr(x1)      
print(x2)               # 輸出數值97的字元
x3 = ord(x2)
print(x3)               # 輸出字元x3的Unicode(10進位)碼值
x4 = '魁'
print(hex(ord(x4)))     # 輸出字元'魁'的Unicode(16進位)碼值

print('------------------------------------------------------------')	#60個

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))

print('------------------------------------------------------------')	#60個

r = 5
PI = 3.14159
area = PI * r ** 2
print("/半徑{0:3d}圓面積是{1:10.2f}/".format(r,area))
print("/半徑{0:>3d}圓面積是{1:>10.2f}/".format(r,area))
print("/半徑{0:<3d}圓面積是{1:<10.2f}/".format(r,area))
print("/半徑{0:^3d}圓面積是{1:^10.2f}/".format(r,area))

print('------------------------------------------------------------')	#60個

r = 5
PI = 3.14159
area = PI * r ** 2
print(f"/半徑{r:3d}圓面積是{area:10.2f}/")
print(f"/半徑{r:>3d}圓面積是{area:>10.2f}/")
print(f"/半徑{r:<3d}圓面積是{area:<10.2f}/")
print(f"/半徑{r:^3d}圓面積是{area:^10.2f}/")

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('---- os --------------------------------------------------------')	#60個

"""
import test
packagedir = os.path.dirname(test.__file__)
"""

print('------------------------------------------------------------')	#60個

print(2 ** 32)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

import os

def getuser():
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
        print(name)
        user = os.environ.get(name)
        if user:
            print(user)
            return user

print('get user name')
ccc = getuser()
print(ccc)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

globs = {}
globs = globs.copy()
print(globs)

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


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('---- 新進 未整理 --------------------------------------------------------')	#60個





"""
word = word.strip()

    dbg('recursedown(%r)\n' % (dirname,))
##  dbg('fix(%r)\n' % (filename,))

"""


"""
filename = 'C:/_git/vcs/_1.data/______test_files2/news_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.json';
with open(filename, "w", encoding = 'utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)
"""



print('全圖640X480, 每160X160裁一塊出來')
W = 640
H = 480
w = 160
h = 160

"""
for(y = 0; y < H; y += h)
  for(x = 0; x < W; x += w)
"""

for y in range(0, H, h):
    for x in range(0, W, w):
        box = x, y, min(W, x + w), min(H, y + h)
        print(box)
        #tile = ImageTk.PhotoImage(image.crop(box))
        #canvas.create_image(x, y, image = tile, anchor = NW)
        #print(x, y)
        #print(box)





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


print("------------------------------------------------------------")  # 60個

for envname in "TMPDIR", "TEMP", "TMP":
    dirname = os.getenv(envname)
    print("cccccc", dirname)
    # print(dirname)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import sys

"""
import shutil
import os

fullpath = os.path.abspath('myprime.py')
path, filename = os.path.split(fullpath)
filename, extname = os.path.splitext(filename)
if not os.path.exists("test-dir"):
    os.mkdir("test-dir")
targetfullpath = os.path.join(path, os.path.join("test-dir", "00"+extname))
shutil.copy(fullpath, targetfullpath)

try:
    print("實際上預期可能會有例外的程式碼寫在這裡！")
    10 / 0
    print("在可能發生例外的指令之下的程式碼放在這邊！")
except Exception as e:
    print("發生錯誤了，錯誤訊息如下：")
    print(e)
else:
    print("沒有發生任何錯誤。")
finally:
    print("不管如何，都要執行這裡")

print('------------------------------------------------------------')	#60個

#form PIL import Image

source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for file in allfiles:
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
"""
print("------------------------------------------------------------")  # 60個

import os
from PIL import Image

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
"""

post_html = """
</table>
</body>
</html>
"""
"""
table_html = ""

source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for file in allfiles:
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容            
            table_html += "<tr><td><a href='{}'><img src='{}'></a></td></tr>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

import os
from PIL import Image

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
<tr>
"""

post_html = """
</tr>
</table>
</body>
</html>
"""


table_html = ""
"""
source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for index, file in enumerate(allfiles):
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容         
            table_html += "<td><a href='{}'><img src='{}'></a></td>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
            if (index+1) % 3 == 0:
                table_html += "</tr><tr>"
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

from stat import *

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

st = os.lstat(filename)

itime = ST_MTIME
# itime = ST_CTIME
anytime = st[itime]
size = st[ST_SIZE]
print("檔案大小 :", size, "拜")

print("------------------------------------------------------------")  # 60個


import os
import sys

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"


short_filename = os.path.basename(filename)

print(short_filename)

cache_dir = os.path.dirname(filename)
print(cache_dir)

head, tail = short_filename[:-3], short_filename[-3:]
print(head)
print(tail)

print("------------------------------------------------------------")  # 60個

import sys
import os

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

canonic = os.path.abspath(filename)
print(canonic)

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
canonic = os.path.normcase(filename)
print(canonic)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("計算字數")

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename1 = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/alice.txt"
filename2 = (
    "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/siddhartha.txt"
)
filename3 = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/moby_dick.txt"
filename4 = (
    "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/little_women.txt"
)

filenames = [filename1, filename2, filename3, filename4]

filename = "C:/_git/vcs/_1.data/______test_files1/poetry2.txt"

for filename in filenames:
    count_words(filename)

print("------------------------------------------------------------")  # 60個

print("統計一個檔案的字數")

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

print("------------------------------------------------------------")  # 60個

b = 'abcdefg'
c = list(b)         #list
print(type(c))
print(c)

for d in reversed(c):
    print(d)

print('------------------------------------------------------------')	#60個

import numpy as np

a = np.array([2,3,4,5,6])
print(f'a = {a}')
b = np.ma.masked_where(a > 3, a)
print(f'b = {b}')

print('------------------------------------------------------------')	#60個

"""
y = x ^ 2
x = [x for x in range(31)]
y = [(y * y) for y in x]
"""

print('------------------------------------------------------------')	#60個

import os
import sys

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
head, ext = os.path.splitext(filename)
head, base = os.path.split(filename)

print('------------------------------------------------------------')	#60個

name = 'aaaamock'
message = '%s(%%s)' % name

print(message)

print('------------------------------------------------------------')	#60個

number = 123456
NUMBER_OF_DIGITS = 10
print(number)
numberList = list(str(number).zfill(NUMBER_OF_DIGITS))
print(numberList)
numberList = list(str(number))
print(numberList)

print('------------------------------------------------------------')	#60個

# 位元運算子綜合應用
x = 12
y = 8
print(x & y)
print(x ^ y)
print(x | y)
print(~x)

print("------------------------------------------------------------")  # 60個

word = [
    "holiday",
    "happy",
    "birth",
    "yesterday",
    "holiday",
    "car",
    "yellow",
    "happy",
    "mobile",
    "cup",
    "happy",
    "holiday",
    "holiday",
    "desk",
    "birth",
]
print("holiday 出現的次數", word.count("holiday"))

print("------------------------------------------------------------")  # 60個

word = [
    "holiday",
    "happy",
    "birth",
    "yesterday",
    "holiday",
    "car",
    "yellow",
    "happy",
    "mobile",
    "cup",
    "happy",
    "holiday",
    "holiday",
    "desk",
    "birth",
]
search_str = "yellow"
print("單字 %s 第一次出現的索引值%d" % (search_str, word.index(search_str)))

print("------------------------------------------------------------")  # 60個

info = [
    ["C程式設計", "朱大峰", "480"],
    ["Python程式設計", "吳志明", "500"],
    ["Java程式設計", "許伯如", "540"],
]

for book, author, price in info:
    print("%10s %3s" % (book, author), " 書籍訂價:", price)


info = [
    ["C程式設計", "朱大峰", "480"],
    ["Python程式設計", "吳志明", "500"],
    ["Java程式設計", "許伯如", "540"],
]

for book, author, price in info:
    print("%10s %3s" % (book, author), " 書籍訂價:", price)

str1 = "淡泊以明志，寧靜以致遠"
print("原字串", str1)
print("欄寬20，字串置中", str1.center(20))
print("字串置中，# 填補", str1.center(20, "#"))
print("欄寬20，字串靠左", str1.ljust(20, "@"))
print("欄寬20，字串靠右", str1.rjust(20, "!"))

mobilephone = "931828736"
print("字串左側補0:", mobilephone.zfill(10))

str2 = "Time create hero.,I love my family."
print("以逗點分割字元", str2.partition(","))

str3 = "忠孝\n仁愛\n信義\n和平"
print("依\\n分割字串", str3.splitlines(False))

print("------------------------------------------------------------")  # 60個

result = lambda x: 3 * x - 1  # lambda()函數
print(result(3))  # 輸出數值8

print("------------------------------------------------------------")  # 60個

def formula(x, y):  # 自訂函數
    return 3 * x + 2 * y


result = lambda x: 3 * x - 1  # lambda()函數
print(result(3))  # 輸出數值8


def formula(x, y):  # 自訂函數
    return 3 * x + 2 * y


formula = lambda x, y: 3 * x + 2 * y  # 表示lambda有二個參數
print(formula(5, 10))  # 傳入兩個數值讓lambda()函數做運算，輸出數值35

print("------------------------------------------------------------")  # 60個

str1 = "I love python."
print("原字串內容: ", str1)
print("轉換成串列: ", list(str1))
print("轉換成值組: ", tuple(str1))
print("字串長度: ", len(str1))

list1 = [8, 23, 54, 33, 12, 98]
print("原串列內容: ", list1)
print("串列中最大值: ", max(list1))
print("串列中最小值: ", min(list1))

relist = reversed(list1)  # 反轉串列
for i in relist:  # 將反轉後的串列內容依序印出
    print(i, end=" ")
print()  # 換行
print("串列所有元素總和: ", sum(list1))  # 印出總和
print("串列元素由小到大排序: ", sorted(list1))

print("------------------------------------------------------------")  # 60個

print("int(8.4)=", int(8.4))
print("bin(14)=", bin(14))
#print("hex(84)=", hex(84))
print("oct(124)=", oct(124))
print("float(6)=", float(6))
print("abs(-6.4)=", abs(-6.4))
print("divmod(58,5)=", divmod(58, 5))
print("pow(3,4)=", pow(3, 4))
print("round(3.5)=", round(3.5))
print("chr(68)=", chr(68))
print("ord('%s')=%d" % ("A", ord("A")))
print("str(1234)=", str(1234))
print("sorted([5,7,1,8,9])=", sorted([5, 7, 1, 8, 9]))
print("max(4,6,7,12,3)=", max(4, 6, 7, 12, 3))
print("min(4,6,7,12,3)=", min(4, 6, 7, 12, 3))
print("len([5,7,1,8,9])=", len([5, 7, 1, 8, 9]))

print("------------------------------------------------------------")  # 60個

loc = ([1, 2, 3, 4], [11, 12, 13, 14])
print(type(loc))
print(loc)
print(loc[::-1])

print("------------------------------------------------------------")  # 60個

'''
#! /usr/bin/env python3
"""n2w: 數字轉英文模組, 包含一個num2words函式, 也能獨立執行
獨立執行用法: n2w num
              num: 0~999,999,999,999,999 之間的整數 (可用逗號分隔)
範例: n2w 10,003,103
輸入 10,003,103 後會輸出 ten million three thousand one hundred three
"""

import string, argparse

# 數字與英文的對應字典
_1to9dict = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
_10to19dict = {
    "0": "ten",
    "1": "eleven",
    "2": "twelve",
    "3": "thirteen",
    "4": "fourteen",
    "5": "fifteen",
    "6": "sixteen",
    "7": "seventeen",
    "8": "eighteen",
    "9": "nineteen",
}
_20to90dict = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

# 數字位數與數字英文單位的對應串列(list)
_magnitude_list = [
    (0, ""),
    (3, " thousand "),
    (6, " million "),
    (9, " billion "),
    (12, " trillion "),
    (15, ""),
]


# 數字轉英文的函式
def num2words(num_string):
    """num2words(num_string): convert number to English words"""
    if num_string == "0":
        return "zero"
    num_string = num_string.replace(",", "")
    num_length = len(num_string)
    max_digits = _magnitude_list[-1][0]
    if num_length > max_digits:
        return "Sorry, can't handle numbers with more than  " "{0} digits".format(
            max_digits
        )
    num_string = "00" + num_string
    word_string = ""

    # 用迴圈從數字最右邊逐次取三個數字來處理，亦即從右邊三個一組進行轉換
    for mag, name in _magnitude_list:
        if mag >= num_length:
            return word_string
        else:
            hundreds, tens, ones = (
                num_string[-mag - 3],
                num_string[-mag - 2],
                num_string[-mag - 1],
            )
            if not (hundreds == tens == ones == "0"):
                word_string = _handle1to999(hundreds, tens, ones) + name + word_string


# 處理1~999的函式
def _handle1to999(hundreds, tens, ones):
    if hundreds == "0":
        return _handle1to99(tens, ones)
    else:
        return _1to9dict[hundreds] + " hundred " + _handle1to99(tens, ones)


# 處理1~99的函式
def _handle1to99(tens, ones):
    if tens == "0":
        return _1to9dict[ones]
    elif tens == "1":
        return _10to19dict[ones]
    else:
        return _20to90dict[tens] + " " + _1to9dict[ones]


num = "12345678"
# 將第一個命令列參數值轉為英文，其餘命令列參數不處理
result = num2words(num)
print("{0} 的英文念法是: {1}".format(num, result))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


word = "maintenance"
word.count("n")

len("thunderbolt")


animal = ["cat", "dog", "duck"]
len(animal)


max(100, 10, 50)
min(300, 30, 3000)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

""" no file
import zipfile

files = zipfile.ZipFile("C:/workplace/test.zip")

files.namelist()

files.extract("d/c.txt")

files.extractall()

files.close()
"""

print("------------------------------------------------------------")  # 60個

import requests

r = requests.get("https://tw.yahoo.com/")
print(r.text)

print("------------------------------------------------------------")  # 60個

import pprint

r = requests.get("https://tw.yahoo.com/")
pprint.pprint(r.text)


print("------------------------------------------------------------")  # 60個

import requests

base_url = "https://zipcloud.ibsnet.co.jp/api/search"

query_parameter = "?zipcode="

zipcode = "1600021"

request_url = base_url + query_parameter + zipcode

request_url

requests.get(request_url).json()


# 有這樣的 API 啊，網址是：https://zipcloud.ibsnet.co.jp/doc/api，請幫我寫出來

'''

print("------------------------------------------------------------")  # 60個

import requests, pprint

api_url = "https://zh.wikipedia.org/w/api.php"

api_params = {
    "format": "json",
    "action": "query",
    "titles": "柔道",
    "prop": "revisions",
    "rvprop": "content",
}

wiki_data = requests.get(api_url, params=api_params).json()

pprint.pprint(wiki_data)


# pip install wikipedia


import wikipedia

wikipedia.set_lang("zh")
wikipedia.summary("柔道")

# python wiki_sample.py

# python try_sys.py 想查詢的關鍵字

# python wiki_sample_final.py 柔道

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")

print("------------------------------------------------------------")  # 60個

import requests

from bs4 import BeautifulSoup

html_data = requests.get("http://tw.yahoo.com")

soup = BeautifulSoup(html_data.text, "html.parser")

print(soup.title)

print("------------------------------------------------------------")  # 60個

import requests

from bs4 import BeautifulSoup

game_ranking_html = requests.get(
    "https://www.kamatari.org/blog/2021/best-games-of-2021/"
)

soup = BeautifulSoup(game_ranking_html.text, "html.parser")

for game in soup.findAll("h2"):
    print(game.text)


print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

game_ranking_html = requests.get(
    "https://www.kamatari.org/blog/2021/best-games-of-2021/"
)
soup = BeautifulSoup(game_ranking_html.text, "html.parser")
for game in soup.findAll("h2"):
    print(game.text)

print("------------------------------------------------------------")  # 60個

print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])])

"""
array([[1, 4],
       [2, 5],
       [3, 6]])
"""

#array([[1, 2, 3, ..., 4, 5, 6]])

print('------------------------------------------------------------')	#60個

#numpy.c_() and numpy.r_()的用法


#####np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
#####np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()。

#np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等。
#np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。


#1.numpy.c_:

import numpy as np

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.c_[x,y]
print('z:',z, z.shape)

#2.numpy.r_用法:

import numpy as np

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.r_[x,y]
print('z:',z, z.shape)

print("------------------------------------------------------------")  # 60個
import requests

# 郵遞區號
zipcode = "1000001"

# API 端點
api_endpoint = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# 進行查詢
response = requests.get(api_endpoint)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 驗證 API 回應狀態
    if data['status'] == 200:
        # 取出第一筆地址資訊
        address_info = data['results'][0]

        # 印出完整郵遞區域
        print(f"{address_info['address1']} {address_info['address2']} {address_info['address3']}")
    else:
        print("API 回應錯誤，訊息：", data['message'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


""" fail
import requests

# 郵遞區號
zipcode = "100-0001"

# API 端點
api_endpoint = "http://your_api_endpoint"

# 你的 API 金鑰
api_key = "your_api_key"

# 設定查詢參數
params = {
    'apikey': api_key,
    'zipcode': zipcode,
}

# 進行查詢
response = requests.get(api_endpoint, params=params)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 印出郵遞區域
    print(data['area'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)
"""


print('------------------------------------------------------------')	#60個

from PIL import Image

def blue_to_red(image_path):
    img = Image.open(image_path)
    r, g, b = img.split() # 分離三個通道
    img = Image.merge("RGB",(b,g,r))# 將藍色通道和通道互換
    img.show()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#blue_to_red(filename)

print('------------------------------------------------------------')	#60個

"""
from PIL import Image

def blue_to_red2(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            #若該點的藍色成分明顯超過紅色及綠色,我們便將之視為藍色
            if b > r and b > g:
                #將藍色分轉為紅色
                pixels[x, y] = (b, g, r)
    img.show()
    
    
    
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
blue_to_red2(filename)
"""    

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

import tkinter.messagebox as msg

response = msg.askyesno('糟糕了!!!', '還好嗎？')

if (response == True):
	print('還 OK')
else:
	print('有點麻煩')


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


import calendar
print(calendar.month(2022, 7))


import calendar
print(calendar.__file__)

import calendar as cal
print(cal.month(2022, 8))

from calendar import month, isleap
print(month(2022, 9))

isleap(2024)

import calendar
calendar.isleap(2022)

from calendar import isleap
isleap(2022)


print('------------------------------------------------------------')	#60個

import tkinter as tk

window=tk.Tk()
tk.Label(window, text='紅', bg='red', width=20).pack()
tk.Label(window, text='藍', bg='green', width=20).pack()
tk.Label(window, text='綠', bg='blue', width=20).pack()
window.mainloop()



print('------------------------------------------------------------')	#60個



window = tk.Tk()

topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i],

text = topping[i]).pack(anchor=tk.W)

def buy():
	for i in check_value:
		if check_value[i].get() == True:
			print(topping[i])

tk.Button(window, text='點餐', command=buy).pack()

window.mainloop()



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

import tkinter as tk
window=tk.Tk()
topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}
check_value={}
for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)
window.mainloop()

"""
請問迴圈裡面 check_value [i] = tk.BooleanVar() 這一行，能否舉個例子，假設第 0 個按鈕被勾選，check_value 長怎樣；假設第 0、1 個按鈕被勾選，check_value 長怎樣 ... 依此類推
"""

print('------------------------------------------------------------')	#60個

window = tk.Tk()
radio_value = tk.IntVar()
radio_value.set(1)
lunch = {0:'A 套餐',1:'B 套餐',2:'C 套餐'}
tk.Radiobutton(window, text = lunch[0], variable = radio_value, value = 0).pack()
tk.Radiobutton(window, text = lunch[1], variable = radio_value, value = 1).pack()
tk.Radiobutton(window, text = lunch[2], variable = radio_value, value = 2).pack()
def buy():
	value = radio_value.get()
	print(lunch[value])

tk.Button(window, text='點餐', command=buy).pack()
window.mainloop()


print('------------------------------------------------------------')	#60個

window = tk.Tk()
string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()
window.mainloop()


print('------------------------------------------------------------')	#60個

window = tk.Tk()

def fileopen():
	print('進行開啟檔案的處理')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label=' 檔案', menu=filemenu)

filemenu.add_command(label='開啟檔案', command=fileopen)

window.config(menu=menubar)

window.mainloop()


print('------------------------------------------------------------')	#60個

import tkinter.filedialog as fd

window = tk.Tk()

def open(): 
	filename = fd.askopenfilename()
	print('open file => ' + filename)

def exit(): 
	window.destroy()

def find():
	print('find ! ')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='open', command=open)

filemenu.add_separator()

filemenu.add_command(label='exit', command=exit)

editmenu = tk.Menu(menubar)

menubar.add_cascade(label='Edit', menu=editmenu)

editmenu.add_command(label='find', command=find)

window.config(menu=menubar)


print('------------------------------------------------------------')	#60個

"""
請參考以下程式，幫我利用 tkinter 生成選單視窗，需要的檔案結構如下：

檔案：
	開啟新檔
	開啟舊檔
	另存為
	結束
編輯：
	剪下
	複製
	貼上
說明：
	關於本程式

----------- 以下是參考的程式架構 --------
"""
""" TBD
import tkinter as tk
import tkinter.filedialog as fd
window = tk.Tk()
def open():
	filename = fd.askopenfilename()
print('open file => ' + filename)
def exit():
	window.destroy()
def find():
	print('find !')
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='open', command=open)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='find', command=find)
window.config(menu=menubar)
window.mainloop()

"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import requests

api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

response = requests.get(api_url)

response_dict = response.json()


print("------------------------------------------------------------")  # 60個

response_dict.keys()
response_dict["total"]


import requests, pprint

search_api_url = "https://collectionapi.metmuseum.org/public/collection/v1/search?"
query_parameter = "q=python&hasImages=true"
search_url = search_api_url + query_parameter
print(search_url)
search_response = requests.get(search_url)
pprint.pprint(search_response.json())


print("------------------------------------------------------------")  # 60個

get_object_url = (
    "https://collectionapi.metmuseum.org/public/collection/v1/objects/435864"
)

object_response = requests.get(get_object_url)

object_response.json()["objectURL"]

object_response.json()["title"]

object_response.json()["primaryImageSmall"]

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
import datetime as dt

x = dt.datetime(2020, 10, 22)
print(x)

x = dt.datetime(year=2020, month=10, day=22)
print(x)

y = dt.datetime(2020, 10, 22, 10, 30, 45)  # 設定日期與時間
print(y)

print("------------------------------------------------------------")  # 60個

# 3-4-2 timedelta 物件

x = dt.timedelta(hours=1, minutes=30)  # 1 小時又 30 分

print(x)
y = dt.timedelta(days=1, seconds=30)  # 1 天又 30 秒
print(y)

# 3-4-3 用 timedelta 來增減 datetime 或 timedelta 的時間

import datetime as dt

x = dt.datetime(2020, 10, 22, 10, 30, 45)  # 原始時間

y = dt.timedelta(days=1, hours=2, minutes=5)

print(x)

print(x + y)  # 用 timedelta 來增減 datetime 的時間

print(x - y)

print(x + y * 2)


print("------------------------------------------------------------")  # 60個


""" fail
# 3-4-4 將 datetime 時間以格式化方式輸出

import datetime as dt

x = dt.datetime(2020, 10, 22, 10, 30, 45)

s1 = x.strftime("%Y/%m/%d %H-%M-%S")
print(s1)

s2 = x.strftime("%Y 年 %m 月 %d 日 %H : %M : %S")
print(s2)
"""

print("------------------------------------------------------------")  # 60個

# 3-4-5 用字串來建立 datetime 物件

import datetime as dt

s = "2020/10/22 10-30-45"  # 含有特定格式之日期時間字串

x = dt.datetime.strptime(s, "%Y/%m/%d %H-%M-%S")


print(x)

print(type(x))


print("------------------------------------------------------------")  # 60個

# 4-1-1 lambda 函式簡介

power = lambda x: x**2

print(power(10))


add = lambda a, b: a + b

print(add(5, 3))

print("------------------------------------------------------------")  # 60個

# 4-1-2 在 lambda 內使用一行 if 條件判斷式

absolute = lambda x: x if x >= 0 else -x

func = lambda x: (x**2 - 40 * x + 350) if 10 <= x < 30 else 50

# 4-2-1 str.split()：分割字串為 list 元素

sentence = "This is a test sentence"

print(sentence.split(" "))

["This", "is", "a", "test", "sentence"]

# 4-2-2 用字串正規化分割字串為 list

import re

sentence = "This,is a,test.sentence"
time_data = "2020/05/20_12:30:45"

print(re.split("[,. ]", sentence))  # 用逗點、句點和空格來分割字串

print(re.split("[/_:]", time_data))

print("------------------------------------------------------------")  # 60個

a = [1, -2, 3, -4, 5]

new = []

for x in a:
    new.append(abs(x))  # 走訪 a 的元素, 取絕對值後放入 new

print(new)

str_list = ["This", "is", "a", "test", "sentence"]

print(list(map(str.upper, str_list)))

print("------------------------------------------------------------")  # 60個

# 4-2-4 用 flter() 篩選容器元素

str_list = ["This", "is", "a", "test", "sentence"]

print(list(filter(lambda x: len(x) >= 3, str_list)))

["This", "test", "sentence"]

# 4-2-5 再探 sorted()：自訂目標容器的排序方式

str_list = ["This", "is", "a", "test", "sentence"]

print(sorted(str_list, key=len, reverse=True))

nest_list = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]

print(sorted(nest_list))

print(sorted(nest_list, key=lambda x: x[1]))

print(sorted(nest_list, key=lambda x: x[1], reverse=True))

print("------------------------------------------------------------")  # 60個

# 4-3-1 介紹 list 生成式

a = [1, -2, 3, -4, 5]

print([abs(x) for x in a])

print("------------------------------------------------------------")  # 60個

a = [1, -2, 3, -4, 5]

print([x**2 for x in a])

str_list = ["This", "is", "a", "test", "sentence"]

print([s.upper() for s in str_list])

# 4-3-2 在 list 生成式使用 if 過濾元素

a = [1, -2, 3, -4, 5]

print([x for x in a if x > 0])

str_list = ["This", "is", "a", "test", "sentence"]

print([x for x in str_list if len(x) >= 3])

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

person1 = {"name": "Amy", "phone": "049-1234567", "age": 20}
person2 = {"name": "Jack", "phone": "02-4455666", "age": 25}
person3 = {"name": "Nacy", "phone": "04-9876543", "age": 17}
persons = [person1, person2, person3]
print(type(person1))
print(type(person2))
print(type(person3))
print(type(persons))
print(person1)
print(person2)
print(person3)
print(persons)

print("------------------------------------------------------------")  # 60個

POSTGRES = {
    "user": "admin",
    "password": "123456",
    "db": "NTUHQA",
    "host": "localhost",
    "port": "5432",
}

string = "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s" % POSTGRES

print(string)

print("------------------------------------------------------------")  # 60個

animals = ["cat", "dog", "bat"]
for index, animal in enumerate(animals):
    print(index, animal)

animals = ["cat", "dog", "bat"]
for animal in animals:
    print(animal)

d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8}
for animal, legs in d.items():
    print("動物: %s 有 %d 隻腳" % (animal, legs))

d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8}
for animal in d:
    legs = d[animal]
    print(animal, legs)


d = {"cat": "white", "dog": "black"}  # 建立字典
print(d["cat"])  # 使用Key取得項目: 顯示 "white"
print("cat" in d)  # 是否有Key: 顯示 "True"
d["pig"] = "pink"  # 新增項目
print(d["pig"])  # 顯示 "pink"
print(d.get("monkey", "N/A"))  # 取出項目+預設值: 顯示 "N/A"
print(d.get("pig", "N/A"))  # 取出項目+預設值: 顯示 "pink"
del d["pig"]  # 使用Key刪除項目
print(d.get("pig", "N/A"))  # "pig"不存在: 顯示 "N/A"


from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)


print("------------------------------------------------------------")  # 60個


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(x))

print("------------------------------------------------------------")  # 60個

str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出")
print(str2)

print("------------------------------------------------------------")  # 60個

x1 = 97
x2 = chr(x1)
print(x2)  # 輸出數值97的字元
x3 = ord(x2)
print(x3)  # 輸出字元x3的Unicode碼值
x4 = "魁"
print(ord(x4))  # 輸出字元'魁'的Unicode碼值

print("------------------------------------------------------------")  # 60個

x = 0x5D  # 這是16進為整數
print(x)  # 列出10進位的結果
y = 93  # 這是10進為整數
print(hex(y))  # 列出轉換成16進位的結果

print("------------------------------------------------------------")  # 60個

x = 0b1101  # 這是2進為整數
print(x)  # 列出10進位的結果
y = 13  # 這是10進為整數
print(bin(y))  # 列出轉換成2進位的結果

print("------------------------------------------------------------")  # 60個

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))

print("------------------------------------------------------------")  # 60個

james = [23, 19, 22, 31, 18]  # 定義james串列
print("列印james第1-3場得分", james[0:3])
print("列印james第2-4場得分", james[1:4])
print("列印james第1,3,5場得分", james[0:6:2])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day09\clock.py

from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

'''
if __name__ == '__main__':
    main()
'''

from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return '我是一个圆'


class Rect(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        return '我是一个矩形'


if __name__ == '__main__':
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]
    for shape in shapes:
        print(shape)
        print('周长:', shape.perimeter())
        print('面积:', shape.area())

print("------------------------------------------------------------")  # 60個

import datetime

def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

now = datetime.datetime.now()
date = now.date
month = now.month
year = now.year

m, y = (month, year) if month >= 3 else (month + 12, year - 1)
c, y = y // 100, y % 100
w = (y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10) % 7
month_words = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
print(f'{month_words[month - 1]} {year}'.center(20))
print('Su Mo Tu We Th Fr Sa')
print(' ' * 3 * w, end='')
days = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
][is_leap(year)][month - 1]   
for day in range(1, days + 1):
    print(str(day).rjust(2), end=' ')
    w += 1
    if w == 7:
        print()
        w = 0
print()

print("------------------------------------------------------------")  # 60個

f = [x for x in range(1, 10)]

print(f)

print(sys.getsizeof(f))  # 查看對象佔用內存的字節數

print("------------------------------------------------------------")  # 60個

print("設計一個函數返回給定文件名的後綴名。\n")


def get_suffix(filename, has_dot=False):
    """
    獲取文件名的後綴名

    :param filename: 文件名
    :param has_dot: 返回的後綴名是否需要帶點
    :return: 文件的後綴名
    """
    pos = filename.rfind(".")
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ""


filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
print(get_suffix(filename))

print("------------------------------------------------------------")  # 60個

print("計算指定的年月日是這一年的第幾天\n")

def is_leap_year(year):
    """
    判斷指定的年份是不是閏年

    :param year: 年份
    :return: 閏年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    計算傳入的日期是這一年的第幾天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第幾天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

print(which_day(1980, 11, 28))
print(which_day(1981, 12, 31))
print(which_day(2018, 1, 1))
print(which_day(2016, 3, 1))

print("------------------------------------------------------------")  # 60個

import numpy as np

print("二維陣列 6 X 4")
a = np.array(
    [[0, 0, 0, 1], [1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4], [4, 4, 4, 5], [5, 5, 5, 6]]
)
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.nbytes)

print("第3列 之 第1~4項(不含尾)")
print(a[3, 1:4])

print("前2列 之 第2欄之後")
print(a[:2, 2:])

print("第2列 之 全部")
print(a[2, :])

print("全部列 之 第3欄, 轉成row")
print(a[:, 3])

print("全部列 之 偶數欄")
print(a[:, ::2])

print("偶數列 之 036欄")
print(a[::2, ::3])

# axis = 0 : 第0維 直行
# axis = 1 : 第1維 橫列
print("全部和:", a.sum())
print("直行加:", a.sum(axis=0))
print("橫列加:", a.sum(axis=1))

# np.argmin()求最小值對應的索引
# np.argmax()求最大值對應的索引

print("每個直行的最小值:", a.min(axis=0))
print("每個直行的最小值對應的索引:", a.argmin(axis=0))
print("每個直行的標準差:", a.std(axis=0))

print("全部平均:", a.mean())
print("直行平均:", a.mean(axis=0))
print("橫列平均:", a.mean(axis=1))

print("------------------------------------------------------------")  # 60個

print("一維陣列 10個元素")
a = np.arange(10)
print(a)

print("前4項")
print(a[:4])

print("第3項 至 第7項(不含尾)")
print(a[3:7])

print("第5項 至 最後")
print(a[5:])

print("第3至第9項 跳一個")
print(a[3:9:2])

print("第2項開始至最後, 跳一個")
print(a[2::2])

print("從頭至最後, 跳二個")
print(a[::3])

print("------------------------------------------------------------")  # 60個

print("使用 numpy函數 對 list做處理")

x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]

print(np.max(x))
print(np.mean(x))
print(np.min(x))

print("------------------------------------------------------------")  # 60個

print("用numpy建立資料")
a = np.arange(5)
print(a)
a = np.arange(2,5,1)
print(a)
a = np.linspace(2,5,4)
print(a)
a = np.logspace(0,2,5)
print(a)

a = np.empty(5) # 生成5個元素，值爲隨機數的數組（速度快）
print(a)
a = np.zeros(5) # 生成5個值全爲0的數組
print(a)
a = np.ones(5) # 生成5個值全爲1的數組
print(a)
a = np.full(5, 6) # 生成5個值全爲6的數組
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1,2,3,4,5,6], dtype=np.int64)
print(a.dtype) 
a = a.astype(np.float32)
print(a.dtype) 
print(a.dtype.type)


print("------------------------------------------------------------")  # 60個

print("分段函數")

x=np.arange(10)
print(x)

print(np.where(x<5, x, 9-x))


a=np.arange(10)
print(np.select([x<3,x>6], [-1,1], 0))


a=np.arange(10)
print(np.piecewise(x, [x<3,x>6], [lambda x: x * 2, lambda x: x * 3]))

print("------------------------------------------------------------")  # 60個

print("統計函數")
a=np.arange(10,0,-1)
print(a)
print(a.mean())
print(a.var())
print(a.std())
print(np.average(a, weights=np.arange(0,10,1)))
print(np.median(a))
print(np.percentile(a, 75))


print(a.min())
print(a.max())
print(a.ptp())
print(a.argmin())
print(a.argmax())
print(a.argsort())
a.sort()
print(a)

a=np.random.randint(0,5,10)
print(a) 
print(np.unique(a)) 
print(np.bincount(a)) 
print(np.histogram(a,bins=5))

print("------------------------------------------------------------")  # 60個

print("矩陣與二維數組")
a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(type(a))

a = np.mat(np.random.random((2,2)))
print(a)
print(np.eye(2))
print(np.diag([2,3]))

a = np.mat([[1.,2.],[3.,4.]])
print(np.dot(a,a))    # 矩陣乘積
print(np.multiply(a,a))    # 矩陣點乘
print(a.T)   # 矩陣轉置
print(a.I)   # 矩陣求逆
print(np.trace(a))    # 求矩陣的跡
print(np.linalg.eig(a))   # 特徵分解

a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

print("------------------------------------------------------------")  # 60個

# id的用法

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25, "蘋果": 18}
cfruits = fruits.copy()
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)

print("------------------------------------------------------------")  # 60個

"""
双色球随机选号程序
"""

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")
        print("%02d" % ball, end=" ")
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input("机选几注: "))
    for _ in range(n):
        display(random_select())


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個

"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low**3 + mid**3 + high**3:
        print(num)


print("------------------------------------------------------------")  # 60個

# 函数的定义和使用 - 求最大公约数和最小公倍数

def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(15, 27))
print(lcm(15, 27))

print("------------------------------------------------------------")  # 60個

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print(strtime)
mydate = time.strptime("2018-1-1", "%Y-%m-%d")
print(mydate)

# shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
os.system("ls -l")
# os.chdir('/Users/Hao')
os.system("ls -l")
# os.mkdir('test')

print("------------------------------------------------------------")  # 60個

# 用range创建数值列表
list1 = list(range(1, 11))  # 不含尾
print(list1)

print("------------------------------------------------------------")  # 60個

c = 1 + 3j
print("c的資料型態：", type(c))
print("c是否為複數？", isinstance(1 + 3j, complex))

print("------------------------------------------------------------")  # 60個

sigma = 0
k = int(input("請輸入k值："))  # 輸入k值
for n in range(0, k, 1):
    if n & 1:  # 如果n是奇數
        sigma += float(-1 / (2 * n + 1))
    else:  # 如果n是偶數
        sigma += float(1 / (2 * n + 1))
print("PI = %f" % (sigma * 4))

print("------------------------------------------------------------")  # 60個

# 九九乘法表的雙重迴圈
for i in range(1, 10):
    for j in range(1, 10):
        print("{0}*{1}={2:2d}  ".format(i, j, i * j), sep="\t", end="")
        if j >= 7:
            break  # 設定跳出的條件
    print("\n-------------------------------------------------------\n")


print("------------------------------------------------------------")  # 60個
info = [
    ["C程式設計", "朱大峰", "480"],
    ["Python程式設計", "吳志明", "500"],
    ["Java程式設計", "許伯如", "540"],
]

for book, author, price in info:
    print("%10s %3s" % (book, author), " 書籍訂價:", price)


print("------------------------------------------------------------")  # 60個

word = [
    "holiday",
    "happy",
    "birth",
    "yesterday",
    "holiday",
    "car",
    "yellow",
    "happy",
    "mobile",
    "cup",
    "happy",
    "holiday",
    "holiday",
    "desk",
    "birth",
]
print("holiday 出現的次數", word.count("holiday"))


print("------------------------------------------------------------")  # 60個

str1 = "do your best what you can do"
s1 = str1.count("do", 0)
s2 = str1.count("o", 0, 20)
print("{}\n「do」出現{}次,「o」出現{}次".format(str1, s1, s2))


print("------------------------------------------------------------")  # 60個

str1 = "設定中文字型及負號正確顯示"
print("原字串內容: ", str1)
print("轉換成串列: ", list(str1))
print("轉換成值組: ", tuple(str1))
print("字串長度: ", len(str1))

list1 = list(str1)
print("原串列內容: ", list1)
print("串列中最大值: ", max(list1))
print("串列中最小值: ", min(list1))

relist = reversed(list1)  # 反轉串列
for i in relist:  # 將反轉後的串列內容依序印出
    print(i, end=" ")
print()  # 換行
print("串列元素由小到大排序: ", sorted(list1))


print("------------------------------------------------------------")  # 60個


result = lambda x: 3 * x - 1  # lambda()函數
print(result(3))  # 輸出數值8

print("------------------------------------------------------------")  # 60個


def formula(x, y):  # 自訂函數
    return 3 * x + 2 * y


formula = lambda x, y: 3 * x + 2 * y  # 表示lambda有二個參數
print(formula(5, 10))  ##傳入兩個數值讓lambda()函數做運算，輸出數值35


print("------------------------------------------------------------")  # 60個

str1 = "淡泊以明志，寧靜以致遠"
print("原字串", str1)
print("欄寬20，字串置中", str1.center(20))
print("字串置中，# 填補", str1.center(20, "#"))
print("欄寬20，字串靠左", str1.ljust(20, "@"))
print("欄寬20，字串靠右", str1.rjust(20, "!"))

mobilephone = "931828736"
print("字串左側補0:", mobilephone.zfill(10))

str2 = "Time create hero.,I love my family."
print("以逗點分割字元", str2.partition(","))

str3 = "忠孝\n仁愛\n信義\n和平"
print("依\\n分割字串", str3.splitlines(False))


print("------------------------------------------------------------")  # 60個
math.sqrt(sum(pow(x - (sum(data) / len(data)), 2) for x in data) / len(data))

mean = sum(data) / len(data)
variance = sum(pow(x - mean, 2) for x in data) / len(data)
std = math.sqrt(variance)


print("------------------------------------------------------------")  # 60個

print("a", "b", "c", sep="|")

print("a", "b", "c", end="\n\n")



print("------------------------------------------------------------")  # 60個




prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票價格大於100元的股票構造一個新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)

print("------------------------------------------------------------")  # 60個


"""
迭代工具 - 排列 / 組合 / 笛卡爾積
"""
import itertools

itertools.permutations('ABCD')
itertools.combinations('ABCDE', 3)
itertools.product('ABCD', '123')


"""
找出序列中出現次數最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

x = -10
print("以下輸出abs( )函數的應用")
print(x)  # 輸出x變數
print(abs(x))  # 輸出abs(x)
x = 5
y = 3
print("以下輸出pow( )函數的應用")
print(pow(x, y))  # 輸出pow(x,y)
x = 47.5
print("以下輸出round(x)函數的應用")
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
x = 48.5
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
x = 49.5
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
print("以下輸出round(x,n)函數的應用")
x = 2.15
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.25
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.151
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.251
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)

print("------------------------------------------------------------")  # 60個

dist = 384400  # 地球到月亮距離
speed = 1225  # 馬赫速度每小時1225公里
total_hours = dist // speed  # 計算小時數
days, hours = divmod(total_hours, 24)  # 商和餘數
print("總供需要天數")
print(days)
print("小時數")
print(hours)

print("------------------------------------------------------------")  # 60個

id_no = 1
ename = 'mouse'
cname = "米老鼠"
weight = 8

print("編號 %d 英文名 %s 中文名 %s 體重 %d" % (id_no, ename, cname, weight))
print("編號 {} 英文名 {} 中文名 {} 體重 {}".format(id_no, ename, cname, weight))

print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

x = 100
print("x=/%-6d/" % x)
y = 10.5
print("y=/%-6.2f/" % y)
s = "Deep"
print("s=/%-6s/" % s)

print("------------------------------------------------------------")  # 60個

cars = ["Honda", "Toyota", "Ford", "BMW"]
print("目前串列內容 = ", cars)
print("使用pop( )刪除串列元素")
popped_car = cars.pop()  # 刪除串列末端值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ", cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)  # 刪除串列索引為1的值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ", cars)

print("------------------------------------------------------------")  # 60個

cars = ["toyota", "nissan", "honda"]
search_str = "nissan"
i = cars.index(search_str)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_str, i))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_val, j))

print("------------------------------------------------------------")  # 60個

cars = ["toyota", "nissan", "honda"]
search_str = "nissan"
num1 = cars.count(search_str)
print("所搜尋元素 %s 出現 %d 次" % (search_str, num1))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print("所搜尋元素 %s 出現 %d 次" % (search_val, num2))

print("------------------------------------------------------------")  # 60個

sc = [
    ["洪錦魁", 80, 95, 88, 0],
    ["洪冰儒", 98, 97, 96, 0],
]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
print(sc[0])
print(sc[1])

print("------------------------------------------------------------")  # 60個

aaa = 123

print("%-10d 保留10位向左靠齊")
print("|%-10d|" % aaa)

print("%10d  保留10位向右靠齊")
print("|%10d|" % aaa)

print("------------------------------------------------------------")  # 60個

sc = [
    [1, "洪錦魁", 80, 95, 88, 0, 0, 0],
    [2, "洪冰儒", 98, 97, 96, 0, 0, 0],
    [3, "洪雨星", 91, 93, 95, 0, 0, 0],
    [4, "洪冰雨", 92, 94, 90, 0, 0, 0],
    [5, "洪星宇", 92, 97, 80, 0, 0, 0],
]
# 計算總分與平均
print("填入總分與平均")
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])  # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)  # 填入平均
    print(sc[i])
sc.sort(key=lambda x: x[5], reverse=True)  # 依據總分高往低排序
# 以下填入名次
print("填入名次")
for i in range(len(sc)):  # 填入名次
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x: x[0])  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])

print("------------------------------------------------------------")  # 60個

sc = [
    [1, "洪錦魁", 80, 95, 88, 0, 0, 0],
    [2, "洪冰儒", 98, 97, 96, 0, 0, 0],
    [3, "洪雨星", 91, 93, 95, 0, 0, 0],
    [4, "洪冰雨", 92, 94, 90, 0, 0, 0],
    [5, "洪星宇", 92, 97, 90, 0, 0, 0],
]
# 計算總分與平均
print("填入總分與平均")
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])  # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)  # 填入平均
    print(sc[i])
sc.sort(key=lambda x: x[5], reverse=True)  # 依據總分高往低排序
# 以下填入名次
print("填入名次")
for i in range(len(sc)):  # 填入名次
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x: x[0])  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])

print("------------------------------------------------------------")  # 60個

# 陣列: list 與 tuple
arr = ["one", "two", "three"]
print(arr[0])

arr[1] = "hello"
print(arr)

del arr[1]

print(arr)

arr.append(23)
print(arr)

arr = ("one", "two", "three")
print(arr[0])
print(arr)

# arr[1] = 'hello'

print("------------------------------------------------------------")  # 60個

# 最基本簡單的堆疊

s = []
s.append("吃飯")
s.append("睡覺")
s.append("寫程式")

print(s)
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop())

print("------------------------------------------------------------")  # 60個

# 麻煩的優先佇列

q = []
q.append((2, "寫程式"))
q.append((1, "吃飯"))
q.append((3, "睡覺"))

q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)

print("------------------------------------------------------------")  # 60個

# 用切片清除或複製 list 元素

lst = [0, 1, 2, 3, 4]
del lst[:]

print(lst)

lst = [1, 2, 3]
new_lst = lst

print(new_lst)
print(new_lst is lst)

lst[:] = [7, 8, 9]

print(lst)
print(new_lst)
print(new_lst is lst)

copied_lst = lst[:]

print(copied_lst)
print(copied_lst is lst)

lst = [0, 1, 2, 3, 4]
s = slice(1, 4)
print(lst[s])

print("------------------------------------------------------------")  # 60個

squares = [value**2 for value in range(1, 11)]
print(squares)

print("------------------------------------------------------------")  # 60個

# 使用 json.dumps() 美觀列印 dict

import json

config = {
    "lang": "Python",
    "version": [3.6, 3.7, 3.8],
    "date": "2019-10-14",
    "platform": "linux",
    "org": "Python Software Foundation",
    "config_status": 0xC0FFEE,
    "the_answer": 42,
}

print(json.dumps(config, indent=4, sort_keys=False))

print("------------------------------------------------------------")  # 60個

# 以 dir() 與 help() 探索 Python 模組與物件

import datetime

print(dir(datetime))

print("")

print([_ for _ in dir(datetime) if "date" in _.lower()])

# help(datetime)

print("------------------------------------------------------------")  # 60個

print("有f代入數字")

money = 12345
print(f"正確 你得到獎金 ${money} 元")
print("錯誤 你得到獎金 ${money} 元")

print("------------------------------------------------------------")  # 60個

"""
print('11')
filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    print(f.readline())#讀一行

print('22')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    data = f.read() #讀全部成一行串列

print(repr(data))
print(data)
print(data.split())
data = data.split()
for d in data:
    d.strip()
print(data)

print('33')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.readlines())#讀全部成多行串列
"""

print("------------------------------------------------------------")  # 60個

print("用字典建立個人資料")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)

print("------------------------------------------------------------")  # 60個

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

print("------------------------------------------------------------")  # 60個

def printmsg():
    # 函數本身沒有定義變數, 只有執行列印全域變數功能
    print("函數列印: ", msg)  # 列印全域變數

msg = "Global Variable"  # 設定全域變數
print("主程式列印: ", msg)  # 列印全域變數
printmsg()  # 呼叫函數

print("------------------------------------------------------------")  # 60個

def printmsg():
    # 函數本身有定義變數, 將執行列印區域變數功能
    msg = "Local Variable"  # 設定區域變數
    print("函數列印: ", msg)  # 列印區域變數

msg = "Global Variable"  # 這是全域變數
print("主程式列印: ", msg)  # 列印全域變數
printmsg()  # 呼叫函數

print("------------------------------------------------------------")  # 60個

def printmsg():
    global msg
    msg = "Java"  # 更改全域變數
    print("更改後: ", msg)

msg = "Python"
print("更改前: ", msg)
printmsg()

print("------------------------------------------------------------")  # 60個

"""
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(fn, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一行
with open(fn, encoding='utf-8-sig') as file_Obj:  # 開啟utf-8檔案
    obj_list = file_Obj.readlines()               # 每次讀一行
"""

print("------------------------------------------------------------")  # 60個

class Banks:
    # 定義銀行類別
    title = "Taipei Bank"  # 定義屬性

    def motto(self):  # 定義方法
        return "以客為尊"


userbank = Banks()  # 定義物件userbank
print("目前服務銀行是 ", userbank.title)
print("銀行服務理念是 ", userbank.motto())

print("------------------------------------------------------------")  # 60個

str1 = 'Python is funny and powerful'
print('原字串', str1)
print('欄寬40，字串置中', str1.center(40))
print('字串置中，* 填補', str1.center(40, '*'))
print('欄寬10，字串靠左', str1.ljust(40, '='))
print('欄寬40，字串靠右', str1.rjust(40, '#'))

mobilephone = '931666888'
print('字串左側補0:', mobilephone.zfill(10))

str2 = 'Mayor,President'
print('以逗點分割字元', str2.partition(','))

str3 = '禮\n義\n廉\n恥'
print('依\\n分割字串', str3.splitlines(False))

print("------------------------------------------------------------")  # 60個

str1="Happy birthday to my best friend."
s1=str1.count("to",0) #從str1字串索引0的位置開始搜尋
s2=str1.count("e",0,34) #搜尋str1從索引值0到索引值34-1的位置
print("{}\n「to」出現{}次,「e」出現{}次".format(str1,s1,s2))

print("------------------------------------------------------------")  # 60個

i = 10

for j in range(5):
    z = i + j
    print("小寫：%x\t大寫：%X" %(z, z))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%06.2f\n" %(1.2345))
print("不足數位預設空格：%6.2f\n" %(1.2345))
print("小數點保留2位：%.2f\n" %(1.2345))
print("不足數位補0(以*替代)：%0*.2f\n" %(6, 1.2345))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%05d\n" %(66))
print("不足數位預設空格：%5d\n" %(66))
print("小於位數則輸出全部：%2d\n" %(666))
print("不足數位補0(以*替代)：%0*d\n" %(5, 66))

print("------------------------------------------------------------")  # 60個

list1 = ["A", True, 10, 3.14, "G"]

for i in range(len(list1)):
   print("索引位置：%s\t對應值：%s\t型態：%s\n" %(i, list1[i], type(list1[i])))

print("------------------------------------------------------------")  # 60個

person = ["John", "Merry", "Mi", "Jason"]
addPerson = "David"

if person.count(addPerson) == 0:
   person.insert(len(person) - 2, addPerson)

print("搜尋剛新增人員索引位置：", person.index(addPerson))

person1 = person.copy()
person.clear()

print("複製原串列：", person1)
print("原串列：", person)

print("------------------------------------------------------------")  # 60個

likeBasketball = set(("class A", "class B", "class C"))
likeDodgeball = set(("class A", "class F", "class k"))

setDifference = likeBasketball.difference(likeDodgeball)
print("\nlikeBasketball差集：", setDifference)
setDifference = likeDodgeball.difference(likeBasketball)
print("likeDodgeball差集：", setDifference)

setIntersection = likeBasketball.intersection(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的交集：", setIntersection)

setUnion = likeBasketball.union(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的聯集：", setUnion)

setSymmetric_difference = likeBasketball.symmetric_difference(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的對稱差：", setSymmetric_difference)

print("------------------------------------------------------------")  # 60個

Index = "Hello Python, This is Program"

print("Index字串：", Index)
print(Index[-3:-25:-2])

print("------------------------------------------------------------")  # 60個

strName = "台北永和三支"
strCode = "3388128"
intAount = 123456
intMoney = 456789
	
print("\n郵局：%s" %(strName))
print("郵局代號為%s，轉帳戶頭為%02d" %(strCode, intAount))
print("匯入金額：%c%.2f" %(36, intMoney))
	
if intMoney < 20000:
    print("%c\n" %("成"))

print("------------------------------------------------------------")  # 60個

print("="*30, "\n")

print("------------------------------------------------------------")  # 60個

number={1,2,3,4,5,6,7,8,9,10,11,12}
print(number)
lotto1={3,5,7,10,12} #第一組幸運彩蛋
print("第一組樂透:",lotto1)
lotto2={2,5,6,11,12} #第二組幸運彩蛋
print("第二組樂透:",lotto2)
lucky=lotto1 | lotto2
print("有 %d 個數字出現在其中一次開獎" %len(lucky), lucky)
biglucky=lotto1 & lotto2
print("有 %d 個數字出現在每一次開獎" %len(biglucky), biglucky)
badnum=number -lucky
print("總共有 %d 個不幸運的數字" %len(badnum), badnum)

print("------------------------------------------------------------")  # 60個

phrase = 'Happy holiday.'
print('原字串：', phrase)
print('將首字大寫 ', phrase.capitalize())
print('每個單字的首字會大寫', phrase.title())
print('全部轉為小寫字元', phrase.lower()) 
print('判斷字串首字元是否為大寫', phrase.istitle())
print('是否皆為大寫字元', phrase.isupper())
print('是否皆為小寫字元', phrase.islower())

print("------------------------------------------------------------")  # 60個

s= "我畢業於宜蘭高中."
print(s)
s1=s.replace("宜蘭高中", "高雄中學")
print(s1)

print("------------------------------------------------------------")  # 60個

fruit = ['apple', 'orange', 'watermelon']
print('反轉前內容：', fruit)
fruit.reverse() 
print('反轉後內容：', fruit)
score = [65,76,54,32,18]
print('反轉前內容：', score)
score.reverse() 
print('反轉後內容：', score)

print("------------------------------------------------------------")  # 60個

score = [98, 46, 37, 66, 69]
print('排序前順序：',score)
score.sort() #省略reverse參數, 遞增排序
print('遞增排序：', score)
letter = ['one', 'time', 'happy', 'child']
print('排序前順序：')
print(letter)
letter.sort(reverse = True) #依字母做遞減排序
print('遞減排序：')
print(letter)

print("------------------------------------------------------------")  # 60個

str1 = "happy \nclever \nwisdom"
print( str1.split() ) #以空格與換行符號(\n)來分割
print( str1.split(' ', 2 ) ) 

print("------------------------------------------------------------")  # 60個

wd = 'Alex is optimistic and clever.'
print('字串:', wd)
print('Alex為開頭的字串嗎', wd.startswith('Alex')) 
print('clever為開頭的字串嗎', wd.startswith('clever', 0))
print('optimistic從指定位置的開頭的字串嗎', wd.startswith('optimisti', 8)) 
print('clever.為結尾字串嗎', wd.endswith('clever.'))  

print("------------------------------------------------------------")  # 60個

pay = (8000, 7200, 8300, 4700, 5500)
print(pay)
print(type(pay))
print('由小而大：',sorted(pay))
print('由大而小：', sorted(pay, reverse = True))

print('資料仍維持原順序：')
print(pay)

print("------------------------------------------------------------")  # 60個

word1 = "zoo"
word2 = "animal"
print("交換前: ")
print('單字1={},單字2={}'.format(word1,word2))

word2,word1 = word1,word2
print("交換後: ")
print('單字1={},單字2={}'.format(word1,word2))

print("------------------------------------------------------------")  # 60個

product = (('iPhone','手機','我預算的首選'),
        ('iPad','平板','視股票獲利'),
        ('iPod','播放','價格最親民'))

for(name, c_name,memo) in product:
    print('%-10s %-12s %-10s'%(name,c_name,memo))

print("------------------------------------------------------------")  # 60個

def func(a,b,c):
    x = a +b +c
    return x

print(func(1,2,3))

print("------------------------------------------------------------")  # 60個

def func(a,b,c):
    x = a +b +c
    print(x)

print(func(1,2,3))

print("------------------------------------------------------------")  # 60個

def equation(x,y,z):
    ans = x*y+z*x+y*z
    return ans

print(equation(z=1,y=2,x=3))
print(equation(3, 2, 1))
print(equation(x=3, y=2 , z=1))
print(equation(3, y=2 , z=1))

print("------------------------------------------------------------")  # 60個

score=[97,76,89,76,90,100,87,65]

print('本學期總共考過的數學小考次數', len(score))
print('所有成績由小到大排序的結果為: {}'.format(sorted(score)))
print('本學期所有分數的總和', sum(score))
print('本學期所有分數的平均', round(sum(score)/len(score),1))
print('本學期考最差的分數為', min(score))
print('本學期考最好的分數為', max(score))

print("------------------------------------------------------------")  # 60個

def square_sum(*arg):
    ans=0
    for n in arg:
        ans += n*n
    return ans

ans1=square_sum(1)
print('1*1=',ans1)
ans2=square_sum(1,2)
print('1*1+2*2=',ans2)
ans3=square_sum(1,2,3)
print('1*1+2*2+3*3=',ans3)
ans4=square_sum(1,3,5,7)
print('1*1+3*3+5*5+7*7=',ans4)

def progname(**arg):
    return arg

print(progname(d1='python', d2='java', d3='visual basic'))

print("------------------------------------------------------------")  # 60個

def dinner(mainmeal, *sideorder):
    #列出所點餐點的主餐及點心副餐
    print('所點的主餐為',mainmeal,'所點的副餐點心包括:')
    for snack in sideorder:
        print(snack)

dinner('鐵板豬','烤玉米')
dinner('泰式火鍋','德式香腸','香焦牛奶','幸運餅')

print("------------------------------------------------------------")  # 60個

def Pow(x, y):
    p = 1;
    for i in range(y+1):
        p *= x
    return p
print('請輸入兩數x及y的值函數：')
x=3
y=8
print('次方運算結果：%d' %Pow(x, y))

print("------------------------------------------------------------")  # 60個

def swap_test(x,y):
    print('函數內交換前：x=%d, y=%d' %(x,y))
    x,y=y,x #交換過程
    print('函數內交換前：x=%d, y=%d' %(x,y))     

a=10
b=20 #設定a,b的初值
print('函數外交換前：a=%d, b=%d' %(a,b))
swap_test(a,b) #函數呼叫
print('函數外交換後：a=%d, b=%d' %(a,b))

print("------------------------------------------------------------")  # 60個

print('int(9.6)=',int(9.6))
print('bin(20)=',bin(20))
print('hex(66)=',hex(66))
print('oct(135)=',oct(135))
print('float(70)=',float(70))
print('abs(-3.9)=',abs(-3.9))
print('chr(69)=',chr(69))
print('ord(\'%s\')=%d' %('D',ord('D')))
print('str(543)=',str(543))

print("------------------------------------------------------------")  # 60個

animals = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
for animal in animals:
    print(animal)

print("------------------------------------------------------------")  # 60個

animals = "Python程式設計"
print(animals[0])
print(animals[1])
print(animals[-1])
print(animals[-2])

print("------------------------------------------------------------")  # 60個

animals = "Python"
print(animals.islower())
print("2023".isdigit())

print("------------------------------------------------------------")  # 60個

# 字串函數
animals = 'Hello World!'
print("animals = ", animals)
s = len(animals)
print("len(animals) = ", str(s))
s = max(animals)
print("max(animals) = ", s)
s = min(animals)
print("min(animals) = ", s)
str2 = 'Python程式設計'
print("str2 = ", str2)
s = len(str2)
print("len(str2) = ", str(s))
s = max(str2)
print("max(str2) = ", s)
s = min(str2)
print("min(str2) = ", s)

print("------------------------------------------------------------")  # 60個

animals = 'welcome to python'
print("animals = ", animals)
b = animals.isalnum()
print("animals.isalnum() = ", b)
b = animals.isalpha()
print("animals.isalpha() = ", b)
b = animals.isdigit()
print("animals.isdigit() = ", b)
b = "2023".isdigit()
print('"2023".isdigit() = ', b)
b = animals.isidentifier()
print("animals.isidentifier() = ", b)
b = animals.islower()
print("animals.islower() = ", b)
b = animals.isupper()
print("animals.isupper() = ", b)
b = "   ".isspace()
print('"   ".isspace() = ', b)

print("------------------------------------------------------------")  # 60個

animals = 'welcome to python'
print("animals = ", animals)
b = animals.endswith('thon')
print("animals.endswith('thon') = ", b)
b = animals.startswith('hello')
print("animals.startswith('hello') = ", b)
b = animals.count('o')
print("animals.count('o') = ", b)
b = animals.find('come')
print("animals.find('come') = ", b)
b = animals.find('become')
print("animals.find('become') = ", b)
b = animals.find('o')
print("animals.find('o') = ", b)
b = animals.find('e')
print("animals.find('e') = ", b)
b = animals.rfind('o')
print("animals.rfind('o') = ", b)
b = animals.rfind('e')
print("animals.rfind('e') = ", b)

print("------------------------------------------------------------")  # 60個

animals = 'welcome to python'
print("animals = ", animals)
str2 = 'Welcome to Python'
print("str2 = ", str2)
str3 = 'This is a test.'
print("str3 = ", str3)
s = animals.capitalize()
print("animals.capitalize() = ", s)
s = str2.lower()
print("str2.lower() = ", s)
s = animals.upper()
print("animals.upper() = ", s)
s = animals.title()
print("animals.title() = ", s)
s = str2.swapcase()
print("str2.swapcase() = ", s)
s = str3.replace('is', 'was')
print("str3.replace('is', 'was') = ", s)

print("------------------------------------------------------------")  # 60個

def clean_string(s):
    """
    刪除字符串中的 '\n', '\r' 和前後的空白

    :param s: str，待處理的字符串
    :return: str，刪除後的字符串
    """
    # 刪除 '\n' 和 '\r'
    s = s.replace('\n', '').replace('\r', '')
    # 刪除前後空白
    s = s.strip()
    return s

animals = "  Python is a \nprogramming language.\n\r   "
cleaned_str = clean_string(animals)
print(cleaned_str)  # "Python is a programming language."

print("------------------------------------------------------------")  # 60個

lst1 = []
lst2 = [1, 2, 3, 4, 5]
lst3 = [1, 'Python', 5.5]
print(lst1)
print("lst2: ", lst2)
print(lst3)

print("------------------------------------------------------------")  # 60個

lst4 = list()
lst5 = list(["tom", "mary", "joe"])
lst6 = list("python")
print("lst4:" + str(lst4))
print("lst5:" + str(lst5))
print("lst6:" + str(lst6))


print("------------------------------------------------------------")  # 60個

lst7 = [1, ["tom", "mary", "joe"], [3, 4, 5]]
print("lst7:" + str(lst7))

print("------------------------------------------------------------")  # 60個

lst1 = [1, 2, 3, 4, 5, 6]
print(lst1[0])
print(lst1[1])
print(lst1[-1])
print(lst1[-2])
lst1[1] = 10
lst1[2] = "Python"
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [1, 2, 3, 4, 5, 6]
for e in lst1:
    print(e, end=" ")
print()
animals = ['cat', 'dog', 'bat']
for index, animal in enumerate(animals):
    print(index, animal)

print("------------------------------------------------------------")  # 60個

lst2 = [[2, 4], ['cat', 'dog', 'bat'], [1, 3, 5]]
print(lst2[1][0])
lst2[2][1] = 7
for e1 in lst2:
    for e2 in e1:
        print(e2, end=" ")

print("------------------------------------------------------------")  # 60個

lst2 = [[2, 4], ['cat', 'dog', 'bat'], [1, 3, 5]]
print(lst2[0][1])

print("------------------------------------------------------------")  # 60個

lst1 = [1, 5]
lst1.append(7)
print(lst1)
lst1.extend([9, 11, 13])
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [1, 5, 7, 9, 11, 13]
lst1.insert(1, 3)
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [1, 3, 5, 7, 9, 11, 13]
del lst1[2]
print(lst1)
e1 = lst1.pop()
print(e1, lst1)
e2 = lst1.pop(1)
print(e2, lst1)
lst1.remove(9)
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [4, 2, 8, 9, 1]
print("lst1 = ", lst1)
s = len(lst1)
print("len(lst1) = ", s)
s = max(lst1)
print("max(lst1) = ", s)
s = min(lst1)
print("min(lst1) = ", s)
animals = 'Hello World!'
lst2 = list(animals)
print("lst2 = ", lst2)
for i, v in enumerate(lst2, 0):
    print(i, ":", v, end=" ")
print()
s = sum(lst1)
print("sum(lst1) = ", s) 
lst3 = sorted(lst1)
print("lst3 = sorted(lst1) = ", lst3)

print("------------------------------------------------------------")  # 60個

lst1 = [4, 2, 8, 9, 1, 8]
print("lst1 = ", lst1)
s = lst1.count(8)
print("lst1.count(8) = ", s)
s = lst1.index(8)
print("lst1.index(8) = ", s)
s = lst1.index(1)
print("lst1.index(1) = ", s)
lst1.sort()
print("lst1.sort() = ", lst1)
lst1.reverse()
print("lst1.reverse() = ", lst1)

print("------------------------------------------------------------")  # 60個

def find_max_and_index(lst1):
    """
    找出串列lst1中的最大值和最大值的索引
    :param lst1: 一個包含數字元素的串列
    :return: 一個包含最大值和最大值索引的元組
    """
    max_val = float('-inf')  # 初始化最大值
    max_idx = -1  # 初始化最大值索引

    # 遍歷串列，尋找最大值和最大值索引
    for i, val in enumerate(lst1):
        if val > max_val:
            max_val = val
            max_idx = i

    return max_val, max_idx

# 測試程式
my_lst = [34, 12, 45, 23, 78, 56, 98, 101, 22]
result = find_max_and_index(my_lst)
print("最大值：", result[0])
print("最大值索引：", result[1])

print("------------------------------------------------------------")  # 60個

def concatenate_strings(lst1):
    """
    從lst1中抽出是字串的項目，並連接成一個字串回傳。

    :param lst1: 一個含有多個項目的串列
    :type lst1: list
    :return: 連接所有字串項目後的字串
    :rtype: str
    """

    str_lst = [item for item in lst1 if isinstance(item, str)]
    return ''.join(str_lst)

my_list = ['Hello', 42, 'World', True, 'Python']
result = concatenate_strings(my_list)
print(result)  # 輸出：HelloWorldPython

print("------------------------------------------------------------")  # 60個

x, y = 10, 20
s = "Y= {1} X= {0}".format(x, y)
print(s)
s = "y = {a} x = {b}".format(b=x, a = y)
print(s)

print("------------------------------------------------------------")  # 60個

print("整數: {0:5d}".format(456))
print("整數: {0:05d}".format(123))
print("浮點數: {0:6.3f}".format(123.45678))
print("二進位: {0:b}".format(200))
print("八進位: {0:o}".format(200))
print("十六進位: {0:x}".format(200))

print("------------------------------------------------------------")  # 60個

x, y = 10, 20
s = f"Y= {x} X= {y}"
print(s)

print("------------------------------------------------------------")  # 60個

x = 456
print(f"整數: {x:5d}")
x = 123
print(f"整數: {x:05d}")
x = 123.45678
print(f"浮點數: {x:6.3f}")
x = 200
print(f"二進位: {x:b}")
print(f"八進位: {x:o}")
print(f"十六進位: {x:x}")

print("------------------------------------------------------------")  # 60個

t1 = ()
t2 = (1, 2, 3, 4, 5)
t3 = (1, 'Joe', 5.5)
print(t1)
print("t2 = ", t2)
print(t3)

print("------------------------------------------------------------")  # 60個

t4 = tuple()
t5 = tuple(["tom", "mary", "joe"])
t6 = tuple("python")
print("t4 = " + str(t4))
print("t5 = " + str(t5))
print("t6 = " + str(t6))

print("------------------------------------------------------------")  # 60個

t1 = (1, 2, 3, 4, 5, 6)
print(t1[0])
print(t1[1])
print(t1[-1])
print(t1[-2])

print("------------------------------------------------------------")  # 60個

t1 = (1, 2, 3, 4, 5, 6)
for e in t1:
    print(e, end=" ")

print("------------------------------------------------------------")  # 60個

t1 = (4, 2, 8, 9, 1)
print("t1 = ", t1)
s = len(t1)
print("len(t1) = ", s)
s = max(t1)
print("max(t1) = ", s)
s = min(t1)
print("min(t1) = ", s)
animals = 'Hello World!'
t2 = tuple(animals)
print("t2 = ", t2)
for i, v in enumerate(t2, 0):
    print(str(i) + ":" + v, end=" ")
print()
s = sum(t1)
print("sum(t1) = ", s) 
t3 = sorted(t1)
print("t3 = sorted(t1) = ", t3)

print("------------------------------------------------------------")  # 60個

t1 = (4, 2, 8, 9, 1, 8)
print("t1 = ", t1)
s = t1.count(8)
print("t1.count(8) = ", s)
s = t1.index(8)
print("t1.index(8) = ", s)
s = t1.index(1)
print("t1.index(1) = ", s)

print("------------------------------------------------------------")  # 60個

d1 = {}
d2 = {1: 'apple', 2: 'ball'}
d3 = {
       "name": "joe",
       1: [2, 4, 6]
     }
print(d1)
print("d2 = ", d2)
print(d3)

print("------------------------------------------------------------")  # 60個

d4 = dict()
d5 = dict([(1, "tom"), (2, "mary"), (3, "john")])
print("d4 = " + str(d4))
print("d5 = " + str(d5))

print("------------------------------------------------------------")  # 60個

d1 = {"chicken": 2, "dog": 4, "cat":3}
print(d1["cat"])
print(d1["dog"])
print(d1["chicken"])

print("------------------------------------------------------------")  # 60個

d1 = {"chicken": 2, "dog": 4, "cat":3}
d1["cat"] = 4
print(d1)

print("------------------------------------------------------------")  # 60個

d1 = {"chicken": 2, "dog": 4, "cat":3}
d1["spider"] = 8
print(d1)

print("------------------------------------------------------------")  # 60個

d1 = {"chicken": 2, "dog": 4, "cat":3}
for animal in d1:
    legs = d1[animal]
    print(animal, legs)

print("------------------------------------------------------------")  # 60個

d1 = {"chicken": 2, "dog": 4, "cat":3}
for animal, legs in d1.items():
    print("動物: {0} 有 {1} 隻腳".format(animal, legs))

print("------------------------------------------------------------")  # 60個

d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
del d1[2]
print(d1)
del d1["age"]
print(d1)

print("------------------------------------------------------------")  # 60個

d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
e1 = d1.pop(5)
print(e1, d1)

print("------------------------------------------------------------")  # 60個

d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
e2 = d1.popitem()
print(e2, d1)
e2 = d1.popitem()
print(e2, d1)

print("------------------------------------------------------------")  # 60個

d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
d1.clear()
print(d1)

print("------------------------------------------------------------")  # 60個

d1 = {1:1, 3:9, 5:24, 7:47, 9:83}
print("d1 = ", d1)
s = len(d1)
d2 = dict([(1,"tom"), (2,"mary"), (3, "joe")])
print("d2 = ", d2)
d3 = sorted(d1)
print("d3 = sorted(d1) = ", d3)
 

print("------------------------------------------------------------")  # 60個

d1 = {"tom":2, "bob":3, "mike":4}
print("d1 = ", d1)
i = d1.get("tom")
print("d1.get('tom') = ", i)
i = d1.get("jerry", "不存在")
print("d1.get('jerry', '不存在') = ", i)
t1 = d1.keys()
print("d1.keys() = ", t1)
lst1 = list(t1)
for i in lst1:
    print(i, end=" ")
print()
t1 = d1.values()
print("d1.values() = ", t1)
lst1 = list(t1)
for i in lst1:
    print(i, end=" ")

print("------------------------------------------------------------")  # 60個

def sum_dict_values(d):
    """
    將字典d中的所有值加總並返回總和。

    參數:
    d -- 包含數值的字典。

    返回值:
    所有字典值的總和。
    """
    return sum(d.values())

# 定義一個包含數值的字典
my_dict = {'a': 10, 'b': 20, 'c': 30}

# 使用 sum_dict_values() 函數獲取所有值的總和
total = sum_dict_values(my_dict)

# 列印總和
print(total)

print("------------------------------------------------------------")  # 60個

def find_max_value(d):
    """
    找出字典值的最大值並回傳。
    
    Args:
        d: 一個字典。
        
    Returns:
        字典值的最大值。
    """
    max_value = None  # 初始化最大值為空值
    for value in d.values():  # 遍歷字典的值
        if max_value is None or value > max_value:  # 如果目前值大於最大值
            max_value = value  # 將最大值更新為目前值
    return max_value  # 回傳最大值

# 定義一個字典
my_dict = {"apple": 5, "banana": 2, "orange": 8}

# 呼叫 find_max_value() 函數
max_value = find_max_value(my_dict)

# 列印最大值
print("最大值為：", max_value)

print("------------------------------------------------------------")  # 60個

def create_dict(keys, values):
    """
    建立一個字典，使用傳入的keys作為鍵，values作為值。
    :param keys: 一個包含鍵的串列。
    :param values: 一個包含值的串列，鍵與值一一對應。
    :return: 一個字典，使用傳入的鍵值對建立。
    """
    return dict(zip(keys, values))

keys = ['apple', 'banana', 'orange']
values = [1, 2, 3]

my_dict = create_dict(keys, values)

print(my_dict)  # 輸出: {'apple': 1, 'banana': 2, 'orange': 3}

print("------------------------------------------------------------")  # 60個

animals, str2 = "Hello ", "World!"
str3 = animals + str2
print(str3)
lst1, lst2 = [2, 4], [6, 8, 10]
lst3 = lst1 + lst2
print(lst3)
t1, t2 = (2, 4), (6, 8, 10)
t3 = t1 + t2
print(t3)

print("------------------------------------------------------------")  # 60個

animals = "Hello"
str2 = animals * 3
print(str2)
lst1 = [1, 2]
lst2 = lst1 * 3
print(lst2)
t1 = (1, 2)
t2 = t1 * 3
print(t2)

print("------------------------------------------------------------")  # 60個

str = "Welcome!"
print("come" in str)
print("come" not in str)
lst1 = [2, 4, 6, 8]
print(8 in lst1)
print(2 not in lst1)
t1 = (2, 4, 6, 8)
print(8 in t1)
print(2 not in t1)
d1 = {"tom": 2, "joe": 3}
print("tom" in d1)
print("tom" not in d1)

print("------------------------------------------------------------")  # 60個

print("green" == "glow")
print("green" != "glow")
print("green" > "glow")
print("green" >= "glow")
print("green" < "glow")
print("green" <= "glow")
d1 = {"tom":30, "bobe":3}
d2 = {"bobe":3, "tom":30}
print(d1 == d2)
print(d1 != d2)

print("------------------------------------------------------------")  # 60個

animals = 'Hello World!'
print("animals = ",animals)
s = animals[1:3]
print("animals[1:3] = ", s)
s = animals[1:5]
print("animals[1:5] = ", s)
s = animals[:7]
print("animals[:7] = ", s)
s = animals[4:]
print("animals[4:] = ", s)
s = animals[1:-1]
print("animals[1:-1] = ", s)
s = animals[6:-2]
print("animals[6:-2] = ", s)

print("------------------------------------------------------------")  # 60個

lst1 = list('Hello World!')
print("lst1 = ", lst1)
s = lst1[1:3]
print("lst1[1:3] = ", s)
s = lst1[1:5]
print("lst1[1:5] = ", s)
s = lst1[:7]
print("lst1[:7] = ", s)
s = lst1[4:]
print("lst1[4:] = ", s)
s = lst1[1:-1]
print("lst1[1:-1] = ", s)
s = lst1[6:-2]
print("lst1[6:-2] = ", s)

print("------------------------------------------------------------")  # 60個

t1 = tuple('Hello World!')
print("t1 = ", t1)
s = t1[1:3]
print("t1[1:3] = ", s)
s = t1[1:5]
print("t1[1:5] = ", s)
s = t1[:7]
print("t1[:7] = ", s)
s = t1[4:]
print("t1[4:] = ", s)
s = t1[1:-1]
print("t1[1:-1] = ", s)
s = t1[6:-2]
print("t1[6:-2] = ", s)

print("------------------------------------------------------------")  # 60個

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[1:4] = [3, 5, 7]
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[2:2] = [1, 9]
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[1:3] = []
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [x for x in range(10)]
print(lst1)
lst2 = [x+1 for x in range(10)]
print(lst2)
lst3 = [x for x in range(10) if x % 2 == 1]
print(lst3)
lst4 = [x*2 for x in range(10) if x %2 == 1]
print(lst4)

print("------------------------------------------------------------")  # 60個

d1 = {x: x*x for x in range(10)}
print(d1)
d2 = {x: x*x for x in range(10) if x % 2 == 0}
print(d2)

print("------------------------------------------------------------")  # 60個

r = abs(-10)
print("abs(-10) = ", r)
r = abs(5)
print("abs(5) = ", r)
r = pow(8, 2)
print("pow(8, 2) = ", r)
r = pow(2, 3)
print("pow(2, 3) = ", r)
r = max(9, 3, 12, 32, 81, 92)
print("max(9, 3, 12, 32, 81, 92) = ", r)
r = min(9, 3, 12, 32, 81, 92)
print("min(9, 3, 12, 32, 81, 92) = ", r)
r = round(5.32)
print("round(5.32) = ", r)
r = round(5.52)
print("round(5.52) = ", r)
r = round(3.14568757, 3)
print("round(3.14568757, 3) = ", r)
r = round(3.14568757, 1)
print("round(3.14568757, 1) = ", r)

bmi = 1.23456789

print("您的BMI值為：", round(bmi, 2))

# 輸出BMI值，並四捨五入到小數點後兩位
print("您的BMI值為：", round(bmi, 2))

print("------------------------------------------------------------")  # 60個

"""
path = os.getcwd() + "\\temp"
os.chdir(path)
print(path)
print(os.listdir(path))

print("------------------------------------------------------------")  # 60個
 
path = os.getcwd()
new_path = os.getcwd() + "\\temp"
print("目前工作路徑: ", path)
print(new_path)
os.chdir(new_path)
print("chdir(): ", new_path)
os.mkdir('newDir')
print("mkdir(): ", os.listdir(new_path))

print("------------------------------------------------------------")  # 60個

new_path = os.getcwd() + "\\temp"
print(new_path)
os.chdir(new_path)
os.rename('newDir','newDir2')
print("rename(): ", os.listdir(new_path))

print("------------------------------------------------------------")  # 60個

new_path = os.getcwd() + "\\temp"
print(new_path)
os.chdir(new_path)
os.rmdir('newDir2')
fp = open("aa.txt", "w")
fp.close()
print("rmdir(): ", os.listdir(new_path))
os.remove("aa.txt")
print("remove(): ", os.listdir(new_path))
"""

print("------------------------------------------------------------")  # 60個

import os.path as path
 
fname = path.realpath("ch11-2-2.py")
print(fname)
r = path.split(fname)
print("os.path.split() =", r)
r = path.splitext(fname)
print("os.path.splitext() =", r)

print("------------------------------------------------------------")  # 60個

import os.path as path
 
fname = path.realpath("ch11-2-2.py")
print(fname)
p = path.dirname(fname)
print("p = os.path.dirname() =", p)
f = path.basename(fname)
print("f = os.path.basename() =", f)

print("------------------------------------------------------------")  # 60個

import os.path as path
 
p = "D:\PythonChatGPT\ch11"
f = "ch11-2-2.py"
print(p, f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)

print("------------------------------------------------------------")  # 60個

word = ["holiday", "happy", "birth",
             "yesterday", "holiday", "car",
             "yellow", "happy", "mobile",
             "cup", "happy", "holiday",
             "holiday", "desk", "birth",
             ]
print("holiday 出現的次數", word.count("holiday"))

print("------------------------------------------------------------")  # 60個

word = ["holiday", "happy", "birth",
             "yesterday", "holiday", "car",
             "yellow", "happy", "mobile",
             "cup", "happy", "holiday",
             "holiday", "desk", "birth",
             ]
search_str="yellow"
print("單字 %s 第一次出現的索引值%d" %(search_str,word.index(search_str)))

print("------------------------------------------------------------")  # 60個

no = [105, 25, 8, 179, 60, 57]
print('排序前的資料順序：',no)
no.sort() #省略reverse參數, 遞增排序
print('遞增排序：', no)
zoo = ['tiger', 'elephant', 'lion', 'rabbit']
print('排序前的資料順序：')
print(zoo)
zoo.sort(reverse = True) #依字母做遞減排序
print('依單字字母遞減排序：')
print(zoo)

print("------------------------------------------------------------")  # 60個

friendA= {"Andy", "Axel", "Michael","May"}
friendB = {"Peter", "Axel", "Andy","Julia"}
print(friendA & friendB)
print(friendA | friendB)
print(friendA - friendB)
print(friendA ^ friendB)

print("------------------------------------------------------------")  # 60個

x = 859
y = 935
print("兩數經交換前的值: ")
print('x={},y={}'.format(x,y))
y,x = x,y
print("兩數經交換後的值: ")
print('x={},y={}'.format(x,y))

print("------------------------------------------------------------")  # 60個

tup = (28, 39, 58, 67,97, 54) 
print('目前元組內的所有元素：')
for item in range(len(tup)):
   print ('tup[%2d] %3d' %(item, tup[item]))

print("------------------------------------------------------------")  # 60個

salary = (86000, 72000, 83000, 47000, 55000)
print('原有資料：')
print(salary)
print('--------------------------------')

# 由小而大
print('薪資由小而大排序：',sorted(salary))
print('--------------------------------')

# 遞減排序
print('薪資由大而小排序：', sorted(salary, reverse = True))
print('--------------------------------')

print('資料經排序後仍保留原資料位置：')
print(salary)
print('--------------------------------')

print("------------------------------------------------------------")  # 60個

info = [['C程式設計','朱大峰','480'],
        ['Python程式設計','吳志明','500'],
        ['Java程式設計','許伯如','540']]

for(book, author,price) in info:
    print('%10s %3s'%(book,author),' 書籍訂價:',price)

print("------------------------------------------------------------")  # 60個

original= ["abase", "abate", "abdicate","abhor", "abate", "acrid","appoint", "abate", "kindle"]
print("單字收集的原始內容: ")
print(original)
set1=set(original)
not_duplicatd=list(set1)
print("刪除重複單字的最佳內容: ")
print(not_duplicatd)
print("按照字母的排列順序: ")
not_duplicatd.sort()
print(not_duplicatd)

print("------------------------------------------------------------")  # 60個

str1 = '淡泊以明志，寧靜以致遠'
print('原字串', str1)
print('欄寬20，字串置中', str1.center(20))
print('字串置中，# 填補', str1.center(20, '#'))
print('欄寬20，字串靠左', str1.ljust(20, '@'))
print('欄寬20，字串靠右', str1.rjust(20, '!'))

mobilephone = '931828736'
print('字串左側補0:', mobilephone.zfill(10))

str2 = 'Time create hero.,I love my family.'
print('以逗點分割字元', str2.partition(','))

str3 = '忠孝\n仁愛\n信義\n和平'
print('依\\n分割字串', str3.splitlines(False))

print("------------------------------------------------------------")  # 60個

def fun1(obj, price):
    obj = 'Microwave'
    print('函數內部修改字串及串列資料')
    print('物品名稱:', obj)
    #新增價格
    price.append(12000)
    print('物品售價:', price)

obj1 = 'TV'  #未呼叫函數前的字串
price1 = [24000, 18000, 35600] #未呼叫函數前的串列
print('函數呼叫前預設的字串及串列')
print('物品名稱:', obj1)
print('物品售價:', price1)
fun1(obj1, price1)

print('函數內部被修改過字串及串列:')
print('名字:', obj1) #字串內容沒變
print('分數:', price1) #串列內容已改變

print("------------------------------------------------------------")  # 60個

def payment():
    price = 100
    num = 30
    rate = 0.35  #抽取獎金的百分比
    total = price*num * rate
    return price*num, total
 
e1 ,e2 = payment()
print("總銷售業績{},應付獎金：{}".format(e1, e2))

print("------------------------------------------------------------")  # 60個

str1="do your best what you can do"
s1=str1.count("do",0)
s2=str1.count("o",0,20)
print("{}\n「do」出現{}次,「o」出現{}次".format(str1,s1,s2))


print("------------------------------------------------------------")  # 60個
def hello(word):
      print(word)

hello('Holiday')
hello('Birthday')

print("------------------------------------------------------------")  # 60個

def func(x,y,z):
    formula = x*x+y*y+z*z
    return formula

print(func(z=5,y=2,x=7))
print(func(7, 2, 5))
print(func(x=7, y=2 , z=5))
print(func(7, y=2 , z=5))

print("------------------------------------------------------------")  # 60個

phrase = 'never put off until tomorrow what you can do today.'
print('原字串：', phrase)
print('將首字大寫 ', phrase.capitalize())
print('每個單字的首字會大寫', phrase.title())
print('全部轉為小寫字元', phrase.lower()) 
print('判斷字串首字元是否為大寫', phrase.istitle())
print('是否皆為大寫字元', phrase.isupper())
print('是否皆為小寫字元', phrase.islower())

print("------------------------------------------------------------")  # 60個

print('int(8.4)=',int(8.4))
print('bin(14)=',bin(14))
print('hex(84)=',hex(84))
print('oct(124)=',oct(124))
print('float(6)=',float(6))
print('abs(-6.4)=',abs(-6.4))
print('divmod(58,5)=',divmod(58,5))
print('pow(3,4)=',pow(3,4))
print('round(3.5)=',round(3.5))
print('chr(68)=',chr(68))
print('ord(\'%s\')=%d' %('A',ord('A')))
#print('str(1234)=',str(1234))
print('sorted([5,7,1,8,9])=',sorted([5,7,1,8,9]))
print('max(4,6,7,12,3)=',max(4,6,7,12,3))
print('min(4,6,7,12,3)=',min(4,6,7,12,3))
print('len([5,7,1,8,9])=',len([5,7,1,8,9]))

print("------------------------------------------------------------")  # 60個

def factorial(*arg):
    product=1
    for n in arg:
        product *= n
    return product

ans1=factorial(5)
print(ans1)
ans2=factorial(5,4)
print('5*4=',ans2)
ans3=factorial(5,4,3)
print('5*4*3=',ans3)
ans4=factorial(5,4,3,2)
print('5*4*3*2=',ans4)


def myfruit(**arg):
    return arg

print(myfruit(d1='apple', d2='mango', d3='grape'))

print("------------------------------------------------------------")  # 60個

#引數：x 為底數       
#y 為指數       
#傳回值：次方運算結果 
def Pow(x,y):
    p=1
    for i in range(y):
        p *= x
    return p
print("請輸入次方運算（ex.2 3）：")
x,y=input().split()
print('x=',x)
print('y=',y)
print("次方運算結果: %d" %Pow(int(x), int(y)))

print("------------------------------------------------------------")  # 60個

def func(a,b):
    p1 = a * b
    p2 = a - b
    return p1, p2
 
num1 ,num2 = func(5, 4)
print(num1)  
print(num2)  

print("------------------------------------------------------------")  # 60個

def func(length,width,height):
    p1 = length*width*height
    p2 = length+width+height
    p3 = (length*width+height*length+width*height)*2
    return p1, p2, p3
 
num1 ,num2, num3 = func(5, 4, 3)
print(num1)  
print(num2)
print(num3)

print("------------------------------------------------------------")  # 60個

str1="I love python."
print("原字串內容: ",str1)
print("轉換成串列: ",list(str1))
print("轉換成值組: ",tuple(str1))
print("字串長度: ",len(str1))

list1=[8,23,54,33,12,98]
print("原串列內容: ",list1)
print("串列中最大值: ",max(list1))
print("串列中最小值: ",min(list1))

relist=reversed(list1)#反轉串列
for i in relist: #將反轉後的串列內容依序印出
    print(i,end=' ')
print()#換行
print("串列所有元素總和: ",sum(list1))#印出總和
print("串列元素由小到大排序: ",sorted(list1))

print("------------------------------------------------------------")  # 60個

wd = 'Python is funny and powerful.'
print('字串:', wd)
print('Python為開頭的字串嗎', wd.startswith('Python'))   #回傳True
print('funny為開頭的字串嗎', wd.startswith('funny', 0))#回傳False
print('funny從指定位置的開頭的字串嗎', wd.startswith('funny', 10))  #回傳True
print('powerful.為結尾字串嗎', wd.endswith('powerful.'))  #回傳True

print("------------------------------------------------------------")  # 60個

"""
    函數功能：計算獎金的百分比
    price:產品單價
    num:銷售數量
    price*num:銷售業績總額
    total:實得獎金
"""
def payment():
    price = float(input("產品單價："))
    num = float(input("銷售數量："))
    rate = 0.35  #抽取獎金的百分比
    total = price * num * rate
    return price*num, total

print("------------------------------------------------------------")  # 60個

""" os 模組
import os
directory=os.getcwd()

os.mkdir(directory+"/example")  #建立資料夾
os.mkdir(directory+"/doc")  #建立資料夾
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))

os.rename(directory+"/example",directory+"/sample") #更名
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))

os.rmdir(directory+"/doc")
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

def fib(n):	# 定義函數fib()
    if n==0 :
        return 0 # 如果n=0 則傳回 0
    elif n==1 or n==2:
        return 1
    else:   # 否則傳回 fib(n-1)+fib(n-2)
        return (fib(n-1)+fib(n-2))

print('輸入所要計算第幾個費式數列:')
n=10
for i in range(n+1):# 計算前n個費氏數列
    print('fib(%d)=%d' %(i,fib(i)))

print("------------------------------------------------------------")  # 60個

#老鼠走迷宮
class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.next=None

class Mouse:
    def __init__(self):
        self.first=None
        self.last=None
        
    def empty(self):
            return self.first==None

    def add(self,x,y):
        newNode=Node(x,y)
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            self.last=newNode
        
    def remove(self):
        if self.first==None:
            print('[佇列已經空了]')
            return
        newNode=self.first
        while newNode.next!=self.last:
            newNode=newNode.next
        newNode.next=self.last.next
        self.last=newNode
        
ExitX= 8	#出口的X座標
ExitY= 10	#出口的Y座標
#宣告迷宮陣列
arr= [[1,1,1,1,1,1,1,1,1,1,1,1], \
       [1,0,0,0,1,1,1,1,1,1,1,1], \
       [1,1,1,0,1,1,0,0,0,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,0,0,0,0,1,1,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,1,1,1,0,1,1,0,1,1], \
       [1,1,0,0,0,0,0,0,1,0,0,1], \
       [1,1,1,1,1,1,1,1,1,1,1,1]]

def find(x,y,ex,ey):
    if x==ex and y==ey:     
        if(arr[x-1][y]==1 or arr[x+1][y]==1 or arr[x][y-1] ==1 or arr[x][y+1]==2):
            return 1
        if(arr[x-1][y]==1 or arr[x+1][y]==1 or arr[x][y-1] ==2 or arr[x][y+1]==1):
            return 1
        if(arr[x-1][y]==1 or arr[x+1][y]==2 or arr[x][y-1] ==1 or arr[x][y+1]==1):
            return 1
        if(arr[x-1][y]==2 or arr[x+1][y]==1 or arr[x][y-1] ==1 or arr[x][y+1]==1):
            return 1
    return 0

#主程式


path=Mouse()
x=1	
y=1

print('[迷宮的路徑(0的部分)]')
for i in range(10):
    for j in range(12):
        print(arr[i][j],end='')
    print()
while x<=ExitX and y<=ExitY:
    arr[x][y]=2
    if arr[x-1][y]==0:
        x -= 1
        path.add(x,y)
    elif arr[x+1][y]==0:
        x+=1
        path.add(x,y)
    elif arr[x][y-1]==0:
        y-=1
        path.add(x,y)
    elif arr[x][y+1]==0:
        y+=1
        path.add(x,y)
    elif find(x,y,ExitX,ExitY)==1:
        break
    else:
        arr[x][y]=2
        path.remove()
        x=path.last.x
        y=path.last.y
print('[老鼠走過的路徑(2的部分)]')
for i in range(10):
    for j in range(12):
        print(arr[i][j],end='')
    print()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

N = 50
data=[0] * N

print(type(data))
print(len(data))

for i in range(len(data)):
    data[i]=i

print("------------------------------------------------------------")  # 60個

class Book:
    #定義方法一：取得書籍名稱和價格
    def setInfo(self, title, price):
        self.title = title
        self.price = price
    #定義方法二：輸出書籍名稱和價格
    def showInfo(self):
        print('書籍名稱:{0:6s}, 價格:{1:4s}元'.format(
            self.title, self.price))
# 產生物件
book1=Book()#物件1
book1.setInfo('Python一週速成', '360')
book1.showInfo() #呼叫方法
book2=Book()#物件2
book2.setInfo('網路行銷與社群行銷', '520')
book2.showInfo()

print("------------------------------------------------------------")  # 60個

class Tom():#父類別
    def __init__(self):
        self.height1=178

class Andy(Tom):#父類別是Tom
    def __init__(self):
        self.height2=180
        super().__init__()

class Michael(Tom):#父類別是Tom
    def __init__(self):
        self.height3=185
        super().__init__()
    def display(self):
        print('父親Tom的身高:', self.height1,'公分')
        print('兄弟Andy的身高:', Andy().height2,'公分')
        print('自己Michael的身高:', m1.height3,'公分')

m1=Michael()
m1.display()

print("------------------------------------------------------------")  # 60個

class Book:
    #定義方法一：取得書籍名稱和價格
    def setData(self, title, price):
        self.title = title
        self.price = price
    #定義方法二：輸出書籍名稱和價格
    def showData(self):
        print('書籍名稱:{0:6s}, 價格:{1:4s}'.format(
            self.title, self.price))

print("------------------------------------------------------------")  # 60個

#此程式單純類別定義,沒有任何輸出到螢幕的執行結果
class Company: #定義公司類別
    name='賺大錢有限公司'
    def slogan(self):
        print('優良品質 創新研發 強力行銷')

print("------------------------------------------------------------")  # 60個

class Date:
    def setDate(self,birthday): #第一種方法
        self.birthday =birthday
    def showDate(self): #第二種方法
        print("出生年月日:",self.birthday)
d1 = Date()#第一個物件
d1.setDate("民國67年7月3日")#呼叫方法時傳入字串
d1.showDate()
d2 = Date()#第二個物件
d2.setDate([67,7,3])#呼叫方法時傳入串列

print("------------------------------------------------------------")  # 60個

class Wage:
	def __init__(self, fee=200, hour=80):
		self.fee=fee
		self.hour=hour

	def getArea(self):
		return self.fee* self.hour

tom=Wage()
print("透過init()方法預設值的總薪資: ",tom.getArea(),"元")

jane= Wage(250,100)
print("透過init()方法傳入參數的總薪資: ",jane.getArea(),"元")

print("------------------------------------------------------------")  # 60個

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
tiger = Animal()
daniel= Human()
goldfish=Fish()
alice = Mermaid()
print("tiger是屬於Animal類別:",isinstance(tiger,Animal))
print("daniel是屬於Animal類別:",isinstance(daniel,Animal))
print("goldfish是屬於Animal類別:",isinstance(goldfish,Animal))
print("alice是屬於Animal類別:",isinstance(alice,Animal))
print("===============================================")
print("tiger是屬於Human類別:",isinstance(tiger,Human))
print("daniel是屬於Human類別:",isinstance(daniel,Human))
print("goldfish是屬於Human類別:",isinstance(goldfish,Human))
print("alice是屬於Human類別:",isinstance(alice,Human))
print("===============================================")
print("tiger是屬於Fish類別:",isinstance(tiger,Fish))
print("daniel是屬於Fish類別:",isinstance(daniel,Fish))
print("goldfish是屬於Fish類別:",isinstance(goldfish,Fish))
print("alice是屬於Fish類別:",isinstance(alice,Fish))
print("===============================================")
print("tiger是屬於Mermaid類別:",isinstance(tiger,Mermaid))
print("daniel是屬於Mermaid類別:",isinstance(daniel,Mermaid))
print("goldfish是屬於Mermaid類別:",isinstance(goldfish,Mermaid))
print("alice是屬於Mermaid類別:",isinstance(alice,Mermaid))

print("------------------------------------------------------------")  # 60個

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

print("Mermaid是屬於Fish子類別:",issubclass(Mermaid,Fish))
print("Mermaid是屬於Human子類別:",issubclass(Mermaid,Human))
print("Mermaid是屬於Animal子類別:",issubclass(Mermaid,Animal))

print("------------------------------------------------------------")  # 60個

#多重繼承範例1

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature2(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature3(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
alice = Mermaid()
alice.feature1()
alice.feature2()
alice.feature3()

print("------------------------------------------------------------")  # 60個

#多重繼承範例2

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
alice = Mermaid()
alice.feature1()
alice.feature2()
alice.feature3()
alice.feature4()

print("------------------------------------------------------------")  # 60個

#子類別覆寫父類別的方法
class Normal(): #父類別
    def subsidy(self, income):
        self.money = income
        if self.money >= 500000:
            print('小康家庭補助金額：', end = ' ')
            return 5000
        
class Poor(Normal): #子類別
    def subsidy(self, income): #覆寫subsidy方法
        self.money = income
        if self.money < 300000:
            print('中低收入家庭補助金額：', end = ' ')
            return 10000

student1 = Normal()#建立父類別物件
print(student1.subsidy(780000),'元')

student2 = Poor()#建立子類別物件
print(student2.subsidy(250000),'元')

print("------------------------------------------------------------")  # 60個

#多型實作
class Colleague(): #父類別
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def bonus(self):
        return self.income
    
    def title(self):
        return self.name
    
class Manager(Colleague):#子類別
    def bonus(self):        
        return self.income * 1.5
    
class Director(Colleague): #子類別
    def bonus(self):
        return self.income * 1.2
print('===============================')
obj1 = Colleague('一般性員工', 50000) #父類別物件
print('{:8s} 紅利 {:,}'.format(obj1.title(), obj1.bonus()))

print('===============================')
obj2 = Manager('經理級年終', 80000) #子類別物件
print('{:8s} 紅利 {:,}'.format(obj2.title(), obj2.bonus()))

print('===============================')
obj3 = Director('芏任級年終', 65000) #子類別物件
print('{:8s} 紅利 {:,}'.format(obj3.title(), obj3.bonus()))
print('===============================')

print("------------------------------------------------------------")  # 60個

class Wage:
    def __init__(self, h=80):
        self.__hour=h
    def getHour(self):
        return self.__hour
    def pay(self):
        return hour_fee*self.__hour

hour_fee=200
obj1=Wage(100)
print("每小時基本工資為:",hour_fee,"元")
print("總共工作的小時數:", obj1.getHour())
print("要付給這位工讀生的薪水總額:", obj1.pay(),"元")

print("------------------------------------------------------------")  # 60個

class MobilePhone: #基礎類別
    def touch(self):
        print('我能提供螢幕觸控操作的功能')
        
class HTC(MobilePhone): #衍生類別
    pass

#產生子類別實體
u11 = HTC()
u11.touch()

print("------------------------------------------------------------")  # 60個

class MobilePhone: #基礎類別
    def touch(self):
        print('我能提供螢幕觸控操作的功能')
        
class HTC(MobilePhone): #衍生類別
    def touch(self):
        MobilePhone.touch(self)
        print('我也能提供多點觸控的操作方式')

#產生子類別實體
u11 = HTC()
u11.touch()

print("------------------------------------------------------------")  # 60個

#在子類別呼叫父類別方法—使用super()函式

class Weekday(): #父類別
    def display(self, pay):
        self.price=pay
        print('歡迎來購物')
        print('購買總金額{:,}'.format(self.price))
        
class Holiday(Weekday): #子類別
    def display(self, pay): #覆寫display方法        
        super().display(pay)
        if self.price >= 15000:            
            self.price *= 0.8
        else:
            self.price        
        print('8折 {:,}'.format(self.price))
        
monday = Weekday()#父類別物件
monday.display(25000)

Christmas = Holiday()#子類別物件
Christmas.display(18000)

print("------------------------------------------------------------")  # 60個

#__init__()方法呼叫super()

class Animal():#父類別
    def __init__(self):
        print('我屬於動物類別')
        
class Human(Animal): #子類別
    def __init__(self, name):
        super().__init__()
        print('我也屬於人類類別')

man = Human('黃種人')#子類別實體

print("------------------------------------------------------------")  # 60個


a,b,c=3,5,7;     #宣告a、b及c三個整數變數
print("a= %d b= %d c= %d" %(a,b,c))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("保留區")

cal_dict = {
    "加": lambda x, y: x + y,
    "減": lambda x, y: x - y,
    "乘": lambda x, y: x * y,
    "除": lambda x, y: x / y,
}


def calculator(x, operator, y):
    return cal_dict.get(operator, lambda: None)(x, y)


print(calculator(6, "乘", 7))

calculator = {
    "加": lambda x, y: x + y,
    "減": lambda x, y: x - y,
    "乘": lambda x, y: x * y,
    "除": lambda x, y: x / y,
}

default = lambda: None

print(calculator.get("加", default)(1, 2))
print(calculator.get("乘", default)(3, 5))

print("------------------------------------------------------------")  # 60個

# 使用一般函數
def square1(x):
    value = x**2
    return value

# 輸出平方值
print(square1(10))

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
square2 = lambda x: x**2

# 輸出平方值
print(square2(10))

print("------------------------------------------------------------")  # 60個

result = lambda x : 3*x-1  #lambda()函數
print(result(3)) #輸出數值8

print("------------------------------------------------------------")  # 60個

def formula(x, y): #自訂函數
    return 3*x+2*y

formula = lambda x, y : 3*x+2*y  #表示lambda有二個參數
print(formula (5,10)) ##傳入兩個數值讓lambda()函數做運算，輸出數值35

print("------------------------------------------------------------")  # 60個

total=lambda a,b:a+b
num1=0
num2=0
num1=123
num2=456
print('數值 1+數值 2 =',total(num1,num2))

print("------------------------------------------------------------")  # 60個

animals = "This is a pen."
lst1 = animals.split()
print(lst1)

print("------------------------------------------------------------")  # 60個

animals = """Python is a programming language that lets you work quickly
and integrate systems more effectively."""

# 將 animals 以空白字元切割成串列 lst1
lst1 = animals.split()

# 顯示 lst1 內容
print(lst1)

# 將 lst1 合併成 CSV 字串 str2
str2 = ",".join(lst1)

# 顯示 str2 內容
print(str2)

print("------------------------------------------------------------")  # 60個

str2 = "Tom,Bob,Mary,Joe,John"
lst2 = str2.split(",")
print(lst2)

print("------------------------------------------------------------")  # 60個

str3 = "23\n52\n44\n78"
lst3 = str3.splitlines()
print(lst3)

print("------------------------------------------------------------")  # 60個

str1 = "apple \nbanana \ngrape \norange"
print( str1.split() )
print( str1.split(' ', 2 ) )

print("------------------------------------------------------------")  # 60個

print('字串replace')
s= "My favorite sport is baseball."
print(s)
s1=s.replace("baseball", "basketball")
print(s1)

print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

