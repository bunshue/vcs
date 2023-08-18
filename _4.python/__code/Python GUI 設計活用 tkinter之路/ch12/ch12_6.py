# ch12_6.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple"]

root = Tk()
root.title("ch12_6")                        # 視窗標題
root.geometry("300x210")                    # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)      # 拖曳可以選擇多選項
for fruit in fruits:                        # 建立水果項目
    lb.insert(END,fruit)
lb.insert(ACTIVE,"Orange","Grapes","Mango") # 前面補充建立3個項目
lb.pack(pady=10)

root.mainloop()








