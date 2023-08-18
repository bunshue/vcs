# ch7_7.py
from tkinter import *

root = Tk()
root.title("ch7_7")                   # 視窗標題

lab = Label(root,text="請選擇喜歡的運動",fg="blue",bg="lightyellow",width=30)
lab.grid(row=0)

var1 = IntVar()                      
cbtnNFL = Checkbutton(root,text="美式足球",variable=var1)
cbtnNFL.grid(row=1,sticky=W)

var2 = IntVar()
cbtnMLB = Checkbutton(root,text="棒球",variable=var2)
cbtnMLB.grid(row=2,sticky=W)

var3 = IntVar()
cbtnNBA = Checkbutton(root,text="籃球",variable=var3)
cbtnNBA.grid(row=3,sticky=W)   

root.mainloop()






