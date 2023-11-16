#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk 
from PIL import ImageTk, Image

win = tk.Tk()
img = ImageTk.PhotoImage(Image.open("python.png"))
label1 =tk.Label(win, image = img)
label1.pack()
win.mainloop()


