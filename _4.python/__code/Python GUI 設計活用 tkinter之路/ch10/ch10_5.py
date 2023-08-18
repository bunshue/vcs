# ch10_5.py
from tkinter import *
from tkinter import messagebox

def myMsg1():
    ret = messagebox.askretrycancel("Test1","安裝失敗,再試一次?")
    print("安裝失敗",ret)
def myMsg2():
    ret = messagebox.askyesnocancel("Test2","編輯完成,是或否或取消?")
    print("編輯完成",ret)
root = Tk()
root.title("ch10_5")          # 視窗標題

Button(root,text="安裝失敗",command=myMsg1).pack()
Button(root,text="編輯完成",command=myMsg2).pack()

root.mainloop()






