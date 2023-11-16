#!/usr/bin/python
try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk
win = tk.Tk()

label1 =tk.Label(win,text="Hello World!")
label1.pack()
label2 =tk.Label(win,bg="yellow",text="Hello No2!",fg="red")
label2.pack()
label3 =tk.Label(win,text="Hello No3!")
label3.pack(side="top", anchor="w" )
label4 =tk.Label(win,text="Hello No4!")
label4.place(x=120, y=160)
label5 =tk.Label(win,text="Powen Ko",bg="#ff0000")
label5.place(x=120, y=140)
win.mainloop()