# ch11_3.py
from tkinter import *
def enter(event):                       # Enter事件處理程式
    x.set("滑鼠進入Exit功能鈕")   
def leave(event):                       # Leave事件處理程式
    x.set("滑鼠離開Exit功能鈕")
    
root = Tk()
root.title("ch11_3")
root.geometry("300x180")

btn = Button(root,text="離開",command=root.destroy)
btn.pack(pady=30)
btn.bind("<Enter>",enter)               # 進入綁定enter
btn.bind("<Leave>",leave)               # 離開綁定leave

x = StringVar()
lab = Label(root,textvariable=x,        # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(pady=30)

root.mainloop()








