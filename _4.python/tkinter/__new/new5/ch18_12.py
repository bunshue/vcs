# ch18_12.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_12")             # 視窗標題
label = Label(window)               # 標籤內容             
btn = Button(window,text="Message",command=msgShow)

label.pack()                      
btn.pack()

window.mainloop()






