#!/usr/bin/python 
try:
  import Tkinter as tk  # Python 2.x name
except ImportError:
  import tkinter as tk  # Python 3.x name
win = tk.Tk()
win.wm_title("Hello, Powenko")
win.minsize(width=666, height=480)
win.maxsize(width=666, height=480)
win.resizable(width=False, height=False)
win.mainloop()
