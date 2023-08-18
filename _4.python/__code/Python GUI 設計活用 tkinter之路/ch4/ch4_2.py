# ch4_2.py
from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")
      
root = Tk()
root.title("ch4_2")                 # 視窗標題
label = Label(root)                 # 標籤內容             
btn = Button(root,text="列印訊息",command=msgShow)
label.pack()                      
btn.pack()

root.mainloop()






