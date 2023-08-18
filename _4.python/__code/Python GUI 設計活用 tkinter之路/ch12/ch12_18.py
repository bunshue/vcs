# ch12_18.py
from tkinter import *
def itemsSelected(event):       # 列印所選結果
    obj = event.widget          # 取得事件的物件
    indexs = obj.curselection() # 取得索引
    for index in indexs:        # 將元組內容列出
        print(obj.get(index))
    print("----------")         # 區隔輸出
    
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_18")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root,selectmode=EXTENDED)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemsSelected) # 點選綁定
lb.pack(pady=5)

root.mainloop()











