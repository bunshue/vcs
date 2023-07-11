import tkinter as tk
from tkinter import ttk

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
title = "Label測試"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

#separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


#separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


font_size = 24
w = 40
h = 30

# 設定 Label 
label1a = tk.Label(window, text = '這是標籤元件', fg = 'red', bg = 'yellow', font = ("標楷體", font_size), padx = w, pady = h)
label1a.pack()

cnt = 1
def changeLabelText1a():
    global cnt
    cnt += 1
    label1a.config(text = "這是標籤元件 " + str(cnt))
    
button1a = tk.Button(window, text = "修改標籤之Text", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = changeLabelText1a)
button1a.pack()

def changeLabelText2a():
    global cnt
    cnt += 1
    labela_text.set("這是標籤元件 " + str(cnt))
    print()

def toggleLabelVisible_a():
    print('你按了Button Toggle')
    global labela_visible

    if labela_visible:
        labela_visible = False
        label1a.pack_forget()
        label2a.pack_forget()
        frame.pack(expand = True, before = button3a)
    else:
        labela_visible = True
        frame.pack_forget()
        label1a.pack(expand = True, before = button3a)
        label2a.pack(expand = True, before = button3a)

labela_visible = True

labela_text = tk.StringVar()
labela_text.set('這是標籤元件')
# 設定 Label 

label2a = tk.Label(window, textvariable = labela_text, fg = 'red', bg = 'yellow', font = ("標楷體", font_size), padx = w, pady = h)
label2a.pack()

button2a = tk.Button(window, text = "修改標籤之Text", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = changeLabelText2a)
button2a.pack()

button3a = tk.Button(window, text = "切換標籤顯示與隱藏", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = toggleLabelVisible_a)
button3a.pack()

'''
width = 200
height = 100
frame = tk.Frame(window, bg = 'pink', width = width, height = height)
'''
frame = ttk.Frame(window)

#separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

font_size = 24
w = 30
h = 30

x_st = 450
y_st = 20
dx = 300
dy = 110

# 設定 Label 
label1b = tk.Label(window, text = '這是標籤元件', fg = 'red', bg = 'yellow', font = ("標楷體", font_size), padx = w, pady = h)
label1b.place(x = x_st + dx * 0, y = y_st + dy * 0)

cnt = 1
def changeLabelText1b():
    global cnt
    cnt += 1
    label1b.config(text = "這是標籤元件 " + str(cnt))
    
button1b = tk.Button(window, text = "修改標籤之Text", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = changeLabelText1b)
button1b.place(x = x_st + dx * 0, y = y_st + dy * 1)

def changeLabelText2b():
    global cnt
    cnt += 1
    labelb_text.set("這是標籤元件 " + str(cnt))
    print()

def toggleLabelVisible_b():
    print('你按了Button Toggle')
    global labelb_visible, x_st, y_st, dx, dy

    if labelb_visible:
        labelb_visible = False
        label1b.place_forget()
        label2b.place_forget()
    else:
        labelb_visible = True
        label1b.place(x = x_st + dx * 0, y = y_st + dy * 0)
        label2b.place(x = x_st + dx * 0, y = y_st + dy * 2)

labelb_visible = True

labelb_text = tk.StringVar()
labelb_text.set('這是標籤元件')
# 設定 Label 

label2b = tk.Label(window, textvariable = labelb_text, fg = 'red', bg = 'yellow', font = ("標楷體", font_size), padx = w, pady = h)
label2b.place(x = x_st + dx * 0, y = y_st + dy * 2)

button2b = tk.Button(window, text = "修改標籤之Text", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = changeLabelText2b)
button2b.place(x = x_st + dx * 0, y = y_st + dy * 3)

button3b = tk.Button(window, text = "切換標籤顯示與隱藏", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = toggleLabelVisible_b)
button3b.place(x = x_st + dx * 0, y = y_st + dy * 4)


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

'''
def toggle_label_grid():
    global label_visible

    if label_visible:
        label.grid_forget()
        label_visible = False
    else:
        label_visible = True
        label.grid(column = 1, row = 0)

window.columnconfigure((0,1), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1, uniform = 'a')

button = ttk.Button(window, text = 'toggle Label', command = toggle_label_grid)
button.grid(column = 0, row = 0)

label_visible = True
label = ttk.Label(window, text= 'A label')
label.grid(column = 1, row = 0)
'''

window.mainloop()

