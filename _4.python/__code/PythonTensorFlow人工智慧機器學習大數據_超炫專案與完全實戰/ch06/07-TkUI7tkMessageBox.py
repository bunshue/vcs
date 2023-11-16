#!/usr/bin/python 
__author__ = "Powen Ko, www.powenko.com"
try:
  import Tkinter as tk
  import tkMessageBox
except ImportError:
  import tkinter as tk
  import tkinter.messagebox as tkMessageBox
  #import tkinter.messagebox

win = tk.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = tk.Button(win, text = "Say Hello", command = hello)
B1.pack()

win.mainloop()