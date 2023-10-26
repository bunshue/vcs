import os
import sys
import time
import random
import numpy as np

'''
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


print('---- char ord unicode decode encode --------------------------------------------------------')	#60個

import sys
print('打印出目前系統字符編碼')
print(sys.getdefaultencoding())

print('字元轉unicode')

text = '你'
print('原字串 :', text)
print('Unicode編碼後(10進位) :', ord(text))
print('Unicode編碼後(16進位) :', hex(ord(text)))

print('--------')
"""
#unicode() 不能用
text = '中文 test'
print('原字串 :', text)
print(text, len(text))
#utfstr = unicode(text, 'utf-8')
#-------------
text = 'abcdefg'
print('字串 轉 unicode')
ccc = unicode(text, 'utf-8')
print(ccc)
#-------------
print('unicode 轉 字串')
ddd = str(ccc)
print(ddd)
#-------------
text = "Hello!"
u = unicode(text, "utf-8")
print(u)
#-------------

text = '你好'
text_to_unicode = text.decode(encoding='utf-8')  # 要告訴decode原本的編碼是哪種
print(text_to_unicode)

#text = 'Ribeir\xc3\xa3o Preto'
#print(text.decode('cp1252').encode('utf-8'))

"""
print('--------')

num = 65
print(chr(num)) # 輸出數值num的字元

print('--------')
text = '你好'
print('原字串 :', text)
print('字串 轉 UTF-8 => UTF-8 拜列')
byte_array = text.encode('UTF-8')
print(type(byte_array))
print(byte_array)
print('UTF-8 拜列 轉 字串')
print(byte_array.decode('UTF-8'))
print('--------')
byte_array = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(len(byte_array))
print(byte_array.decode('UTF-8'))

print('--------')
byte_array = b'\xe4\xbd\xa0\xe5\xa5\xbe'
print(len(byte_array))
print(byte_array.decode('UTF-8'))

print('--------')

"""
for i in range(128):
    c = chr(i)
    print(c, end = '')
"""


print('------------------------------------------------------------')	#60個

_b85alphabet = (b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                b"abcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")

_b85chars = [bytes((i,)) for i in _b85alphabet]
print(_b85chars)
print()

_b85chars2 = [(a + b) for a in _b85chars for b in _b85chars]
print(_b85chars2)

print('------------------------------------------------------------')	#60個

print('字串轉拜列')
text = 'lion'
byte_array = repr(text).encode('utf-8') + b'\0'
print(type(byte_array))
print(byte_array)

print('------------------------------------------------------------')	#60個

command1 = 'abcde'
print(type(command1))
print(command1)

command2 = command1.encode()
print(type(command2))
print(command2)

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

import os
print(os.name)

if os.name == 'nt':
    print('Windows NT 系統')
    import nt
    print(sys.getwindowsversion())
    print(sys.getwindowsversion()[:2])
    if sys.getwindowsversion()[:2] >= (6, 0):
        print('Win10')
    else:
        print('非Win10')
else:
    print('非 Windows NT 系統')

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


""" fail in kilo

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

"""


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

import codecs
import contextlib
import io
import locale
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

"""
import time

x = 1000000
pi = 0
time.clock()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.clock()
        print("當 i={:7d} 時 PI={:8.7f}, 所花時間={}".format(i, pi, e_time))
"""

print('------------------------------------------------------------')	#60個

import time
x = 1000000
pi = 0
time.process_time()
for i in range(1, x + 1):
    pi += 4 * ((-1) ** (i + 1) / (2 * i - 1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print("當 i={:7d} 時 PI={:8.7f}, 所花時間={}".format(i, pi, e_time))

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

import copy, random, sys, time

WIDTH = 16
HEIGHT = 8

nextCells = {}  #字典
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = 'Y'
        else:
            nextCells[(x, y)] = 'N'

print(type(nextCells))
print(nextCells)

cells = copy.deepcopy(nextCells)

print('顯示內容')
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(cells[(x, y)], end = '')
    print()

print('------------------------------------------------------------')	#60個

"""
print('Press Ctrl-C to quit.')

while True:
    try:
        time.sleep(1)
        print('A', end = ' ')
    except KeyboardInterrupt:
        print('你按了 ctrl + C, 離開')
        sys.exit()
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('---- os --------------------------------------------------------')	#60個

import test
packagedir = os.path.dirname(test.__file__)

import email
packagedir = os.path.dirname(email.__file__)
print(packagedir)

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

import os
import sys
m = sys.modules.get('__main__')

print(m)

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
'''
print('------------------------------------------------------------')	#60個

