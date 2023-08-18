# ch11_9.py
from tkinter import *
from tkinter import messagebox

def callback():
    res = messagebox.askokcancel("OKCANCEL","結束或取消?")
    if res == True:
        root.destroy()
    else:
        return
    
root = Tk()
root.title("ch11_9")
root.geometry("300x180")
root.protocol("WM_DELETE_WINDOW",callback)  # 更改協定綁定

root.mainloop()








