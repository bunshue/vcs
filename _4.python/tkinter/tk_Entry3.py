'''
使用grid

'''

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
title = "這是主視窗"
window.title(title)

def checkPassword():
    password = '1234'
    enteredPassword = entry2.get()
    if password == enteredPassword:
        label_result.config(text="Correct")
    else:
        label_result.config(text="Incorrect")

label1 = tk.Label(window, text="Username")
entry1 = tk.Entry(window)

label2 = tk.Label(window, text="Password:(1234)")
entry2 = tk.Entry(window, show="*")

button = tk.Button(window, text="Enter", command=checkPassword)
label_result = tk.Label(window)

label1.grid(row=1, column=1)
entry1.grid(row=1, column=2)
label2.grid(row=2, column=1)
entry2.grid(row=2, column=2)
button.grid(row=3, column=2)
label_result.grid(row=4, column=2)


window.mainloop()
