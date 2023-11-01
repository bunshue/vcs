# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("place版面佈局的示範")

plus=tk.Button(win, width=30, text="加法範例")
plus.place(x=10, y=10)
minus=tk.Button(win, width=30, text="減法範例")
minus.place(relx=0.5, rely=0.5, anchor="center")
multiply=tk.Button(win, width=30, text="乘法範例")
multiply.place(relx=0.5, rely=0)
divide=tk.Button(win, width=30, text="除法範例")
divide.place(relx=0.5, rely=0.7)

win.mainloop()
