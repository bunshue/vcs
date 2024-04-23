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

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
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

window.mainloop()



