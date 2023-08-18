# ch9_7.py
from tkinter import *

def printInfo():        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("ch9_7")

sp = Spinbox(root,from_ = 0,to = 10,           
             command = printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()






