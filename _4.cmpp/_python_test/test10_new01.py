items = "03/11/2006".split("/")
print(items)



filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/human2.jpg'

name = filename.split('/')
print(len(name))
print(name)
print(type(name))

ccc = name.reverse()
print(ccc)




x = 2
y = 0.5

print("x**y = "+str(x**y))


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
import numpy as np
import matplotlib.pyplot as plt

#曲線資料加入雜訊
x = np.linspace(-5,5,200)
y = np.sin(x)
yn = y + np.random.rand(1, len(y))*1.5

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,yn,c='blue',marker = '.')
ax.plot(x,y+0.75,'r')
plt.show()
'''

'''
cnstr = '中文 test'
print(cnstr, len(cnstr))
#utfstr = unicode(cnstr, 'utf-8')
'''

def plotfigure(X, X_test, y, yp):
    plt.figure()
    plt.scatter(X, y, c = 'k', label = 'data')
    plt.plot(X_test, yp, c = 'r', label = 'max_depth = 5', linewidth = 2)
    plt.xlabel('data')
    plt.ylabel('target')
    plt.title('Decision Tree Regression')
    plt.legend()
    plt.show()

import numpy as np
from numpy import *
#from sklearn.tree import DecisionTreeRegressor

import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
siny = np.sin(x)

X = mat(x).T
y = siny + np.random.rand(1, len(siny))*1.5 #加入雜訊的點集
y = y.tolist()[0]

plotfigure(X, X_test,y,yp)







print(__file__)
print(__file__.upper())
print(__file__.lower())
print(__name__)


print(__name__)
#print(__name__._version)


print(__doc__)


import sys
print(sys.path)


import os
this_dir = os.path.dirname(__file__)
print(this_dir)

cwd = os.getcwd()
print(cwd)

aa = os.chdir(cwd)
print(aa)

dirname = 'C:/_git/vcs/_4.cmpp/_python_test'
cc = os.chdir(dirname)
print(cc)

cmd = '%s "%s" %s' % (sys.executable, 'aaaa', 'bbbb')
print(cmd)


import os
import sys

isympy_path = os.path.abspath(__file__)
isympy_dir = os.path.dirname(isympy_path)
sympy_top = os.path.split(isympy_dir)[0]
sympy_dir = os.path.join(sympy_top, 'sympy')

if os.path.isdir(sympy_dir):
    #sys.path.insert(0, sympy_top)
    print('is dir')

#print(__path__[0])

theano_nose = os.path.realpath(__file__)
print(theano_nose)


#print(os.listdir(cache.dirname))

print(__doc__)  # the docstring of this module above


import sympy
VERSION = sympy.__version__
print(VERSION)


print('顯示目前的系統編碼')
import sys
print(sys.getdefaultencoding())






string_data1 = '你好'

print('原字串 :', string_data1)
print('用 gb2312 編碼 ')
encode_data = string_data1.encode('gb2312')
print(encode_data)

print('再用 big5 解碼出來')
string_data2 = encode_data.decode('big5')
print(string_data2)

print('萬國碼 unicode, 我')
print('我'.encode('utf8'))

string_data1 = '扂砑腕善衄壽unicode腔垀衄砆牉訧蹋,掀:unicode 2.0 3.0 4.0 梗摯崋欴晤鎢.gb,big-5,gbk,脹脹.坳蠅眳潔腔梗摯薊炵..秪峈扂猁勤森輛俴惆豢,眕扂植懂羶衄勤晤鎢衄徹旃噶,腕悝.褫岆婓厙奻梑祥善涴笱砆牉腔恅梒..洷咡籵徹蠟夔腕善.郅郅!'

print('原字串 :', string_data1)
print('用 big5 編碼 ')
encode_data = string_data1.encode('big5')
print(encode_data)

print('再用 gb2312 解碼出來')
string_data2 = encode_data.decode('gb2312')
print(string_data2)








import sys
print(sys.platform)

print(sys.version)

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


ver_string = "%d.%d" % (sys.version_info[0], sys.version_info[1])
root_key_name = "Software\\Python\\PythonCore\\" + ver_string
print(sys.version_info)
print(ver_string)
print(root_key_name)



import tempfile
#tee_f = open(os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log'), "w")

print(tempfile.gettempdir())

tmp_filename = os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log')
print(tmp_filename)

tmp_filename = os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log', 'ccccc')
print(tmp_filename)

vi = sys.version_info
install_group = "Python %d.%d" % (vi[0], vi[1])
print(install_group)

filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/data/aaaaa.jpg'
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/data/bbbbb.jpg'

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



def bubbleSort(list):
    needNextPass = True
    
    k = 1
    while k < len(list) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(list) - k): 
            if list[i] > list[i + 1]:
                # swap list[i] with list[i + 1]
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
          
                needNextPass = True # Next pass still needed

list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
bubbleSort(list)
for v in list:
    print(v)




students = [
    ("John", "Smith", 96),
    ("Susan", "King", 76),
    ("Kim", "Yao", 99)
]
students.sort(key=lambda e: (e[1]))
print(students)
print(sorted(students, key = lambda t: (t[2]), reverse = True))

        

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

#一維list
mylist = ["A", "B", "C", "D", "E"]

for elem in mylist:
    print(elem)
    

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







import random 

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)


number = random.randint(0, 100) 
number = random.randint(1, 100)



import time

startTime = time.time() # Get start time

#do something
#do something
#do something

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Test time is", testTime, "seconds")


import time
version = time.strftime("-%Y%m%d")
print(version)



print('拆解e-mail')
import re
import requests
regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://csharphelper.com/blog/'
html_data = requests.get(url).text

emails = re.findall(regex, html_data)
for email in emails:
    print(email)




#強制離開程式, 並說明原因
sys.exit('強制離開程式, 並說明原因')




