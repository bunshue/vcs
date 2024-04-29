import random
import time
import math

import pyautogui

print("螢幕截圖")
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

import time
import pyautogui as auto

while True:
    x, y = auto.position()
    # clear_output()
    print(x, y)
    time.sleep(0.5)
    if x < 10:
        print("太左邊  離開")
        break
    elif x > 1200:
        print("太右邊  離開")
        break
    elif y < 10:
        print("太上面  離開")
        break
    elif y > 900:
        print("太下面  離開")
        break

print("------------------------------------------------------------")  # 60個

print("測試 pyautogui")
import pyautogui as auto
import time

auto.PAUSE = 1
x, y = 630, 20
print("移動")
auto.moveTo(x, y, 2)
print("點擊")
auto.click()
x, y = 264, 62
print("移動")
auto.moveTo(x, y, 2)
print("點擊")
auto.click()
print("打字")
auto.typewrite("https://hophd.wordpress.com")
time.sleep(2)
print("Enter")
auto.press("enter")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
