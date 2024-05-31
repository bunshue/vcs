"""
# Python 測試 tkinter, Entry

使用pack Entry

"""

import sys
import tkinter as tk
from tkinter import messagebox

print("------------------------------------------------------------")  # 60個

def calculate():
    print('第零項 : ', name.get())
    print('第一項 : ', num1.get())
    print('第二項 : ', num2.get())
    print('第三項 : ', num3.get())
    num3.set(num1.get() * num2.get())
    name.set('good')

    '''
    # BMI 計算，四捨五入取到小數第二位
    BMI_value = round(weight_msg.get() / ((height_msg.get() / 100) ** 2),2)
    
    #回傳結果，設定 return_msg 數值及評語
    return_msg.set("BMI 計算後數值 = " + str(BMI_value) + "\n" + BMI_Status(BMI_value))
    '''

def calculate_bmi():
    # BMI 計算，四捨五入取到小數第二位
    BMI_value = round(weight_msg.get() / ((height_msg.get() / 100) ** 2),2)
    
    #回傳結果，設定 return_msg 數值及評語
    return_msg.set("BMI 計算後數值 = " + str(BMI_value) + "\n" + BMI_Status(BMI_value))


# 透過 BMI 指數，回傳相對應評語
def BMI_Status(BMI_value):
    if BMI_value < 18.5:
        return "BMI 過低，體重過輕"
    elif BMI_value < 24:
        return "BMI 正常，標準體位"
    else:
        if BMI_value < 27:
            return "BMI 過高，體重過重"
        elif BMI_value < 30:
            return "BMI 過高，輕度肥胖"
        elif BMI_value < 35:
            return "BMI 過高，中度肥胖"
        else:
            return "BMI 過高，重度肥胖"

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
title = "圖形化範例-BMI測量"
window.title(title)


#建立將使用的相關變數(回應值、身高、體重)，這邊需要在建立玩主視窗後才可以建立，否則會報錯
return_msg = tk.StringVar() # BMI 回傳值
height_msg = tk.IntVar() # 身高
weight_msg = tk.IntVar() # 體重


#設定身高、體重的 Label 及 Entry

font_size = 24
w = 20
h = 10

# 設定身高 Label 
label1 = tk.Label(window, text = "請輸入身高:", foreground = "red", font = ("標楷體", font_size), padx = w, pady = h)
label1.pack()

# 設定身高 Entry
entry1 = tk.Entry(window, foreground = "green", textvariable = height_msg)
entry1.pack()

# 設定 Label
label2 = tk.Label(window, text = "請輸入體重:", foreground = "red", font = ("標楷體", font_size), padx = w, pady = h)
label2.pack()

# 設定 Entry
entry2 = tk.Entry(window, foreground = "green", textvariable = weight_msg)
entry2.pack()

#設定回應值 Label

# 設定回應值 Label
label3 = tk.Label(window, textvariable = return_msg, foreground = "red", font = ("標楷體", font_size), padx = w, pady = h)
label3.pack()

#設定功能按鈕，並可觸發自行撰寫的 BMI function

# 設定 Button
button1 = tk.Button(window, text = "BMI 測量", foreground = "blue", font = ("標楷體", font_size), padx = w, pady = h, command = calculate_bmi)
button1.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

name = tk.StringVar()
num1 = tk.IntVar()
num2 = tk.IntVar()
num3 = tk.IntVar()

entry0 = tk.Entry(window, textvariable = name)
entry0.pack()
entry1 = tk.Entry(window, textvariable = num1)
entry1.pack()
entry2 = tk.Entry(window, textvariable = num2)
entry2.pack()
entry3 = tk.Entry(window, textvariable = num3)
entry3.pack()
button2 = tk.Button(window, text = "計算", command = calculate)
button2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


# Entry與Label測試
tk.Label(text = 'Entry與Label同步改變Text').pack()

string = tk.StringVar()
entry = tk.Entry(window, textvariable = string)
entry.pack()
label = tk.Label(window, textvariable = string)
label.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#Entry 預設值
entry_string = tk.StringVar(value = 'test1111')
entry = tk.Entry(window, textvariable = entry_string)
entry.pack()

print('Entry內容 :', entry_string.get())	#Entry取值

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

print("------------------------------------------------------------")  # 60個

#使用grid Entry

def get_entry_text():
    print('取得 id : ', entry1.get())
    print('取得 pd : ', entry2.get())

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

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame1 = tk.Frame(window)
frame1.pack()

label1 = tk.Label(frame1, text = "請輸入資料 : ")
entry1 = tk.Entry(frame1)
label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame2 = tk.Frame(window)
frame2.pack()

button1 = tk.Button(frame2, text = "確定")
button2 = tk.Button(frame2, text = "取消")
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame3 = tk.Frame(window)
frame3.pack()

label1 = tk.Label(frame3, text = "Username:")
entry1 = tk.Entry(frame3)

label2 = tk.Label(frame3, text = "Password:")
entry2 = tk.Entry(frame3, show = "*")

button = tk.Button(frame3, text = "取得Entry資料", command = get_entry_text)

label1.grid(row = 1, column = 1)
entry1.grid(row = 1, column = 2)
label2.grid(row = 2, column = 1)
entry2.grid(row = 2, column = 2)
button.grid(row = 3, column = 2)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame4 = tk.Frame(window)
frame4.pack()

#add textfields
label1 = tk.Label(frame4, text = 'Username:', font = (14))
label2 = tk.Label(frame4, text = 'Password:', font = (14))
#label1.grid(row = 0, column = 0, padx = 5, pady = 5)
#label2.grid(row = 1, column = 0, padx = 5, pady = 5)
label1.pack()
label2.pack()

#get username and password
username = tk.StringVar()
password = tk.StringVar()
entry1b = tk.Entry(frame4, textvariable = username, font = (14))
entry2b = tk.Entry(frame4, textvariable = password, font = (14), show = '*')
#entry1b.grid(row = 0, column = 1)
#entry2b.grid(row = 1, column = 1)
entry1b.pack()
entry2b.pack()

def login():
    print('取得帳號 : ', username.get())
    print('取得密碼 : ', password.get())

def cancel():
    window.destroy()

button1 = tk.Button(frame4, command = login, text = '取得Entry資料', font = (20))
button2 = tk.Button(frame4, command = cancel, text = '離開', font = (14))
#button1.grid(row = 2, column = 1, sticky = tk.W)
#button2.grid(row = 2, column = 1, sticky = tk.E)
button1.pack()
button2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




