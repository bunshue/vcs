# ch18_13.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_13")             # 視窗標題
label = Label(window)               # 標籤內容             
btn1 = Button(window,text="Message",width=15,command=msgShow)
btn2 = Button(window,text="Exit",width=15,command=window.destroy)
label.pack()                      
btn1.pack(side=LEFT)                # 按鈕1
btn2.pack(side=RIGHT)               # 按鈕2

window.mainloop()






