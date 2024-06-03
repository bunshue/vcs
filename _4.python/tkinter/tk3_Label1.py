import sys
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
w = 600
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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('Label的文字使用字型')
font1 = ("Courier", 36, "bold")
label1 = tk.Label(window, text = 'label之字型', font = font1)
label1.pack()

label2a = tk.Label(window, text = '不使用label1之字型')
label2a.pack()

label2b = tk.Label(window, text = '使用label1之字型')
label2b.pack()

font2 = label1["font"]  #將label1的字型讀出來
#label2a.config(font = font2)  #label2a 不使用
label2b.config(font = font2)   #label2b 使用

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('Label測試')
tk.Label(text = '有背景色的Label測試', font = "Raleway").pack()
tk.Label(text = '有背景色的Label測試').pack()
tk.Label(window, text = '有背景色的Label 紅', bg = 'red',   width = 20, height = 2).pack()
tk.Label(        text = '有背景色的Label 綠', bg = 'green', width = 30, height = 2).pack()
tk.Label(window, text = '有背景色的Label 藍', bg = 'blue',  width = 20, height = 2).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('Label使用圖片')

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cloud.gif'
image = tk.PhotoImage(file = filename)

tk.Label(window, image = image).place(x = 430, y = 170, width = 150, height = 150)

print("------------------------------------------------------------")  # 60個

#前後移動控件
label1 = tk.Label(window, text = 'Label 1', background = 'red')
label2 = tk.Label(window, text = 'Label 2', background = 'green')
label3 = tk.Label(window, text = 'Label 3', background = 'blue')

#有寬高的Label
x_st = 30
y_st = 300
dd = 20
label1.place(x = x_st + dd * 0, y = y_st + dd * 0, width = 100, height = 100)
label2.place(x = x_st + dd * 1, y = y_st + dd * 1, width = 100, height = 100)
label3.place(x = x_st + dd * 2, y = y_st + dd * 2, width = 100, height = 100)

button1 = tk.Button(window, text = 'Label 1 (R) 向上移動', command = lambda: label1.lift(aboveThis = label2))
button2 = tk.Button(window, text = 'Label 2 (G) 向上移動', command = lambda: label2.tkraise())
button3 = tk.Button(window, text = 'Label 1 (B) 向上移動', command = lambda: label3.tkraise())

# label1.lift()
# label2.lower()

"""
button1.place(rely = 1, relx = 0.8, anchor = 'se')
button2.place(rely = 1, relx = 1, anchor = 'se')
button3.place(rely = 1, relx = 0.6, anchor = 'se')
"""
button1.pack()
button2.pack()
button3.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text = "Red", bg = "red").pack()
#tk.Label(window, text = "Green", bg = "green").pack(fill = tk.BOTH, expand = 1)
tk.Label(window, text = "Green", bg = "green").pack(fill = tk.BOTH)
tk.Label(window, text = "Blue", bg = "blue").pack(fill = tk.BOTH)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


tk.Label(window, text = "Red", bg = "red").pack(side = tk.LEFT)
#tk.Label(window, text = "Green", bg = "green").pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
tk.Label(window, text = "Green", bg = "green").pack(side = tk.LEFT, fill = tk.BOTH)
tk.Label(window, text = "Blue", bg = "blue").pack(side = tk.LEFT, fill = tk.BOTH)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#label的寫法
label3 = tk.Label(text = 'Created by David Wang', font = ('Times', 22), fg = 'brown')
label3.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

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
title = "Label測試"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

font_size = 18
w = 20
h = 20
x_st = 50
y_st = 20
dx = 300
dy = 80

# 設定 Label 
label1a = tk.Label(window, text = '這是標籤元件 a', fg = 'red', bg = 'yellow', font = ("標楷體", font_size), padx = w, pady = h)
label1a.place(x = x_st + dx * 0, y = y_st + dy * 0)

cnt = 1
def changeLabelText1a():
    global cnt
    cnt += 1
    label1a.config(text = "這是標籤元件 " + str(cnt))
    
