# ch8_8.py
from tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

root = Tk()
root.title("ch8_8")                         # 視窗標題
root.geometry("400x220")
# 以下建立標籤框架與和曲方塊
labFrame = LabelFrame(root,text="選擇最喜歡的運動")
sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(labFrame,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
labFrame.pack(ipadx=5,ipady=5,pady=10)      # 包裝定位標籤框架

btn = Button(root,text="確定",width=10,command=printInfo)
btn.pack()

root.mainloop()






