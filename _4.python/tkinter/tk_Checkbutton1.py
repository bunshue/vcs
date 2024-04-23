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


window.mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.font as tkfont
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
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
asia = tk.IntVar()
chkbut_asia = tk.Checkbutton(win, text='亞洲',variable=asia,anchor=tk.W)
chkbut_asia.pack(padx=90, pady=5, fill=tk.X)
america = tk.IntVar()
chkbut_america = tk.Checkbutton(win, text='美洲',variable=america,anchor=tk.W)
chkbut_america.pack(padx=90, pady=5, fill=tk.X)
europe = tk.IntVar()
chkbut_europe = tk.Checkbutton(win, text='歐洲',variable=europe,anchor=tk.W)
chkbut_europe.pack(padx=90, pady=5, fill=tk.X)
aferica = tk.IntVar()
chkbut_aferica = tk.Checkbutton(win, text='非洲',variable=aferica,anchor=tk.W)
chkbut_aferica.pack(padx=90, pady=5, fill=tk.X)
but = tk.Button(win, text='確定', command=but_click, font=default_font, padx=15)
but.pack(padx=10, pady=5)
lab_result = tk.Label(win, font=default_font, fg='black', width=20)
lab_result.pack(padx=10, pady=(5,10))
win.mainloop()

print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

