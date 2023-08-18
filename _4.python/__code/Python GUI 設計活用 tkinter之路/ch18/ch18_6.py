# ch18_6.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_6")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")             # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容,行號從1算起偶數行是用淺藍色底
tree.tag_configure("evenColor", background="lightblue") # 設定標籤
rowCount = 1                                # 行號從1算起
for state in stateCity.keys():
    if (rowCount % 2 == 1):                 # 如果True則是奇數行
        tree.insert("",index=END,text=state,values=stateCity[state])
    else:
        tree.insert("",index=END,text=state,values=stateCity[state],
                    tags=("evenColor"))     # 建立淺藍色底
    rowCount += 1                           # 行號數加1
tree.pack()

root.mainloop()




