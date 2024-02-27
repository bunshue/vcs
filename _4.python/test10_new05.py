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



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
