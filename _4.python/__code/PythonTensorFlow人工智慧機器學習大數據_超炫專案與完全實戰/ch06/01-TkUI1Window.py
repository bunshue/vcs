#!/usr/bin/python

try:
  import Tkinter as tk    # python 2.x
except ImportError:
  import tkinter as tk    # python 3.x
win = tk.Tk()
# Python 2.x name # Python 3.x name
win.mainloop()
print("hello")

