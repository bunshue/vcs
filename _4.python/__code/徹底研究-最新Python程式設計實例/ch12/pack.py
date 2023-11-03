# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局的示範")

plus=tk.Button(win, width=20, text="加法範例")
plus.pack(side="left")
minus=tk.Button(win, width=20, text="減法範例")
minus.pack(side="left")
multiply=tk.Button(win, width=20, text="乘法範例")
multiply.pack(side="left")
divide=tk.Button(win, width=20, text="除法範例")
divide.pack(side="left")

win.mainloop()
