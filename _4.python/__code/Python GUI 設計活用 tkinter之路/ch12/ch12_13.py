# ch12_13.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_13")           # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1,3))              # 列印索引1-3的項目

root.mainloop()











