'''
tk Treeview 範例
'''

import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Tree Example")

column_name = '序號', '英文名', '中文名', '體重'
print(column_name)
treeview = ttk.Treeview(window, column = column_name, show = "headings")
for col_name in column_name:
    treeview.heading(col_name, text = col_name)
treeview.pack(expand = True, fill = 'y')

animal1 = 1, 'mouse', '老鼠', 1
animal2 = 2, 'panda', '貓熊', 123
animal3 = 3, 'penguin', '企鵝', 29
animal4 = 4, 'lion', '獅子', 270
treeview.insert('', tkinter.END, values = animal1)
treeview.insert('', tkinter.END, values = animal2)
treeview.insert('', tkinter.END, values = animal3)
treeview.insert('', tkinter.END, values = animal4)

window.mainloop()

