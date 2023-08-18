# ch17_21.py
from tkinter import *

def mySearch():
    text.tag_remove("found","1.0",END)              # 刪除標籤但是不刪除標籤定義
    start = "1.0"                                   # 設定搜尋起始位置
    key = entry.get()                               # 讀取搜尋關鍵字

    if (len(key.strip()) == 0):                     # 沒有輸入
        return
    while True:                                     # while迴圈搜尋        
        pos = text.search(key,start,END)            # 執行搜尋
        if (pos == ""):                             # 找不到結束while迴圈
            break
        text.tag_add("found",pos,"%s+%dc" % (pos, len(key)))    # 加入標籤
        start = "%s+%dc" % (pos, len(key))          # 更新搜尋起始位置
                         
root = Tk()
root.title("ch17_21")
root.geometry("300x180")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

entry = Entry()
entry.grid(row=0,column=0,padx=5,sticky=W+E)

btn = Button(root,text="搜尋",command=mySearch)
btn.grid(row=0,column=1,padx=5,pady=5)

# 建立Text
text = Text(root,undo=True)
text.grid(row=1,column=0,columnspan=2,padx=3,pady=5,
          sticky=N+S+W+E)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

text.tag_configure("found", background="yellow")    # 定義未來找到的標籤定義

root.mainloop()












