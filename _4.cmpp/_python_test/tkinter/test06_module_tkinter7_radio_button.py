from tkinter import *

master = Tk()

v = IntVar()

Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)


MODES = [
    ("Monochrome", "1"),
    ("Grayscale", "L"),
    ("True color", "RGB"),
    ("Color separation", "CMYK"),
]

v = StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = Radiobutton(master, text=text, variable=v, value=mode)
    b.pack(anchor=W)

mainloop()

