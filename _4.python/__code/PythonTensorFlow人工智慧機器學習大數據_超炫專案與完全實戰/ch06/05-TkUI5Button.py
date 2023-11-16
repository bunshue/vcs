#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk

def event1():
   print("btn1 pressed.")

win = tk.Tk()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()
win.mainloop()






