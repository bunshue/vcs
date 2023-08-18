# ch2_26.py
from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("ch2_26")

myTitle = "一個人的極境旅行"
myContent = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""

lab1 = Label(root,text=myTitle,
             font="Helvetic 20 bold")
lab1.pack(padx=10,pady=10)

sep = Separator(root,orient=HORIZONTAL)
sep.pack(fill=X,padx=5)

lab2 = Label(root,text=myContent)
lab2.pack(padx=10,pady=10)

root.mainloop()








