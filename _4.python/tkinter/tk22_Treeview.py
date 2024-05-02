"""
tk Treeview 範例
"""

import sys
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個
'''
window = tk.Tk()
window.geometry('800x400')
window.title('Treeview範例')

#設定 Treeview 之標題
column_name = ('第0欄', '第1欄', '第2欄', '第3欄') #tuple
print(type(column_name))
print(column_name)

treeview = ttk.Treeview(window, columns = column_name, show = "headings")

#加入標題方法一
treeview.heading('第0欄', text = '第0欄')
treeview.heading('第1欄', text = '第1欄')
treeview.heading('第2欄', text = '第2欄')
treeview.heading('第3欄', text = "第3欄")

""" 加入標題方法二
for col_name in column_name:
    treeview.heading(col_name, text = col_name)
"""

#treeview.grid(row = 5, column = 0, columnspan = 3, padx = 20, pady = 10)#another
treeview.pack(fill = 'both', expand = True)
#treeview.pack(expand = True, fill = 'y') another

animal1 = 1, 'aaaa', 'AAAA', 111
animal2 = 2, 'bbbb', 'BBBB', 222
animal3 = 3, 'cccc', 'CCCC', 333
animal4 = 4, 'dddd', 'DDDD', 444

print('加入項目到 Treeview, 插入在最後 4 筆')
treeview.insert('', tk.END, values = animal1)   #加入項目到 Treeview, 插入在最後
treeview.insert('', tk.END, values = animal2)   #加入項目到 Treeview, 插入在最後
treeview.insert('', tk.END, values = animal3)   #加入項目到 Treeview, 插入在最後
treeview.insert('', tk.END, values = animal4)   #加入項目到 Treeview, 插入在最後

print('加入項目到 Treeview, 插入在 index = 0')
treeview.insert(parent = '', index = 0, values = animal3) #插入在index = 0
treeview.insert(parent = '', index = 0, values = animal3) #插入在index = 0
treeview.insert(parent = '', index = 0, values = animal3) #插入在index = 0
treeview.insert(parent = '', index = 0, values = animal3) #插入在index = 0
treeview.insert('', 0, values = animal2) #插入在index = 0

print('加入項目到 Treeview, 插入在最後 1 筆')
treeview.insert(parent = '', index = tk.END, values = (5, 'XXXXX', 'YYYYY', 'ZZZZZ'))      #插入在最後

"""
item = treeview.insert("", tk.END, text="Item 1")
treeview.insert(item, tk.END, text="Subitem 1")
"""

def show_info():
    """
    # Get the text of the item whose Id is stored in `my_iid`.
    text = treeview.item(my_iid, option="text")
    # Display it within a message box.
    messagebox.showinfo(title="Item Info", message=text)
    
    x=treeview.get_children()
    for item in x:
        print(x)
    """
    print ('show_info')
    for item in treeview.selection():
        item_text = treeview.item(item,"values")
        print(item_text)

def item_select(_):
    print('你點選了', treeview.selection())
    for i in treeview.selection():
        print(treeview.item(i)['values'])
    # treeview.item(treeview.selection())

def delete_items(_):
    print('你刪除了', treeview.selection())
    for i in treeview.selection():
        treeview.delete(i)

def treeview_bind_function1(_):
    print('AAAA')

def treeview_bind_function2(_):
    print('BBBB')

def treeview_bind_function3(_):
    print('CCCC')

def treeview_bind_function4(_):
    print('DDDD')

treeview.bind('<<TreeviewSelect>>', item_select)
treeview.bind('<Delete>', delete_items)

treeview.bind('<<TreeviewOpen>>', treeview_bind_function1)
treeview.bind('<<TreeviewClose>>', treeview_bind_function2)
treeview.bind('<1>', treeview_bind_function3)

treeview.bind('<ButtonRelease-1>', treeview_bind_function4)


#刪除 Treeview 內的所有項目
#treeview.delete(*treeview.get_children())

button = ttk.Button(text="Show info", command=show_info)
button.pack()

window.mainloop()

sys.exit()

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

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview in Tk")
treeview = ttk.Treeview()

print('加入項目到 Treeview, 插入在最後 1 筆')
item = treeview.insert(parent = '', index = tk.END, text="主項目")#插入在最後
print('加入子項目')
subitem = treeview.insert(item, tk.END, text="加入子項目")
print('加入子項目')
treeview.insert(subitem, tk.END, text="加入孫項目")

treeview.pack()
root.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import messagebox, ttk


root = tk.Tk()
root.title("Treeview in Tk")
treeview = ttk.Treeview()
my_iid = "unique_id"
treeview.insert("", tk.END, text="Item 1", iid=my_iid)
treeview.pack()

button = ttk.Button(text="Show info", command=show_info)
button.pack()

root.mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter
from tkinter import ttk  # 導入內部包

li = ['王記','12','男']
root = tkinter.Tk()
root.title('測試')
tree = ttk.Treeview(root,columns=['1','2','3'],show='headings')
tree.column('1',width=100,anchor='center')
tree.column('2',width=100,anchor='center')
tree.column('3',width=100,anchor='center')
tree.heading('1',text='姓名')
tree.heading('2',text='學號')
tree.heading('3',text='性別')
tree.insert('','end',values=li)
tree.grid()

root.mainloop()

'''
print("------------------------------------------------------------")  # 60個

