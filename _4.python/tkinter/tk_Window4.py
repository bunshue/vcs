import tkinter as tk
from tkinter import ttk

extra_window = None

def button1_click():
    print('你按了子視窗的Button')

class Extra(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.title('extra window')
		self.geometry('300x400')
		ttk.Label(self, text = 'A label').pack()
		ttk.Button(self, text = 'A button', command = button1_click).pack()
		ttk.Label(self, text = 'another label').pack(expand = True)

def create_window():
	global extra_window
	print('開啟子視窗')
	extra_window = Extra()
	# extra_window = tk.Toplevel()
	# extra_window.title('extra window')
	# extra_window.geometry('300x400')
	# ttk.Label(extra_window, text = 'A label').pack()
	# ttk.Button(extra_window, text = 'A button').pack()
	# ttk.Label(extra_window, text = 'another label').pack(expand = True)

def close_window():
        print('關閉子視窗')
        if extra_window != None:
                extra_window.destroy()
                print('已關閉子視窗')
        else:
                print('無子視窗可關閉')

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')

button1 = ttk.Button(window, text = '開啟子視窗', command = create_window)
button1.pack(expand = True)

button2 = ttk.Button(window, text = '關閉子視窗', command = close_window)
button2.pack(expand = True)

# run 
window.mainloop()
