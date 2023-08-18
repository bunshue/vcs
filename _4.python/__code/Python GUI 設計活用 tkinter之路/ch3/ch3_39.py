# ch3_39.py
from tkinter import *

root = Tk()
root.title("ch3_39")
root.geometry("640x480")

night = PhotoImage(file="night.png")
label=Label(root,image=night)
label.place(relx=0.1,rely=0.1,relheight=0.8)

root.mainloop()