print('標題點擊排序')

import random
from tkinter import ttk
from tkinter import *
 
root = Tk()
columns=("aaa","bbb","ccc")
treeview=ttk.Treeview(root,height=18,show="headings",columns=columns )#表格 
 
treeview.column('aaa', width=50, anchor='center') 
treeview.column('bbb', width=100, anchor='center') 
treeview.column('ccc', width=80, anchor='center')
treeview.heading('aaa', text='列1')
treeview.heading('bbb', text='列2')
treeview.heading('ccc', text='列3')
treeview.pack(side=LEFT,fill=BOTH)
for i in range(10):
    treeview.insert('',i,values=(str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9))))
 
 
def treeview_sort_column(tv, col, reverse):#Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    print(tv.get_children(''))
    l.sort(reverse=reverse)#排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):#根據排序后索引移動
        tv.move(k, '', index)
        print(k)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))#重寫標題，使之成為再點倒序的標題
 
'''
#莫名其妙？？？？寫循環的話只有最后一列管用,看論壇說的好像是python2.7管用
for col in columns:
    treeview.heading(col, text=col, command=lambda: treeview_sort_column(treeview, col, False))
'''
 
'''
#基本用法（上邊注釋的只有最后一列管用、索性手工試驗一下可用性，證實可行）
treeview.heading('a', text='123', command=lambda: treeview_sort_column(tree, 'a', False))#重建標題，添加控件排序方法
treeview.heading('b', text='111', command=lambda: treeview_sort_column(tree, 'b', False))#重建標題，添加控件排序方法
treeview.heading('c', text='223', command=lambda: treeview_sort_column(tree, 'c', False))#重建標題，添加控件排序方法
'''
 
#這個代碼對于python3就管用了
for col in columns:#給所有標題加（循環上邊的“手工”）
    treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeview, _col, False))
 
root.mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter
from tkinter import ttk  # 导入内部包
 
li = ['王记','12','男']
root = tkinter.Tk()
root.title('测试')
tree = ttk.Treeview(root,columns=['1','2','3'],show='headings')

tree.column('1',width=100,anchor='center')
tree.column('2',width=100,anchor='center')
tree.column('3',width=100,anchor='center')

tree.heading('1',text='姓名')
tree.heading('2',text='学号')
tree.heading('3',text='性别')

tree.insert('','end',values=li)
tree.grid()

 
def treeviewClick(event):#单击
    print ('单击')
    for item in tree.selection():
        item_text = tree.item(item,"values")
        print(item_text[0])#输出所选行的第一列的值
 
tree.bind('<ButtonRelease-1>', treeviewClick)#绑定单击离开事件===========
 
root.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




"""
Treeview之各種點擊事件

鼠標左鍵單擊按下	1/Button-1/ButtonPress-1
鼠標左鍵單擊松開	ButtonRelease-1
鼠標右鍵單擊	3
鼠標左鍵雙擊	Double-1/Double-Button-1
鼠標右鍵雙擊	Double-3
鼠標滾輪單擊	2
鼠標滾輪雙擊	Double-2
鼠標移動	B1-Motion
鼠標移動到區域	Enter
鼠標離開區域	Leave
獲得鍵盤焦點	FocusIn
失去鍵盤焦點	FocusOut
鍵盤事件	Key
回車鍵	Return
控件尺寸變	Configure

"""
