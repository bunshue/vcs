'''
tk Treeview 範例
'''

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('800x400')
window.title('Treeview Example')

column_name = '序號', '英文名', '中文名', '體重'  #tuple
print(type(column_name))
print(column_name)
treeview = ttk.Treeview(window, column = column_name, show = "headings")
#treeview = ttk.Treeview(window, columns = ('序號', '英文名', '中文名', '體重'), show = 'headings')

'''
for col_name in column_name:
    treeview.heading(col_name, text = col_name)
'''
treeview.heading('序號', text = '序號')
treeview.heading('英文名', text = '英文名')
treeview.heading('中文名', text = '中文名')
treeview.heading('體重', text = '體重')

treeview.pack(fill = 'both', expand = True)
#treeview.pack(expand = True, fill = 'y') another

animal1 = 1, 'mouse', '老鼠', 1
animal2 = 2, 'panda', '貓熊', 123
animal3 = 3, 'penguin', '企鵝', 29
animal4 = 4, 'lion', '獅子', 270
treeview.insert('', tk.END, values = animal1)   #插入在最後
treeview.insert('', tk.END, values = animal2)   #插入在最後
treeview.insert('', tk.END, values = animal3)   #插入在最後
treeview.insert('', tk.END, values = animal4)   #插入在最後
treeview.insert(parent = '', index = 0, values = animal1) #插入在index = 0
treeview.insert(parent = '', index = 0, values = animal2) #插入在index = 0
treeview.insert(parent = '', index = 0, values = animal3) #插入在index = 0
treeview.insert(parent = '', index = 0, values = animal4) #插入在index = 0

treeview.insert(parent = '', index = 0, values = (3, 'aaa', 'bbb', 'ccc')) #插入在index = 0
treeview.insert(parent = '', index = tk.END, values = (5, 'XXXXX', 'YYYYY', 'ZZZZZ'))      #插入在最後

# events
def item_select(_):
    print('你點選了', treeview.selection())
    for i in treeview.selection():
        print(treeview.item(i)['values'])
    # treeview.item(treeview.selection())

def delete_items(_):
    print('你刪除了', treeview.selection())
    for i in treeview.selection():
        treeview.delete(i)

treeview.bind('<<TreeviewSelect>>', item_select)
treeview.bind('<Delete>', delete_items)

window.mainloop()
