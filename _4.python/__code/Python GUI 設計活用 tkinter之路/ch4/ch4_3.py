# ch4_3.py
from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_3")                 # 視窗標題
label = Label(root)                 # 標籤內容             
btn1 = Button(root,text="列印訊息",width=15,command=msgShow)
btn2 = Button(root,text="結束",width=15,command=root.destroy)
label.pack()                      
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

root.mainloop()






