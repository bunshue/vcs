import sys
import tkinter as tk
from tkinter import ttk

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
title = "Combobox 測試"
window.title(title)

# Combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
# combo.configure(values = items)
combo.pack()

# events 
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


from tkinter import *
from tkinter.ttk import *

def selected(event):
    labelVar.set(cbVar.get())

print('最喜歡的運動')

cbVar = StringVar()
cb = Combobox(window, textvariable=cbVar)
cb['value'] = ("籃球","排球","足球","其他")  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', selected)  #設定選取選項後執行的程式
cb.pack()

labelVar = StringVar()  
labelShow = Label(window, textvariable=labelVar)
labelVar.set(cbVar.get())
labelShow.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



import tkinter as tk
import tkinter.ttk as ttk

def showWeather(event):  #下拉選單選取選項後執行的程式
    city = cbVar.get()  #使用者選取的選項
    print(city)
    if city != '請選擇：':  #選擇縣市
        showdata = city + ' 天氣資料：\n'

        labelVar.set(showdata)
    else:
        labelVar.set('請選擇縣市！')

print('縣市天氣資料')

cbVar = tk.StringVar()
cb = ttk.Combobox(window, textvariable=cbVar)   #下拉式選單元件
cb['value'] = ("請選擇：","臺北","新北","桃園","臺中","臺南","高雄","基隆","新竹","嘉義","苗栗","彰化","南投","雲林","嘉義","屏東","宜蘭","花蓮","臺東","澎湖","金門","連江" )  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', showWeather)  #設定選取選項後執行的程式
cb.pack()

labelVar = tk.StringVar()  
labelShow = tk.Label(window, foreground='red', justify='left', textvariable=labelVar)  #標籤元件
labelVar.set('尚未選擇縣市！')
labelShow.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


import tkinter as tk
import tkinter.ttk as ttk

def combobox_selected(event):
    label_text.set(cbVar.get())

#Combobox 下拉選單是 tkinter 的 ttk 加強模組裡的元件
print('Combobox 測試')

cbVar = tk.StringVar()
cb = ttk.Combobox(window, textvariable = cbVar)   #下拉式選單元件
cb['value'] = ("籃球","排球","足球","其他")  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', combobox_selected)  #設定選取選項後執行的程式
cb.pack()

label_text = tk.StringVar()  
label1 = tk.Label(window, textvariable = label_text)
label_text.set(cbVar.get())
label1.pack()

"""
import tkinter as tk
from tkinter import ttk

def show():
    a.set(f'{box.current()}:{box.get()}')    # 顯示索引值與內容

a = tk.StringVar()                           # 定義變數
a.set('')

label = tk.Label(window, textvariable=a)       # 建立標籤，內容為變數
label.pack()

box = ttk.Combobox(window, width=15, values=['七龍珠','海賊王','鬼滅之刃','灌籃高手','排球少年'])
box.pack()

btn = tk.Button(window, text='顯示', command=show)   # 建立按鈕，點擊按鈕時，執行 show 函式
btn.pack()
"""

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

def combox_select(event):
    selected_area = event.widget.get()
    lab_result.config(text=selected_area)

print("試題與測驗分析程式")

default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS=('屏東縣','高雄市','台南市','台東縣')
area = tk.StringVar()
combox = ttk.Combobox(window, value=AREA_OPTIONS, textvariable=area, font=default_font)
combox.bind('<<ComboboxSelected>>', combox_select)
combox.current(0)
combox.pack(padx=10, pady=10)
lab_result = tk.Label(window, font=default_font, fg='black', width=18)
lab_result.pack(padx=10, pady=(5,10))       



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個







separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

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


