from tkinter import *

master = Tk()

#w = Scale(master, from_=0, to=100)
w = Scale(master, from_=0, to=100, resolution=0.1)
w.pack()

w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()

print(w.get())

mainloop()


