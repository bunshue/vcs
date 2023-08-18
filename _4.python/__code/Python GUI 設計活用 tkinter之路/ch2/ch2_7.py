# ch2_7.py
from tkinter import *

root = Tk()
root.title("ch2_7")
label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="nw",
            wraplength = 40)
label.pack()  

root.mainloop()




