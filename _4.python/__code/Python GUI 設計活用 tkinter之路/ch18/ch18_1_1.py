# ch18_1_1.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_1_1")

# 建立Treeview
tree = Treeview(root,columns=("cities"),show="headings")
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("#1",text="City")
# 建立內容
tree.insert("",index=END,text="伊利諾",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉磯")
tree.insert("",index=END,text="江蘇",values="南京")
tree.pack()

root.mainloop()




