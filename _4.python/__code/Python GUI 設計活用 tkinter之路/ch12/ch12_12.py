# ch12_12.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_12")           # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1))                # 列印索引1的項目

root.mainloop()








