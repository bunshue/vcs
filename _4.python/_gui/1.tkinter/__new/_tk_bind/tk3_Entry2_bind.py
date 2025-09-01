'''
綁定鍵盤滑鼠事件 Entry
'''

'''
Entry內可以接收Enter鍵
'''
import tkinter as tk
from tkinter import ttk

def print_contents(event):
    print("接收到訊息 : ", contents.get())

window = tk.Tk()
window.geometry("600x800")
title = '綁定鍵盤滑鼠事件 Entry'
window.title(title)

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

# Create the application variable.
contents = tk.StringVar()
# Set it to some value.
contents.set("Entry 訊息......................")
# Tell the entry widget to watch this variable.
entry["textvariable"] = contents

entry.bind('<FocusIn>', lambda event: print('Entry FocusIn'))
entry.bind('<FocusOut>', lambda event: print('Entry FocusOut'))
entry.bind('<Key-Return>', print_contents)

window.mainloop()

