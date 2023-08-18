# ch18_4.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_4")

# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 格式化欄位
tree.column("#1",anchor=CENTER,width=150)
tree.column("#2",anchor=CENTER,width=150)
# 建立內容
tree.insert("",index=END,text="伊利諾",values=("芝加哥","800"))
tree.insert("",index=END,text="加州",values=("洛杉磯","1000"))
tree.insert("",index=END,text="江蘇",values=("南京","900"))
tree.pack()

root.mainloop()




