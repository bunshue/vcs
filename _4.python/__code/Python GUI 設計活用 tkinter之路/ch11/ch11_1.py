# ch11_1.py
from tkinter import *
def pythonClicked():            # Python核取方塊事件處理程式     
    if varPython.get():
        lab.config(text="選取Python")
    else:
        lab.config(text="取消選取Python")
def javaClicked():              # Java核取方塊事件處理程式
    if varJava.get():
        lab.config(text="選取Java")
    else:
        lab.config(text="取消選取Java")
def buttonClicked():            # Button按鈕事件處理程式
    lab.config(text="Button clicked")
    
root = Tk()
root.title("ch11_1")            # 視窗標題
root.geometry("300x180")        # 視窗寬300高160

btn = Button(root,text="Click me",command=buttonClicked)
btn.pack(anchor=W)
varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()








