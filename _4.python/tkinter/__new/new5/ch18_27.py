# ch18_27.py
from tkinter import *

window = Tk()
window.title("ch18_27")                   # 視窗標題

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

var1 = IntVar()                      
Checkbutton(window,text="美式足球",
                  variable=var1).grid(row=1,sticky=W)
var2 = IntVar()
Checkbutton(window,text="棒球",
                  variable=var2).grid(row=2,sticky=W)                
var3 = IntVar()
Checkbutton(window,text="籃球",
                  variable=var3).grid(row=3,sticky=W)   

window.mainloop()






