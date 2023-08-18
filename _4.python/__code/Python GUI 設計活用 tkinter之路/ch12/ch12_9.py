# ch12_9.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_9")                    # 視窗標題
root.geometry("300x210")                # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)  # 拖曳可以選擇多選項
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)    
lb.pack(pady=10)
lb.selection_set(0,3)                   # 預設選擇第0-3索引項目

root.mainloop()








