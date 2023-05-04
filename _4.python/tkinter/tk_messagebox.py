#
# MessageBox測試
#

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

'''
參考
https://docs.python.org/3/library/tkinter.messagebox.html
'''

def ask_yes_no():
    # answer = tkinter.messagebox.askquestion('Title', 'Body')
    # print(answer)
    tkinter.messagebox.showerror('Info title', 'Here is some information')

def error_mesg_box():
    tkinter.messagebox.showerror(title='錯誤',
                         message=('錯誤訊息1\n' +
                                  '錯誤訊息2\n' +
                                  '錯誤訊息3\n' +
                                  '錯誤訊息4'))
def ask_yes_no2():
    response = tkinter.messagebox.askyesno('糟糕!!!', '還好嗎？')
    if(response==True):
        print('沒問題');
    else:
        print('有問題');

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

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

tk.Label(text='Yes/No 測試').pack()
button1 = tk.Button(window, text = '建立 Yes / No 視窗訊息', command = ask_yes_no)
#button1.pack(expand = True)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

tk.Label(text='錯誤訊息 測試').pack()
button2 = tk.Button(window, text = '建立 錯誤 視窗訊息', command = error_mesg_box)
#button2.pack(expand = True)
button2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

tk.Label(text='Yes/No 測試').pack()
button3 = tk.Button(window, text = '建立 Yes / No 視窗訊息', command = ask_yes_no2)
#button3.pack(expand = True)
button3.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

my_mesg = "大雄：1964年8月7日\n哆啦A夢：2112年9月3日\n靜香：1964年12月2日\n小夫：1964年2月29日\n胖虎：1964年6月15日\n哆啦美：2114年12月2日"
msg = tk.Message(window, text = my_mesg)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線


import sys
import tkinter as tk
import tkinter.messagebox as messagebox

def show_error():

    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(title='IdleX Error',
                         message=('Unable to located "idlexlib".\n' +
                                  'Make sure it is located in the same directory ' +
                                  'as "idlexlib" or run setup.py to install IdleX.\n' +
                                  '  python setup.py install --user'))

show_error()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線


def func1():
    if tkinter.messagebox.askyesno("關閉窗口","確認關閉窗口嗎"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW",func1)

window.mainloop()


