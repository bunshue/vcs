import tkinter as tk
from tkinter import ttk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)


spinbox = ttk.Spinbox(window, from_=0, to=100, increment=0.1)
spinbox.pack()

#w = ttk.Spinbox(window, from_=0, to=10)
w = ttk.Spinbox(window, values=(1, 2, 4, 8))
w.pack()

#w = ttk.Spinbox(window, from_=0, to=10)
w = ttk.Spinbox(window, values=(1, 2, 4, 8))
w.pack()


window.mainloop()

