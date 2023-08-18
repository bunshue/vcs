# ch3_11.py
from tkinter import *

window = Tk()
window.title("ch3_11")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack()                         # 包裝與定位元件
lab2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
lab3.pack(ipady=10)                 # ipady=10包裝與定位元件

window.mainloop()






