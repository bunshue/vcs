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




def changeString():
    stringToCopy = entry.get()
    #stringToCopy = stringToCopy[::-1]
    #entry.delete(0, tk.END)
    entry.insert(0, stringToCopy)

entry = tk.Entry(window)
button = tk.Button(window, text="Change", command=changeString)

entry.pack()
button.pack()

class App:
    def __init__(self, master):

        frame = tk.Frame(master)
        frame.pack()

        self.button = tk.Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)
    def say_hi(self):
        print("hi there, everyone!")

app = App(window)




import time

slider = tk.Scale(window, from_=0, to=10)
slider.pack()

label = tk.Label(window)
label.pack()

#slider.set(clicks)
#label.config(text="Time: " + str(score))




print('Label 測試')
w = tk.Label(window, text="Hello, world!")
w.pack()

print('Canvas 測試')
colour = "#FF0000"
canvas = tk.Canvas(window, width=300, height=50, bg=colour)
canvas.pack()


print('Scale 測試')
slider = tk.Scale(window, from_=0, to=100)
slider.pack()


print('Checkbutton 測試')
var = tk.IntVar()

c = tk.Checkbutton(window, text="Expand", variable=var)
c.pack()



window.mainloop()

window.destroy() # optional; see description below


