import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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
title = "Frame 測試"
window.title(title)

# slider
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(
	window, 
	command = lambda value: progress.stop(), 
	from_ = 0, 
	to = 25,
	length = 300,
	orient = 'horizontal',
	variable = scale_float)
scale.pack()

# progress bar
progress = ttk.Progressbar(
	window, 
	variable = scale_float, 
	maximum = 25,
	orient = 'horizontal',
	mode = 'indeterminate',
	length = 400)
progress.pack()

# progress.start(1000)

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()

# exercise 
# create a progress that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the progress bar
exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(window, orient = 'vertical', variable = exercise_int)
exercise_progress.pack()
exercise_progress.start()

label = ttk.Label(window, textvariable = exercise_int)
label.pack()

exercise_scale = ttk.Scale(window, variable = exercise_int, from_ = 0, to = 100)
exercise_scale.pack()

window.mainloop()

