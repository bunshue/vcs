
print("------------------------------------------------------------")  # 60個

secretcode = '112299'                                   # 設定密碼
codeNotFound = True                                     # 尚未找到密碼為True
for i1 in range(0, 10):                                 # 第一位數
    if codeNotFound:            # 檢查是否找到沒有找到才會往下執行
        for i2 in range(0, 10):                         # 第二位數
            if codeNotFound:    # 檢查是否找到沒有找到才會往下執行
                for i3 in range(0, 10):                 # 第三位數
                    if codeNotFound:
                        for i4 in range(0, 10):
                            if codeNotFound:
                                for i5 in range(0, 10):
                                    if codeNotFound:
                                        for i6 in range(0, 10):
                                            code = str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6) # 組成密碼
                                            if code == secretcode:              # 比對密碼
                                                print('Bingo!', code)
                                                codeNotFound = False            # 註明已經比對成功
                                                break
                                            else:
                                                print(code)                     # 列印無效碼

print("------------------------------------------------------------")  # 60個

import pyautogui
import time

time.sleep(10)      # 這10秒需要繪圖視窗取得焦點,選擇畫筆和選擇顏色
pyautogui.click()   # 按一下設定繪圖起始點                     
displacement = 300
while displacement > 10:
    pyautogui.dragRel(displacement, 0, duration=0.2)
    pyautogui.dragRel(0, displacement, duration=0.2)
    pyautogui.dragRel(-displacement, 0, duration=0.2)
    pyautogui.dragRel(0, -displacement, duration=0.2)
    displacement -= 10

print("------------------------------------------------------------")  # 60個

import pyautogui
import time

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)

pyautogui.typewrite('Ming-Chi Institute of Technology', 0.1)
pyautogui.typewrite(['enter'],0.1)
pyautogui.typewrite('Department of Artificial Intelligence', 0.1)
pyautogui.typewrite(['enter'],0.1)
pyautogui.typewrite('Name : Jiin-Kwei Hung', 0.1)

print("------------------------------------------------------------")  # 60個

import sqlite3
conn = sqlite3.connect("data29_1.db")   # 資料庫連線
sql = '''SELECT name, tel
        from students
        where gender = "F"'''
results = conn.execute(sql)
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import threading, time

def wakeUp(mytime,note,job):
    print(job," 開始")
    starttime = int(time.time())
    while int(time.time()) - starttime < mytime:
        pass
    print(note)
    print(job," 結束")
    
print("程式階段1")
threadObj1 = threading.Thread(target=wakeUp,
                args=[30,'買機票去北京','threadJob1'])
threadObj1.start()              # threadObj1執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒

threadObj2 = threading.Thread(target=wakeUp,
                args=[60,'送花給女友', 'threadJob2'])
threadObj2.start()              # threadObj1執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒

print("程式階段2,正常工作")

print("------------------------------------------------------------")  # 60個

import turtle

def mysquare(x,y,n):
    t.penup()
    t.setpos(x+n/2,y+n/2)
    t.pendown()   
    t.seth(-180)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.penup()
    t.setpos(0,0)
    t.seth(0)
    
x,y = eval(input("請輸入x和y : "))
n = eval(input("請輸入n : "))

t = turtle.Pen()
mysquare(x,y,n)

print("------------------------------------------------------------")  # 60個

import turtle
import random
colorsList = ['green', 'blue', 'red']

t = turtle.Pen()
t.ht()                      # 隱藏海龜
t.speed(0)
t.penup()
t.setpos(-200,0)
t.pendown()
r=100
for i in range(1, 51):
    t.color(random.choice(colorsList))
    t.circle(r)
    t.penup()
    t.fd(5)
    t.pendown()
    r = r - 1

print("------------------------------------------------------------")  # 60個

import turtle 
import random

def is_inside():
    ''' 測試是否在繪布範圍 '''
    left = (-t.screen.window_width() / 2) + 100             # 左邊牆
    right = (t.screen.window_width() / 2) - 100             # 右邊牆
    top = (t.screen.window_height() / 2) - 100              # 上邊牆
    bottom = (-t.screen.window_height() / 2) + 100          # 下邊牆
    x, y = t.pos()                                          # 海龜座標
    is_inside = (left < x < right) and (bottom < y < top)
    return is_inside

def turtle_move():
    colors = ['blue', 'pink', 'green', 'red', 'yellow', 'aqua']
    t.color(random.choice(colors))              # 繪圖顏色
    t.begin_fill()
    if is_inside():                             # 如果在繪布範圍
        t.right(random.randint(320, 350))       # 海龜移動角度
        t.forward(length)
    else:
        t.backward(length)
    t.end_fill()
    
t = turtle.Pen()
length = 100                                    # 線長
width = 10                                      # 線寬
t.pensize(width)                                # 設定畫筆寬
t.screen.bgcolor('black')                       # 畫布背景
while True:
    turtle_move()

print("------------------------------------------------------------")  # 60個

import yfinance as yf
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載蘋果公司最近 6 個月的股價數據
tsm = yf.Ticker("TSM")
data = tsm.history(period="6mo")

# 計算5天, 20天和60天移動平均線
data['MA5'] = data['Close'].rolling(window=5).mean()
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA60'] = data['Close'].rolling(window=60).mean()

