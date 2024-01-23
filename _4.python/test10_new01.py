import os
import sys
import time
import math
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

target_url = 'https://www.nkust.edu.tw/p/403-1000-12-{}.php'

for page in range(1, 6):
    html = target_url.format(page)
    print(html)

print('------------------------------------------------------------')	#60個

print('格式化字串')

print(12345)

print('八位數 前面補0')
print('{:08d}\n{:08d}\n{:08d}'.format(123, 1234, 12345))

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

def test():
    for x in 'abcde':
        for y in '12345':
            print(y, x, end = ' ')

test()

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

print(2 ** 32)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

globs = {}
globs = globs.copy()
print(globs)

print('------------------------------------------------------------')	#60個

"""
word = word.strip()

    dbg('recursedown(%r)\n' % (dirname,))
##  dbg('fix(%r)\n' % (filename,))

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

"""
y = x ^ 2
x = [x for x in range(31)]
y = [(y * y) for y in x]
"""

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

loc = ([1, 2, 3, 4], [11, 12, 13, 14])
print(type(loc))
print(loc)
print(loc[::-1])

print("------------------------------------------------------------")  # 60個


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

#數字交換
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

print("------------------------------------------------------------")  # 60個

for number in range(100):
    print(format(number, '5d'), end = '')
    if number % 10 == 9:
        print()

print("------------------------------------------------------------")  # 60個

word = "maintenance"
word.count("n")

len("thunderbolt")


animal = ["cat", "dog", "duck"]
len(animal)


max(100, 10, 50)
min(300, 30, 3000)

print("------------------------------------------------------------")  # 60個

""" wait long
print("requests 1")
import requests

r = requests.get("https://tw.yahoo.com/")
print(r.text)

print("------------------------------------------------------------")  # 60個

print("requests 2")
import requests

base_url = "https://zipcloud.ibsnet.co.jp/api/search"

query_parameter = "?zipcode="

zipcode = "1600021"

request_url = base_url + query_parameter + zipcode

request_url

requests.get(request_url).json()


# 有這樣的 API 啊，網址是：https://zipcloud.ibsnet.co.jp/doc/api，請幫我寫出來

print("------------------------------------------------------------")  # 60個

print("requests 3")
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


"""
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

"""
print("requests 4")
import requests
api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
response = requests.get(api_url)
response_dict = response.json()

response_dict.keys()
response_dict["total"]

get_object_url = (
    "https://collectionapi.metmuseum.org/public/collection/v1/objects/435864"
)

object_response = requests.get(get_object_url)

object_response.json()["objectURL"]

object_response.json()["title"]

object_response.json()["primaryImageSmall"]
"""

print("------------------------------------------------------------")  # 60個



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
#print(hex(y))  # 列出轉換成16進位的結果  fail in sugar

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

#數位時鐘
from time import time, localtime, sleep

class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        #走字
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
        #显示时间
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

"""
if __name__ == '__main__':
    main()
"""

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

print()

help(get_suffix)    #測試docstring

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

print("------------------------------------------------------------")  # 60個

# 用range创建数值列表
list1 = list(range(1, 11))  # 不含尾
print(list1)

print("------------------------------------------------------------")  # 60個

c = 1 + 3j
print("c的資料型態：", type(c))
print("c是否為複數？", isinstance(1 + 3j, complex))

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

#迭代工具 - 排列 / 組合 / 笛卡爾積

import itertools

itertools.permutations('ABCD')
itertools.combinations('ABCDE', 3)
itertools.product('ABCD', '123')


#找出序列中出現次數最多的元素

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

print("有f代入數字")

money = 12345
print(f"正確 你得到獎金 ${money} 元")
print("錯誤 你得到獎金 ${money} 元")

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

print("串列")
score=[97,76,89,76,90,100,87,65]

print('本學期總共考過的數學小考次數', len(score))
print('所有成績由小到大排序的結果為: {}'.format(sorted(score)))
print('本學期所有分數的總和', sum(score))
print('本學期所有分數的平均', round(sum(score)/len(score),1))
print('本學期考最差的分數為', min(score))
print('本學期考最好的分數為', max(score))

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
#print('hex(66)=',hex(66))  fail in sugar
print('oct(135)=',oct(135))
print('float(70)=',float(70))
print('abs(-3.9)=',abs(-3.9))
print('chr(69)=',chr(69))
print('ord(\'%s\')=%d' %('D',ord('D')))
print('str(543)=',str(543))

print("------------------------------------------------------------")  # 60個

animals = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
for animal in animals:
    print(animal, end = ' ')
print()

print("------------------------------------------------------------")  # 60個

animals = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
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
animals = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
print("animals = ", animals)
s = len(animals)
print("len(animals) = ", str(s))
s = max(animals)
print("max(animals) = ", s)
s = min(animals)
print("min(animals) = ", s)

animals = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
animals = 'Python程式設計'
print("animals = ", animals)
s = len(animals)
print("len(animals) = ", str(s))
s = max(animals)
print("max(animals) = ", s)
s = min(animals)
print("min(animals) = ", s)

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
animals = 'Welcome to Python'
print("animals = ", animals)
str3 = 'This is a test.'
print("str3 = ", str3)
s = animals.capitalize()
print("animals.capitalize() = ", s)
s = animals.lower()
print("animals.lower() = ", s)
s = animals.upper()
print("animals.upper() = ", s)
s = animals.title()
print("animals.title() = ", s)
s = animals.swapcase()
print("animals.swapcase() = ", s)
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

word = ["holiday", "happy", "birth",
        "yesterday", "holiday", "car",
        "yellow", "happy", "mobile",
        "cup", "happy", "holiday",
        "holiday", "desk", "birth",
        ]
print("holiday 出現的次數", word.count("holiday"))

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

print("集合")
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

"""
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
"""

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

N = 50
data=[0] * N

print(type(data))
print(len(data))

for i in range(len(data)):
    data[i]=i

print("------------------------------------------------------------")  # 60個

a,b,c=3,5,7;     #宣告a、b及c三個整數變數
print("a= %d b= %d c= %d" %(a,b,c))

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("字串 字典 集合 串列 元組")
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

print('字串的 title 用法, 首字大寫')
s = 'this is a lion mouse'

print(s.title())

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


print('---- os --------------------------------------------------------')	#60個

"""
import test
packagedir = os.path.dirname(test.__file__)
"""


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

print("------------------------------------------------------------")  # 60個

for envname in "TMPDIR", "TEMP", "TMP":
    dirname = os.getenv(envname)
    print("cccccc", dirname)
    # print(dirname)

print("------------------------------------------------------------")  # 60個

"""
import shutil
import os

fullpath = os.path.abspath('myprime.py')
path, filename = os.path.split(fullpath)
filename, extname = os.path.splitext(filename)
if not os.path.exists("test-dir"):
    os.mkdir("test-dir")
targetfullpath = os.path.join(path, os.path.join("test-dir", "00"+extname))
#shutil.copy(fullpath, targetfullpath)

try:
    print("實際上預期可能會有例外的程式碼寫在這裡！")
    #10 / 0
    shutil.copy(fullpath, targetfullpath)
    print("在可能發生例外的指令之下的程式碼放在這邊！")
except Exception as e:
    print("發生錯誤了，錯誤訊息如下：")
    print(e)
else:
    print("沒有發生任何錯誤。")
finally:
    print("不管如何，都要執行這裡")
