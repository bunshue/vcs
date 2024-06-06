import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

print("------------------------------------------------------------")  # 60個
'''
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Spin 測試"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

spinbox = ttk.Spinbox(window, from_=0, to=100, increment=0.1)
spinbox.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#w = ttk.Spinbox(window, from_=0, to=10)
w = ttk.Spinbox(window, values=(1, 2, 4, 8))
w.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#w = ttk.Spinbox(window, from_=0, to=10)
w = ttk.Spinbox(window, values=(1, 2, 4, 8))
w.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
	window, 
	from_ = 3, 
	to = 20, 
	increment = 3, 
	command = lambda: print(spin_int.get()),
	textvariable = spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['value'] = (1,2,3,4,5)
spin.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# create a spinbox that contains the letters A B C D E 
# and print the value whenever the value is decreased

exercise_letters = ('A', 'B', 'C', 'D', 'E')
exercise_string = tk.StringVar(value = exercise_letters[0])
exercise_spin = ttk.Spinbox(window, textvariable = exercise_string, values = exercise_letters)
exercise_spin.pack()

exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_string.get()))

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def spinbox_select():
    selected_month = month.get()
    lab_result.config(text=selected_month)    

print("試題與測驗分析程式")

default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
month = tk.IntVar()
month.set(1)
spinbox = tk.Spinbox(window, from_=1, to=12, textvariable=month, command=spinbox_select, font=default_font)
spinbox.pack(padx=10, pady=10)
lab_result = tk.Label(window, font=default_font, fg='black')
lab_result.pack(padx=10, pady=(5,10))

window.mainloop()
'''
print("------------------------------------------------------------")  # 60個


from tkinter import *
    
window = Tk()
window.geometry("600x400")

spin = Spinbox(window,from_=10,to=30,increment=2)
spin.pack(pady=20)

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def printInfo():        # 列印顯示的值
    print(sp.get())
    
window = Tk()
window.geometry("600x400")

sp = Spinbox(window,from_ = 0,to = 10,           
             command = printInfo)
sp.pack(pady=10,padx=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())
    
window = Tk()
window.geometry("600x400")

sp = Spinbox(window,
             values=(10,38,170,101),    # 以元組儲存數值
             command=printInfo)
sp.pack(pady=10,padx=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())
    
window = Tk()
window.geometry("600x400")

cities = ("新加坡","上海","東京")       # 以元組儲存數值

sp = Spinbox(window,
             values=cities,    
             command=printInfo)
sp.pack(pady=10,padx=10)

window.mainloop()



print("------------------------------------------------------------")  # 60個


import random

def fnTest():
    global ans		#宣告ans為全域變數來記錄答案
    n=int(spnNum.get()) #取得使用者選擇的位數
    num=[[1,9],[10,99],[100,999]]   #用二維串列儲存各位數的亂數範圍
    r1=random.randint(num[n-1][0],num[n-1][1])
    r2=random.randint(num[n-1][0],num[n-1][1])
    if(r2>r1):	#若r2>r1就兩者互換
        r1,r2=r2,r1
    if(spnOpt.get()=='加法'):	#若選擇'加法'
        opt='+'
        ans=r1+r2
    else:
        opt='-'
        ans=r1-r2        
    lblTest.config(text='{} {} {} ='.format(r1,opt,r2))
    entAns.focus_set()
    buttonTest.config(state='disable')
    buttonAns.config(state='normal')
    
def fnAns():
    global ans
    userAns=int(entAns.get())
    if(userAns==ans):
        msg.set('太棒了！答案正確！')
    else:
        msg.set('答錯了！答案是：{}'.format(ans))
    buttonTest.config(state='normal')
    buttonAns.config(state='disable')
    
window = tk.Tk()
window.geometry("600x400")
window.title('加減法測驗')

frmTest=tk.Frame(window,relief='raised',borderwidth=2)
frmTest.pack(side='left',padx=5,pady=3)
lblTest=tk.Label(frmTest,text=' ',font=('微軟正黑體',20))
lblTest.pack(pady=5)
ans=tk.IntVar()
entAns=tk.Entry(frmTest,textvariable=ans)
entAns.pack(pady=5)
msg=tk.StringVar()
msg.set('設定後按 <出題> 鈕開始測驗')
lblMsg=tk.Label(frmTest,textvariable=msg)
lblMsg.pack(pady=5)
frmSet=tk.Frame(window,relief='raised',borderwidth=2)
frmSet.pack(side='left',padx=5,pady=3)
tk.Label(frmSet,text='運算：').pack(anchor='w')
lstOpt=['加法','減法']
spnOpt=tk.Spinbox(frmSet,values=lstOpt)
spnOpt.pack(anchor='w')
tk.Label(frmSet,text='位數：').pack(anchor='w')
spnNum=tk.Spinbox(frmSet,from_=1,to=3)
spnNum.pack(anchor='w')

buttonTest=tk.Button(frmSet, text='出題', command=fnTest)
buttonTest.pack(side='left',pady=3)

buttonAns=tk.Button(frmSet, text='核對', command=fnAns,state='disable')
buttonAns.pack(side='right',pady=3)

ans=0

window.mainloop()




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

