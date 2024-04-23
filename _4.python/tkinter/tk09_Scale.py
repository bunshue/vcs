import sys

print("------------------------------------------------------------")  # 60個

import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = 'Scale 測試'
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

import time

slider = tk.Scale(window, from_=0, to=10)
slider.pack()

label = tk.Label(window)
label.pack()

#slider.set(clicks)
#label.config(text="Time: " + str(score))

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print('Scale 測試')
slider = tk.Scale(window, from_ = 0, to = 100)
slider.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


tk.Label(text='Scale測試').pack()
#w = tk.Scale(window, from_=0, to=100)
w = tk.Scale(window, from_=0, to=100, resolution=0.1)
w.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


w = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL)
w.pack()

print(w.get())


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import *
def bgUpdate(source):
    ''' 更改畫布背景顏色 '''
    red = rSlider.get()                                 # 讀取red值
    green = gSlider.get()                               # 讀取green值
    blue = bSlider.get( )                               # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))      # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)      # 將顏色轉成16進位字串
    canvas.config(bg=myColor)                           # 設定畫布背景顏色
    
tk = Tk()
canvas = Canvas(tk, width=640, height=240)              # 初始化背景
rSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
gSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
bSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
gSlider.set(125)                                        # 設定green是125
rSlider.grid(row=0, column=0)                           
gSlider.grid(row=0, column=1)                           
bSlider.grid(row=0, column=2)                           
canvas.grid(row=1, column=0, columnspan=3)              
mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import *
def bgUpdate(source):
    ''' 更改畫布背景顏色 '''
    red = rSlider.get()                                 # 讀取red值
    green = gSlider.get()                               # 讀取green值
    blue = bSlider.get( )                               # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))      # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)      # 將顏色轉成16進位字串
    canvas.config(bg=myColor)                           # 設定畫布背景顏色
    
tk = Tk()
canvas = Canvas(tk, width=640, height=240)              # 初始化背景
rSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
gSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
bSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
gSlider.set(125)                                        # 設定green是125
rSlider.grid(row=1, column=1)                           # 第一行第一欄
gSlider.grid(row=1, column=2)                           # 第一行第二欄
bSlider.grid(row=1, column=3)                           # 第一行第三欄
canvas.grid(row=2, column=1, columnspan=3)              # 第二行全部
mainloop()

print("------------------------------------------------------------")  # 60個



slider1 = Scale(window,from_=0,to=10).pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL).pack()

print("------------------------------------------------------------")  # 60個

def printInfo():
    print(slider1.get(),slider2.get())
    
slider1 = Scale(window,from_=0,to=10)
slider1.pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL)
slider2.set(3)                      # 設定水平捲軸值
slider2.pack()
tk.Button(window,text="Print",command=printInfo).pack()


print("------------------------------------------------------------")  # 60個

from tkinter import *
    
window = Tk()
window.title("ch18_34")             # 視窗標題

slider1 = Scale(window,from_=0,to=10).pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL).pack()

window.mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import *

def printInfo():
    print(slider1.get(),slider2.get())
    
window = Tk()
window.title("ch18_35")             # 視窗標題

slider1 = Scale(window,from_=0,to=10)
slider1.pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL)
slider2.set(3)                      # 設定水平尺度值
slider2.pack()
Button(window,text="Print",command=printInfo).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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
title = "Frame 測試"
window.title(title)

# slider
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(
	window, 
	command = lambda value: progress.stop(), 
	from_ = 0, 
	to = 25,
	length = 300,
	orient = 'horizontal',
	variable = scale_float)
scale.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# progress bar
progress = ttk.Progressbar(
	window, 
	variable = scale_float, 
	maximum = 25,
	orient = 'horizontal',
	mode = 'indeterminate',
	length = 400)
progress.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# progress.start(1000)

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


# exercise 
# create a progress that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the progress bar
exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(window, orient = 'vertical', variable = exercise_int)
exercise_progress.pack()
exercise_progress.start()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


label = ttk.Label(window, textvariable = exercise_int)
label.pack()

exercise_scale = ttk.Scale(window, variable = exercise_int, from_ = 0, to = 100)
exercise_scale.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


