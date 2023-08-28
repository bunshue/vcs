import tkinter as tk
# 事件
def sys_out(even):
    from tkinter import messagebox
    if messagebox.askokcancel('Exit','Confirm to exit?'):
        root.destroy()
root = tk.Tk()
root.geometry('300x200')
#绑定事件到Esc键，当按下Esc键就会调用sys_out函数，弹出对话框
root.bind('<Escape>',sys_out)
root.mainloop()
