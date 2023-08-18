# ch12_4.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_4")                    # 視窗標題
root.geometry("300x210")                # 視窗寬300高210

lb = Listbox(root,selectmode=MULTIPLE)  # 建立可以多選項的listbox
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

root.mainloop()








