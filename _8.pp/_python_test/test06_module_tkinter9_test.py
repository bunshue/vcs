from tkinter import *

master = Tk()

#w = Spinbox(master, from_=0, to=10)
w = Spinbox(master, values=(1, 2, 4, 8))
w.pack()

mainloop()
