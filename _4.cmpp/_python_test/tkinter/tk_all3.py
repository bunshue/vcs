import tkinter as tk
#import tkinter		#the same
from tkinter import *	#the same

window = tk.Tk()

print('Label 測試')
w = Label(window, text="Hello, world!")
w.pack()

print('Canvas 測試')
colour = "#FF0000"
canvas = tk.Canvas(window, height=300, width=300, bg=colour)
canvas.pack()


print('Scale 測試')
slider = tk.Scale(window, from_=0, to=100)
slider.pack()


print('Checkbutton 測試')
var = IntVar()

c = Checkbutton(window, text="Expand", variable=var)
c.pack()


'''

window = Tk()

#w = Spinbox(window, from_=0, to=10)
w = Spinbox(window, values=(1, 2, 4, 8))
w.pack()

window = Tk()

#w = Spinbox(window, from_=0, to=10)
w = Spinbox(window, values=(1, 2, 4, 8))
w.pack()

'''

window.mainloop()

