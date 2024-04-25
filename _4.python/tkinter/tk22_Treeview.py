"""
tk Treeview 範例
"""

import sys
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

# canvas 
# canvas = tk.Canvas(window, bg = 'white', scrollregion = (0,0,2000,5000))
# canvas.create_line(0,0,2000,5000, fill = 'green', width = 10)
# for i in range(100):
# 	l = randint(0,2000)
# 	t = randint(0,5000)
# 	r = l + randint(10,500)
# 	b = t + randint(10,500)
# 	color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
# 	canvas.create_rectangle(l,t,r,b, fill = color)
# canvas.pack(expand = True, fill = 'both')

# # mousewheel scrolling 
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))

# # scrollbar 
# scrollbar = ttk.Scrollbar(window, orient = 'vertical', command = canvas.yview)
# canvas.configure(yscrollcommand = scrollbar.set)
# scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

# # exercise: 
# # create a horizontal scrollbar at the bottom and use it to scroll the canvas left and right
# scrollbar_bottom = ttk.Scrollbar(window, orient = 'horizontal', command = canvas.xview)
# canvas.configure(xscrollcommand = scrollbar_bottom.set)
# scrollbar_bottom.place(relx = 0, rely = 1, relwidth = 1, anchor = 'sw')

# # also add an event to scroll left / right on Ctrl + mousewheel 
# canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), "units"))

# text 
# text = tk.Text(window)
# for i in range(1, 200):
# 	text.insert(f'{i}.0', f'text: {i} \n')
# text.pack(expand = True, fill = 'both')

# scrollbar_text = ttk.Scrollbar(window, orient = 'vertical', command = text.yview)
# text.configure(yscrollcommand = scrollbar_text.set)
# scrollbar_text.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

# treeview
table = ttk.Treeview(window, columns = (1,2), show = 'headings')
table.heading(1, text = 'First name')
table.heading(2, text = 'Last name')
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']
for i in range(100):
	table.insert(parent = '', index = tk.END, values = (choice(first_names), choice(last_names)))
table.pack(expand = True, fill = 'both')

scrollbar_table = ttk.Scrollbar(window, orient = 'vertical', command = table.yview)
table.configure(yscrollcommand = scrollbar_table.set)
scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
