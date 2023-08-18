# ch4_1.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
root = Tk()
root.title("ch4_1")                 # 視窗標題
label = Label(root)                 # 標籤內容             
btn = Button(root,text="列印訊息",command=msgShow)
label.pack()                      
btn.pack()

root.mainloop()