"""

print('------------------------------------------------------------')	#60個

import stat

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

st = os.lstat(filename)

anytime = st[stat.ST_MTIME]
size = st[stat.ST_SIZE]
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





print('------------------------------------------------------------')	#60個



import os
import sys

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
head, ext = os.path.splitext(filename)
head, base = os.path.split(filename)

print('------------------------------------------------------------')	#60個


# shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
os.system("ls -l")
# os.chdir('/Users/Hao')
os.system("ls -l")
# os.mkdir('test')

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




print('開始計時')
starttime = int(time.time())    # 起始秒數

print("------------------------------------------------------------")  # 60個

import time                         # 導入模組time

print("計算1970年1月1日00:00:00至今的秒數 = ", int(time.time()))

print("------------------------------------------------------------")  # 60個

import time                         # 導入模組time

print(time.asctime())               # 列出目前系統時間 

print("------------------------------------------------------------")  # 60個

import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

endtime = int(time.time())  # 結束秒數
print("所花時間: ", endtime - starttime, " 秒")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個



""" no file
import zipfile

files = zipfile.ZipFile("C:/workplace/test.zip")

files.namelist()

files.extract("d/c.txt")

files.extractall()

files.close()
"""

print("------------------------------------------------------------")  # 60個

# pip install wikipedia


import wikipedia

wikipedia.set_lang("zh")
wikipedia.summary("柔道")

# python wiki_sample.py

# python try_sys.py 想查詢的關鍵字

# python wiki_sample_final.py 柔道


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

str = "{1} * {0} = {2}"
a = 3
b = "5"
print(str.format(a, b, a * int(b)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch02\date.py

year=2023
month=12
day=27
print("日期：%s-%s-%s" %(year, month, day))

print("------------------------------------------------------------")  # 60個

Val=170
print("Val的八進位數=%o" %Val)#以%o格式化字元輸出
print("Val的十六進位數=%x" %Val)#以%x格式化字元輸出 

print("------------------------------------------------------------")  # 60個

weight=123
print("您在月球上體重為：%.5f 公斤" %(weight * 0.17))

print("------------------------------------------------------------")  # 60個

company="藍海科技股份有限公司"
year=27
print("{}已成立公司 {} 年" .format (company, year))

print("------------------------------------------------------------")  # 60個

print("{0:10}收入：{1:_^12}".format("Axel", 52000))
print("{0:10}收入：{1:>12}".format("Michael", 87000))
print("{0:10}收入：{1:*<12}".format("May", 36000))

print("------------------------------------------------------------")  # 60個

num = 168
print ("數字 %s 的浮點數：%5.1f" % (num,num))
print ("數字 %s 的八進位：%o" % (num,num))
print ("數字 %s 的十六進位：%x" % (num,num))
print ("數字 %s 的二進位：%s" % (num,bin(num)))

print("------------------------------------------------------------")  # 60個

print("編號 姓名    底薪  業務獎金 加給補貼")
print("%3d %3s %6d %6d %6d" %(801,"朱正富",32000,10000,5000))
print("%3d %3s %6d %6d %6d" %(805,"曾自強",35000,8000,7000))
print("%3d %3s %6d %6d %6d" %(811,"陳威動",43000,15000,6000))

print("------------------------------------------------------------")  # 60個

num1=30
print(num1)
num1="happy"
print(num1)
a=b=12
print(a,b)
name,salary,weight="陳大富",60000,85.7
print(name,salary,weight)

print("------------------------------------------------------------")  # 60個

x = 15; y = 10
print(x & y)  
print(x ^ y)   
print(x | y)  
print(~x)

print("------------------------------------------------------------")  # 60個


x=1234
print("共需花費: %d 元" % x)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

phrase = ["三陽開泰", "事事如意", "五福臨門"]
for index, x in enumerate(phrase):
    print ("{0}--{1}".format(index, x))

print("------------------------------------------------------------")  # 60個




X = [1, 2,3, 4,5]
Y = [1, 4,9,16,25]
Z = list(zip(X, Y))   #zip : 兩串或更多串資料，同編號放一起的動作
print(Z)


X, Y = zip(*Z)  #Z裡面的點一個一個拿出來
print(X)
print(Y)

print("------------------------------------------------------------")  # 60個

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = zip(a, b)
print(list(c)) # 输出 [(1, 'a'), (2, 'b'), (3, 'c')]


loc = ([1, 2, 3, 4], [11, 12, 13, 14])
for i in zip(*loc):
    print(i)


x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
t = (x, y, z)
print(t)
for i in zip(*t):
    print(i)


# 4-3-3 在 list 生成式用 zip() 同時走訪多個容器

a = [1, -2, 3, -4, 5]
b = [9, 8, -7, -6, -5]

print([[x, y] for x, y in zip(a, b)])
print([x + y for x, y in zip(a, b)])

print("------------------------------------------------------------")  # 60個

a = [1, -2, 3, -4, 5]

b = [9, 8, -7, -6, -5]

print([x + y for x, y in zip(a, b) if x + y >= 0])


# 4-3-4 以巢狀 list 生成式產生複合 list

a = [1, 2, 3]

b = ["A", "B"]

print([[x, y] for x in a for y in b])



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

num1 = [1, 3, 5]
num2 = [2, 4, 6]
num3 = num1 + num2           # 字串為主的串列相加
print(num3)

print("------------------------------------------------------------")  # 60個

cars = ['toyota', 'nissan', 'honda']
nums = [1, 3, 5]
carslist = cars * 3           # 串列乘以數字
print(carslist)
numslist = nums * 5           # 串列乘以數字
print(numslist)   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_13.py

# ch6_13.py
James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
Love = ['Kevin Love',20, 18, 30, 22, 15]    # 定義Love串列
game3 = James[4] + Love[4]
LKgame = James[0] + ' 和 ' +  Love[0] + '第四場總得分 = ' 
print(LKgame, game3)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_14.py

# ch6_14.py
warriors = ['Curry', 'Durant', 'Iquodala', 'Bell', 'Thompson']
print("2018年初NBA勇士隊主將陣容", warriors)
del warriors[3]                 # 不明原因離隊
print("2018年末NBA勇士隊主將陣容", warriors)
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_15.py

# ch6_15.py
nums1 = [1, 3, 5]
print("刪除nums1串列索引1元素前   = ",nums1)
del nums1[1]
print("刪除nums1串列索引1元素後   = ",nums1)
nums2 = [1, 2, 3, 4, 5, 6]
print("刪除nums2串列索引[0:2]前   = ",nums2)
del nums2[0:2]
print("刪除nums2串列索引[0:2]後   = ",nums2)
nums3 = [1, 2, 3, 4, 5, 6]
print("刪除nums3串列索引[0:6:2]前 = ",nums3)
del nums3[0:6:2]
print("刪除nums3串列索引[0:6:2]後 = ",nums3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_16.py

# ch6_16.py
cars = ['Toyota', 'Nissan', 'Honda']
print("cars串列長度是 = %d" %  len(cars))
if len(cars) != 0:
    del cars[0]
    print("刪除cars串列元素成功")
    print("cars串列長度是 = %d" % len(cars))
else:
    print("cars串列內沒有元素資料")
nums = []
print("nums串列長度是 = %d" % len(nums))
if len(nums) != 0:
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_17.py

# ch6_17.py
strN = "DeepStone"
strU = strN.upper( )           # 改成大寫
strL = strN.lower( )           # 改成小寫
strT = strN.title( )           # 改成第一個字母大寫其他小寫
print("大寫輸出:",strU,"\n小寫輸出:",strL,"\n第一字母大寫:",strT)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_18.py

# ch6_18.py
strN = " DeepStone "
strL = strN.lstrip( )       # 刪除字串左邊多餘空白
strR = strN.rstrip( )       # 刪除字串右邊多餘空白
strB = strN.lstrip( )       # 先刪除字串左邊多餘空白
strB = strB.rstrip( )       # 再刪除字串右邊多餘空白
strO = strN.strip( )        # 一次刪除頭尾端多餘空白
print("/%s/" % strN)
print("/%s/" % strL)
print("/%s/" % strR)
print("/%s/" % strB)
print("/%s/" % strO)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_19.py

# ch6_19.py
cars = ['bmw', 'benz', 'audi']     
carF = "我開的第一部車是 " + cars[1].title( )
carN = "我現在開的車子是 " + cars[0].upper( )
print(carF)
print(carN)

print("------------------------------------------------------------")  # 60個

cars = ['Honda','Toyota','Ford']     
print("目前串列內容 = ",cars)
print("在索引1位置插入Nissan")
cars.insert(1,'Nissan')
print("新的串列內容 = ",cars)
print("在索引0位置插入BMW")
cars.insert(0,'BMW')
print("最新串列內容 = ",cars)

print("------------------------------------------------------------")  # 60個

cars = ['Honda','Toyota','Ford','BMW']     
print("目前串列內容 = ",cars)
print("使用pop( )刪除串列元素")
popped_car = cars.pop( )          # 刪除串列末端值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)          # 刪除串列索引為1的值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_23.py

# ch6_23.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
print("使用remove( )刪除串列元素")
expensive = 'bmw'
cars.remove(expensive)            # 刪除第一次出現的元素bmw
print("所刪除的內容是: " + expensive.upper( ) + " 因為太貴了" )
print("新的串列內容",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_24.py

# ch6_24.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
# 直接列印cars[::-1]顛倒排序,不更改串列內容
print("列印使用[::-1]顛倒排序\n", cars[::-1])
# 更改串列內容
print("使用reverse( )顛倒排序串列元素")
cars.reverse( )            # 顛倒排序串列
print("新的串列內容 = ",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_25.py

# ch6_25.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用sort( )由小排到大")
cars.sort( )            
print("排序串列結果 = ",cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort( )由小排到大")
nums.sort( )            
print("排序串列結果 = ",nums)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_26.py

# ch6_26.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用sort( )由大排到小")
cars.sort(reverse=True)            
print("排序串列結果 = ",cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort( )由大排到小")
nums.sort(reverse=True)            
print("排序串列結果 = ",nums)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_27.py

# ch6_27.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列car內容 = ",cars)
print("使用sorted( )由小排到大")
cars_sorted = sorted(cars)            
print("排序串列結果 = ",cars_sorted)
print("原先串列car內容 = ",cars)
nums = [5, 3, 9, 2]     
print("目前串列num內容 = ",nums)
print("使用sorted( )由小排到大")
nums_sorted = sorted(nums)            
print("排序串列結果 = ",nums_sorted)
print("原先串列num內容 = ",nums)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_28.py

# ch6_28.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列car內容 = ",cars)
print("使用sorted( )由大排到小")
cars_sorted = sorted(cars,reverse=True)            
print("排序串列結果    = ",cars_sorted)
print("原先串列car內容 = ",cars)
nums = [5, 3, 9, 2]     
print("目前串列num內容 = ",nums)
print("使用sorted( )由大排到小")
nums_sorted = sorted(nums,reverse=True)            
print("排序串列結果    = ",nums_sorted)
print("原先串列num內容 = ",nums)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_29.py

# ch6_29.py
cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
i = cars.index(search_str)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_str, i))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_val, j))


print("------------------------------------------------------------")  # 60個

James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
games = len(James)                          # 求元素數量
score_Max = max(James[1:games])             # 最高得分
i = James.index(score_Max)                  # 場次
print(James[0], "在第 %d 場得最高分 %d" % (i, score_Max))

print("------------------------------------------------------------")  # 60個

cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
num1 = cars.count(search_str)
print("所搜尋元素 %s 出現 %d 次" % (search_str, num1))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print("所搜尋元素 %s 出現 %d 次" % (search_val, num2))


print("------------------------------------------------------------")  # 60個

char = '-'
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))
char ='***'
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))
char = '\n'             # 換行字元
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))

print("------------------------------------------------------------")  # 60個

James = [['Lebron James','SF','12/30/84'],23,19,22,31,18] # 定義James串列
games = len(James)                                        # 求元素數量
score_Max = max(James[1:games])                           # 最高得分
i = James.index(score_Max)                                # 場次
name = James[0][0]
position = James[0][1]
born = James[0][2]
print("姓名     : ", name)
print("位置     : ", position)
print("出生日期 : ", born)
print("在第 %d 場得最高分 %d" % (i, score_Max))

print("------------------------------------------------------------")  # 60個

cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.append(cars2)
print("執行append( )後串列cars1內容 = ", cars1)
print("執行append( )後串列cars2內容 = ", cars2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_34.py

# ch6_34.py
cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.extend(cars2)
print("執行extend( )後串列cars1內容 = ", cars1)
print("執行extend( )後串列cars2內容 = ", cars2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_35.py

# ch6_35.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_36.py

# ch6_36.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)
                   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_37.py

# ch6_37.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

mysports = ['basketball', 'baseball']
friendsports = mysports[:]
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

string = "Python"
# 正值索引
print(" string[0] = ", string[0],
      "\n string[1] = ", string[1],
      "\n string[2] = ", string[2],
      "\n string[3] = ", string[3],
      "\n string[4] = ", string[4],
      "\n string[5] = ", string[5])
# 負值索引
print(" string[-1] = ", string[-1],
      "\n string[-2] = ", string[-2],
      "\n string[-3] = ", string[-3],
      "\n string[-4] = ", string[-4],
      "\n string[-5] = ", string[-5],
      "\n string[-6] = ", string[-6])
# 多重指定觀念
s1, s2, s3, s4, s5, s6 = string
print("多重指定觀念的輸出測試 = ",s1,s2,s3,s4,s5,s6)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_40.py

# ch6_40.py
string = "Deep Learning"                # 定義字串
print("列印string第1-3元素     = ", string[0:3])
print("列印string第2-4元素     = ", string[1:4])
print("列印string第2,4,6元素   = ", string[1:6:2])
print("列印string第1到最後元素 = ", string[1:])
print("列印string前3元素       = ", string[0:3])
print("列印string後3元素       = ", string[-3:])

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41.py

# ch6_41.py
string = "Deep Learning"                # 定義字串
strlen = len(string)
print("字串長度", strlen)
maxstr = max(string)
print("字串最大的unicode碼值和字元", ord(maxstr), maxstr)
minstr = min(string)
print("字串最小的unicode碼值和字元", ord(minstr), minstr)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41_1.py

# ch6_41_1.py
str1 = "Silicon Stone Education"
str2 = "DeepStone"
str3 = "深石數位"

sList1 = str1.split()                       # 字串轉成串列
sList2 = str2.split()                       # 字串轉成串列
sList3 = str3.split()                       # 字串轉成串列
print(str1, " 串列內容是 ", sList1)         # 列印串列
print(str1, " 串列字數是 ", len(sList1))    # 列印字數
print(str2, " 串列內容是 ", sList2)         # 列印串列
print(str2, " 串列字數是 ", len(sList2))    # 列印字數
print(str3, " 串列內容是 ", sList3)         # 列印串列
print(str3, " 串列字數是 ", len(sList3))    # 列印字數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41_2.py

# ch6_41_2.py
msg = """CIA Mark told CIA Linda that the secret USB
had given to CIA Peter"""
print("字串開頭是CIA: ", msg.startswith("CIA"))
print("字串結尾是CIA: ", msg.endswith("CIA"))
print("CIA出現的次數: ",msg.count("CIA"))

print("------------------------------------------------------------")  # 60個

x = 10
y = 10
z = 15
r = 20
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))
r = x                               # r的值將變為10
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))

print("------------------------------------------------------------")  # 60個

x = 10
y = 10
z = 15
r = z - 5
boolean_value = x is y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d, " % (x, y), boolean_value)

boolean_value = x is z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d, " % (x, z), boolean_value)

boolean_value = x is r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d, " % (x, r), boolean_value)

boolean_value = x is not y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d, " % (x, y), boolean_value)

boolean_value = x is not z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d, " % (x, z), boolean_value)

boolean_value = x is not r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d, " % (x, r), boolean_value)

print("------------------------------------------------------------")  # 60個

mysports = ['basketball', 'baseball']
sports1 = mysports          # 拷貝位址
sports2 = mysports[:]       # 拷貝新串列
print("我喜歡的運動 = ", mysports, "位址是 = ", id(mysports))
print("運動 1       = ", sports1,  "位址是 = ", id(sports1))
print("運動 2       = ", sports2,  "位址是 = ", id(sports2))
boolean_value = mysports is sports1
print("我喜歡的運動 is 運動 1     = ", boolean_value)

boolean_value = mysports is sports2
print("我喜歡的運動 is 運動 2     = ", boolean_value)

boolean_value = mysports is not sports1
print("我喜歡的運動 is not 運動 1 = ", boolean_value)

boolean_value = mysports is not sports2
print("我喜歡的運動 is not 運動 2 = ", boolean_value)

print("------------------------------------------------------------")  # 60個

drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)        # 數值初始是0
print(enumerate_drinks)                     # 傳回enumerate物件所在記憶體
print("下列是輸出enumerate物件類型")
print(type(enumerate_drinks))               # 列出物件類型

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_48.py

# ch6_48.py
drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)                # 數值初始是0
print("轉成串列輸出, 初始值是 0 = ", list(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)    # 數值初始是10
print("轉成串列輸出, 初始值是10 = ", list(enumerate_drinks))

print("------------------------------------------------------------")  # 60個

players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:
    print(player)
   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_4.py

# ch7_4.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_5.py

# ch7_5.py
players = ['curry', 'jordan', 'james', 'durant', 'obama']
for player in players:
    print(player.title( ) + ", it was a great game.")
    print("I can not wait to see your next game, " + player.title( ))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_6.py

# ch7_6.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
print("列印前3位球員")
for player in players[:3]:
    print(player)
print("列印後3位球員")
for player in players[-3:]:
    print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_7.py

# ch7_7.py
n = 5
number1 = list(range(n))
print("當n值是%d時的range( )串列 = " % n, number1)
n = 8
number2 = list(range(n))
print("當n值是%d時的range( )串列 = " % n, number2)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_8.py

# ch7_8.py
n = 5
print("當n值是%d時的range( )串列元素:" % n)
for number in range(n):
    print(number)
n = 8
print("當n值是%d時的range( )串列元素:" % n)
for number in range(n):
    print(number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_9.py

# ch7_9.py
start = 2
end = 6
number1 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number1)
start = -2
end = 3
number2 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number2)
start = -5
end = -1
number3 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number3)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_10.py

# ch7_10.py
start = 2
end = 6
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)
start = -2
end = 3
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)
start = -5
end = -1
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_11.py

# ch7_11.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number1)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number2)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_12.py

# ch7_12.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)

print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))
total = sum(number)
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))
total = sum(number)
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))       # 建立串列
total = 0                         # 總計
for i in number:
    total += i
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
total = 0                         # 總計
for i in range(1, n+1):
    total += i
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

squares = []                     # 建立空串列
n = 100
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    value = num * num            # 元素平方
    squares.append(value)        # 加入串列
print(squares)

print("------------------------------------------------------------")  # 60個

squares = []                     # 建立空串列
n = 100
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    squares.append(num ** 2)     # 加入串列
print(squares)

print("------------------------------------------------------------")  # 60個

n = 100
if n > 10 : n = 10               # 最大值是10
squares = [num ** 2 for num in range(1, n+1)]
print(squares)

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
    print()         # 換行輸出
    

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("aa", end="")
    print()                # 換行輸出
    

print("------------------------------------------------------------")  # 60個

print("測試1")
for digit in range(1, 11):
    if digit == 5:
        break
    print(digit, end=', ')
print( )
print("測試2")
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end=', ')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_22.py

# ch7_22.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = 10
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index += 1                          # 索引加1

print("------------------------------------------------------------")  # 60個

players = [['James', 202],
           ['Curry', 193],
           ['Durant', 205],
           ['Jordan', 199],
           ['David', 211]]
for player in players:
    if player[1] < 200:
        continue
    print(player)

print("------------------------------------------------------------")  # 60個

print("請輸入大於1的整數做質數測試 = 119")

num = 119

if num == 2:                                # 2是質數所以直接輸出
    print("%d是質數" % num)
else:
    for n in range(2, num):                 # 用2 .. num-1當除數測試
        if num % n == 0:                    # 如果整除則不是質數
            print("%d不是質數" % num)
            break                           # 離開迴圈
    else:                                   # 否則是質數
        print("%d是質數" % num)

print("------------------------------------------------------------")  # 60個

i = 1                   # 設定i初始值
while i <= 9:           # 當i大於9跳出外層迴圈
    j = 1               # 設定j初始值
    while j <= 9:       # 當j大於9跳出內層迴圈
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
        j += 1          # 內層迴圈加1
    print()             # 換行輸出
    i += 1              # 外層迴圈加1

print("------------------------------------------------------------")  # 60個

players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = 5
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引index
while index < len(players):             # 是否index在串列長度範圍
    if index == n:                      # 是否達到想列出的人數
        break
    print(players[index], end=" ")
    index += 1                          # 索引index加1

print("------------------------------------------------------------")  # 60個

index = 0
while index <= 10:
    index += 1
    if ( index % 2 != 0 ):  # 測試是否奇數
        continue            # 不往下執行
    print(index)            # 輸出偶數
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_35.py

# ch7_35.py
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']
fruit = 'apple'
print("刪除前的fruits", fruits)
while fruit in fruits:      # 只要串列內有apple迴圈就繼續
    fruits.remove(fruit)
print("刪除後的fruits", fruits)

print("------------------------------------------------------------")  # 60個

buyers = [['James', 1030],              # 建立買家購買紀錄
           ['Curry', 893],
           ['Durant', 2050],
           ['Jordan', 990],
           ['David', 2110]]
goldbuyers = []                         # Gold買家串列
vipbuyers =[]                           # VIP買家串列
while buyers:                           # 執行買家分類迴圈分類完成迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 1000:          # 用1000圓執行買家分類條件
        vipbuyers.append(index_buyer)   # 加入VIP買家串列
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)

print("------------------------------------------------------------")  # 60個

drinks = ["coffee", "tea", "wine"]

# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)

print("****************")   

# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)

print("------------------------------------------------------------")  # 60個

numbers1 = (1, 2, 3, 4, 5)      # 定義元組元素是整數
fruits = ('apple', 'orange')    # 定義元組元素是字串
mixed = ('James', 50)           # 定義元組元素是不同型態資料
val_tuple = (10,)               # 只有一個元素的元祖
print(numbers1)
print(fruits)
print(mixed)
print(val_tuple)
# 列出元組資料型態
print("元組mixed資料型態是: ",type(mixed))

print("------------------------------------------------------------")  # 60個

numbers1 = (1, 2, 3, 4, 5)      # 定義元組元素是整數
fruits = ('apple', 'orange')    # 定義元組元素是字串
val_tuple = (10,)               # 只有一個元素的元祖
print(numbers1[0])              # 以中括號索引值讀取元素內容
print(numbers1[4])
print(fruits[0],fruits[1])
print(val_tuple[0])
x, y = ('apple', 'orange')      # 有趣的應用也可以用x,y=fruits
print(x,y)

print("------------------------------------------------------------")  # 60個

keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
for key in keys:
    print(key)

print("------------------------------------------------------------")  # 60個

fruits = ('apple', 'orange')        # 定義元組元素是水果
print("原始fruits元組元素")
for fruit in fruits:
    print(fruit)

fruits = ('watermelon', 'grape')    # 定義新的元組元素
print("\n新的fruits元組元素")
for fruit in fruits:
    print(fruit)

print("------------------------------------------------------------")  # 60個

fruits = ('apple', 'orange', 'banana', 'watermelon', 'grape')
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
print(fruits[-2:])
print(fruits[0:5:2])

print("------------------------------------------------------------")  # 60個

keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
print("keys元組長度是 %d " % len(keys))

print("------------------------------------------------------------")  # 60個

keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
list_keys = list(keys)              # 將元組改為串列
list_keys.append('secret')          # 增加元素
print("列印元組", keys)
print("列印串列", list_keys)

print("------------------------------------------------------------")  # 60個

keys = ['magic', 'xaab', 9099]      # 定義串列元素是字串與數字
tuple_keys = tuple(keys)            # 將串列改為元組
print("列印串列", keys)
print("列印元組", tuple_keys)

print("------------------------------------------------------------")  # 60個

tup = (1, 3, 5, 7, 9)
print("tup最大值是", max(tup))
print("tup最小值是", min(tup))

print("------------------------------------------------------------")  # 60個

drinks = ("coffee", "tea", "wine")
enumerate_drinks = enumerate(drinks)                # 數值初始是0
print("轉成元組輸出, 初始值是 0 = ", tuple(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)    # 數值初始是10
print("轉成元組輸出, 初始值是10 = ", tuple(enumerate_drinks))

print("------------------------------------------------------------")  # 60個

drinks = ("coffee", "tea", "wine")
# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")   
# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)

print("------------------------------------------------------------")  # 60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列

f, i = zip(*player)                 # 執行unzip
print("fields = ", f)
print("info   = ", i)

print("------------------------------------------------------------")  # 60個

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
del fruits['西瓜']
print("新fruits字典內容:", fruits)
   

print("------------------------------------------------------------")  # 60個

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
fruits.clear( )
print("新fruits字典內容:", fruits)
 

print("------------------------------------------------------------")  # 60個

soldier0 = {}           # 建立空字典
print("空小兵字典", soldier0)
soldier0['tag'] = 'red'
soldier0['score'] = 3
print("新小兵字典", soldier0)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_13.py

# ch9_13.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
cfruits = fruits.copy( )
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_14.py

# ch9_14.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
empty_dict = {}
print("fruits字典元素數量     = ", len(fruits))
print("noodles字典元素數量    = ", len(noodles))
print("empty_dict字典元素數量 = ", len(empty_dict))

print("------------------------------------------------------------")  # 60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
print("Stephen Curry是 %s 的球員" % players['Stephen Curry'])
print("Kevin Durant是 %s 的球員" % players['Kevin Durant'])
print("Paul Gasol是 %s 的球員" % players['Paul Gasol']) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_17.py

# ch9_17.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name, team in players.items( ):
    print("\n姓名: ", name)
    print("隊名: ", team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_18.py

# ch9_18.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in players.keys( ):
    print("姓名: ", name)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_19.py

# ch9_19.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in players:
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_20.py

# ch9_20.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in sorted(players.keys( )):
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_21.py

# ch9_21.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for team in players.values( ):
    print(team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_21_1.py

# ch9_21_1.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for team in set(players.values( )):
    print(team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_22.py

# ch9_22.py
soldier0 = {'tag':'red', 'score':3, 'speed':'slow'}         # 建立小兵
soldier1 = {'tag':'blue', 'score':5, 'speed':'medium'}
soldier2 = {'tag':'green', 'score':10, 'speed':'fast'}
armys = [soldier0, soldier1, soldier2]                      # 小兵組成串列
for army in armys:                                          # 列印小兵
    print(army)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_23.py

# ch9_23.py
armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
for soldier in armys[:3]:
    print(soldier)
# 列印小兵數量
print("小兵數量 = ", len(armys))

print("------------------------------------------------------------")  # 60個

armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'blue'
        soldier['score'] = 5
        soldier['speed'] = 'medium'
# 列印編號35到40的小兵
print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)

print("------------------------------------------------------------")  # 60個

# 建立內含字串的字典
sports = {'Curry':['籃球', '美式足球'],
          'Durant':['棒球'],
          'James':['美式足球', '棒球', '籃球']}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items( ):
          print("%s 喜歡的運動是: " % name)
# 列印value,這是串列
          for sport in favorite_sport:
              print("   ", sport)

print("------------------------------------------------------------")  # 60個

# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印內含字典的字典
for account, account_info in wechat_account.items( ):
    print("使用者帳號 = ", account)                   # 列印鍵(key)
    name = account_info['last_name'] + " " + account_info['first_name']
    print("姓名       = ", name)                      # 列印值(value)
    print("城市       = ", account_info['city'])      # 列印值(value)


print("------------------------------------------------------------")  # 60個

# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印字典元素個數
print("wechat_account字典元素個數       ", len(wechat_account))
print("wechat_account['cshung']元素個數 ", len(wechat_account['cshung']))
print("wechat_account['kevin']元素個數  ", len(wechat_account['kevin']))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_29.py

# ch9_29.py
# 將串列轉成字典
seq1 = ['name', 'city']         # 定義串列
list_dict1 = dict.fromkeys(seq1)
print("字典1 ", list_dict1)
list_dict2 = dict.fromkeys(seq1, 'Chicago')
print("字典2 ", list_dict2)
# 將元組轉成字典
seq2 = ['name', 'city']         # 定義元組
tup_dict1 = dict.fromkeys(seq2)
print("字典3 ", tup_dict1)
tup_dict2 = dict.fromkeys(seq2, 'New York')
print("字典4 ", tup_dict2)

print("------------------------------------------------------------")  # 60個

fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print("Value = ", ret_value1)
ret_value2 = fruits.get('Grape')
print("Value = ", ret_value2)
ret_value3 = fruits.get('Grape', 10)
print("Value = ", ret_value3)

print("------------------------------------------------------------")  # 60個

langs = {'Python', 'C', 'Java', 'Python', 'C'}
print(type(langs))
print(langs)

print("------------------------------------------------------------")  # 60個

# 集合由整數所組成
integer_set = {1, 2, 3, 4, 5}
print(integer_set)
# 集合由不同資料型態所組成
mixed_set = {1, 'Python', (2, 5, 10)}
print(mixed_set)
# 集合的元素是不可變的所以程式第6行所設定的元組元素改成
# 第10行串列的寫法將會產生錯誤
# mixed_set = { 1, 'Python', [2, 5, 10]}

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_4.py

# ch10_4.py
x = {}                      # 這是建立空字典非空集合
print("列印     = ", x)
print("列印類別 = ", type(x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_5.py

# ch10_5.py
empty_dict = {}                      # 這是建立空字典
print("列印類別 = ", type(empty_dict))
empty_set = set()                    # 這是建立空集合
print("列印類別 = ", type(empty_set))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_6.py

# ch10_6.py
x = set('DeepStone mean Deep Learning')
print(x)
print(type(x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_7.py

# ch10_7.py
# 表達方式1
fruits = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits)
print(x)
# 表達方式2
y = set(['apple', 'orange', 'apple', 'banana', 'orange'])
print(y)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_8.py

# ch10_8.py
cities = set(('Beijing', 'Tokyo', 'Beijing', 'Taipei', 'Tokyo'))
print(cities)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_9.py

# ch10_9.py
fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列
print("原先串列資料fruits1 = ", fruits1)
print("新的串列資料fruits2 = ", fruits2)

print("------------------------------------------------------------")  # 60個

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both = math & physics
print("同時參加數學與物理夏令營的成員 ",both)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}         # 定義集合A
B = {3, 4, 5, 6, 7}         # 定義集合B
# 將intersection( )應用在A集合
AB = A.intersection(B)      # A和B的交集
print("A和B的交集是 ", AB)
# 將intersection( )應用在B集合
BA = B.intersection(A)      # B和A的交集
print("B和A的交集是 ", BA)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_12.py

# ch10_12.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember = math | physics
print("同時參加數學與物理夏令營的成員 ",allmember)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}             # 定義集合A
B = {3, 4, 5, 6, 7}             # 定義集合B
# 將union( )應用在A集合
AorB = A.union(B)               # A和B的聯集
print("A和B的聯集是 ", AorB)    
# 將union( )應用在B集合
BorA = B.union(A)               # B和A的聯集
print("B和A的聯集是 ", BorA)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_14.py

# ch10_14.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_only = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only)
physics_only = physics - math
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",physics_only)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}             # 定義集合A
B = {3, 4, 5, 6, 7}             # 定義集合B
# 將difference( )應用在A集合
A_B = A.difference(B)           # A-B的差集
print("A-B的差集是 ", A_B)    
# 將difference( )應用在B集合
B_A = B.difference(A)           # B-A的差集
print("B-A的差集是 ", B_A)

print("------------------------------------------------------------")  # 60個

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_physics = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
# 將symmetric_difference( )應用在A集合
A_sydi_B = A.symmetric_difference(B)    # A和B的對稱差集
print("A和B的對稱差集是 ", A_sydi_B)    
# 將symmetric_difference( )應用在B集合
B_sydi_A = B.symmetric_difference(A)    # B和A的對稱差集
print("B和A的對稱差集是 ", B_sydi_A)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                              
print("A與B集合相等", A == B)
# 列出A與C集合是否相等                             
print("A與C集合相等", A == C)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                             
print("A與B集合不相等", A != B)
# 列出A與C集合是否不相等                              
print("A與C集合不相等", A != C)          

print("------------------------------------------------------------")  # 60個

# 方法1
fruits = set("orange")
print("字元a是屬於fruits集合?", 'a' in fruits)
print("字元d是屬於fruits集合?", 'd' in fruits)
# 方法2
cars = {"Nissan", "Toyota", "Ford"}
boolean = "Ford" in cars
print("Ford in cars", boolean)
boolean = "Audi" in cars
print("Audi in cars", boolean)

print("------------------------------------------------------------")  # 60個

# 方法1
fruits = set("orange")
print("字元a是不屬於fruits集合?", 'a' not in fruits)
print("字元d是不屬於fruits集合?", 'd' not in fruits)
# 方法2
cars = {"Nissan", "Toyota", "Ford"}
boolean = "Ford" not in cars
print("Ford not in cars", boolean)
boolean = "Audi" not in cars
print("Audi not in cars", boolean)

print("------------------------------------------------------------")  # 60個

def greeting( ):
    """我的第一個Python函數設計"""
    print("Python歡迎你")
    print("祝福學習順利")
    print("謝謝")

# 以下的程式碼也可稱主程式
greeting( )
greeting( )
greeting( )
greeting( )
greeting( )


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_2.py

# ch11_2.py
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi,", name, "Good Morning!")
greeting('Nelson')

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")
greeting('Nelson')

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")

print("------------------------------------------------------------")  # 60個

def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest('旅遊', '敦煌')
interest('程式設計', 'Python')

print("------------------------------------------------------------")  # 60個

def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest(interest_type = '旅遊', subject = '敦煌')  # 位置正確
interest(subject = '敦煌', interest_type = '旅遊')  # 位置更動

print("------------------------------------------------------------")  # 60個

def interest(interest_type, subject = '敦煌'):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest('旅遊')                                     # 傳遞一個參數
interest(interest_type = '旅遊')                     # 傳遞一個參數
interest('旅遊', '張家界')                           # 傳遞二個參數
interest(interest_type = '旅遊', subject = '張家界') # 傳遞二個參數
interest(subject = '張家界', interest_type = '旅遊') # 傳遞二個參數
interest('閱讀', '旅遊類')                # 傳遞二個參數,不同的主題

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")

ret_value = greeting('Nelson')
print("greeting( )傳回值 = ", ret_value)
print(ret_value, " 的 type  = ", type(ret_value))

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    return                      # Python將自動回傳None
ret_value = greeting('Nelson')
print("greeting( )傳回值 = ", ret_value)
print(ret_value, " 的 type  = ", type(ret_value))

print("------------------------------------------------------------")  # 60個

def mutifunction(x1, x2):
    """ 加, 減, 乘, 除四則運算 """
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2
    return addresult, subresult, mulresult, divresult

x1 = x2 = 10
add, sub, mul, div = mutifunction(x1, x2)
print("加法結果 = ", add)
print("減法結果 = ", sub)
print("乘法結果 = ", mul)
print("除法結果 = ", div)

print("------------------------------------------------------------")  # 60個

def guest_info(firstname, middlename, lastname, gender):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎妳'
    return welcome

info1 = guest_info('宇', '星', '洪', 'M')
info2 = guest_info('雨', '冰', '洪', 'F')
print(info1)
print(info2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_15.py

# ch11_15.py
def guest_info(firstname, lastname, gender, middlename = ''):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎妳'
    return welcome

info1 = guest_info('濤', '劉', 'M')
info2 = guest_info('雨', '洪', 'F', '冰')
print(info1)
print(info2)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_16.py

# ch11_16.py
def build_vip(id, name):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    return vip_dict

member = build_vip('101', 'Nelson')
print(member)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_17.py

# ch11_17.py
def build_vip(id, name, tel = ''):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict

member1 = build_vip('101', 'Nelson')
member2 = build_vip('102', 'Henry', '0952222333')
print(member1)
print(member2)


print("------------------------------------------------------------")  # 60個

def product_msg(customers):
    str1 = '親愛的: '
    str2 = '本公司將在2020年12月20日北京舉行產品發表會'
    str3 = '總經理:深石敬上'
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')

members = ['Damon', 'Peter', 'Mary']
product_msg(members)

print("------------------------------------------------------------")  # 60個

def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

unserved = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served = []                                       # 已服務餐點

# 列出餐廳處理前的點餐內容
show_unserved_meal(unserved)                      # 列出未服務餐點
show_served_meal(served)                          # 列出已服務餐點

# 餐廳服務過程
kitchen(unserved, served)                         # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_unserved_meal(unserved)                      # 列出未服務餐點
show_served_meal(served)                          # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_21.py

# ch11_21.py
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served_list = []                                    # 已服務餐點

# 列出餐廳處理前的點餐內容
show_unserved_meal(order_list)                      # 列出未服務餐點
show_served_meal(served_list)                       # 列出已服務餐點

# 餐廳服務過程
kitchen(order_list, served_list)                    # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_unserved_meal(order_list)                      # 列出未服務餐點
show_served_meal(served_list)                       # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_22.py

# ch11_22.py
def kitchen(unserved, served):
    """ 將所點的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_order_meal(unserved):
    """ 顯示所點的餐點 """
    print("=== 下列是所點的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served_list = []                                    # 已服務餐點

# 列出餐廳處理前的點餐內容
show_order_meal(order_list)                         # 列出所點的餐點
show_served_meal(served_list)                       # 列出已服務餐點

# 餐廳服務過程
kitchen(order_list[:], served_list)                 # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_order_meal(order_list)                         # 列出所點的餐點
show_served_meal(served_list)                       # 列出已服務餐點

print("------------------------------------------------------------")  # 60個

def make_icecream(*toppings):
    # 列出製作冰淇淋的配料
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_24.py

# ch11_24.py
def make_icecream(icecream_type, *toppings):
    # 列出製作冰淇淋的配料
    print("這個 ", icecream_type, " 冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('香草', '草莓醬')
make_icecream('芒果', '草莓醬', '葡萄乾', '巧克力碎片')

print("------------------------------------------------------------")  # 60個

def build_dict(name, age, **players):
    # 建立NBA球員的字典資料
    info = {}           # 建立空字典
    info['Name'] = name
    info['Age'] = age
    for key, value in players.items( ):
        info[key] = value
    return info         # 回傳所建的字典

player_dict = build_dict('James', '32',
                         City = 'Cleveland',
                         State = 'Ohio')

print(player_dict)      # 列印所建字典

print("------------------------------------------------------------")  # 60個

def factorial(n):
    # 計算n的階乘, n 必須是正整數
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

value = 3
print(value, " 的階乘結果是 = ", factorial(value))
value = 5
print(value, " 的階乘結果是 = ", factorial(value))

print("------------------------------------------------------------")  # 60個

def printmsg( ):
    # 函數本身沒有定義變數, 只有執行列印全域變數功能
    print("函數列印: ", msg)    # 列印全域變數

msg = 'Global Variable'         # 設定全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數

print("------------------------------------------------------------")  # 60個

print("111")
def printmsg( ):
    # 函數本身有定義變數, 將執行列印區域變數功能
    msg = 'Local Variable'      # 設定區域變數
    print("函數列印: ", msg)    # 列印區域變數

msg = 'Global Variable'         # 這是全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數

print("------------------------------------------------------------")  # 60個

print("222")
def defmsg( ):
    msg = 'pringmsg variable'

def printmsg( ):
    print(msg)      # 列印defmsg( )函數定義的區域變數

printmsg( )         # 呼叫printmsg( )

print("------------------------------------------------------------")  # 60個

print("333")

def defmsg( ):
    msg = 'pringmsg variable'

print(msg)         # 主程式列印區域變數產生錯誤

print("------------------------------------------------------------")  # 60個

def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print("更改後: ", msg)
msg = "Python"
print("更改前: ", msg)
printmsg()

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
square = lambda x: x ** 2

# 輸出平方值
print(square(10))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_32.py

# ch11_32.py
# 使用一般函數
def square(x):
    value = x ** 2
    return value

# 輸出平方值
print(square(10))

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
product = lambda x, y: x * y

# 輸出相乘結果
print(product(5, 10))

print("------------------------------------------------------------")  # 60個

def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object

# 輸出奇數串列
print("奇數串列: ",[item for item in filter_object])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_35.py

# ch11_35.py
def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object
oddlist = [item for item in filter_object]
# 輸出奇數串列
print("奇數串列: ",oddlist)

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

oddlist = list(filter(lambda x: (x % 2 == 1), mylist))

# 輸出奇數串列
print("奇數串列: ",oddlist)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_37.py

# ch11_37.py
mylist = [5, 10, 15, 20, 25, 30]

squarelist = list(map(lambda x: x ** 2, mylist))

# 輸出串列元素的平方值
print("串列的平方值: ",squarelist)

print("------------------------------------------------------------")  # 60個

def fun(arg):
    pass

print("------------------------------------------------------------")  # 60個

def fun(arg):
    pass

print("列出fun的type類型   :      ", type(fun))
print("列出lambda的type類型:      ", type(lambda x:x))
print("列出內建函數abs的type類型: ", type(abs))

print("------------------------------------------------------------")  # 60個

print("目前Python版本是: ", sys.version)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print( bool(0) )
print( bool("") )
print( bool(" ") )
print( bool(1) )
print( bool("XYZ") )

print("------------------------------------------------------------")  # 60個

num=123
print(num)
num1=bin(num) #2進位
print(num1)
num2=oct(num) #8進位
print(num2)

num3=1234
print(num3)
print(int(num1,2)) #將2進位的字串轉換成10進位數值
print(int(num2,8)) #將8進位的字串轉換成10進位數值
#print(int(num3,16))#將16進位的字串轉換成10進位數值 fail in sugar

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\change.py

str = "{1} * {0} = {2}"
a = 3
b = "5"
print(str.format(a, b, a * int(b)))

print("------------------------------------------------------------")  # 60個

year=2024
month=1
day=20
print("日期：%s-%s-%s" %(year, month, day))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\digit.py

print("請輸入一個十進位數: ",end="")
Val=1234
print("Val的八進位數=%o" %Val)#以%o格式化字元輸出
print("Val的十六進位數=%x" %Val)#以%x格式化字元輸出 

print("------------------------------------------------------------")  # 60個

company="藍海科技股份有限公司"
year=27
print("{}已成立公司 {} 年" .format (company, year))

print("------------------------------------------------------------")  # 60個

print("{0:10}收入：{1:_^12}".format("Axel", 52000))
print("{0:10}收入：{1:>12}".format("Michael", 87000))
print("{0:10}收入：{1:*<12}".format("May", 36000))

print("------------------------------------------------------------")  # 60個

num = 168
print ("數字 %s 的浮點數：%5.1f" % (num,num))
print ("數字 %s 的八進位：%o" % (num,num))
print ("數字 %s 的十六進位：%x" % (num,num))
print ("數字 %s 的二進位：%s" % (num,bin(num)))

print("------------------------------------------------------------")  # 60個

print("編號 姓名    底薪  業務獎金 加給補貼")
print("%3d %3s %6d %6d %6d" %(801,"朱正富",32000,10000,5000))
print("%3d %3s %6d %6d %6d" %(805,"曾自強",35000,8000,7000))
print("%3d %3s %6d %6d %6d" %(811,"陳威動",43000,15000,6000))

print("------------------------------------------------------------")  # 60個

print("13579")
print("1+2")
print("Hello, how are you?")
print("I'm all right, but it's raining.")
print('I\'m all right, but it\'s raining.')

print("------------------------------------------------------------")  # 60個

print(type(23))  #輸出結果 <class 'int'>
print(type(3.14)) #輸出結果 <class 'float'>
print(type("happy birthday")) #輸出結果 <class 'str'>
print(type(True)) #輸出結果 <class 'bool'>

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\variable.py

num1=30
print(num1)
num1="happy"
print(num1)
a=b=12
print(a,b)
name,salary,weight="陳大富",60000,85.7
print(name,salary,weight)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\bit_op.py

x = 15; y = 10
print(x & y)  
print(x ^ y)   
print(x | y)  
print(~x)

print("------------------------------------------------------------")  # 60個

a=19; b=13 
#比較運算子運算關係
print("a=%d b=%d " %(a,b))
print("--------------------------------")
print("a>b,比較結果為 %d 值" %(a>b))
print("a<b,比較結果為 %d 值" %(a<b))
print("a>=b,比較結果為 %d 值" %(a>=b))
print("a<=b,比較結果為 %d 值" %(a<=b))
print("a==b,比較結果為 %d 值" %(a==b))
print("a!=b,比較結果為 %d 值" %(a!=b))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\compound.py

num=8
num*=9
print(num)
num+=1
print(num)
num//=9
print(num)
num %= 5
print(num)
num -= 2
print(num)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\cost.py

x=(765/17+1)*2*210;
print("共需花費: %d 元" %x)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\logic.py

a,b,c=5,10,6
result = a>b and b>c;   #條件式a>b的傳回值與條件式b>c的傳回值做and運算
result = a<b or c!=a;   #條件式a<b的傳回值與條件式c!=a的傳回值做or運算
result = not result;	#將result的值做not運算

print("------------------------------------------------------------")  # 60個

a,b,c=3,5,7 #宣告a、b及c三個整數變
print("a= %d b= %d c= %d" %(a,b,c))
print("====================================")
print("a<b and b<c or c<a = %d" %(a<b and b<c or c<a))
print("not(a==b)and (not a<b) = %d" %(not(a==b)and (not a<b)))
#包含關係與邏輯運算子的運算式求值

print("------------------------------------------------------------")  # 60個

b = 13
print(b << 2)
print(b >> 1)

print("------------------------------------------------------------")  # 60個

phrase = ["三陽開泰", "事事如意", "五福臨門"]
for index, x in enumerate(phrase):
    print ("{0}--{1}".format(index, x))

print("------------------------------------------------------------")  # 60個

for a in range(1,6): #外層for迴圈控制
    for b in range(1,a+1): #內層for迴圈控制
        if b==4:
            break
        print(b,end="") #印出b的值
    print()

print("------------------------------------------------------------")  # 60個

total=0
for count in range(1, 100, 2): 
    total += count #將數值累加
print("數值1~100之間的奇數累計=",total)

print("------------------------------------------------------------")  # 60個

k=20
sigma=0
for n in range(int(k)+1):
    if(n % 2!=0): #如果n是奇數
        sigma += float(-1/(2*n+1))
    else:  #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))

print("------------------------------------------------------------")  # 60個

#不一樣
k = 20
sigma = 0
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

for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\while.py

x, y = 1, 10
while x < y:
    print(x, end = ' ')
    x += 1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\align.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExCarry.py

i = 10

for j in range(5):
    z = i + j
    print("小寫：%x\t大寫：%X" %(z, z))

print("------------------------------------------------------------")  # 60個

"""
dictStudent = {}

def isHasKeyAndNotNone():
    findKey = str(input("請輸入欲查詢的key："))
    
    if findKey in dictStudent and dictStudent.get(findKey, None) == None:
        EditData(findKey)
        
    elif findKey in dictStudent and dictStudent.get(findKey, None) != None:
        print("%s的值：%s" %(findKey, dictStudent[findKey]))
        CheckOtherKeyValue()
        
    else:
        dictStudent.setdefault(findKey, None)
        print("%s不存在已自動建立key" %(findKey))

def EditData(findKey):
    strInputValue = str(input("請輸入值："))
    dictStudent[findKey] = strInputValue
    CheckOtherKeyValue()

def CheckOtherKeyValue():
    for key, values in dictStudent.items():
        if values == None:
            print(dictStudent)
            strCheck = str(input("目前還有其他欄位值為None，是否繼續進行編輯(Y/N)："))

            while strCheck == "Y":
                isHasKeyAndNotNone()
            else:
                print(dictStudent)
                break

strFieldName = str(input("請輸入欄位名稱(以逗號分隔)："))
dictStudent = dictStudent.fromkeys(strFieldName.split(","))

isHasKeyAndNotNone()
"""
print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExFloat.py

print("\n不足數位補0：%06.2f\n" %(1.2345))

print("不足數位預設空格：%6.2f\n" %(1.2345))

print("小數點保留2位：%.2f\n" %(1.2345))

print("不足數位補0(以*替代)：%0*.2f\n" %(6, 1.2345))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExInteger.py

print("\n不足數位補0：%05d\n" %(66))

print("不足數位預設空格：%5d\n" %(66))

print("小於位數則輸出全部：%2d\n" %(666))

print("不足數位補0(以*替代)：%0*d\n" %(5, 66))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExList.py

list1 = ["A", True, 10, 3.14, "G"]

for i in range(len(list1)):
   print("索引位置：%s\t對應值：%s\t型態：%s\n" %(i, list1[i], type(list1[i])))

print("------------------------------------------------------------")  # 60個

"""
def EditData():
    if len(strEditTitle) > 0:
        print(strEditTitle)
    else:
        print(strTitle)

    print("作者：", strName)
    print("暱稱：", strId)
    print("Gmail：", strEmail)
    print("興趣：", strJoin)

strTitle = ""
strEditTitle = "撰寫Python小網站"

isEditTitle = str(input("是否要更改名稱(Y/N)："))
isSymbol = str(input("是否要更改前後星號(Y/N)："))

if isEditTitle == "Y" and isSymbol == "Y":
    strEditTitle = str(input("請輸入欲更改名稱："))
    strSymbol = str(input("請輸入欲更改前後符號："))

    strEditTitle = strEditTitle.center(36, strSymbol)
    
elif isEditTitle == "Y" and isSymbol == "N":
    strEditTitle = str(input("請輸入欲更改名稱："))
    strEditTitle = strEditTitle.center(36, "*")

elif isEditTitle == "N" and isSymbol == "Y":
    strSymbol = str(input("請輸入欲更改前後符號："))
    strTitle = strTitle.center(36, strSymbol)

strName = str(input("請輸入名字："))
strId = str(input("請輸入暱稱："))
strEmail = str(input("請輸入Gmail："))

while strEmail.endswith("@gmail.com") == False:
    strEmail = str(input("請重新輸入Gmail："))

strSavor = str(input("你的興趣(以逗號分隔)："))
strJoin = "|".join(strSavor.split(","))


print("="*30, "\n")
EditData()

print("------------------------------------------------------------")  # 60個

tupleData = ()
listData = []

print("\n\n")

strFieldName = str(input("請輸入不可修改欄位名稱(逗號為分隔索引位置；頓號則為放置在同一個索引位置)："))
strFieldData = str(input("請輸入欄位對應資料(逗號為分隔索引位置；頓號則為放置在同一個索引位置)："))

for i in range(len(strFieldName.split(","))):
    listData.append(strFieldName.split(",")[i])
    
for j in range(len(strFieldData.split(","))):
    x = 0

    if len(listData)%2 == 0:
        x = len(listData) - 1
    else:
        x = len(listData) + 1
        
    listData.insert(x, [strFieldData.split(",")[j] for x in range(1)])
    
listToTuple = tuple(listData)
print("\n")
print("list轉換tuple：", listToTuple)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#設置底薪(BaseSalary)、結案獎金件數(Case)、職位獎金(OfficeBonus)
BaseSalary = 25000
CaseBonus = 1000
OfficeBonus = 5000

#請輸入職位名稱(Engineer)、結案獎金金額(CaseAmount)變數
Engineer = str(input("請輸入職位名稱："))
Case = int(input("請輸入結案案件數(整數)："))


#計算獎金function
def CalculateCase(case, caseBonus):
    return case * caseBonus

def CalculateSalary(baseSalary, officeBonus):
    return baseSalary + officeBonus

CaseAmount = CalculateCase(Case, CaseBonus)
SalaryAmount = CalculateSalary(BaseSalary, OfficeBonus)

print("該工程師薪資：", CaseAmount + SalaryAmount)
"""
print("------------------------------------------------------------")  # 60個

import time

t = time.time()
tLocal = time.localtime(t)

print("轉換時間形式(年/月/日)：", time.strftime("%Y/%m/%d", tLocal))
print("轉換時間形式(年/月/日 時:分:秒)：", time.asctime (tLocal))

print("------------------------------------------------------------")  # 60個

# 以 dir() 與 help() 探索 Python 模組與物件

import datetime

print(dir(datetime))

print("")

print([_ for _ in dir(datetime) if "date" in _.lower()])

# help(datetime)

print("------------------------------------------------------------")  # 60個




#syntax
print('顯示模組的所有名稱dir()')
print(dir(random))
print("------------------------------------------------------------")  # 60個


# id的用法

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25, "蘋果": 18}
cfruits = fruits.copy()
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)



