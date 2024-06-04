'''
"""
OptionMenu

"""


import tkinter as tk

print("------------------------------------------------------------")  # 60個


print('下拉式選單')

# order.py


def fnOK():
    global order,total		#宣告order,tota為全域變數
    f=selFood.get()  #取得使用者選擇的菜單
    n=selNum.get()   #取得使用者選擇的數量
    i=foods.index(f) #取得菜單在foods串列的索引值
    m=money[i]*n     #計算本次點餐的小計
    total+=m         #計算點餐的總計
    order+='{} {} 碗 {}元\n'.format(foods[i],n,m) #加入本次點餐的資訊
    lblOrder.config(text='{}總計： {} 元'.format(order,total))
    
window = tk.Tk()
window.title('台中肉圓點餐系統')
window.geometry('300x160')

foods = ['肉圓','冬粉湯','魚丸湯']  #菜單項目串列
money=[40,30,30]                  #單價串列
selFood = tk.StringVar()
selFood.set('肉圓')
opnFood=tk.OptionMenu(window, selFood, *foods)
opnFood.config(width=10,font=('微軟正黑體',14))
opnFood.grid(row=0,column=0,pady=5)
selNum = tk.IntVar()
selNum.set(1)
opnNum=tk.OptionMenu(window, selNum, 1,2,3,4,5)
opnNum.config(width=8,font=('微軟正黑體',14))
opnNum.grid(row=0,column=1)
lblOrder=tk.Label(window,text='')
lblOrder.grid(row=1,column=0,columnspan=2,sticky='w')
btnOK=tk.Button(window, text='確定', command=fnOK)
btnOK.grid(row=1,column=1,sticky='n')
order=''    #點餐的文字訊息
total=0     #點餐的總計

window.mainloop()


'''



print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()
root.geometry("300x180")

var = StringVar(root)
optionmenu = OptionMenu(root,var,"Python","Java","C")
optionmenu.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個


root = Tk()
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
var.set("Python")                           # 建立預設選項
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
var.set(omTuple[0])                         # 建立預設選項
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

def printSelection():
    print("The selection is : ", var.get())
    
root = Tk()
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
var.set("Python")                           # 建立預設選項
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack(pady=10)

btn = Button(root,text="Print",command=printSelection)
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()

print("------------------------------------------------------------")  # 60個


