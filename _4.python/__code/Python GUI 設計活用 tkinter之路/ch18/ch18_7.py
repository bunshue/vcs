# ch18_7.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_7")

asia = {"中國":"北京","日本":"東京","泰國":"曼谷","韓國":"首爾"}
euro = {"英國":"倫敦","法國":"巴黎","德國":"柏林","挪威":"奧斯陸"}
             
# 建立Treeview
tree = Treeview(root,columns=("capital"))
# 建立欄標題
tree.heading("#0",text="國家")             # 圖標欄位icon column
tree.heading("capital",text="首都")
# 建立id
idAsia = tree.insert("",index=END,text="Asia")
idEuro = tree.insert("",index=END,text="Europe")
# 建立idAsia底下內容
for country in asia.keys():
    tree.insert(idAsia,index=END,text=country,values=asia[country])
# 建立idEuro底下內容
for country in euro.keys():
    tree.insert(idEuro,index=END,text=country,values=euro[country])     
tree.pack()

root.mainloop()




