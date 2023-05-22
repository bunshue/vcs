def click1():
    textvar.set("我已經被按過了！")

import tkinter as tk

win = tk.Tk()

textvar = tk.StringVar()
button1 = tk.Button(win, textvariable=textvar, command=click1)
textvar.set("按鈕")
button1.pack()

win.mainloop()
