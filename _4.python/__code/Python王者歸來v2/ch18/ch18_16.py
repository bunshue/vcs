# ch18_16.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = Tk()
window.title("ch18_16")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
btn1.grid(row=2,column=0)
btn2 = Button(window,text="Quit",command=window.quit)
btn2.grid(row=2,column=1)

window.mainloop()






