# ch9_8.py
from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("ch9_8")

sp = Spinbox(root,
             values=(10,38,170,101),    # 以元組儲存數值
             command=printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()






