# ch12_16_1.py
from tkinter import *
def itemSelected(event):        # 列出所選單一項目
    index = lb.curselection()   # 取得索引
    var.set(lb.get(index))      # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_16_1")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected) # 點選綁定
lb.pack(pady=5)

root.mainloop()











