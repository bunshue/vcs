# Python 測試 tkinter 2

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


print('ListBox測試')

listbox = tk.Listbox(window)
listbox.pack()

listbox.insert(tk.END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(tk.END, item)



print('Label測試')

tk.Label(text="one").pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=5)

tk.Label(text="two").pack()


print('RadioButton測試')

v = tk.IntVar()

tk.Radiobutton(window, text="One", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(window, text="Two", variable=v, value=2).pack(anchor=tk.W)

MODES = [
    ("Monochrome", "1"),
    ("Grayscale", "L"),
    ("True color", "RGB"),
    ("Color separation", "CMYK"),
]

v = tk.StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = tk.Radiobutton(window, text=text, variable=v, value=mode)
    b.pack(anchor=tk.W)





window.mainloop()


