"""
# Python 測試 tkinter, Entry


"""

import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
title = "Entry 測試"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

# Entry與Label測試
tk.Label(text = 'Entry與Label同步改變Text').pack()

string = tk.StringVar()
entry = tk.Entry(window, textvariable = string)
entry.pack()
label = tk.Label(window, textvariable = string)
label.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

#Entry 預設值
entry_string = tk.StringVar(value = 'Entry 預設值')
entry = tk.Entry(window, textvariable = entry_string)
entry.pack()

print('Entry內容 :', entry_string.get())	#Entry取值

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def get_entry_text():
    print('取得帳號 :', entry1a.get())
    print('取得密碼 :', entry2a.get())


#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame3 = tk.Frame(window)
frame3.pack()

label1 = tk.Label(frame3, text = "Username:")
entry1a = tk.Entry(frame3)

label2 = tk.Label(frame3, text = "Password:")
entry2a = tk.Entry(frame3, show = "*")

button = tk.Button(frame3, text = "取得Entry資料", command = get_entry_text)

label1.pack()
entry1a.pack()
label2.pack()
entry2a.pack()
button.pack()

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame4 = tk.Frame(window)
frame4.pack()

#get username and password
username = tk.StringVar()
password = tk.StringVar()
entry1b = tk.Entry(frame4, textvariable = username, font = (14))
entry2b = tk.Entry(frame4, textvariable = password, font = (14), show = '*')
entry1b.pack()
entry2b.pack()

def get_entry_data():
    print('取得帳號 :', username.get())
    print('取得密碼 :', password.get())

button1 = tk.Button(frame4, command = get_entry_data, text = '取得Entry資料', font = (20))
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import random

print('用 Entry 和 grid 做 表格')

COLUMN = 10
ROW = 8

def set_numbers():
    for i in range(ROW):
        for j in range(COLUMN):
            cells[i][j].set(random.randint(0, 9))

def get_numbers1():
    for i in range(ROW):
        for j in range(COLUMN):
            print(cells[i][j].get())

def get_numbers2():
    values = [[eval(x.get()) for x in cells[i]] for i in range(ROW)]
    print(values)
    
window = tk.Tk()
window.geometry("600x800")
title = "Entry 測試"
window.title(title)

frame = tk.Frame(window, height = 0, width = 0, bg = 'pink', bd = 5) # Hold entries 
frame.pack()

cells = []
for i in range(ROW):
    cells.append([])
    for j in range(COLUMN):
        cells[i].append(tk.StringVar())
        
for i in range(ROW):
    for j in range(COLUMN):
        tk.Entry(frame, width = 8, justify = tk.RIGHT, textvariable = cells[i][j]).grid(row = i, column = j)
        
tk.Button(window, text = "填數字", command = set_numbers).pack()
tk.Button(window, text = "取得數字1", command = get_numbers1).pack()
tk.Button(window, text = "取得數字2", command = get_numbers2).pack()

set_numbers()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

# 輸入文字框中的字元被顯示為“*”
entry11 = tk.Entry(window, show = '*', width = 30)
entry11.pack()

# 輸入文字框中的字元被顯示為“#”
entry12 = tk.Entry(window, show = '#', width = 30)
entry12.pack()

# 設定背景色 設定前景色
entry13 = tk.Entry(window, bg = 'red', fg = 'blue')
entry13.pack()

# 設定勾選文字的背景色和前景色
entry14 = tk.Entry(window, selectbackground = 'red', selectforeground = 'gray')
entry14.pack()

# 將文字框設定為禁用
entry15 = tk.Entry(window, state = tk.DISABLED)
entry15.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

