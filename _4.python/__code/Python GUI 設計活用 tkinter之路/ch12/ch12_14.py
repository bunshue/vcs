# ch12_14.py
from tkinter import *
def callback():                 # 列印所選的項目                
    indexs = lb.curselection()
    for index in indexs:        # 取得索引值
        print(lb.get(index))    # 列印所選的項目
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_14")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

lb = Listbox(root,selectmode=MULTIPLE)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=5)
btn = Button(root,text="Print",command=callback)
btn.pack(pady=5)

root.mainloop()











