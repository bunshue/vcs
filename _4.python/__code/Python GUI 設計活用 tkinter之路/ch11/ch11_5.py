# ch11_5.py
from tkinter import *
def key(event):                     # 處理鍵盤按a ... z
    print("按了 " + repr(event.char) + " 鍵") 
   
root = Tk()
root.title("ch11_5")

root.bind("<Key>",key)              # <Key>鍵綁定key函數

root.mainloop()








