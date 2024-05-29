# Python 測試 tkinter : Checkbutton

import sys
import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox

print("------------------------------------------------------------")  # 60個
'''
def choose():
    str = "你喜歡的球類運動："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + ball[i] + " "
    print(str)
    msg.set(str)


# 建立主視窗
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
title = "這是主視窗"
window.title(title)

x_st = 100
y_st = 250
dx = 120
dy = 100

choice = []
ball = ["足球", "籃球", "棒球", "排球", "網球", "羽毛球"]
msg = tk.StringVar()
label1 = tk.Label(window, text = "選擇喜歡的球類運動：")
label1.pack()
label1.place(x = x_st + dx * 0, y = y_st + dy * 1 - 20)
label2 = tk.Label(window, fg = "red", textvariable = msg)
label2.pack()
label2.place(x = x_st + dx * 0, y = y_st + dy * 1 + 20)

for i in range(0, len(ball)):
    item = tk.IntVar()
    choice.append(item)
    item = tk.Checkbutton(window, text = ball[i], variable = choice[i], command = choose)
    item.pack()
    item.place(x = x_st + dx * i, y = y_st + dy * 1)


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


print('Checkbutton 測試')
var = tk.IntVar()

c = tk.Checkbutton(window, text = "CheckButton", variable = var)
c.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# Checkbutton測試
tk.Label(text = 'Checkbutton測試').pack(anchor=tk.W)
topping = {0:'海苔', 1:'水煮蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):
    check_value[i] = tk.BooleanVar()
    tk.Checkbutton(window, variable = check_value[i], text = topping[i]).pack(anchor = tk.W)

def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(topping[i])

tk.Button(window, text = '點菜', command = buy).pack(anchor = tk.W)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()


print("------------------------------------------------------------")  # 60個

# 建立主視窗
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
title = "這是主視窗"
window.title(title)
#window.title("試題與測驗分析程式")

print("試題與測驗分析程式")

def but_click():
    selected_options = ''
    if asia.get():
        selected_options += chkbut_asia.cget('text')
    if america.get():
        selected_options += chkbut_america.cget('text')
    if europe.get():
        selected_options += chkbut_europe.cget('text')
    if aferica.get():
        selected_options += chkbut_aferica.cget('text')
    lab_result.config(text=selected_options)   
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
asia = tk.IntVar()
chkbut_asia = tk.Checkbutton(window, text='亞洲',variable=asia,anchor=tk.W)
chkbut_asia.pack(padx=90, pady=5, fill=tk.X)
america = tk.IntVar()
chkbut_america = tk.Checkbutton(window, text='美洲',variable=america,anchor=tk.W)
chkbut_america.pack(padx=90, pady=5, fill=tk.X)
europe = tk.IntVar()
chkbut_europe = tk.Checkbutton(window, text='歐洲',variable=europe,anchor=tk.W)
chkbut_europe.pack(padx=90, pady=5, fill=tk.X)
aferica = tk.IntVar()
chkbut_aferica = tk.Checkbutton(window, text='非洲',variable=aferica,anchor=tk.W)
chkbut_aferica.pack(padx=90, pady=5, fill=tk.X)
but = tk.Button(window, text='確定', command=but_click, font=default_font, padx=15)
but.pack(padx=10, pady=5)
lab_result = tk.Label(window, font=default_font, fg='black', width=20)
lab_result.pack(padx=10, pady=(5,10))



window.mainloop()

print("------------------------------------------------------------")  # 60個

# 建立主視窗
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
title = "這是主視窗"
window.title(title)

from tkinter import ttk
# checkbutton
check1 = ttk.Checkbutton(
	window, 
	text = 'checkbox 1', 
	command = lambda: print('ccccc'),
	variable = 'ccccc',
	onvalue = 10,
	offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(
	window, 
	text = 'Checkbox 2',
	command = '')
check2.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

check_bool = tk.BooleanVar()

exercise_check = ttk.Checkbutton(
	window, 
	text = 'exercise check', 
	variable = check_bool, 
	#command = lambda: print(radio_string.get()))
        command = lambda: print('你按了check_button'))
exercise_check.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

'''
print("------------------------------------------------------------")  # 60個

print("Checkbutton")

# 建立主視窗
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
title = "這是主視窗"
window.title(title)
#window.title('Checkbutton 核取方塊')

def check(): #回應核取方塊變數狀態
   print('這學期預定選修的科目包括:', var1.get(), var2.get(), var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=tk.Label(window, text = '選修的科目：', font = ft1).pack()
item1 = '人工智慧'
var1 = tk.StringVar()
chk1 = tk.Checkbutton(window, text = item1, font = ft1,
    variable = var1, onvalue = item1, offvalue = '')
chk1.pack()
item2 = '程式語言'
var2 = tk.StringVar()
chk2 = tk.Checkbutton(window, text = item2, font = ft1,
    variable = var2, onvalue = item2, offvalue = '')
chk2.pack()
item3 = '數位行銷'
var3 = tk.StringVar()
chk3 = tk.Checkbutton(window, text = item3, font = ft1,
    variable = var3, onvalue = item3, offvalue = '')
chk3.pack()
btnShow = tk.Button(window, text = '列出選修結果', font = ft2, command = check)
btnShow.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i],

text = topping[i]).pack(anchor=tk.W)

def buy():
	for i in check_value:
		if check_value[i].get() == True:
			print(topping[i])

tk.Button(window, text='點餐', command=buy).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window=tk.Tk()

topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}
check_value={}
for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)
window.mainloop()

