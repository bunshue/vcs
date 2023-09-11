import sys

from tkinter import *

print('------------------------------------------------------------')	#60個


from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x140")
root.title("ch15_1")

# 使用預設建立進度條
pb1 = Progressbar(root)
pb1.pack(pady=20)
pb1["maximum"] = 100
pb1["value"] = 50

# 使用各參數設定方式建立進度條
pb2 = Progressbar(root,orient=HORIZONTAL,length=200,mode ="determinate")
pb2.pack(pady=20)
pb2["maximum"] = 100
pb2["value"] = 50

root.mainloop()






#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch15\ch15_2.py

# ch15_2.py
from tkinter import *
from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    for i in range(100):
        pb["value"] = i+1           # 每次更新1
        root.update()               # 更新畫面
        time.sleep(0.05)
 
root = Tk()
root.title("ch15_2")

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btn = Button(root,text="Running",command=running)
btn.pack(pady=10)

root.mainloop()













print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch15\ch15_3.py

# ch15_3.py
from tkinter import *
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
 
root = Tk()
root.title("ch15_3")
bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小    

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"] = 0                     # Prograssbar初始值
 
btn = Button(root,text="Load",command=load)
btn.pack(pady=10)

root.mainloop()













print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch15\ch15_4.py

# ch15_4.py
from tkinter import *
from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    while pb.cget("value") <= pb["maximum"]:        
        pb.step(2)
        root.update()               # 更新畫面
        print(pb.cget("value"))     # 列印指針值
        time.sleep(0.05)
 
root = Tk()
root.title("ch15_4")

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btn = Button(root,text="Running",command=running)
btn.pack(pady=10)

root.mainloop()













print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch15\ch15_5.py

# ch15_5.py
from tkinter import *
from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
root = Tk()
root.title("ch15_5")

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btnRun = Button(root,text="Run",command=run)    # 建立Run按鈕
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop = Button(root,text="Stop",command=stop) # 建立Stop按鈕
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()













print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch15\ch15_6.py

# ch15_6.py
from tkinter import *
from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
root = Tk()
root.title("ch15_6")

pb = Progressbar(root,length=200,mode="indeterminate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btnRun = Button(root,text="Run",command=run)    # 建立Run按鈕
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop = Button(root,text="Stop",command=stop) # 建立Stop按鈕
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()













print('------------------------------------------------------------')	#60個









