import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

print('enumerate 的用法')

print('字串轉串列')
animal_string = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
animal_list = list(animal_string)

for i, ani in enumerate(animal_list):
    print(i, ani)

print("------------------------------------------------------------")  # 60個

print('字串轉串列')
animal_string = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
animal_list = list(animal_string)

print(type(animal_list))

print('字串切片 slicing')

n = 3
m = 9

print('第n個')
cc = animal_list[n]
print(cc)
print('第n個 到 第m-1個')
cc = animal_list[n:m]
print(cc)
print('第n個 到 最後一個')
cc = animal_list[n:]
print(cc)
print('第0個 到 第m-1個')
cc = animal_list[:m]
print(cc)
print('全部')
cc = animal_list[:]
print(cc)
print('反相')
cc = animal_list[::-1]
print(cc)

print("------------------------------------------------------------")  # 60個

"""
import os
import sys

def usage(msg):
    sys.stdout = sys.stderr
    print("Error:", msg)
    print("Use ``%s -h'' for help" % sys.argv[0])

prefix = 'aaaa'
exec_prefix = 'bbbb'
binlib = 'kkkk'
incldir = 'qqqq'

check_dirs = [prefix, exec_prefix, binlib, incldir]
for dir in check_dirs:
    if not os.path.exists(dir):
        usage('needed directory %s not found' % dir)
    if not os.path.isdir(dir):
        usage('%s: not a directory' % dir)

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
    
base = os.path.basename(filename)
base, ext = os.path.splitext(base)

dirname = os.path.dirname(filename)
print(dirname)
"""

print("------------------------------------------------------------")  # 60個

import datetime
now = datetime.datetime.now() # current date and time

date_time = now.strftime('%Y年%m月%d日, %H:%M:%S')
print("現在時間 :", date_time)

import datetime

dt = datetime.datetime(2006, 3, 11, 9, 15),
print(dt)

cc = time.strftime("%Y-%m-%d %H:%M")
print(cc)

cc = time.strftime('%Y-%m-%d %H:%M+%Z')
print(cc)

print("------------------------------------------------------------")  # 60個

import random

NUM_DIGITS = 10

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


secretNum = getSecretNum()
print(secretNum)

print("------------------------------------------------------------")  # 60個

import time
currentTime = time.asctime()

print("時間 :", currentTime)

entrySecond = time.time()
print("時間 :", entrySecond)

print("------------------------------------------------------------")  # 60個

print("檔案或資料夾存在 = ", os.path.exists('ch14'))
print("檔案或資料夾存在 = ", os.path.exists('C:\\_git\\vcs\\_1.data\\______test_files3'))
print("檔案或資料夾存在 = ", os.path.exists('ch14_4.py'))
print(" --- ")

print("是絕對路徑 = ", os.path.isabs('ch14_4.py'))
print("是絕對路徑 = ", os.path.isabs('C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py'))
print(" --- ")

print("是資料夾 = ", os.path.isdir('C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py'))
print("是資料夾 = ", os.path.isdir('C:\\_git\\vcs\\_1.data\\______test_files3'))
print(" --- ")

print("是檔案 = ", os.path.isfile('C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py'))
print("是檔案 = ", os.path.isfile('C:\\_git\\vcs\\_1.data\\______test_files3'))

print("------------------------------------------------------------")  # 60個

newdir = 'C:\\_git\\vcs\\_1.data\\______test_files3'

currentdir = os.getcwd()
print("列出目前工作資料夾 ", currentdir)

# 如果newdir不存在就建立此資料夾
if os.path.exists(newdir):
    print("已經存在 %s " % newdir)
else:
    os.mkdir(newdir)
    print("建立 %s 資料夾成功" % newdir)

# 將目前工作資料夾改至newdir
os.chdir(newdir)
print("列出最新工作資料夾 ", os.getcwd())

# 將目前工作資料夾返回
os.chdir(currentdir)
print("列出返回工作資料夾 ", currentdir)

print("------------------------------------------------------------")  # 60個

files = ['ch14_1.py', 'ch14_2.py', 'ch14_3.py']
for file in files:
    print(os.path.join('C:\\_git\\vcs\\_1.data\\______test_files3', file))   

