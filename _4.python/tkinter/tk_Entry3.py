'''
使用grid Entry
'''
def checkPassword():
    password = '1234'
    enteredPassword = entry2.get()
    if password == enteredPassword:
        label_result.config(text="Correct")
    else:
        label_result.config(text="Incorrect")


import tkinter as tk
from tkinter import messagebox

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

#新建一個Frame, row, column重新計算
frame1 = tk.Frame(window)
frame1.pack()

label1 = tk.Label(frame1, text = "請輸入資料 : ")
entry1 = tk.Entry(frame1)
label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)

#新建一個Frame, row, column重新計算
frame2 = tk.Frame(window)
frame2.pack()

button1 = tk.Button(frame2, text = "確定")
button2 = tk.Button(frame2, text = "取消")
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#新建一個Frame, row, column重新計算
frame3 = tk.Frame(window)
frame3.pack()

label1 = tk.Label(frame3, text = "Username")
entry1 = tk.Entry(frame3)

label2 = tk.Label(frame3, text = "Password:(1234)")
entry2 = tk.Entry(frame3, show = "*")

button = tk.Button(frame3, text = "Enter", command = checkPassword)
label_result = tk.Label(frame3)

label1.grid(row = 1, column = 1)
entry1.grid(row = 1, column = 2)
label2.grid(row = 2, column = 1)
entry2.grid(row = 2, column = 2)
button.grid(row = 3, column = 2)
label_result.grid(row = 4, column = 2)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



#新建一個Frame, row, column重新計算
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
entry1 = tk.Entry(frame4, textvariable = username, font = (14))
entry2 = tk.Entry(frame4, textvariable = password, font = (14), show = '*')
#entry1.grid(row = 0, column = 1)
#entry2.grid(row = 1, column = 1)
entry1.pack()
entry2.pack()

#action when login button is clicked
def login():
    if username.get()=='admin' and password.get()=='admin':
        messagebox.showinfo(title = 'Login status', message = 'You have logged in.')
    else:
        messagebox.showerror(title = 'Login error', message = 'Username/Password is incorrect.')

#action when cancel button is clicked
def cancel():
    status = messagebox.askyesno(title = 'Question', message = 'Do you want to close the window?')
    if status==True:
        window.destroy()
    else:
        messagebox.showwarning(title = 'Warning', message = 'Please login again!')

button1 = tk.Button(frame4, command = login, text = 'Login', font = (14))
button2 = tk.Button(frame4, command = cancel, text = 'Cancel', font = (14))
#button1.grid(row = 2, column = 1, sticky = tk.W)
#button2.grid(row = 2, column = 1, sticky = tk.E)
button1.pack()
button2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()
