# ch17_22.py
from tkinter import *

def spellingCheck():
    text.tag_remove("spellErr","1.0",END)           # 刪除標籤但是不刪除標籤定義
    textwords = text.get("1.0",END).split()         # Text控件的內文
    print("字典內容\n",textwords)                   # 列印字典內容

    startChar = ("(")                               # 可能的啟始字元
    endChar = (".", ",", ":", ";", "?", "!", ")")   # 可能的結束字元
        
    start = "1.0"                                   # 檢查起始索引位置
    for word in textwords:     
        if word[0] in startChar:                    # 是否含非字母的啟始字元
            word = word[1:]                         # 刪除非字母的啟始字元         
        if word[-1] in endChar:                     # 是否含非字母的結束字元
            word = word[:-1]                        # 刪除非字母的結束字元                        
        if  (word not in dicts and word.lower() not in dicts):
            print("error", word)
            pos = text.search(word, start, END)
            text.tag_add("spellErr", pos, "%s+%dc" % (pos,len(word)))            
            pos = "%s+%dc" % (pos,len(word))     
    
def clrText():
    text.tag_remove("spellErr","1.0",END)
                            
root = Tk()
root.title("ch17_22")
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1) 

chkBtn = Button(toolbar,text="拼字檢查",command=spellingCheck)
chkBtn.pack(side=LEFT,padx=5,pady=5)

clrBtn = Button(toolbar,text="清除",command=clrText)
clrBtn.pack(side=LEFT,padx=5,pady=5)

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")

text.tag_configure("spellErr", foreground="red")    # 定義未來找到的標籤定義
with open("myDict.txt", "r") as dictObj:
    dicts = dictObj.read().split("\n")              # 自訂字典串列
    
root.mainloop()












