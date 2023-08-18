# ch18_8.py
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
      
root = Tk()
root.title("ch18_8")

Style().configure("Treeview",rowheight=35)  # 格式化擴充row高度

info = ["鳳凰新聞App可以獲得中國各地最新消息",
        "瑞士國家鐵路App提供全瑞士火車時刻表",
        "可口可樂App是一個娛樂的軟件"]

tree = Treeview(root,columns=("說明"))
tree.heading("#0",text="App")           # 圖標欄位icon column
tree.heading("#1",text="功能說明")
tree.column("#1",width=300)             # 格式化欄標題

img1 = Image.open("news.jpg")           # 插入鳳凰新聞App圖示
imgObj1 = ImageTk.PhotoImage(img1)
tree.insert("",index=END,text="鳳凰新聞",image=imgObj1,values=info[0])

img2 = Image.open("sbb.jpg")            # 插入瑞士國家鐵路App圖示
imgObj2 = ImageTk.PhotoImage(img2)
tree.insert("",index=END,text="瑞士鐵路",image=imgObj2,values=info[1])

img3 = Image.open("coca.jpg")           # 插入可口可樂App圖示          
imgObj3 = ImageTk.PhotoImage(img3)
tree.insert("",index=END,text="可口可樂",image=imgObj3,values=info[2])    
tree.pack()

root.mainloop()




