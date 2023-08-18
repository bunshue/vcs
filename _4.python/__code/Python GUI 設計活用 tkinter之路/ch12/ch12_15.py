# ch12_15.py
from tkinter import *
def callback():                 # 列印檢查結果                
    print(lb.selection_includes(3))
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_15")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

lb = Listbox(root,selectmode=MULTIPLE)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=5)
btn = Button(root,text="Check",command=callback)
btn.pack(pady=5)

root.mainloop()











