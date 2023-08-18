# ch7_9.py
from tkinter import *
# 以下是callback方法
def selAll():                               # 選取全部字串
    entry.select_range(0,END)
def deSel():                                # 取消選取
    entry.select_clear()
def clr():                                  # 刪除文字
    entry.delete(0,END)
def readonly():                             # 設定Entry狀態
    if var.get() == True:
        entry.config(state=DISABLED)        # 設為DISABLED
    else:
        entry.config(state=NORMAL)          # 設為NORMAL

root = Tk()
root.title("ch7_9")                         # 視窗標題

# 以下row=0建立Entry
entry = Entry(root)
entry.grid(row=0,column=0,columnspan=4,
           padx=5,pady=5,sticky=W)
# 以下row=1建立Button
btnSel = Button(root,text="選取",command=selAll)
btnSel.grid(row=1,column=0,padx=5,pady=5,sticky=W)
btnDesel = Button(root,text="取消選取",command=deSel)
btnDesel.grid(row=1,column=1,padx=5,pady=5,sticky=W)
btnClr = Button(root,text="刪除",command=clr)
btnClr.grid(row=1,column=2,padx=5,pady=5,sticky=W)
btnQuit = Button(root,text="結束",command=root.destroy)
btnQuit.grid(row=1,column=3,padx=5,pady=5,sticky=W)
# 以下row=2建立Checkboxes
var = BooleanVar()
var.set(False)
chkReadonly = Checkbutton(root,text="唯讀",variable=var,
                          command=readonly)
chkReadonly.grid(row=2,column=0)

root.mainloop()






