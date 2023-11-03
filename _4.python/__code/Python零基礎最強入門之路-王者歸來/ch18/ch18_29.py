# ch18_29.py
from tkinter import *
from tkinter import messagebox

def myMsg():                    # 按Good Morning按鈕時執行
    messagebox.showinfo("My Message Box","Python tkinter早安")
    
window = Tk()
window.title("ch18_29")         # 視窗標題
window.geometry("300x160")      # 視窗寬300高160

Button(window,text="Good Morning",command=myMsg).pack()

window.mainloop()






