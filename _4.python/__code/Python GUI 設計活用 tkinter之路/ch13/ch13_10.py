# ch13_10.py
from tkinter import *
from  tkinter.ttk  import *
def comboSelection(event):                      # 顯示選項
    labelVar.set(var.get())                     # 同步標籤內容                      
    
root = Tk()
root.title("ch13_10")                           # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var)            # 建立Combobox
cb["value"] = ("Python","Java","C#","C")        # 設定選項內容
cb.current(0)                                   # 設定預設選項
cb.bind("<<ComboboxSelected>>",comboSelection)  # 綁定
cb.pack(side=LEFT,pady=10,padx=10)

labelVar = StringVar()
label = Label(root,textvariable=labelVar)       # 建立Label
labelVar.set(var.get())                         # 設定Label的初值
label.pack(side=LEFT)

root.mainloop()










