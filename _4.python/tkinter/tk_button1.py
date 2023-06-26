import tkinter as tk

def button0Click():
    print("你按了button0")

def button1Click():
    print("你按了button1")

def button2Click():
    print("你按了button2")

def button3Click():
    print("你按了button3")

def button4Click():
    print("你按了button4")

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
y_st = 100
dx = 120;
dy = 100;
w = 12
h = 3

button0 = tk.Button(window, text = "Button0", width = w, height = h, command = button0Click)
button0.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

button1 = tk.Button(window, text = "Button1", width = w, height = h, command = button1Click)
button1.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

button2 = tk.Button(window, text = "Button2", width = w, height = h, command = button2Click)
button2.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

button3 = tk.Button(window, text = "Button3", width = w, height = h, command = button3Click)
button3.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

button4 = tk.Button(window, text = "Button4", width = w, height = h, command = button4Click)
button4.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

button0.place(x = x_st + dx * 0, y = y_st + dy * 0)
button1.place(x = x_st + dx * 1, y = y_st + dy * 0)
button2.place(x = x_st + dx * 2, y = y_st + dy * 0)
button3.place(x = x_st + dx * 3, y = y_st + dy * 0)
button4.place(x = x_st + dx * 4, y = y_st + dy * 0)

window.mainloop()
