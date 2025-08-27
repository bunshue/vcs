"""
# Python 測試 tkinter, Entry


"""

import sys
import random
import tkinter as tk

print("------------------------------------------------------------")  # 60個

print("用 Entry 和 grid 做 表格 1")

COLUMN1 = 10
ROW1 = 8


def set_numbers():
    for i in range(ROW1):
        for j in range(COLUMN1):
            cells1[i][j].set(random.randint(0, 9))


def get_numbers1():
    for i in range(ROW1):
        for j in range(COLUMN1):
            print(cells1[i][j].get(), end=" ")
        print()


def get_numbers2():
    values = [[eval(x.get()) for x in cells1[i]] for i in range(ROW1)]
    print(values)


window = tk.Tk()
window.geometry("700x800")
window.title("Entry 測試")

frame = tk.Frame(window, height=0, width=0, bg="pink", bd=5)  # Hold entries
frame.pack()

cells1 = []
for i in range(ROW1):
    cells1.append([])
    for j in range(COLUMN1):
        cells1[i].append(tk.StringVar())

for i in range(ROW1):
    for j in range(COLUMN1):
        tk.Entry(frame, width=8, justify=tk.RIGHT, textvariable=cells1[i][j]).grid(
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


print("用 Entry 和 grid 做 表格 2")


def get_numbers3():
    """
    # Get the numbers from the entries
    values = [[print(x.get())
               for x in cells2[i]] for i in range(9)]

    print('ok')
    """
    for i in range(ROW2):
        for j in range(COLUMN2):
            cc = cells2[i][j].get()
            if cc == "":
                print("X", end=" ")
            else:
                print(cc, end=" ")
        print()


ROW2 = 8
COLUMN2 = 12

frame = tk.Frame(window, bg="pink")

frame.pack()

cells2 = []  # A list of variables tied to entries
for i in range(ROW2):
    cells2.append([])
    for j in range(COLUMN2):
        cells2[i].append(tk.StringVar())

for i in range(ROW2):
    for j in range(COLUMN2):
        tk.Entry(frame, width=2, justify=tk.RIGHT, textvariable=cells2[i][j]).grid(
            row=i, column=j
        )

tk.Button(window, text="取得數字", command=get_numbers3).pack()

for i in range(ROW2):
    for j in range(COLUMN2):
        cells2[i][j].set("1")

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


def get_data():
    print("取得資料(變數) :", pdir.get())
    print("取得資料(控件) :", entry1.get())


pdir = tk.StringVar()
pdir.set("D:/_git/vcs/_1.data/______test_files1/_mp3/")

entry1 = tk.Entry(window, textvariable=pdir, width=50)
entry1.pack()

button1 = tk.Button(window, text="取得資料", command=get_data)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


""" 新進

print("密碼資料")
label = tk.Label(window, text="請輸入密碼: ").pack()
entry = tk.Entry(window, bg="yellow", fg="red", show="*").pack()


#entry內的文字靠右對齊
Entry(frame1, width = 5, justify = RIGHT).pack(side = LEFT)
Entry(frame1, width = 5, justify = RIGHT).pack(side = LEFT)
Entry(frame1, width = 5, justify = RIGHT).pack(side = LEFT)


"""
