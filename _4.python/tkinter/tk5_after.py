"""
# 會動的tk範例 after

"""

import sys
import time
import random
import tkinter as tk
import tkinter.ttk as ttk

print("------------------------------------------------------------")  # 60個

import datetime

def run_digital_clock(label1):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        label1.config(text=str(now))     # 列出標籤數字內容
        label1.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 啟動呼叫

window = tk.Tk()
label1=tk.Label(window,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=18,              # 寬10高3
            font="Helvetic 20 bold")        # 字型設定
label1.pack()
run_digital_clock(label1)                          # 呼叫數字更動方法

window.mainloop()

print('------------------------------------------------------------')	#60個

def run_digital_clock(label1):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        label1.config(text=str(now))     # 列出標籤數字內容
        label1.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 持續呼叫

window = tk.Tk()
label1=tk.Label(window,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=18,              # 寬10高3
            font="Helvetica 20 bold")       # 字型設定
label1.pack()
run_digital_clock(label1)                          # 呼叫數字更動方法
Button(window,text="結束",width=15,command=window.destroy).pack(pady=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
 
def load():                         # 啟動Prograssbar
    pb["value"] = 0                 # Prograssbar初始值
    pb["maximum"] = maxbytes        # Prograddbar最大值
    loading()
def loading():                      # 模擬下載資料
    global bytes
    bytes += 500                    # 模擬每次下在500bytes
    pb["value"] = bytes             # 設定指針
    if bytes < maxbytes:
        pb.after(50,loading)        # 經過0.05秒繼續執行loading
 
window = tk.Tk()

bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小    

pb = tk.Progressbar(window,length=200,mode="determinate",orient=tk.HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"] = 0                     # Prograssbar初始值
 
btn = tk.Button(window,text="Load",command=load)
btn.pack(pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('秒數計算中...')
window.geometry('100x100+150+150')

counter = 0 #儲存數值

# 自訂函式一：顯示標籤(Label)元件
def display(label):
   counter = 0
   
   # 自訂函式二
   def count():
      global counter #全域變數
      counter += 1
      label.config(text = str(counter),
         bg = 'pink', width = 20, height = 2)
      label.after(1000, count)
   count()
   
#設定標籤並把它放入主視窗
show = tk.Label(window, fg = 'gray')
show.pack()
display(show)

# 設定按鈕
btnStop = tk.Button(window, text = 'Stop',
    width = 20, command = window.destroy)
btnStop.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

import random           

def update_data():
    # 更新標籤顯示的數據為1到100的隨機數
    label_data.config(text=str(random.randint(1, 100)))
    # 每1000毫秒(即1秒)後再次調用update_data函數更新數據
    window.after(1000, update_data)

window = tk.Tk()
window.title("數據監控")                      # 視窗標題
# 建立一個標籤用於顯示數據, 初始值為0, 字體設置為Helvetica, 大小為48
label_data = tk.Label(window, text="0", font=("Helvetica", 48))
label_data.pack()                           # 將標籤添加到視窗中
update_data()           # 呼叫update_data( )函數以開始數據更新過程

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = Tk() 
        
xWidth = 300
yHeight = 100
canvas = tk.Canvas(window, width=xWidth, height=yHeight)
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
        
canvas = tk.Canvas(window,width=xWidth, height=yHeight)
canvas.pack()

startAngle = 0
while True:
    startAngle += 5
    displayFan(startAngle)
    canvas.after(50) 
    canvas.update()
            
window.mainloop() 

print("------------------------------------------------------------")  # 60個

from random import *

def display():
    if Flag:       
        if ball.get() == "1":
            raceResult.set("恭喜你贏了, Ball 1勝利")
        else:
            raceResult.set("抱歉你輸了, Ball 1勝利")
    else:
        if ball.get() == "1":
            raceResult.set("抱歉你輸了, Ball 2勝利")
        else:
            raceResult.set("恭喜你贏了, Ball 2勝利")
    startBtn.set("重置")

def running():
    global Flag
    if startBtn.get() == "重置":
        startBtn.set("開始")
        raceResult.set("")
        canvas.delete('all')
        canvas.create_text(10,50,text="1")
        id1 = canvas.create_oval(20,50,70,100,fill='yellow')
        canvas.create_text(10,150,text="2")
        id2 = canvas.create_oval(20,150,70,200,fill='aqua')
        return
    canvas.delete('all')
    canvas.create_text(10,50,text="1")
    id1 = canvas.create_oval(20,50,70,100,fill='yellow')
    canvas.create_text(10,150,text="2")
    id2 = canvas.create_oval(20,150,70,200,fill='aqua')
    id1Loc, id2Loc = 0, 0
    for x in range(0, 100):
        if ball.get() == '1':
            weight = 40
            raceResult.set("")
        elif ball.get() == '2':
            weight = 60
            raceResult.set("")
        else:
            raceResult.set("輸入錯誤!")
            return
        if randint(1,100) > weight:
            canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
            id2Loc += 1
        else:
            canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素
            id1Loc += 1
        tk.update()                 # 強制tkinter重繪
        canvas.after(50)
    if id1Loc > id2Loc:
        Flag = True
    else:
        Flag = False
    display()

window = tk.Tk()
canvas= tk.Canvas(window, width=500, height=250)
canvas.pack()
canvas.create_text(10,50,text="1")
canvas.create_oval(20,50,70,100,fill='yellow')
canvas.create_text(10,150,text="2")
canvas.create_oval(20,150,70,200,fill='aqua')

Flag = True                         # 判斷那一球勝利

frame = tk.Frame(tk)                   # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入獲勝的球, 按鈕Button
tk.Label(frame, text="那一個球獲勝 : ").pack(side=LEFT)
ball = tk.StringVar()
ball.set("1or2")
entry = tk.Entry(frame, textvariable=ball).pack(side=LEFT,padx=3)
startBtn = tk.StringVar()
startBtn.set("開始")
tk.Button(frame, textvariable=startBtn,command=running).pack(side=LEFT)
raceResult = tk.StringVar()

tk.Label(frame,width=16,textvariable=raceResult).pack(side=LEFT,padx=3)

window.mainloop() 


window = tk.Tk()
canvas= tk.Canvas(window, width=500, height=150)
canvas.pack()
id = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



