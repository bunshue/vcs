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

