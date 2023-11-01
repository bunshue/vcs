# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("grid版面佈局的示範")

plus=tk.Button(win, width=20, text="加法範例")
plus.grid(column=0,row=0)
minus=tk.Button(win, width=20, text="減法範例")
minus.grid(column=0,row=1)
multiply=tk.Button(win, width=20, text="乘法範例")
multiply.grid(column=1,row=0)
divide=tk.Button(win, width=20, text="除法範例")
divide.grid(column=1,row=1)

win.mainloop()