print("------------------------------------------------------------")  # 60個

for dirName, sub_dirNames, fileNames in os.walk('oswalk'):
    print("目前工作目錄名稱:   ", dirName)
    print("目前子目錄名稱串列: ", sub_dirNames)
    print("目前檔案名稱串列:   ", fileNames, "\n")

print("------------------------------------------------------------")  # 60個

msg = "CIA Mark told CIA Linda that the secret USB had given to CIA Peter"
print("CIA最後出現位置: ", msg.rfind("CIA",0,len(msg)))
print("CIA最後出現位置: ", msg.rfind("CIA"))

print("------------------------------------------------------------")  # 60個

"""
import re
import requests
import bs4

# 馬丁路德 I have a dream
url = 'http://www.analytictech.com/mb021/mlk.htm'
page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
p_elems = [element.text for element in soup.find_all('p')]

speech = ' '.join(p_elems)  # 將段落內容串在一起

# 修正錯字、刪除多餘的空格、移除非字母內容
speech = speech.replace(')mowing', 'knowing')
speech = re.sub('\s+', ' ', speech) 
speech_edit = re.sub('[^a-zA-Z]', ' ', speech)
speech_edit = re.sub('\s+', ' ', speech_edit)

print(speech_edit)
"""
print("------------------------------------------------------------")  # 60個

name = "荀彧"
money = 120

print("%s: %.2f元" % (name, money))

print("------------------------------------------------------------")  # 60個

str1 = "Welcome to the United States and have a nice day"

list1 = str1.split()
print(list1)

str2 = "-".join(list1)
print(str2)

print("------------------------------------------------------------")  # 60個

import traceback                            # 導入taceback

def passWord(pwd):
    #檢查密碼長度必須是5到8個字元
    pwdlen = len(pwd)                       # 密碼長度
    if pwdlen < 5:                          # 密碼長度不足            
        raise Exception('密碼長度不足')
    if pwdlen > 8:                          # 密碼長度太長
        raise Exception('密碼長度太長')
    print('密碼長度正確')

for pwd in ('aaabbbccc', 'aaa', 'aaabbb'):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        errlog = open('tmp_error_text1.txt', 'a')   # 開啟錯誤檔案
        errlog.write(traceback.format_exc())   # 寫入錯誤檔案
        errlog.close()                         # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案 tmp_error_text1.txt 完成")
        print("密碼長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

import traceback

def division(x, y):
    try:                        # try - except指令
        return x / y
    except:                     # 捕捉所有異常
        errlog = open('tmp_error_text2.txt', 'a')   # 開啟錯誤檔案
        errlog.write(traceback.format_exc())   # 寫入錯誤檔案
        errlog.close()                         # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案 tmp_error_text2.txt 完成")
        print("異常發生")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3

print('------------------------------------------------------------')	#60個

"""
std_data = dict()
with open(filename, encoding='utf-8') as fp:
    alldata = fp.readlines()
    for item in alldata:
        no, name = item.rstrip('\n').split(',')
        std_data[no] = name
print(std_data)
"""

print("------------------------------------------------------------")  # 60個

data = b'wxy\x7a'
print(data)               # b'wxyz'，以ASCII字元輸出

print(type(data), type(data[0]))
# <class 'bytes'>, <class 'int'>

print(data[0], hex(data[0]))
# 'w' ASCII碼119，十六進位'0x77'

print(b'\x7a' in data)    # 可以用 in 來判斷
print(data[2:])           # 可以切片

print("------------------------------------------------------------")  # 60個

data = b'wxy\x7a'
print(data)               # b'wxyz'，以ASCII字元輸出

ba = bytearray(data)
print(type(ba), type(ba[0]))
# <class 'bytearray'>, <class 'int'>

ba[3] = 0x70              # 修改資料
print(ba)                 # 變成 bytearray(b'wxyp')

print("------------------------------------------------------------")  # 60個

import time

print('range(5)', range(5))
print('list(range(5))', list(range(5)))

# range
tStart = time.time()
for i in range(10000000):
    pass
tEnd = time.time()
print('range time:', tEnd - tStart)

print("------------------------------------------------------------")  # 60個


def getSevSegStr(number, minWidth=0):
    """Return a seven-segment display string of number. The returned
    string will be padded with zeros if it is smaller than minWidth."""

    # Convert number to string in case it's an int or float:
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':  # Render the decimal point.
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue  # Skip the space in between digits.
        elif numeral == '-':  # Render the negative sign:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # Render the 0.
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # Render the 1.
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # Render the 2.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # Render the 3.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # Render the 4.
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # Render the 5.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':  # Render the 6.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # Render the 7.
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # Render the 8.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # Render the 9.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # Add a space (for the space in between numerals) if this
        # isn't the last numeral and the decimal point isn't next:
        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)

