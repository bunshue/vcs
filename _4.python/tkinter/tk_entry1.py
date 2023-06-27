# Python 測試 tkinter, Entry

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


import tkinter as tk

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

def checkPW():
    if(pw.get() == "1234"):
        msg.set("密碼正確，歡迎登入！")
    else:
        msg.set("密碼錯誤，請修正密碼！")

pw = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(window, text = "請輸入密碼：(1234)")
label.pack()
entry = tk.Entry(window, textvariable = pw)
entry.pack()
button = tk.Button(window, text="登入", command = checkPW)
button.pack()
lblmsg = tk.Label(window, fg="red", textvariable = msg)
lblmsg.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


# Entry與Label測試
tk.Label(text = 'Entry與Label測試').pack()
string = tk.StringVar()
entry = tk.Entry(window, textvariable = string).pack()
label = tk.Label(window, textvariable = string).pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


label1=tk.Label(window, text = "輸入成績：")
label1.place(x = 20, y = 20)
score = tk.StringVar()
entryUrl = tk.Entry(window, textvariable = score)
entryUrl.place(x = 90, y = 20)
btnDown = tk.Button(window, text = "計算成績")
btnDown.place(x = 80, y = 50)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()


