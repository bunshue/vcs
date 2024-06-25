"""
# Python 測試 tkinter, Entry


"""

import sys
import random
import tkinter as tk

print("------------------------------------------------------------")  # 60個

print("用 Entry 和 grid 做 表格")

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
window.title("Entry 測試")

frame = tk.Frame(window, height=0, width=0, bg="pink", bd=5)  # Hold entries
frame.pack()

cells = []
for i in range(ROW):
    cells.append([])
    for j in range(COLUMN):
        cells[i].append(tk.StringVar())

for i in range(ROW):
    for j in range(COLUMN):
        tk.Entry(frame, width=8, justify=tk.RIGHT, textvariable=cells[i][j]).grid(
            row=i, column=j
        )

tk.Button(window, text="填數字", command=set_numbers).pack()
tk.Button(window, text="取得數字1", command=get_numbers1).pack()
tk.Button(window, text="取得數字2", command=get_numbers2).pack()

set_numbers()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# 輸入文字框中的字元被顯示為“*”
entry11 = tk.Entry(window, show="*", width=30)
entry11.pack()

# 輸入文字框中的字元被顯示為“#”
entry12 = tk.Entry(window, show="#", width=30)
entry12.pack()

# 設定背景色 設定前景色
entry13 = tk.Entry(window, bg="red", fg="blue")
entry13.pack()

# 設定勾選文字的背景色和前景色
entry14 = tk.Entry(window, selectbackground="red", selectforeground="gray")
entry14.pack()

# 將文字框設定為禁用
entry15 = tk.Entry(window, state=tk.DISABLED)
entry15.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