"""
請問迴圈裡面 check_value [i] = tk.BooleanVar() 這一行，能否舉個例子，假設第 0 個按鈕被勾選，check_value 長怎樣；假設第 0、1 個按鈕被勾選，check_value 長怎樣 ... 依此類推
"""

print('------------------------------------------------------------')	#60個

""" fail
topping = {0:'海苔', 1:'水煮蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)

def buy():
	for i in check_value:
		if check_value[i].get() == True:
			print(topping[i])

tk.Button(window, text='點菜', command=buy).pack()

window.mainloop()
"""

print('------------------------------------------------------------')	#60個


from tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + " "
    x.set(selection)

window = Tk()
window.title("ex18_6")                     # 視窗標題

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球",
          4:"桌球", 5:"排球"}               # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(window,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
Button(window,text="確定",width=10,command=printInfo).grid(row=i+2)

x = StringVar()
display = Label(window,textvariable=x, bg="lightgreen",width=30)
display.grid(row=i+3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

window = Tk()
window.title("ch18_27")                   # 視窗標題

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

var1 = IntVar()                      
Checkbutton(window,text="美式足球",
                  variable=var1).grid(row=1,sticky=W)
var2 = IntVar()
Checkbutton(window,text="棒球",
                  variable=var2).grid(row=2,sticky=W)                
var3 = IntVar()
Checkbutton(window,text="籃球",
                  variable=var3).grid(row=3,sticky=W)   

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

window = Tk()
window.title("ch18_28")                     # 視窗標題

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(window,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
Button(window,text="確定",width=10,command=printInfo).grid(row=i+2)

window.mainloop()

print("------------------------------------------------------------")  # 60個

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
title = "這是主視窗"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def select():
    print('你的選項是 :', var.get())

ft = ('標楷體', 14)
tk.Label(window, 
      text = "請問您的最高學歷: ", font = ft,
      justify = tk.LEFT, padx = 20).pack()
place = [('博士', 1), ('碩士', 2),('大學', 3),
          ('高中', 4),('國中', 5),('國小', 6)]
var = tk.IntVar()
var.set(2)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = tk.W)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def first():
    tk.messagebox.showinfo('顯示類對話方塊',
            '「顯示」類是以「show」開頭，只會顯示一個「確定」鈕。')

def second():
    tk.messagebox.askretrycancel('詢問類對話方塊', 
            '「詢問」類是以「ask」為開頭，伴隨2~3個按鈕來產生互動。')

tk.Button(window, text='顯示類對話方塊', command = first).pack(side = 'left', padx = 10)
tk.Button(window, text='詢問類對話方塊', command = second).pack(side = 'left')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

sentences="玉階生白露，夜久侵羅襪。\n卻下水晶簾，玲瓏望秋月。"

text = tk.Text(window, width = 30, height = 14, bg = "yellow", wrap=tk.WORD)
text.insert(tk.END,sentences)
text.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print("ScrollBar捲軸")

text = tk.Text(window, width = "30", height = "5")
#text.grid(row = 0, column = 0)
text.pack()
scrollbar = tk.Scrollbar(command = text.yview, orient = tk.VERTICAL)
#scrollbar.grid(row = 0, column = 1, sticky = "ns")
scrollbar.pack()
text.configure(yscrollcommand = scrollbar.set)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def select():
    print('你的選項是 :', var.get())

ft = ('標楷體', 14)
tk.Label(window,
         text = "請選擇精通的程式語言: ", font = ft,
         justify = tk.LEFT, padx = 20).pack()
place = [('Python語言', 1), ('C語言', 2),
         ('C++語言', 3),('Java語言', 4)]
var = tk.IntVar()
var.set(3)

for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
                   font = ft, variable = var, padx = 20,
                   command = select).pack(anchor = tk.NW)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print("密碼資料")

label = tk.Label(window, text = "請輸入密碼: ")
label.pack()
entry = tk.Entry(window,bg='yellow',fg='red',show='*')
entry.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def check(): #回應核取方塊變數狀態
   print('這學期預定選修的科目包括:', var1.get(), var2.get()
         ,var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=tk.Label(window, text = '選修的科目：', font = ft1).pack()
item1 = '人工智慧'
var1 = tk.StringVar()
chk1 = tk.Checkbutton(window, text = item1, font = ft1,
                      variable = var1, onvalue = item1, offvalue = '')
chk1.pack()
item2 = '程式語言'
var2 = tk.StringVar()
chk2 = tk.Checkbutton(window, text = item2, font = ft1,
                   variable = var2, onvalue = item2, offvalue = '')
chk2.pack()
item3 = '數位行銷'
var3 = tk.StringVar()
chk3 = tk.Checkbutton(window, text = item3, font = ft1,
                      variable = var3, onvalue = item3, offvalue = '')
chk3.pack()
btnShow = tk.Button(window, text = '列出選修結果', font = ft2,
                 command = check)
btnShow.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

button = tk.Button(window, text = "Press", underline=0)
button.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



window.mainloop()


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




""" ppg
tk.Label(window,text="請選擇喜歡的運動", fg="blue",bg="lightyellow",width=30).grid(row=0)

var1 = tk.IntVar()                      
tk.Checkbutton(window,text="美式足球", variable=var1).grid(row=1,sticky=tk.W)
var2 = tk.IntVar()
tk.Checkbutton(window,text="棒球", variable=var2).grid(row=2,sticky=tk.W)
var3 = tk.IntVar()
tk.Checkbutton(window,text="籃球", variable=var3).grid(row=3,sticky=tk.W)
"""



"""

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

tk.Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(window,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
tk.Button(window,text="確定",width=10,command=printInfo).grid(row=i+2)


"""

