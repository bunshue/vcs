# ch11_4.py
from tkinter import *
from tkinter import messagebox

def leave(event):                       # <Esc>事件處理程式
    ret = messagebox.askyesno("ch11_4","是否離開?")
    if ret == True:
        root.destroy()                  # 結束程式
    else:
        return
   
root = Tk()
root.title("ch11_4")

root.bind("<Escape>",leave)             # Esc鍵綁定leave函數
lab = Label(root,text="測試Esc鍵",      # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(padx=30,pady=30)

root.mainloop()








