import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

'''
import datetime
today = datetime.date.today()
print('今天的日期 :', today)

print("------------------------------------------------------------")  # 60個

print("enumerate() 一個串列")

animals = ['鼠', '牛', '虎', '兔']

print('用 for')
for _ in enumerate(animals):
    print(_)

print('用 list')
print(list(enumerate(animals)))

print('用 unpacking 取出內容')

for index, ani in enumerate(animals):
    print(index, ani)

print("------------------------------------------------------------")  # 60個

print('字元相關的兩個內建函式')

print('字元轉數值')
cc = ord('豬')
print(cc)

print('數值轉字元')
nn = 35948 + 5
cc = chr(nn)
print(cc)

print("------------------------------------------------------------")  # 60個

#lambda匿名函數

# List 含有 Tuple
student = [
    ("Eugene", 1989, "Taipei"),
    ("Davie", 1993, "Kaohsiung"),
    ("Michelle", 1999, "Yilan"),
    ("Peter", 1988, "Hsinchu"),
    ("Connie", 1997, "Pingtung"),
]

# 定義sort()方法參數key
na = lambda item: item[0]
student.sort(key=na)
print("依名字排序：")
for name in student:
    print("{:6s},{}, {:10s}".format(*name))

# 直接在sort()方法帶入lamdba()函式
student.sort(key=lambda item: item[2], reverse=True)
print("依出生地遞減排序：")
for name in student:
    print("{:6s},{}, {:10s}".format(*name))

print("------------------------------------------------------------")  # 60個

print('內建函式dir()檢視目前的名稱空間')
print(dir())

print()

import qrcode
print(dir())

print()

#看單一模組的函式
import math
print(dir(math))
print()

print("------------------------------------------------------------")  # 60個

import sys
print(sys.path) #查詢模組路徑

print('加入路徑')

foldername = 'C:/_git/vcs/_1.data/______test_files5'

sys.path.append(foldername)

print(sys.path) #查詢模組路徑

print("------------------------------------------------------------")  # 60個

print('使用自定義模組')
import sys

foldername = 'C:/_git/vcs/_4.python/import_module'
sys.path.append(foldername)

import module_my  #引用後, 出現 __pycache__

cc = module_my.numRand2(14, 52)
print(cc)

print(module_my.__name__)

print(__name__)



print("------------------------------------------------------------")  # 60個


size = 25

for i in range(size):
    for j in range(size):
        if i % 2 == 1 or j % 2 == 1:
            print('■', end='')
        else:
            print('□', end='')
    print()
 



print("------------------------------------------------------------")  # 60個

list1 = [1, 2, 3, 4, 5, 6, 7]
# 找最小、最大元素
print(min(list1), max(list1))
# 串列長度、串列加總
print(len(list1), sum(list1))

s0 = slice(0, 2)                 # 切片物件：定義切片範圍
s1 = slice(1, -1, 2)
print(list1[s0], list1[s1])      # list1直接帶入切片範圍
# 結果：([1, 2], [2, 4, 6])

print("------------------------------------------------------------")  # 60個

fset = frozenset(['a', 'b', 'c'])
print(fset)           # frozenset({'a', 'b', 'c'})

#fset.remove('a')      # 不能修改，AttributeError
# frozenset根本沒有remove()可用！

print("------------------------------------------------------------")  # 60個

keys = ('name', 'age', 'job')
values = ('Amy', 25, 'writer')
dic1 = dict(zip(keys, values))      # zip真好用！
print(dic1)
# {'name': 'Amy', 'age': 25, 'job': 'writer'}


print("------------------------------------------------------------")  # 60個

names = ['Amy', 'Bob', 'Cathy']
scores = [70, 92, 85]
list1 = list(enumerate(zip(names, scores)))
# [(0, ('Amy', 70)), (1, ('Bob', 92)), (2, ('Cathy', 85))]
for item in list1:
    print(item[0], item[1][0], item[1][1])


print(list(zip(('a', 'b', 'c'), (30, 41, 52))))
# [('a', 30), ('b', 41), ('c', 52)]


print(list(enumerate(['a', 'b', 'c'])))  
# [(0, 'a'), (1, 'b'), (2, 'c')]
    
print("------------------------------------------------------------")  # 60個

list1 = [30, 45, 1024, 2500, 699, 126]

# 過濾出小於1000元的消費
list2 = [num for num in list1 if num<1000]
sum1 = sum(list2)        # 用sum做消費加總
avg1 = sum1/len(list2)   # 用len取消費筆數

print(sum1)
print(avg1)


print("------------------------------------------------------------")  # 60個


"""

system
print(sys.builtin_module_names)


for fullname in sys.modules:
    module = sys.modules[fullname]
    print(fullname, module)

"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import glob

jpg = glob.glob("./demo/*.[jJ][pP][gG]")  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
print(jpg)
"""
['./demo/pic-001.jpg', './demo/pic-002.jpg', './demo/pic-003.jpg',
'./demo/pic-004.jpg', './demo/pic-005.jpg', './demo/pic-006.jpg',
'./demo/pic-007.jpg', './demo/pic-008.jpg', './demo/pic-009.jpg',
'./demo/pic-010.jpg']
"""





import glob

images = glob.glob("./demo/*")
print(images)



print("------------------------------------------------------------")  # 60個



import time

n = 20  # 設定進度條總長
for i in range(n + 1):
    print(f'\r[{"█"*i}{" "*(n-i)}] {i*100/n}%', end="")  # 輸出不換行的內容
    time.sleep(0.5)



print("------------------------------------------------------------")  # 60個

h = float(input("請輸入身高(cm)：")) / 100
w = float(input("請輸入體重(kg)："))
bmi = round(w / (h * h), 3)  # 使用 round 四捨五入到小數點三位

'''


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import pyautogui

