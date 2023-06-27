import tkinter as tk
import tkinter.ttk as ttk

def combobox_selected(event):
    label_text.set(cbVar.get())

#Combobox 下拉選單是 tkinter 的 ttk 加強模組裡的元件
print('Combobox 測試')
window = tk.Tk()

# 設定主視窗大小
window.geometry('300x300')

cbVar = tk.StringVar()
cb = ttk.Combobox(window, textvariable = cbVar)   #下拉式選單元件
cb['value'] = ("籃球","排球","足球","其他")  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', combobox_selected)  #設定選取選項後執行的程式
cb.place(x=70, y=15)

label_text = tk.StringVar()  
label1 = tk.Label(window, textvariable = label_text)
label_text.set(cbVar.get())
label1.place(x = 80, y = 120)

'''
import tkinter as tk
from tkinter import ttk

def show():
    a.set(f'{box.current()}:{box.get()}')    # 顯示索引值與內容

a = tk.StringVar()                           # 定義變數
a.set('')

label = tk.Label(window, textvariable=a)       # 建立標籤，內容為變數
label.pack()

box = ttk.Combobox(window, width=15, values=['七龍珠','海賊王','鬼滅之刃','灌籃高手','排球少年'])
box.pack()

btn = tk.Button(window, text='顯示', command=show)   # 建立按鈕，點擊按鈕時，執行 show 函式
btn.pack()
'''


window.mainloop()

