# Python 測試 tkinter 1

import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

import time

slider = tk.Scale(window, from_=0, to=10)
slider.pack()

label = tk.Label(window)
label.pack()

#slider.set(clicks)
#label.config(text="Time: " + str(score))

window.mainloop()

