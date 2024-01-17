# ch18_33.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_33")             # 視窗標題
label = Label(window)               # 標籤內容

sun_gif = PhotoImage(file="sun.gif")
btn = Button(window,image=sun_gif,command=msgShow)

label.pack()                      
btn.pack()

window.mainloop()






