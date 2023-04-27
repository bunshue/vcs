from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry("200x200")
def func1():
    if tkinter.messagebox.askyesno("关闭窗口","确认关闭窗口吗"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW",func1)

root.mainloop()
