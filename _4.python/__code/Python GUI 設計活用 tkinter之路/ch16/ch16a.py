# ch16_1.py
from tkinter import *
from tkinter import messagebox

def hello():
    messagebox.showinfo("Hello","歡迎使用功能表")

root = Tk()
root.title("ch16_1")
root.geometry("300x180")

# 建立最上層功能表
menubar = Menu(root)
menubar.add_command(label="Hello!",command=hello)
menubar.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()












