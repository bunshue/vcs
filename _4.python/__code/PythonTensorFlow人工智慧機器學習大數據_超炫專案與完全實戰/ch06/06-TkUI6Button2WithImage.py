#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk 
from PIL import ImageTk, Image

win = tk.Tk()

def event1():
   print("btn1 pressed.")

img = ImageTk.PhotoImage(Image.open("python.png"))
btn1 =tk.Button(win,text="press me", image=img ,command=event1)
btn1.pack()
win.mainloop()