import os
print(os.name)
print(os.sys.platform)


print('------------------------------------------------------------')	#60個

for envname in 'TMPDIR', 'TEMP', 'TMP':
    dirname = os.getenv(envname)
    print('cccccc', dirname)
    #print(dirname)

print('------------------------------------------------------------')	#60個

import numpy as np
import pandas as pd

print(np.__version__)

import numpy 
print(numpy.version.version)

#使用 importlib.metadata 模块查找 NumPy 模块的版本
from importlib_metadata import version
print(version('numpy'))

import pkg_resources
print(pkg_resources.get_distribution('numpy').version)


print('查詢已安裝的 Pandas 版本')
print(pd.__version__)

import pandas as pd
print(pd.__version__)

print('------------------------------------------------------------')	#60個

#import this	可以看到 Zen of Python

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



import sys

'''
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
'''
print('------------------------------------------------------------')	#60個

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
'''
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
'''
print('------------------------------------------------------------')	#60個

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
'''
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
'''
print('------------------------------------------------------------')	#60個


import sys, os, time
from stat import *

secs_per_year = 365.0 * 24.0 * 3600.0   # Scale factor
now = time.time()                       # Current time, for age computations

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
    
st = os.lstat(filename)

itime = ST_MTIME
#itime = ST_CTIME
anytime = st[itime]
size = st[ST_SIZE]
age = now - anytime
byteyears = float(size) * float(age) / secs_per_year

print(filename.ljust(50), end=' ')
print(repr(int(byteyears)).rjust(8))

print()

print(filename.ljust(60), end=' ')
print(repr(int(byteyears)).rjust(8))


print('------------------------------------------------------------')	#60個



import os
import sys

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'


short_filename = os.path.basename(filename)

print(short_filename)

cache_dir = os.path.dirname(filename)
print(cache_dir)

head, tail = short_filename[:-3], short_filename[-3:]
print(head)
print(tail)



print('------------------------------------------------------------')	#60個



import sys
import os
    
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

canonic = os.path.abspath(filename)
print(canonic)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
canonic = os.path.normcase(filename)
print(canonic)

print('------------------------------------------------------------')	#60個


import datetime

text = '2012-09-20'
y = datetime.datetime.strptime(text, '%Y-%m-%d')
z = datetime.datetime.now()
diff = z - y
print(diff)

print(z)
nice_z = datetime.datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)


text = '2012-09-20'
year_s, mon_s, day_s = text.split('-')
ttt = datetime.datetime(int(year_s), int(mon_s), int(day_s))
print(ttt)



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('計算字數')

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/alice.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/siddhartha.txt'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/moby_dick.txt'
filename4 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/little_women.txt'

filenames = [filename1, filename2, filename3, filename4]

filename = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

for filename in filenames:
    count_words(filename)

print('------------------------------------------------------------')	#60個


print('統計一個檔案的字數')

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


print('------------------------------------------------------------')	#60個

