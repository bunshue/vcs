# ch2_12.py
from tkinter import *

root = Tk()
root.title("ch2_12")
label=Label(root,text="abcdefghijklmnopqrstuvwy",
            fg="blue",bg="lightyellow",
            wraplength=80,
            justify="right")
label.pack()  

root.mainloop()




