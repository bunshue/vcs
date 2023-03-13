from tkinter import *
from tkinter.ttk import *

def selected(event):
    labelVar.set(cbVar.get())

window = Tk()

window.title('最喜歡的運動')

# 設定主視窗大小
w = 300
h = 160
size = str(w)+'x'+str(h)
window.geometry(size)

cbVar = StringVar()
cb = Combobox(window, textvariable=cbVar)
cb['value'] = ("籃球","排球","足球","其他")  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', selected)  #設定選取選項後執行的程式
cb.place(x=70, y=15)

labelVar = StringVar()  
labelShow = Label(window, textvariable=labelVar)
labelVar.set(cbVar.get())
labelShow.place(x=80, y=120)

window.mainloop()

