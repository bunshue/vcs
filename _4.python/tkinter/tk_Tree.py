'''
tk tree 範例
'''

import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Tree Example")

column_name = 'aaa', 'bbb', 'ccc', 'ddd'
print(column_name)
tree = ttk.Treeview(window, column = column_name, show = "headings")
for col_name in column_name:
    tree.heading(col_name, text = col_name)
tree.pack(expand = True, fill = 'y')

number = 1, 2, 3, 4
print(type(number))
print(number)
tree.insert('', tkinter.END, values = number)
tree.insert('', tkinter.END, values = number)
tree.insert('', tkinter.END, values = number)
tree.insert('', tkinter.END, values = number)

window.mainloop()