print("ccccc")

s1 = "lion"
s2 = "mouse"

print(id(s1))
print(id(s2))

s2 = "lions"

print(id(s1))
print(id(s2))


print('測試 eval()')

numberStr = '12.34*56.78'
print('數值公式 :', numberStr)

number = eval(numberStr)
print("計算結果 : %5.2f" % number)



print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)

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

print(type(23))  #輸出結果 <class 'int'>
print(type(3.14)) #輸出結果 <class 'float'>
print(type("happy birthday")) #輸出結果 <class 'str'>
print(type(True)) #輸出結果 <class 'bool'>

print("------------------------------------------------------------")  # 60個


"""
# python 預設函數

range(0
dir()
help()


"""


"""
type()
int()
float()


"""




print("python之基本函數")
print('int(8.4)=',int(8.4))
print('bin(14)=',bin(14))
#print('hex(84)=',hex(84))
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
#print("str(1234)=", str(1234))
print("sorted([5,7,1,8,9])=", sorted([5, 7, 1, 8, 9]))
print("max(4,6,7,12,3)=", max(4, 6, 7, 12, 3))
print("min(4,6,7,12,3)=", min(4, 6, 7, 12, 3))
print("len([5,7,1,8,9])=", len([5, 7, 1, 8, 9]))

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


number = 3.14159
print("四捨五入到小數點後兩位：", round(number, 4))


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