print('螢幕截圖')
myScreenshot = pyautogui.screenshot()
myScreenshot.save("tmp_screen.png")

print("------------------------------------------------------------")  # 60個

import pyautogui

myScreenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
myScreenshot.save("tmp_screen_crop.png")



print("------------------------------------------------------------")  # 60個

import pyautogui
from time import sleep

for i in range(5):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f"./tmp_test{i}.png")
    sleep(2)


print("------------------------------------------------------------")  # 60個



import pyautogui
import requests

myScreenshot = pyautogui.screenshot()  # 截圖
myScreenshot.save("./test.png")  # 儲存為 test.png

url = "https://notify-api.line.me/api/notify"
token = "你的權杖"
headers = {"Authorization": "Bearer " + token}  # 設定 LINE Notify 權杖
data = {"message": "測試一下！"}  # 設定 LINE Notify message ( 不可少 )
image = open("./test.png", "rb")  # 以二進位方式開啟圖片
imageFile = {"imageFile": image}  # 設定圖片資訊
data = requests.post(url, headers=headers, data=data, files=imageFile)  # 發送 LINE Notify


print("------------------------------------------------------------")  # 60個

import pyautogui
import requests
import time


# 定義截圖的函式
def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("./test.png")

    t = time.time()  # 取得到目前為止的秒數
    t1 = time.localtime(t)  # 將秒數轉換為 struct_time 格式的時間
    now = time.strftime("%Y/%m/%d %H:%M:%S", t1)  # 輸出為特定格式的文字
    sendLineNotify(now)  # 執行發送 LINE Notify 的函式，發送的訊息為時間


# 定義發送 LINE Notify 的函式
def sendLineNotify(msg):
    url = "https://notify-api.line.me/api/notify"
    token = "你的權杖"
    headers = {"Authorization": "Bearer " + token}
    data = {"message": msg}
    image = open("./test.png", "rb")
    imageFile = {"imageFile": image}
    data = requests.post(url, headers=headers, data=data, files=imageFile)


# 使用for 迴圈，每隔五秒截圖發送一次
for i in range(5):
    screenshot()
    time.sleep(5)

print("------------------------------------------------------------")  # 60個

import pyautogui

width, hwight = pyautogui.size()
print(width, hwight)

print("------------------------------------------------------------")  # 60個


#撈出一層
import os

print('Current dir:', os.getcwd())

