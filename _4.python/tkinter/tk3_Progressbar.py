"""
Progressbar

"""

import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

from tkinter import *

print("------------------------------------------------------------")  # 60個


from tkinter.ttk import *

window = Tk()
window.geometry("600x400")

# 使用預設建立進度條
pb1 = Progressbar(window)
pb1.pack(pady=20)
pb1["maximum"] = 100
pb1["value"] = 50

# 使用各參數設定方式建立進度條
pb2 = Progressbar(window,orient=HORIZONTAL,length=200,mode ="determinate")
pb2.pack(pady=20)
pb2["maximum"] = 100
pb2["value"] = 50

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    for i in range(100):
        pb["value"] = i+1           # 每次更新1
        window.update()               # 更新畫面
        time.sleep(0.05)
 
window = Tk()
window.geometry("600x400")

pb = Progressbar(window,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
button1 = Button(window,text="Running",command=running)
button1.pack(pady=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    while pb.cget("value") <= pb["maximum"]:        
        pb.step(2)
        window.update()               # 更新畫面
        print(pb.cget("value"))     # 列印指針值
        time.sleep(0.05)
 
window = Tk()
window.geometry("600x400")

pb = Progressbar(window,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
button1 = Button(window,text="Running",command=running)
button1.pack(pady=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
window = Tk()
window.geometry("600x400")

pb = Progressbar(window,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
buttonRun = Button(window,text="Run",command=run)    # 建立Run按鈕
buttonRun.pack(side=LEFT,padx=5,pady=10)

buttonStop = Button(window,text="Stop",command=stop) # 建立Stop按鈕
buttonStop.pack(side=LEFT,padx=5,pady=10)

window.mainloop()


print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
window = Tk()
window.geometry("600x400")

pb = Progressbar(window,length=200,mode="indeterminate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
buttonRun = Button(window,text="Run",command=run)    # 建立Run按鈕
buttonRun.pack(side=LEFT,padx=5,pady=10)

buttonStop = Button(window,text="Stop",command=stop) # 建立Stop按鈕
buttonStop.pack(side=LEFT,padx=5,pady=10)

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


