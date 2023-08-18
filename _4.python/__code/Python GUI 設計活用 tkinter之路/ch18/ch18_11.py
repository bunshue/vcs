# ch18_11.py
from tkinter import *
from tkinter.ttk import *
def removeItem():                   # 刪除所選項目
    ids = tree.selection()          # 取得所選項目
    for id in ids:                  # 所選項目可能很多所以用迴圈
        tree.delete(id)             # 刪除所選項目
def insertItem():
    state = stateEntry.get()        # 獲得stateEntry的輸入
    city = cityEntry.get()          # 獲得cityEntry的輸入
# 如果輸入資料未完全不往下執行
    if (len(state.strip())==0 or len(city.strip())==0):
        return
    tree.insert("",END,text=state,values=(city))    # 插入
    stateEntry.delete(0,END)        # 刪除stateEntry
    cityEntry.delete(0,END)         # 刪除cityEntry
         
root = Tk()
root.title("ch18_11")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 以下3行主要是應用在縮放視窗
root.rowconfigure(1,weight=1)       # row1會隨視窗縮放1:1變化
root.columnconfigure(1,weight=1)    # column1會隨視窗縮放1:1變化
root.columnconfigure(3,weight=1)    # column3會隨視窗縮放1:1變化

stateLab = Label(root,text="State :")   # 建立State :標籤
stateLab.grid(row=0,column=0,padx=5,pady=3,sticky=W)
stateEntry = Entry()                    # 建立State :文字方塊
stateEntry.grid(row=0,column=1,sticky=W+E,padx=5,pady=3)
cityLab = Label(root,text="City : ")    # 建立City :標籤
cityLab.grid(row=0,column=2,sticky=E)
cityEntry = Entry()                     # 建立City :文字方塊
cityEntry.grid(row=0,column=3,sticky=W+E,padx=5,pady=3)
# 建立Insert按鈕
inBtn = Button(root,text="插入",command=insertItem)
inBtn.grid(row=0,column=4,padx=5,pady=3)            
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
tree.grid(row=1,column=0,columnspan=5,padx=5,sticky=W+E+N+S)

rmBtn = Button(root,text="刪除",command=removeItem)   # 刪除鈕
rmBtn.grid(row=2,column=2,padx=5,pady=3,sticky=W)

root.mainloop()




