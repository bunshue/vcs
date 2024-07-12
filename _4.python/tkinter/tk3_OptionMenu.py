"""
OptionMenu 下拉式選單

"""

import sys
import tkinter as tk
import tkinter.ttk as ttk

print("------------------------------------------------------------")  # 60個

def printSelection():
    print("你選擇了 :", var.get())
    
window = tk.Tk()
window.geometry("300x180")

omTuple = ("鼠","牛","虎")             # tuple儲存表單項目
var = tk.StringVar()
var.set("虎")                           # 建立預設選項
var.set(omTuple[0])                         # 建立預設選項
#optionmenu = tk.OptionMenu(window,var,"鼠","牛","虎") same
optionmenu = tk.OptionMenu(window,var,*omTuple)  # 建立OptionMenu
optionmenu.pack(pady=10)

btn = tk.Button(window,text="打印",command=printSelection)
btn.pack(pady=10,anchor=tk.S,side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
測試OptionMenu(選擇項)
用來做多選一，選中的項在頂部顯
"""
def show():
    varLabel.set(var.get())

window = tk.Tk()

tupleVar = ("鼠","牛","虎", "兔", "龍")
var = tk.StringVar()
var.set(tupleVar[0])
optionMenu = tk.OptionMenu(window, var, *tupleVar)
optionMenu.pack()

varLabel = tk.StringVar()
tk.Label(window, textvariable=varLabel, width=20, height=3, bg='lightblue', fg='red').pack()
tk.Button(window, text='打印', command=show).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font

def familyChanged(event):  # font family更新
    f = Font(family=familyVar.get())  # 取得新font family
    text.configure(font=f)  # 更新text的font family


window = tk.Tk()
window.geometry("600x400")

# 建立font family OptionMenu
familyVar = tk.StringVar()
familyFamily = ("Arial", "Times", "Courier")
familyVar.set(familyFamily[0])
family = tk.OptionMenu(window, familyVar, *familyFamily, command=familyChanged)
family.pack(pady=2)

# 建立Text
text = tk.Text(window)
text.pack(fill=tk.BOTH, expand=True, padx=3, pady=2)
text.focus_set()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font


def familyChanged(event):  # font family更新
    f = Font(family=familyVar.get())  # 取得新font family
    text.configure(font=f)  # 更新text的font family


window = tk.Tk()
window.geometry("600x400")

# 建立font family OptionMenu
familyVar = tk.StringVar()
familyFamily = ("Arial", "Times", "Courier")
familyVar.set(familyFamily[0])
family = tk.OptionMenu(window, familyVar, *familyFamily, command=familyChanged)
family.pack(pady=2)

# 建立Text
text = tk.Text(window)
text.pack(fill=tk.BOTH, expand=True, padx=3, pady=2)
text.focus_set()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font


def familyChanged(event):  # font family更新
    f = Font(family=familyVar.get())  # 取得新font family
    text.configure(font=f)  # 更新text的font family


def weightChanged(event):  # weight family更新
    f = Font(weight=weightVar.get())  # 取得新font weight
    text.configure(font=f)  # 更新text的font weight


window = tk.Tk()
window.geometry("600x400")

# 建立工具列
toolbar = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
toolbar.pack(side=tk.TOP, fill=tk.X, padx=2, pady=1)

# 建立font family OptionMenu
familyVar = tk.StringVar()
familyFamily = ("Arial", "Times", "Courier")
familyVar.set(familyFamily[0])
family = tk.OptionMenu(toolbar, familyVar, *familyFamily, command=familyChanged)
family.pack(side=tk.LEFT, pady=2)

# 建立font weight OptionMenu
weightVar = tk.StringVar()
weightFamily = ("normal", "bold")
weightVar.set(weightFamily[0])
weight = tk.OptionMenu(toolbar, weightVar, *weightFamily, command=weightChanged)
weight.pack(pady=3, side=tk.LEFT)

# 建立Text
text = tk.Text(window)
text.pack(fill=tk.BOTH, expand=True, padx=3, pady=2)
text.focus_set()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font


def familyChanged(event):  # font family更新
    f = Font(family=familyVar.get())  # 取得新font family
    text.configure(font=f)  # 更新text的font family


def weightChanged(event):  # weight family更新
    f = Font(weight=weightVar.get())  # 取得新font weight
    text.configure(font=f)  # 更新text的font weight


window = tk.Tk()
window.geometry("600x400")

# 建立工具列
toolbar = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
toolbar.pack(side=tk.TOP, fill=tk.X, padx=2, pady=1)

# 建立font family OptionMenu
familyVar = tk.StringVar()
familyFamily = ("Arial", "Times", "Courier")
familyVar.set(familyFamily[0])
family = tk.OptionMenu(toolbar, familyVar, *familyFamily, command=familyChanged)
family.pack(side=tk.LEFT, pady=2)

# 建立font weight OptionMenu
weightVar = tk.StringVar()
weightFamily = ("normal", "bold")
weightVar.set(weightFamily[0])
weight = tk.OptionMenu(toolbar, weightVar, *weightFamily, command=weightChanged)
weight.pack(pady=3, side=tk.LEFT)

# 建立Text
text = tk.Text(window)
text.pack(fill=tk.BOTH, expand=True, padx=3, pady=2)
text.focus_set()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font


def familyChanged(event):  # font family更新
    f = Font(family=familyVar.get())  # 取得新font family
    text.configure(font=f)  # 更新text的font family


def weightChanged(event):  # weight family更新
    f = Font(weight=weightVar.get())  # 取得新font weight
    text.configure(font=f)  # 更新text的font weight


def sizeSelected(event):  # size family更新
    f = Font(size=sizeVar.get())  # 取得新font size
    text.configure(font=f)  # 更新text的font size


window = tk.Tk()
window.geometry("600x400")

# 建立工具列
toolbar = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
toolbar.pack(side=tk.TOP, fill=tk.X, padx=2, pady=1)

# 建立font family OptionMenu
familyVar = tk.StringVar()
familyFamily = ("Arial", "Times", "Courier")
familyVar.set(familyFamily[0])
family = tk.OptionMenu(toolbar, familyVar, *familyFamily, command=familyChanged)
family.pack(side=tk.LEFT, pady=2)

# 建立font weight OptionMenu
weightVar = tk.StringVar()
weightFamily = ("normal", "bold")
weightVar.set(weightFamily[0])
weight = tk.OptionMenu(toolbar, weightVar, *weightFamily, command=weightChanged)
weight.pack(pady=3, side=tk.LEFT)

# 建立font size Combobox
sizeVar = tk.IntVar()
size = ttk.Combobox(toolbar, textvariable=sizeVar)
sizeFamily = [x for x in range(8, 30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>", sizeSelected)
size.pack(side=tk.LEFT)

# 建立Text
text = tk.Text(window)
text.pack(fill=tk.BOTH, expand=True, padx=3, pady=2)
text.focus_set()

window.mainloop()

print("------------------------------------------------------------")  # 60個

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

print('------------------------------------------------------------')	#60個

