# ch18_12.py
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
def doubleClick(event):
    e = event.widget                        # 取得事件控件
    iid = e.identify("item",event.x,event.y)    # 取得連按2下項目id
    state = e.item(iid,"text")              # 取得State
    city = e.item(iid,"values")[0]          # 取得City
    str = "{0} : {1}".format(state,city)    # 格式化
    messagebox.showinfo("Double Clicked",str)   # 輸出
         
root = Tk()
root.title("ch18_12")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.bind("<Double-1>",doubleClick)     # 連按2下綁定doubleClick方法
tree.pack()

root.mainloop()




