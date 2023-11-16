#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk 
from PIL import ImageTk, Image

win = tk.Tk()

def event1():
	value1=entry1.get()
	print(value1)
	value2=float(value1)
	value2=value2*0.15
	print(value2)
	label1.config(text='Button Pressed')


label1 =tk.Label(win,text="Hello World!")
label1.pack()

entry1=tk.Entry(win)
entry1.pack()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()
win.mainloop()


""" 
TW

________


buton

US_____

"""


"""   US ______
     button
     ________

"""





