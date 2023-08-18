# ch14_7.py
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
def msg():
    messagebox.showinfo("Notebook","歡迎使用Notebook")

root = Tk()
root.title("ch14_7")
root.geometry("300x160")

notebook = Notebook(root)           # 建立Notebook

frame1 = Frame()                    # 建立Frame1
frame2 = Frame()                    # 建立Frame2

label = Label(frame1,text="Python") # 在Frame1建立標籤控件
label.pack(padx=10,pady=10)
btn = Button(frame2,text="Help",command=msg) # 在Frame2建立按鈕控件
btn.pack(padx=10,pady=10)

notebook.add(frame1,text="頁次1")   # 建立頁次1同時插入Frame1
notebook.add(frame2,text="頁次2")   # 建立頁次2同時插入Frame2
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()











