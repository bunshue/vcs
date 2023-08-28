import tkinter as tk
from tkinter import ttk
 
win = tk.Tk()
win.title("Python图形界面") #添加标题 
label1=ttk.Label(win, text="选择数字")
label1.grid(column=1, row=0)    #添加一个标签，并将其列设置为1，行设置为0
 
#button被点击之后会被执行
def clickMe(): #当acction被点击时,该函数则生效"显示当前选择的数"
 
    print(numberChosen.current())#输出下所选的索引
 
    if numberChosen.current()==0 :#判断列表当前所选~~~~~~~~~~~
        label1.config(text="选了1")#注意，上面的label1如果直接.grid会出错
    if numberChosen.current()==1 :
        label1.config(text="选了6")
    if numberChosen.current()==2 :
        label1.config(text="选了第"+ str(numberChosen.current()+1)+"个") 
#按钮
action = ttk.Button(win, text="单击我", command=clickMe)  #创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=2, row=1) #设置其在界面中出现的位置,column代表列,row代表行 
# 创建一个下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 6, 3)     #设置下拉列表的值
numberChosen.grid(column=1, row=1)  #设置其在界面中出现的位置,column代表列,row代表行
numberChosen.current(0)    #设置下拉列表默认显示的值，0为numberChosen['values']的下标值 
win.mainloop()      #当调用mainloop()时,窗口才会显示出来
