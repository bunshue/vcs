'''
tk使用之範本

'''

print('------------------------------------------------------------')	#60個
print('準備工作')

import os
import sys
import csv
import time
import tkinter as tk



dummy_data = 'abcd'
count = 0

print('------------------------------------------------------------')	#60個

def show_info():
    print('目前選取的內容 : ')
    str = "選擇："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + stage_no[i] + " "
    print(str)

def button00Click():
    print('你按了button00')

def button01Click():
    print('你按了button01')

def button02Click():
    print('你按了button02')

def button03Click():
    print('你按了button03')

def button04Click():
    print('你按了button04')

def button05Click():
    print('你按了button05')

def button10Click():
    print('你按了button10')

def button11Click():
    print('你按了button11')

def button12Click():
    print('你按了button12')

def button13Click():
    print('你按了button13')

def button14Click():
    #print('你按了button14')
    set_data()
    clear_text1()

def button15Click():
    #print('你按了button15')
    window.destroy()  # 關閉視窗

def set_data():
    '''
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0","end")
    mesg= mesg + dummy_data
    print(mesg)
    text1.insert('end', mesg)
    '''
    global count
    count = count + 1
    message = '  次數' + str(count)
    text1.insert('end', message)

def clear_text1():
    text1.delete(1.0, 'end')
    # 執行 clear 函式時，清空內容

window = tk.Tk()

main_message1 = tk.StringVar()
main_message2 = tk.StringVar()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W)+'x'+str(H)
#size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
#window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

#顯示在正中央
screenWidth = window.winfo_screenwidth()    # 螢幕寬度
screenHeight = window.winfo_screenheight()  # 螢幕高度
W = 800                                     # 視窗寬
H = 800                                     # 視窗高
x_st = (screenWidth - W) / 2                # 視窗左上角x軸位置
y_st = (screenHeight - H ) / 2              # 視窗左上角Y軸位置
window.geometry("%dx%d+%d+%d" % (W, H, x_st, y_st))

# 設定主視窗標題
window.title('tk使用之範本')

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")
#window.configure(bg = '#00ff00')   # 視窗背景顏色
#window.configure(bg = 'yellow')    # 視窗背景顏色

icon_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.ico'
window.iconbitmap(icon_filename)   # 更改圖示

x_st = 50
y_st = 50
dx = 120
dy = 80
w = 12
h = 3

button00 = tk.Button(window, width = w, height = h, command = button00Click, text = 'xxx')
button00.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

#開啟資料庫按鈕
#button01 = tk.Button(window, width = w, height = h, command = button01Click, text = 'xxx')
#button01.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button01_text = tk.StringVar()
#button01 = tk.Button(window, textvariable = button01_text, command = lambda:button01Click(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
button01 = tk.Button(window, textvariable = button01_text, width = w, height = h, command = lambda:button01Click())
#button01 = tk.Button(window, command = xxxxxxx, text='選取檔案')
button01_text.set("xxx")

button02 = tk.Button(window, width = w, height = h, command = button02Click, text = 'xxx')
button02.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button03 = tk.Button(window, width = w, height = h, command = button03Click, text = 'xxx')
button03.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button04 = tk.Button(window, width = w, height = h, command = button04Click, text = 'xxx')
button04.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button05 = tk.Button(window, width = w, height = h, command = button05Click, text = 'xxx')
button05.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button00.place(x = x_st + dx * 0, y = y_st + dy * 0)
button01.place(x = x_st + dx * 1, y = y_st + dy * 0)
button02.place(x = x_st + dx * 2, y = y_st + dy * 0)
button03.place(x = x_st + dx * 3, y = y_st + dy * 0)
button04.place(x = x_st + dx * 4, y = y_st + dy * 0)
button05.place(x = x_st + dx * 5, y = y_st + dy * 0)

button10 = tk.Button(window, width = w, height = h, command = button10Click, text = 'xxx')
button10.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button11 = tk.Button(window, width = w, height = h, command = button11Click, text = 'xxx')
button11.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button12 = tk.Button(window, width = w, height = h, command = button12Click, text = 'xxx')
button12.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button13 = tk.Button(window, width = w, height = h, command = button13Click, text = 'xxx')
button13.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button14 = tk.Button(window, width = w, height = h, command = button14Click, text = 'Set/Clear Data')
button14.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button15 = tk.Button(window, width = w, height = h, command = button15Click, text = '離開')
button15.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button10.place(x = x_st + dx * 0, y = y_st + dy * 1)
button11.place(x = x_st + dx * 1, y = y_st + dy * 1)
button12.place(x = x_st + dx * 2, y = y_st + dy * 1)
button13.place(x = x_st + dx * 3, y = y_st + dy * 1)
button14.place(x = x_st + dx * 4, y = y_st + dy * 1)
button15.place(x = x_st + dx * 5, y = y_st + dy * 1)

font_size = 20

# 加入 Label
label_message1 = tk.Label(window, font=("標楷體", font_size), fg = 'red', textvariable = main_message1)
label_message1.pack()
label_message1.place(x = 5, y = 0 + 10)
main_message1.set('')

label_message2 = tk.Label(window, font=("標楷體", font_size), fg = 'red', textvariable = main_message2)
label_message2.pack()
label_message2.place(x = 5 + W * 3 / 4, y = 0 + 10)
main_message2.set('')

# 加入 Text
text1 = tk.Text(window, width = 100, height = 30)  # 放入多行輸入框
text1.pack()
text1.place(x = x_st + dx * 0, y = y_st + dy * 3 + 50)

message = ""
main_message1.set(message)

window.mainloop()

