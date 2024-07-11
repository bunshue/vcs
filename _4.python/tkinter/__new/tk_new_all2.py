import sys

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

print("------------------------------------------------------------")  # 60個

def printInfo():  # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (entry1.get(), entry2.get()))
    print('清除 entry1 entry2 的資料')
    entry1.delete(0, tk.END)  # 刪除account文字方塊的帳號內容
    entry2.delete(0, tk.END)  # 刪除pwd文字方塊的密碼內容

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 26")

label1 = tk.Label(window, text="Account")  # account標籤
label1.grid(row=1)

label2 = tk.Label(window, text="Password")  # pwd標籤
label2.grid(row=2)

entry1 = tk.Entry(window)  # 文字方塊account
entry2 = tk.Entry(window, show="*")  # 文字方塊pwd
entry1.insert(0, "Kevin")  # 預設Account內容
entry2.insert(0, "pwd")  # 預設pwd內容
entry1.grid(row=1, column=1)  # 定位文字方塊account
entry2.grid(row=2, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
button1 = tk.Button(window, text="Login", command=printInfo)
button1.grid(row=3, column=0, sticky=tk.W, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 27")

label1 = tk.Label(window, text="Account")  # account標籤
label1.grid(row=1)

label2 = tk.Label(window, text="Password")  # pwd標籤
label2.grid(row=2)

entry1 = tk.Entry(window)  # 文字方塊account
entry2 = tk.Entry(window, show="*")  # 文字方塊pwd
entry1.insert(1, "Kevin")  # 預設Account內容
entry2.insert(1, "pwd")  # 預設pwd內容
entry1.grid(row=1, column=1)  # 定位文字方塊account
entry2.grid(row=2, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
button1 = tk.Button(window, text="Login", command=printInfo)
button1.grid(row=3, column=0, sticky=tk.W, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 28")

# 以下是 LabelFrame 標籤框架
labelframe1 = tk.LabelFrame(window, text="資料驗證")  # 建立標籤框架
labelframe1.pack(padx=10, pady=5, ipadx=5, ipady=5)  # 包裝與定位標籤框架

label1 = tk.Label(labelframe1, text="Account")  # account標籤
label1.grid(row=0, column=0)

label2 = tk.Label(labelframe1, text="Password")  # pwd標籤
label2.grid(row=1, column=0)

entry1 = tk.Entry(labelframe1)  # 文字方塊account
entry1.grid(row=0, column=1)  # 定位文字方塊account
entry2 = tk.Entry(labelframe1, show="*")  # 文字方塊pwd
entry2.grid(row=1, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
button1 = tk.Button(labelframe1, text="Login", command=printInfo)
button1.grid(row=2, column=0, sticky=tk.W, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
