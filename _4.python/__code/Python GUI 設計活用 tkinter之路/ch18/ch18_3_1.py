# ch18_3_1.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_3_1")

list1 = ["芝加哥","800"]               # 以串列方式設定欄內容         
list2 = ["洛杉磯","1000"]
list3 = ["南京","900"]
# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 建立內容
tree.insert("",index=END,text="伊利諾",values=list1)
tree.insert("",index=END,text="加州",values=list2)
tree.insert("",index=END,text="江蘇",values=list3)
tree.pack()

root.mainloop()