button1a = tk.Button(window, text = "修改標籤之Text a", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = changeLabelText1a)
button1a.place(x = x_st + dx * 0, y = y_st + dy * 1)

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
label2a.place(x = x_st + dx * 0, y = y_st + dy * 2)

button2a = tk.Button(window, text = "修改標籤之Text a", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = changeLabelText2a)
button2a.pack()
button2a.place(x = x_st + dx * 0, y = y_st + dy * 3)

button3a = tk.Button(window, text = "切換標籤顯示與隱藏 a", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = toggleLabelVisible_a)
button3a.pack()
button3a.place(x = x_st + dx * 0, y = y_st + dy * 4)

"""
width = 200
height = 100
frame = tk.Frame(window, bg = 'pink', width = width, height = height)
"""
frame = ttk.Frame(window)

x_st = 400
y_st = 20

# 設定 Label 
label1b = tk.Label(window, text = '這是標籤元件 b', fg = 'red', bg = 'yellow', font = ("標楷體", font_size), padx = w, pady = h)
label1b.place(x = x_st + dx * 0, y = y_st + dy * 0)

cnt = 1
def changeLabelText1b():
    global cnt
    cnt += 1
    label1b.config(text = "這是標籤元件 " + str(cnt))
    
button1b = tk.Button(window, text = "修改標籤之Text b", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = changeLabelText1b)
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

button2b = tk.Button(window, text = "修改標籤之Text b", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = changeLabelText2b)
button2b.place(x = x_st + dx * 0, y = y_st + dy * 3)

button3b = tk.Button(window, text = "切換標籤顯示與隱藏 b", foreground = "blue", font = ("標楷體", font_size), padx = w / 3, pady = h / 3, command = toggleLabelVisible_b)
button3b.place(x = x_st + dx * 0, y = y_st + dy * 4)

window.mainloop()

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
title = "Label測試"
window.title(title)


label1 =tk.Label(window, text="Hello World!")
label1.pack()
label2 =tk.Label(window, bg="yellow",text="Hello No2!",fg="red")
label2.pack()
label3 =tk.Label(window, text="Hello No3!")
label3.pack(side="top", anchor="w" )
label4 =tk.Label(window, text="Hello No4!")
label4.place(x=120, y=160)
label5 =tk.Label(window, text="Powen Ko",bg="#ff0000")
label5.place(x=120, y=140)



window.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

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

img = ImageTk.PhotoImage(Image.open(filename))
label1 =tk.Label(window, image = img)
label1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
使用 label 顯示圖片 jpg + gif
"""

from PIL import Image, ImageTk

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 900
x_st = 100
y_st = 50
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "使用 label 顯示圖片"
window.title(title)

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_書畫字圖/_peony3/原來奼紫嫣紅開遍.jpg'
im = Image.open(filename)

"""
#case 1 bitmap image
# bitmap image
image = ImageTk.BitmapImage(im, foreground = "white")
tk.Label(window, image = image, bg = "blue", bd = 0).pack()
"""

#case 2 picture image
# photo image
image = ImageTk.PhotoImage(im)

label1 = tk.Label(window, text = '多人圖片', image = image, bd = 20, bg = 'red')
label1.pack()
#tk.Label(window, text = '多人圖片', image = image, bd = 0, bg = 'red', width = 1200).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print('用 Label 顯示一張圖片')
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_書畫字圖/_peony3/原來奼紫嫣紅開遍.jpg'

image2 = Image.open(filename)
image2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(window, image = image2)   #用Label顯示圖片
label2.image = image
label2.pack()



import random

# Choose four random cards
def shuffle():
    random.shuffle(imageList)
    for i in range(4):
        labelList[i]["image"] = imageList[i]

imageList = [] # Store images for cards
for i in range(1, 53):
    imageList.append(tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_poker_card/card/" + str(i) + ".gif"))

frame = tk.Frame(window) # Hold four labels for cards
frame.pack()

labelList = [] # A list of four labels
for i in range(4):
    labelList.append(tk.Label(frame, image = imageList[i]))
    labelList[i].pack(side = tk.LEFT)

tk.Button(window, text = "Shuffle", command = shuffle).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個







"""
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
"""


