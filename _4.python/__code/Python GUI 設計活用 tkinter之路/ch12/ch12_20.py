# ch12_20.py
from tkinter import *
def itemsSorted():                  # 排序
    if (var.get() == True):         # 如果設定
        revBool = True              # 大到小排序是True
    else:
        revBool = False             # 大到小排序是False
    listTmp = list(lb.get(0,END))   # 取得項目內容
    sortedList = sorted(listTmp,reverse=revBool) # 執行排序
    lb.delete(0,END)                # 刪除原先Listbox內容
    for item in sortedList:         # 將排序結果插入Listbox
        lb.insert(END,item)
            
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_20")               # 視窗標題

lb = Listbox(root)                  # 建立Listbox          
for fruit in fruits:                # 建立水果項目
    lb.insert(END,fruit)
lb.pack(padx=10,pady=5)

# 建立排序按鈕
btn = Button(root,text="排序",command=itemsSorted)
btn.pack(side=LEFT,padx=10,pady=5)

# 建立排序設定核取方塊
var = BooleanVar()
cb = Checkbutton(root,text="大到小排序",variable=var)
cb.pack(side=LEFT)

root.mainloop()











