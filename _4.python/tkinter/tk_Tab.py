import tkinter as tk
from tkinter import ttk

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
title = "Tab 測試"
window.title(title)

# Notebook widget
notebook = ttk.Notebook(window)

#Tab第1頁
tab1 = ttk.Frame(notebook)
#加一些控件到Tab第1頁
label1 = ttk.Label(tab1, text = 'Text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text = 'Button in tab 1')
button1.pack()

#Tab第2頁
tab2 = ttk.Frame(notebook)
#加一些控件到Tab第2頁
label2 = ttk.Label(tab2, text = 'Text in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

#Tab第3頁
tab3 = ttk.Frame(notebook)
#加一些控件到Tab第3頁
button_exercise_1 = ttk.Button(tab3, text = 'button 1')
button_exercise_1.pack()
button_exercise_2 = ttk.Button(tab3, text = 'button 2')
button_exercise_2.pack()
label_exercise_2 = ttk.Label(tab3, text = 'Label')
label_exercise_2.pack()

notebook.add(tab1, text = '第一頁')
notebook.add(tab2, text = '第二頁')
notebook.add(tab3, text = '第三頁')
notebook.pack()

window.mainloop()
