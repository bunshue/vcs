import os
import sys
import time
import random

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



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
