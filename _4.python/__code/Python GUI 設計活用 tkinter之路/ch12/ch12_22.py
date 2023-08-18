# ch12_22.py
from tkinter import *


root = Tk()
root.title("ch12_22")                   # 視窗標題

scrollbar = Scrollbar(root)             # 建立捲軸
scrollbar.pack(side=RIGHT, fill=Y)

# 建立Listbox, yscrollcommand指向scrollbar.set方法
lb = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(50):                     # 建立50筆項目
    lb.insert(END, "Line " + str(i))
lb.pack(side=LEFT,fill=BOTH,expand=True)

scrollbar.config(command=lb.yview)

root.mainloop()