count = 0
for item in os.listdir():
    count += 1
    print(count, item)
print('Total', count, 'items in', os.getcwd())
print("------------------------------------------------------------")  # 60個

import os

foldername = 'C:/_git/vcs/_1.data/______test_files5'

for item in os.walk(foldername):
    print('dir name:', item[0])
    print('sub-dir list:', item[1])
    print('file list:', item[2])
    print('='*80)
    
print("------------------------------------------------------------")  # 60個

import os
from datetime import datetime

foldername = 'C:/_git/vcs/_1.data/______test_files5'

for entry in os.scandir(foldername):
    info = entry.stat()
    # epoch timestamp轉換成日期字串
    da = datetime.utcfromtimestamp(info.st_mtime)
    dstr = da.strftime('%Y/%m/%d')
    if entry.is_dir():
        print('資料夾：', entry.name, '最後存取時間：', dstr)
    elif entry.is_file():
        print('檔案：', entry.name, '最後存取時間：', dstr)
        
print("------------------------------------------------------------")  # 60個

import os

def dirTree(path, level=0):
    if level>1:
        return
    for item in os.listdir(path):
        path2 = os.path.join(path, item)
        if os.path.isdir(path2):
            for i in range(level):
                print('   ', end='')
            print('+--'+item)
            try:
                dirTree(path2, level+1)
            except:
                pass

foldername = 'C:/_git/vcs/_1.data/______test_files5'

dirTree(foldername)

print("------------------------------------------------------------")  # 60個

import os
from datetime import datetime

#foldername = os.getcwd()
foldername = 'C:/_git/vcs/_1.data/______test_files5'

for entry in os.scandir(foldername):
    info = entry.stat()
    da = datetime.utcfromtimestamp(info.st_mtime)
    dstr = da.strftime('%d/%m/%Y')
    if entry.is_file():
        size = int(os.path.getsize(entry.name)/1024)
        ext = os.path.splitext(entry.name)
        print(entry.name, '\t'+str(size)+'KB\t', str(ext[-1].replace('.', ''))+'\t', dstr)
    elif entry.is_dir():
        print(entry.name, '\t\t\t<DIR>\t', dstr)
        
print("------------------------------------------------------------")  # 60個



print('分割字串')
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

ss = filename.split("/")
print(filename)
print(len(ss))
for _ in ss:
    print(_)



players = ["X", "O"]
current_player = players[0]
current_player = players[(players.index(current_player) + 1) % 2]
print(current_player)
current_player = players[(players.index(current_player) + 1) % 2]
print(current_player)
current_player = players[(players.index(current_player) + 1) % 2]
print(current_player)
current_player = players[(players.index(current_player) + 1) % 2]
print(current_player)
current_player = players[(players.index(current_player) + 1) % 2]
print(current_player)

print("------------------------------------------------------------")  # 60個

print('亂數不重複 範圍 個數')
num = random.sample(range(1, 20), 10)

print(type(num))
print(num)
print('排序')

num.sort()
print(num)

print("------------------------------------------------------------")  # 60個

print('測試不定引數的函式')

#定義函式
def funtionTest(*number):
    print('你傳入了', len(number), '個引數')
    outcome = 1
    for item in number:
        outcome *= item
    return outcome

#呼叫函式
print('呼叫函式並傳入 1 個引數 :', funtionTest(7))
print('呼叫函式並傳入 2 個引數 :', funtionTest(12, 3))
print('呼叫函式並傳入 4 個引數 :', funtionTest(3, 5, 9, 14))

print("------------------------------------------------------------")  # 60個

print('print語法')

for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print("------------------------------------------------------------")  # 60個


"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：
用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
QQ号是5~12的数字且首位不能为0
"""

import re


#username = input('请输入用户名: ')
username = "lion_mouse"
m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
if not m1:
    print('请输入有效的用户名.')

#qq = input('请输入QQ号: ')
qq = "12345678"
m2 = re.match(r'^[1-9]\d{4,11}$', qq)
if not m2:
    print('请输入有效的QQ号.')
if m1 and m2:
    print('你输入的信息是有效的!')



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
