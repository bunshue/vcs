# Python 測試 tkinter : Checkbutton

def choose():
    str = "你喜歡的球類運動："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + ball[i] + " "
    print(str)
    msg.set(str)

import tkinter as tk

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


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線


print('Checkbutton 測試')
var = tk.IntVar()

c = tk.Checkbutton(window, text = "CheckButton", variable = var)
c.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

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


window.mainloop()

