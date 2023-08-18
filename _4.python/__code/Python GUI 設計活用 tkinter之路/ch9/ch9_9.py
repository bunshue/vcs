# ch9_9.py
from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("ch9_9")
cities = ("新加坡","上海","東京")       # 以元組儲存數值

sp = Spinbox(root,
             values=cities,    
             command=printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()






