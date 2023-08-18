# ch18_9.py
from tkinter import *
from tkinter.ttk import *
def treeSelect(event):
    widgetObj = event.widget                # 取得控件
    itemselected = widgetObj.selection()[0] # 取得選項
    col1 = widgetObj.item(itemselected,"text")  # 取得圖標欄內容
    col2 = widgetObj.item(itemselected,"values")[0] # 取得第0索引欄位內容
    str = "{0} : {1}".format(col1,col2)     # 取得所選項目內容
    var.set(str)                            # 設定狀態列內容
         
root = Tk()
root.title("ch18_9")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview
tree = Treeview(root,columns=("cities"),selectmode=BROWSE)
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

tree.bind("<<TreeviewSelect>>",treeSelect)  # Treeview控件Select發生
tree.pack()

var = StringVar()
label = Label(root,textvariable=var,relief="groove")    # 建立狀態列
label.pack(fill=BOTH,expand=True)

root.mainloop()




