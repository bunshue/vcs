# Python 新進測試 14  tkinter

def choose():
    str = "你喜歡的球類運動："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + ball[i] + " "
    print(str)
    msg.set(str)

import tkinter as tk

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 600
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

choice = []
ball = ["足球", "籃球", "棒球"]
msg = tk.StringVar()
label1 = tk.Label(window, text="選擇喜歡的球類運動：")
label1.pack()

for i in range(0, len(ball)):
    tem = tk.IntVar()
    choice.append(tem)
    item = tk.Checkbutton(window, text=ball[i], variable=choice[i], command=choose)
    item.pack()
label2 = tk.Label(window, fg="red", textvariable=msg)
label2.pack()

window.mainloop()

