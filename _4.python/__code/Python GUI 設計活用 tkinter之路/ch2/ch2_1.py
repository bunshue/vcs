# ch2_1.py
from tkinter import *

root = Tk()
root.title("ch2_1")
label=Label(root,text="I like tkinter")
label.pack()        # 包裝與定位元件
print(type(label))  # 傳回Label物件

root.mainloop()




