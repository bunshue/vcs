#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk
  from tkinter import StringVar

def event1():
    t1=float(entry1.get())
    t1=t1/30.5
    print(t1)
    v.set(str(t1))

win = tk.Tk()
entry1=tk.Entry(win)
entry1.pack()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()
v = StringVar()
label1 =tk.Label(win,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")
win.mainloop()



