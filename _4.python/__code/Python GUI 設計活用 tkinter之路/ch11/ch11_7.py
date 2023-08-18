# ch11_7.py
from tkinter import *
def buttonClicked(event):           # Button按鈕事件處理程式
    print("I like tkinter")

# 所傳遞的物件onoff是btn物件    
def toggle(onoff):                  # 切換綁定
    if var.get() == True:           # 如果True綁定
        onoff.bind("<Button-1>",buttonClicked)
    else:                           # 如果False不綁定
        onoff.unbind("<Button-1>")
    
root = Tk()
root.title("ch11_7")                # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

btn = Button(root,text="tkinter")   # 建立按鈕tkinter
btn.pack(anchor=W,padx=10,pady=10)

var = BooleanVar()                  # 建立核取方塊
cbtn = Checkbutton(root,text="bind/unbind",variable=var,
                   command=lambda:toggle(btn))
cbtn.pack(anchor=W,padx=10)

root.mainloop()








