import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')

# checkbutton
check1 = ttk.Checkbutton(
	window, 
	text = 'checkbox 1', 
	command = lambda: print('ccccc'),
	variable = 'ccccc',
	onvalue = 10,
	offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(
	window, 
	text = 'Checkbox 2',
	command = '')
check2.pack()

radio1 = ttk.Radiobutton(
	window, 
	text = 'Radiobutton 1', 
	value = 1, 
	variable = 'this is a lion-mouse',
	command = lambda: print('aaa'))
radio1.pack()

radio2 = ttk.Radiobutton(window, text = 'Radiobutton 2', value = 1, variable = 'aaaaaa')
radio2.pack()

def radio_func():
	print(check_bool.get())
	check_bool.set(False)
# data
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

# widgets
exercise_radio1 = ttk.Radiobutton(
	window, 
	text = 'Radio A', 
	value = 'A', 
	command = radio_func, 
	variable = radio_string)
exercise_radio2 = ttk.Radiobutton(
	window, 
	text = 'Radio B', 
	value = 'B', 
	command = radio_func, 
	variable = radio_string)
exercise_check = ttk.Checkbutton(
	window, 
	text = 'exercise check', 
	variable = check_bool, 
	command = lambda: print(radio_string.get()))

# layout
exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()

# run 
window.mainloop()

