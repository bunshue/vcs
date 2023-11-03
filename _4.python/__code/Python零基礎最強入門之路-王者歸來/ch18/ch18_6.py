# ch18_6.py
from tkinter import *

window = Tk()
window.title("ch18_6")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=BOTTOM)              # 包裝與定位元件
lab2.pack(side=BOTTOM)              # 包裝與定位元件
lab3.pack(side=BOTTOM)              # 包裝與定位元件

window.mainloop()






