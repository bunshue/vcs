"""
# 用 Notebook 元件 頁箋

"""

import sys

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.ttk as ttk


def msg():
    print("你按了button")


window = tk.Tk()
window.title("")
window.geometry("640x480")

notebook = ttk.Notebook(window)  # 建立Notebook

frame1 = tk.Frame()  # 建立Frame1
frame2 = tk.Frame()  # 建立Frame2

label = tk.Label(frame1, text="Python")  # 在Frame1建立標籤控件
label.pack(padx=10, pady=10)
btn = tk.Button(frame2, text="Help", command=msg)  # 在Frame2建立按鈕控件
btn.pack(padx=10, pady=10)

notebook.add(frame1, text="頁次1")  # 建立頁次1同時插入Frame1
notebook.add(frame2, text="頁次2")  # 建立頁次2同時插入Frame2
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=tk.TRUE)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import ttk

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
# size = str(W) + 'x' + str(H)
# size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = "Tab 測試"
window.title(title)

# Notebook widget
notebook = ttk.Notebook(window)

# Tab第1頁
tab1 = ttk.Frame(notebook)
# 加一些控件到Tab第1頁
label1 = ttk.Label(tab1, text="Text in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text="Button in tab 1")
button1.pack()

# Tab第2頁
tab2 = ttk.Frame(notebook)
# 加一些控件到Tab第2頁
label2 = ttk.Label(tab2, text="Text in tab 2")
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

# Tab第3頁
tab3 = ttk.Frame(notebook)
# 加一些控件到Tab第3頁
button_exercise_1 = ttk.Button(tab3, text="button 1")
button_exercise_1.pack()
button_exercise_2 = ttk.Button(tab3, text="button 2")
button_exercise_2.pack()
label_exercise_2 = ttk.Label(tab3, text="Label")
label_exercise_2.pack()

notebook.add(tab1, text="第一頁")
notebook.add(tab2, text="第二頁")
notebook.add(tab3, text="第三頁")
notebook.pack()

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
