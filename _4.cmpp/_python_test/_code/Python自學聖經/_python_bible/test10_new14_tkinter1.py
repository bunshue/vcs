# Python 新進測試 14  tkinter

def clickme():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了！")
    if(btntext.get() == "按我！"):
        btntext.set("回復原來文字！")
    else:
        btntext.set("按我！")

# 導入套件
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

labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(window, fg="red", textvariable=labeltext)
labeltext.set("歡迎光臨Tkinter！")
label1.pack()

button1 = tk.Button(window, textvariable=btntext, command=clickme)
btntext.set("按我！")
button1.pack()

window.mainloop()







