
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


x = 2
y = 0.5

print("x**y = " + str(x ** y))


lst = [3, 2, 1, 5, 9, 0]
sorted(lst)
print(lst)


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




username = 'david'
password = '1234'
if username=='david' and password=='1234':
    print('歡迎光臨本網站！')
else:
    print('帳號或密碼錯誤！')





from urllib import parse

string = '豬頭三'

string_url = parse.quote(string)
print('原字串:\t' + string)
print('轉網址:\t' + string_url)




import pandas as pd
import numpy as np
import random

my_array = np.arange(10)  # [0 1 2 3 4]

print('原list')
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

sum_my_array = sum(my_array)
print('和')
print(sum_my_array)

'''
index = []
ran = random.sample(range(0, 10),2)
for i in ran:
    index.append(i)
index.sort()
'''

for i in range(10):
    timeout = random.choice(range(80,180))
    print('timeout', timeout)

import random
import time

n = 10
lst = list(range(n))
print(lst)
random.shuffle(lst)
print(lst)
startTime = time.time()
lst.sort()
print("Sort time in Python is", int(time.time() - startTime), "seconds")

print(lst)




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

import sys
vi = sys.version_info
install_group = "Python %d.%d" % (vi[0], vi[1])
print(install_group)

filename1 = 'C:/_git/vcs/_1.data/______test_files1/aaaaa.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/bbbbb.jpg'

print("Copied %s to %s" % (filename1, filename2))

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
print(a[4:7])
print(a.replace("learn", "teach"))
print(a.split(" "))
print(a+b)




candyCan = ["apple", "strawberry", "grape", "mango"]

candyCan[1] = "peach"
print(candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

candyCan.append("banana")
print(candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

candyCan.insert(1, "orange")
print(candyCan)



candyCan = ["apple", "strawberry", "grape", "mango"]

print(candyCan[1])
print(candyCan[-1])
print(candyCan[1:3])



candyCan = ["apple", "strawberry", "grape", "mango"]

print(candyCan)
print(len(candyCan))
print(type(candyCan))

candyCan = ["apple", "strawberry", "grape", "mango"]

print("apple" in candyCan)
print("banana" in candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

newCandy = ["banana", "orange"]
temp = candyCan + newCandy
print(temp)
print(candyCan)
print(newCandy)

'''
candyCan = ("apple", "strawberry", "mango", "peach", "grape")

candyCan[1] = "banana"


candyCan = ("apple", "strawberry", "mango", "peach", "grape")

print(candyCan)
print(len(candyCan))

print(candyCan[0])
print(candyCan[1:3])

print(candyCan.count("mango"))
print(candyCan.index("mango"))
'''



candyFlavor = {"apple", "strawberry", "mango", "mango"}
print(candyFlavor)

candyFlavor.add("orange")
print(candyFlavor)

candyFlavor.remove("orange")
print(candyFlavor)

newFlavor = {"apple", "banana"}
candyFlavor.update(newFlavor)
print(candyFlavor)



candyNumber = {"apple": 5, "strawberry": 10, "mango": 3}

print(candyNumber)

print(candyNumber["apple"])
candyNumber["apple"] = 6
print(candyNumber)

candyNumber["banana"] = 8
print(candyNumber)

candyNumber.pop("banana")
print(candyNumber)

print(candyNumber.keys())
print(candyNumber.values())
print(candyNumber.items())

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





import sys, os, time, difflib, argparse
from datetime import datetime, timezone

path = 'C:/_git/vcs/_4.python'
t1 = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
print(t1)

t2 = t1.astimezone().isoformat()
print(t2)


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print(filename)


print('file: %s' % filename)
print('file: %r' % filename)

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

import sys

usage = """Usage: %s [-cd] paths...
    -c: recognize Python source files trying to compile them
    -d: debug output""" % sys.argv[0]

print('msgsssssss', file = sys.stderr)
print(usage, file = sys.stderr)

import os
import sys

print(sys.maxsize)
print(2 ** 32)

import selenium

print(selenium.__version__)

import os
import stat

print(os.name)
print(os.sep)


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'


foldername = os.path.dirname(filename)
print(filename)
print(foldername)

mode = os.stat(filename).st_mode

print(mode)

print(stat.S_IWOTH)

print(mode & stat.S_IWOTH)

print(mode)

print(stat.S_IWGRP)

print(mode & stat.S_IWGRP)

if os.path.exists(filename):
    print('True')
else:
    print('False')
    

if os.path.isdir(filename):
    print('True')
else:
    print('False')

if os.listdir(foldername):
    print('True')
else:
    print('False')


total = 7
for i in range(0, (total+1)):
    #print(i)	# 0 ~ 7
    print(u"download: " + str(100 * i / total ) + " %.")












