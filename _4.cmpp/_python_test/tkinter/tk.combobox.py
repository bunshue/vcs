import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def combobox_selected(event):
    label_text.set(cbVar.get())

window = Tk()

window.title('最喜歡的運動')

# 設定主視窗大小
w = 300
h = 160
size = str(w)+'x'+str(h)
window.geometry(size)

cbVar = tk.StringVar()
cb = Combobox(window, textvariable=cbVar)
cb['value'] = ("籃球","排球","足球","其他")  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', combobox_selected)  #設定選取選項後執行的程式
cb.place(x=70, y=15)

label_text = tk.StringVar()  
label1 = Label(window, textvariable=label_text)
label_text.set(cbVar.get())
label1.place(x=80, y=120)

window.mainloop()