# 繪製股價和移動平均線
plt.figure(figsize=(10,6))
plt.plot(data['Close'], label='TSMC Close', color='blue')
plt.plot(data['MA5'], label='5-Day MA', color='green')
plt.plot(data['MA20'], label='20-Day MA', color='red')
plt.plot(data['MA60'], label='60-Day MA', color='magenta')

# 標題和圖例
plt.title('台積電美國股價 5 日, 20 日和 60日移動平均線')
plt.xlabel('日期')
plt.ylabel('價格')
plt.legend()

# 顯示圖表
plt.show()

print("------------------------------------------------------------")  # 60個

import threading 
import os  
from pytube import YouTube  

def download_video(url):
    try:
        yt = YouTube(url)                       # 建立 YouTube 物件
        yt.streams[0].download(download_path)   # 選擇第1個並下載
        print(f"下載完成 : {url}")              # 輸出下載完成的訊息
    except Exception as e:
        print(f"錯誤下載 {url}: {str(e)}")      # 如果錯誤, 輸出錯誤訊息

# 下載影片的 URL 列表
urls = [
    "https://www.youtube.com/watch?v=dhzsf5QXmns",
    "https://www.youtube.com/watch?v=z8eE3CGyQiE",
    "https://www.youtube.com/watch?v=GLlsu31FBt8",
    "https://www.youtube.com/watch?v=VMCk7fh9SGw",
    "https://www.youtube.com/watch?v=_32sspKCF8Y",
    "https://www.youtube.com/watch?v=DRayCRQvycI",
    "https://www.youtube.com/watch?v=SebJgj__zLg",
    "https://www.youtube.com/watch?v=FakRY8Ufxgs&t=126s",
    "https://www.youtube.com/watch?v=99XQsOSRrkk",
    "https://www.youtube.com/watch?v=hIrAsMmlQzg",
]

# 定義當前目錄下的 out36_5 資料夾作為下載路徑
download_path = os.path.join(os.getcwd(), 'tmp_out36_5')

# 檢查該資料夾是否存在，如果不存在則建立
if not os.path.exists(download_path):
    os.makedirs(download_path)

threads = []                                    # 建立一個空串列儲存執行緒

# 為每個 URL 建立一個新的執行緒
for url in urls:
    thread = threading.Thread(target=download_video, args=(url,))
    threads.append(thread)                      # 將執行緒添加到串列中
    thread.start()                              # 開始執行緒的執行

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print("所有影片下載完成")                       

print("------------------------------------------------------------")  # 60個

from tkinter import * 
    
window = Tk()           
window.title("ex19_2")  

xWidth = 400
yHeight = 250
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
for i in range(20):
    canvas.create_oval(10+i*5, 10+i*5, xWidth-10-i*5, yHeight-10-i*5)
        
window.mainloop() 



print("------------------------------------------------------------")  # 60個

from tkinter import * 

window = Tk() 
window.title("ex19_4.py") 
        
xWidth = 300
yHeight = 100
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
x = 0
yMsg = 45
canvas.create_text(x, yMsg, text="王者歸來", tags="msg")
        
dx = 5
while True:
    canvas.move("msg", dx, 0)  
    canvas.after(100)       
    canvas.update()         
    if x < xWidth:
        x += dx             
    else:
        x = 0               
        canvas.delete("msg")                             
        canvas.create_text(x, yMsg, text = "王者歸來", tags = "msg")
                
window.mainloop() 

print("------------------------------------------------------------")  # 60個

from tkinter import *
def displayFan(startingAngle):
    canvas.delete("fan")    
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 0, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 120, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 240, extent = 60, fill = "green", tags = "fan")        

xWidth = 300
yHeight = 300
r = 120

window = Tk() 
window.title("ex19_6.py") 
        
canvas = Canvas(window,width=xWidth, height=yHeight)
canvas.pack()

startAngle = 0
while True:
    startAngle += 5
    displayFan(startAngle)
    canvas.after(50) 
    canvas.update()
            
window.mainloop() 

print("------------------------------------------------------------")  # 60個

from tkinter import *
import math

def paintTree(depth, x1, y1, length, angle):
    if depth >= 0:
        depth -= 1
        x2 = x1 + int(math.cos(angle) * length)
        y2 = y1 - int(math.sin(angle) * length)
        # 繪線
        drawLine(x1, y1, x2, y2)
        # 繪左邊
        paintTree(depth,x2, y2, length*sizeRatio, angle+angleValue)
        # 繪右邊
        paintTree(depth, x2, y2, length*sizeRatio, angle-angleValue)
        
# 繪製p1和p2之間的線條
def drawLine(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2,tags="myline")

# 顯示
def show():
    canvas.delete("myline")
    myDepth = depth.get()
    paintTree(myDepth, myWidth/2, myHeight, myHeight/3, math.pi/2)
    
# main
tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight) # 建立畫布
canvas.pack()

frame = Frame(tk)                               # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入depth數Entry, 按鈕Button
Label(frame, text="輸入depth : ").pack(side=LEFT)
depth = IntVar()
depth.set(0)
entry = Entry(frame, textvariable=depth).pack(side=LEFT,padx=3)
Button(frame, text="Recursive Tree",
       command=show).pack(side=LEFT)
angleValue = math.pi / 4                       # 設定角度
sizeRatio = 0.6                                 # 設定下一層的長度與前一層的比率是0.6

tk.mainloop()

print("------------------------------------------------------------")  # 60個



