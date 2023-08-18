# ch17_10.py
from tkinter import *

def selectedText():                             # 列印所選的文字
    try:
        selText = text.get(SEL_FIRST,SEL_LAST)
        print("選取文字: ",selText)
    except TclError:
        print("沒有選取文字")
      
root = Tk()
root.title("ch17_10")
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print selection",command=selectedText)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song")    # 插入文字

root.mainloop()


