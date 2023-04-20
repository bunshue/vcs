import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('500x500')

# widgets 
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'green', width = 10)
label3 = ttk.Label(window, text = 'Label 3', background = 'blue', width = 10)

# layout 
# label1.pack()
# label2.pack()

# grid 
window.columnconfigure((0,2), weight = 1, uniform = 'a')    #column 為  0 1 2
window.rowconfigure((0,2), weight = 1, uniform = 'a')       #row 為  0 1 2

'''
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0, sticky = 'nsew')
label3.grid(row = 0, column = 1)
'''
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1)
label3.grid(row = 0, column = 2)

# run
window.mainloop()
