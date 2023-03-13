# Python 測試 tkinter 2

def BMI():
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
h = 600
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "圖形化範例-BMI測量"
window.title(title)


#建立將使用的相關變數(回應值、身高、體重)，這邊需要在建立玩主視窗後才可以建立，否則會報錯
return_msg = tk.StringVar() # BMI 回傳值
height_msg = tk.IntVar() # 身高
weight_msg = tk.IntVar() # 體重


#設定身高、體重的 Label 及 Entry

font_size = 24
w = 40
h = 30

# 設定身高 Label 
height_label = tk.Label(window, text="請輸入身高:", foreground="red", font=("標楷體", font_size), padx = w, pady = h)
height_label.pack()

# 設定身高 Entry
height_entry = tk.Entry(window, foreground="green", textvariable=height_msg)
height_entry.pack()

# 設定 Label
weight_label = tk.Label(window, text="請輸入體重:", foreground="red", font=("標楷體", font_size), padx = w, pady = h)
weight_label.pack()

# 設定 Entry
weight_entry = tk.Entry(window, foreground="green", textvariable=weight_msg)
weight_entry.pack()

#設定回應值 Label

# 設定回應值 Label
returnMsg_label = tk.Label(window, textvariable=return_msg, foreground="red", font=("標楷體", font_size), padx = w, pady = h)
returnMsg_label.pack()

#設定功能按鈕，並可觸發自行撰寫的 BMI function

# 設定 Button
bmi_button = tk.Button(window, text="BMI 測量", foreground="blue", font=("標楷體", font_size), padx = w, pady = h, command=BMI)
bmi_button.pack()

#執行視窗程式需要使用到 mainloop() 函數，將此視窗加入事件監視迴圈，才會產生 GUI 視窗
window.mainloop()