print('七段顯示器')

for i in range(0, 1000, 167):
    ccc = getSevSegStr(i, 5)
    print(ccc)



print("------------------------------------------------------------")  # 60個

st = 10
sp = 20

for number in range(st, sp):  # Main program loop.
    # Convert to hexadecimal/binary and remove the prefix:
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DEC:', number, '   HEX:', hexNumber, '   BIN:', binNumber)

print("------------------------------------------------------------")  # 60個


# 函數文件字串 docstring 註明此函數的功能與用法
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi,", name, "Good Morning!")
greeting('Nelson')


#用help(函數名稱)列出此函數的文件字串

help(greeting)

print("------------------------------------------------------------")  # 60個

# dict01.py

dictBook = {"A001": ["木偶奇遇記", 199], "A002": ["三隻小豬", 120], "A003": ["白雪公主", 99]}
print(dictBook)
# 印出 dictBook所有元素
print("書號A001：", dictBook["A001"])  # 印出dictBook字典鍵A001的值 ['木偶奇遇記', 199]
print("書號A002：", dictBook["A002"])  # 印出dictBook字典鍵A002的值 ['三隻小豬', 120]
print("書號A003：", dictBook["A003"])  # 印出dictBook字典鍵A003的值 ['白雪公主', 99]


print("------------------------------------------------------------")  # 60個

# dict02.py

tupleBookId = ("A001", "A002", "A003")
dictBook = {"A001": ["木偶奇遇記", 199], "A002": ["三隻小豬", 120], "A003": ["白雪公主", 99]}
print("書號\t書名\t單價")
print("========================")

for key in list(tupleBookId):
    print(key, end="\t")
    for col in dictBook[key]:
        print(col, end="\t")
    print()


print("------------------------------------------------------------")  # 60個

# dict03.py

dictBook = {"A001": ["木偶奇遇記", 199]}
print("編輯前字典內容：", dictBook)

dictBook["A002"] = ["三隻小豬", 120]
print("新增後字典內容：", dictBook)

dictBook["A002"] = ["白雪公主", 120]
print("修改後字典內容：", dictBook)

print("是否有書號A001的書籍：", "A001" in dictBook)

del dictBook["A001"]
print("刪除後字典內容：", dictBook)

print("是否有書號A001的書籍：", "A001" in dictBook)


print("------------------------------------------------------------")  # 60個

#一次改變一個數列
celsius = [21, 25, 29]
fahrenheit = [(x * 9 / 5 + 32) for x in celsius]
print(fahrenheit)

print("------------------------------------------------------------")  # 60個

print("列出所有python關鍵字")
import keyword
print(keyword.kwlist)

print("------------------------------------------------------------")  # 60個

import re

files = os.listdir("_data")
txtList = []
# 測試1
pattern = '(.*).txt'
print("列印*.txt")
for filename in files:
    #print(filename)
    fnresult = re.search(pattern,filename)      # 傳回搜尋結果
    if fnresult != None:
        txtList.append(filename)
print(txtList)

pyList = []  
# 測試2
print("列印ch14_10.py - ch14_19.py")
pattern = '(ch14_1(\d).py)'
for filename in files:
    fnresult = re.search(pattern,filename)      # 傳回搜尋結果
    if fnresult != None:
        pyList.append(filename)
print(pyList)

print("------------------------------------------------------------")  # 60個

import re

text = "這個是、那個是、那個是、哪個是"
word1 = "這.是"
word2 = ".個是"

pattern = re.compile(word1)
count = len(re.findall(pattern, text))
print(word1, ":", count, "個")

pattern = re.compile(word2)
count = len(re.findall(pattern, text))
print(word2, ":", count, "個")

