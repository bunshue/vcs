from tkinter import *
from tkinter.ttk import *

def selected(event):
    labelVar.set(cbVar.get())

win = Tk()
win.title('最喜歡的運動')
win.geometry('300x160')

cbVar = StringVar()
cb = Combobox(win, textvariable=cbVar)
cb['value'] = ("籃球","排球","足球","其他")  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', selected)  #設定選取選項後執行的程式
cb.place(x=70, y=15)

labelVar = StringVar()  
labelShow = Label(win, textvariable=labelVar)
labelVar.set(cbVar.get())
labelShow.place(x=80, y=120)

win.mainloop()

