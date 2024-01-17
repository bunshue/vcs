# ch18_4.py
from tkinter import *

window = Tk()
window.title("ch18_4")              # 視窗標題
label = Label(window,text="I like tkinter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label.pack()                        # 包裝與定位元件

window.mainloop()






