# ch13_9.py
from tkinter import *
from  tkinter.ttk  import *
def printSelection():                               # 列印選項
    print(var.get())
    
root = Tk()
root.title("ch13_9")                                # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var)                # 建立Combobox
cb["value"] = ("Python","Java","C#","C")            # 設定選項內容
cb.current(0)                                       # 設定預設選項
cb.pack(pady=10)

btn = Button(root,text="Print",command=printSelection) # 建立按鈕
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()