print("------------------------------------------------------------")  # 60個

import re

text = "這個是測試資料。"
word1 = ".個是"
word2 = "那個是"

print("置換前 :", text)
pattern = re.compile(word1)
text = re.sub(pattern, word2, text)
print("置換後 :", text)

print("------------------------------------------------------------")  # 60個

"""
localtime()返回元組的日期與時間資料結構 用索引方式獲得個別內容
索引	名稱	說明
0	tm_year	年 	2020
1	tm_mon	月 	1-12
2	tm_mday 日	1-31
3	tm_hour	時	0-23
4	tm_min	分	0-59
5	tm_sec	秒	0-59
6	tm_wday	星期	0:一, 1:二...
7	tm_yday	年第幾天
8	tm_isdst 夏令時間 0:不是, 1:是
"""

import time                         # 導入模組time

xtime = time.localtime()            #使用localtime()方法列出目前時間的結構
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

print("------------------------------------------------------------")  # 60個

print('撈出一層jg檔')
def get_imlist(path):
    """ 返回目錄中所有JPG圖像的文件名列表 """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

foldername = 'C:/_git/vcs/_1.data/______test_files1'

cc = get_imlist(foldername)

print(cc)

print("------------------------------------------------------------")  # 60個

#相同斜率平行移動
import matplotlib.pyplot as plt

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [(2 * y - 2) for y in x]
y3 = [(2 * y + 2) for y in x]
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

#plt.show()

print(x)

print("------------------------------------------------------------")  # 60個


chicken = 20
rabbit = 15
print("雞有 {} 隻, 兔有 {} 隻".format(int(chicken), int(rabbit)))
print("雞有 {} 隻, 兔有 {} 隻".format(chicken, rabbit))


print("------------------------------------------------------------")  # 60個


import glob

print("方法1:列出指定目錄的所有檔案")
for file in glob.glob('C:\\_git\\vcs\\_1.data\\______test_files3\*.*'):
    print(file)
    
print("方法2:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_1*.py'):
    print(file)
    
print("方法3:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_2*.*'):
    print(file)

print("------------------------------------------------------------")  # 60個

import glob

cc = glob.glob(r'C:/_git/vcs/_1.data/______test_files1/*')
print(type(cc))
print(cc)

files = ["da1.c", "da2.py", "da3.py", "da4.java"]
py = []
for file in files:
    if file.endswith(".py"):  # 以.py為副檔名
        py.append(file)  # 加入串列
print(py)


import glob

print(glob.glob(r'./test/*'))         # 找出所有檔案
print(glob.glob(r'./test/*.txt'))     # 找出所有副檔名為 .txt 的檔案，例如 1.txt、hello.txt
print(glob.glob(r'./test/[0-9].txt')) # 找出所以名稱為一個數字，副檔名為 .txt 的檔案，例如 1.txt、2.txt
print(glob.glob(r'./test/????.*'))    # 找出所有檔名有四個字元的檔案，例如 test.txt、demo.py
print(glob.glob(r'./test/t*.*'))      # 找出所有 t 開頭的檔案，例如 test.txt、test.py
print(glob.glob(r'./test/*e*.*'))     # 找出所有檔名裡有 e 的檔案，例如 test.txt、hello.py


print("------------------------------------------------------------")  # 60個

import os

files = ["c1.py", "c2.py", "c3.py"]
for file in files:
    print(os.path.join("D:\\test", file))

print("------------------------------------------------------------")  # 60個



"""
# 如果檔案在目前工作目錄下可以省略路徑
print(os.path.getsize("ch14_1.py"))
print(os.path.getsize("D:\\Python\\ch14\\ch14_1.py"))

print("------------------------------------------------------------")  # 60個


print(os.listdir("D:\\Python\\ch14"))
print(os.listdir("."))                  # 這代表目前工作目錄

print("------------------------------------------------------------")  # 60個

totalsizes = 0
print("列出D:\\Python\\ch14工作目錄的所有檔案")
for file in os.listdir('D:\\Python\\ch14'):
    print(file)
    totalsizes += os.path.getsize(os.path.join('D:\\Python\\ch14', file))

print("全部檔案大小是 = ", totalsizes)
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
