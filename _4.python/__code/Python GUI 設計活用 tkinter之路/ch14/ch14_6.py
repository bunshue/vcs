# ch14_6.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch14_6")
root.geometry("300x160")

notebook = Notebook(root)           # 建立Notebook

frame1 = Frame()                    # 建立Frame1
frame2 = Frame()                    # 建立Frame2

notebook.add(frame1,text="頁次1")   # 建立頁次1同時插入Frame1
notebook.add(frame2,text="頁次2")   # 建立頁次2同時插入Frame2
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()











