# ch13_7.py
from tkinter import *
from  tkinter.ttk  import *
 
root = Tk()
root.title("ch13_7")                        # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var)        # 建立Combobox
cb["value"] = ("Python","Java","C#","C")    # 設定選項內容
cb.current(0)                               # 設定預設選項
cb.pack(pady=10)

root.mainloop()










