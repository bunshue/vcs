# ch18_10.py
from tkinter import *
from tkinter.ttk import *
def removeItem():                   # 刪除所選項目
    iids = tree.selection()         # 取得所選項目
    for iid in iids:                # 所選項目可能很多所以用迴圈
        tree.delete(iid)            # 刪除所選項目
         
root = Tk()
root.title("ch18_10")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview,可以有多項選擇selectmode=EXTENDED
tree = Treeview(root,columns=("cities"),selectmode=EXTENDED)
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.pack()

rmBtn = Button(root,text="Remove",command=removeItem)   # 刪除鈕
rmBtn.pack(pady=5)

root.mainloop()




