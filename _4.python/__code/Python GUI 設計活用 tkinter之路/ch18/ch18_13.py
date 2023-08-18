# ch18_13.py
from tkinter import *
from tkinter.ttk import *
         
root = Tk()
root.title("ch18_13")

stateCity = {"Illinois":"芝加哥","California":"洛杉磯",
             "Texas":"休士頓","Washington":"西雅圖",
             "Jiangsu":"南京","Shandong":"青島",
             "Guangdong":"廣州","Fujian":"廈門",
             "Mississippi":"Oxford","Kentucky":"Lexington",
             "Florida":"Miama","Indiana":"West Lafeyette"}

tree = Treeview(root,columns=("cities"))
yscrollbar = Scrollbar(root)            # y軸scrollbar物件
yscrollbar.pack(side=RIGHT,fill=Y)      # y軸scrollbar包裝顯示
tree.pack()
yscrollbar.config(command=tree.yview)   # y軸scrollbar設定
tree.configure(yscrollcommand=yscrollbar.set)
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])

root.mainloop()