'''
import numpy as np

N = 10

a = np.arange(N)    #numpy.ndarray

print(type(a))
print(a)

b = range(1, 11)    #range
print(type(b))
print(b)

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

print('取得本程式名稱')
progname = os.path.basename(sys.argv[0])
print(progname)

print('------------------------------------------------------------')	#60個

n = list(range(100))
r = list(range(25))
n = list(range(10)) * 10



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

time.sleep(random.randint(20, 50) / 10.0)

print('------------------------------------------------------------')	#60個

"""
drawTime = time.time()
#等待使用者按鍵輸入
input()  # This function call doesn't return until Enter is pressed.
timeElapsed = time.time() - drawTime

timeElapsed = round(timeElapsed, 4)
print('You took', timeElapsed, 'seconds to draw.')
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


pigLatin = 'this is a lion-mouse'


try:
    pyperclip.copy(pigLatin)
    print('(Copied pig latin to clipboard.)')
except NameError:
    pass  # Do nothing if pyperclip wasn't installed.

print('------------------------------------------------------------')	#60個

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


spongecase = 'this is aaaaaaaaa'

try:
    pyperclip.copy(spongecase)
    print('(cOpIed SpOnGeCasE to ClIpbOaRd.)')
except:
    pass  # Do nothing if pyperclip wasn't installed.

print('------------------------------------------------------------')	#60個


import random

numberOfDice = 5
numberOfSides = 6

# Simulate the dice rolls:
rolls = []
for i in range(numberOfDice):
    rollResult = random.randint(1, numberOfSides)
    rolls.append(rollResult)

print(type(rolls))
print(rolls)

# Display the total:
print('Total:', sum(rolls))


# Display the individual rolls:
for i, roll in enumerate(rolls):
    rolls[i] = str(roll)
print(', '.join(rolls), end='')

'''

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#位元運算子綜合應用
x = 12; y = 8
print(x & y)  
print(x ^ y)   
print(x | y)  
print(~x)

print('------------------------------------------------------------')	#60個

word = ["holiday", "happy", "birth",
             "yesterday", "holiday", "car",
             "yellow", "happy", "mobile",
             "cup", "happy", "holiday",
             "holiday", "desk", "birth",
             ]
print("holiday 出現的次數", word.count("holiday"))

print('------------------------------------------------------------')	#60個

word = ["holiday", "happy", "birth",
             "yesterday", "holiday", "car",
             "yellow", "happy", "mobile",
             "cup", "happy", "holiday",
             "holiday", "desk", "birth",
             ]
search_str="yellow"
print("單字 %s 第一次出現的索引值%d" %(search_str,word.index(search_str)))

print('------------------------------------------------------------')	#60個

info = [['C程式設計','朱大峰','480'],
        ['Python程式設計','吳志明','500'],
        ['Java程式設計','許伯如','540']]

for(book, author,price) in info:
    print('%10s %3s'%(book,author),' 書籍訂價:',price)


info = [['C程式設計','朱大峰','480'],
        ['Python程式設計','吳志明','500'],
        ['Java程式設計','許伯如','540']]

for(book, author,price) in info:
    print('%10s %3s'%(book,author),' 書籍訂價:',price)

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


print('------------------------------------------------------------')	#60個

result = lambda x : 3*x-1  #lambda()函數
print(result(3)) #輸出數值8

print('------------------------------------------------------------')	#60個

def formula(x, y): #自訂函數
    return 3*x+2*y

formula = lambda x, y : 3*x+2*y  #表示lambda有二個參數
print(formula (5,10)) ##傳入兩個數值讓lambda()函數做運算，輸出數值35

result = lambda x : 3*x-1  #lambda()函數
print(result(3)) #輸出數值8

def formula(x, y): #自訂函數
    return 3*x+2*y

formula = lambda x, y : 3*x+2*y  #表示lambda有二個參數
print(formula (5,10)) ##傳入兩個數值讓lambda()函數做運算，輸出數值35

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

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
print('str(1234)=',str(1234))
print('sorted([5,7,1,8,9])=',sorted([5,7,1,8,9]))
print('max(4,6,7,12,3)=',max(4,6,7,12,3))
print('min(4,6,7,12,3)=',min(4,6,7,12,3))
print('len([5,7,1,8,9])=',len([5,7,1,8,9]))

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


try:
    import a_python_module
except ImportError:
    print('匯入模組 a_python_module 失敗')
    print('請安裝模組')
    #sys.exit()


print('------------------------------------------------------------')	#60個

import time, sys

print('Press Ctrl-C to stop.')

try:
    while True:  # Main program loop.
        print('wait', end = ' ')
        time.sleep(1)  # Add a pause.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.



print('------------------------------------------------------------')	#60個


""" 統計亂數
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper  # Flip the case.
"""





print('------------------------------------------------------------')	#60個





print('作業完成')


