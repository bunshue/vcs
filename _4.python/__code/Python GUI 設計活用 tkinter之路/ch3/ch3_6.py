# ch3_6.py
from tkinter import *

window = Tk()
window.title("ch3_6")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(fill=X)                   # 填滿X軸包裝與定位元件
lab2.pack(pady=10)                  # y軸增加10像素
lab3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()





