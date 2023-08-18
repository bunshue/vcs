# ch12_21.py
from tkinter import *
def getIndex(event):                    # 處理按一下選項
    lb.index = lb.nearest(event.y)      # 目前選項的索引
    
def dragJob(event):                     # 處理拖曳選項
    newIndex = lb.nearest(event.y)      # 目前選項的新索引
    if newIndex < lb.index:             # 往上拖曳
        x = lb.get(newIndex)            # 獲得新位置內容
        lb.delete(newIndex)             # 刪除新位置的內容
        lb.insert(newIndex+1,x)         # 放回原先新位置的內容
        lb.index = newIndex             # 選項的新索引
    elif newIndex > lb.index:           # 往下拖曳
        x = lb.get(newIndex)            # 獲得新位置內容
        lb.delete(newIndex)             # 刪除新位置的內容
        lb.insert(newIndex-1,x)         # 放回原先新位置的內容
        lb.index = newIndex             # 選項的新索引

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_21")                   # 視窗標題

lb = Listbox(root)                      # 建立Listbox          
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
    lb.bind("<Button-1>",getIndex)      # 按一下綁定getIndex
    lb.bind("<B1-Motion>",dragJob)      # 拖曳綁定dragJob
lb.pack(padx=10,pady=10)

root.mainloop()











