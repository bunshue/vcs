#
# MessageBox測試
#

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
#from tkinter import messagebox

import tkinter.messagebox as msg

'''
參考
https://docs.python.org/3/library/tkinter.messagebox.html
'''

def ask_yes_no():
    # answer = messagebox.askquestion('Title', 'Body')
    # print(answer)
    messagebox.showerror('Info title', 'Here is some information')

def error_mesg_box():
    messagebox.showerror(title='錯誤',
                         message=('錯誤訊息1\n' +
                                  '錯誤訊息2\n' +
                                  '錯誤訊息3\n' +
                                  '錯誤訊息4'))
def ask_yes_no2():
    response = msg.askyesno('糟糕!!!', '還好嗎？')
    if(response==True):
        print('沒問題');
    else:
        print('有問題');

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

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



window.mainloop()

#window.destroy() # optional; see description below


