# ch18_14.py
from tkinter import *
from tkinter.ttk import *
def treeview_sortColumn(col):
    global reverseFlag                  # 定義排序旗標全域變數
    lst = [(tree.set(st, col), st) 
            for st in tree.get_children("")]
    print(lst)                          # 列印串列
    lst.sort(reverse=reverseFlag)       # 排序串列
    print(lst)                          # 列印串列
    for index, item in enumerate(lst):  # 重新移動項目內容
        tree.move(item[1],"",index)
    reverseFlag = not reverseFlag       # 更改排序旗標
            
root = Tk()
root.title("ch18_14")
reverseFlag = False                     # 排序旗標註明是否反向排序

myStates = {"Illinois","California","Texas","Washington",
            "Jiangsu","Shandong","Guangdong","Fujian",
            "Mississippi","Kentucky","Florida","Indiana"}

tree = Treeview(root,columns=("states"),show="headings")
yscrollbar = Scrollbar(root)            # y軸scrollbar物件
yscrollbar.pack(side=RIGHT,fill=Y)      # y軸scrollbar包裝顯示
tree.pack()
yscrollbar.config(command=tree.yview)   # y軸scrollbar設定
tree.configure(yscrollcommand=yscrollbar.set)
# 建立欄標題
tree.heading("states",text="State")
# 建立內容
for state in myStates:                  # 第一次的Treeview內容
    tree.insert("",index=END,values=(state,))
# 點選標題欄將啟動treeview_sortColumn
tree.heading("#1",text="State",
             command=lambda c="states": treeview_sortColumn(c))

root.mainloop()




